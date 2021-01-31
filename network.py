"""
这里实现有关网络的一切功能
"""
import subprocess
import json
import os

from comment import read_all_record, write_all_record

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from threading import Thread
import time
import re
import psutil
import netifaces


class SetNetWork(object):
    def __init__(self, main_window):
        self.Window = main_window                                                # 初始化主窗口对象
        self.net_card_data = dict()                                              # 网卡信息
        self.load_ip()                                                           # 初始化IP下拉框数据
        self.load_net_card_data()                                                # 加载系统网卡信息
        self.load_net_card_data_to_combobox()                                    # 将网卡信息加载到下拉框
        self.Window.manualSetIp.setChecked(True)
        self.Window.manualSetDns.setChecked(True)
        self.ip_dhcp = False
        self.dns_dhcp = False
        Thread(target=self.internet_and_gateway_status_monitor).start()          # 网络状况监控
       
        
    def set_ip_toggled(self):
        """setCheckable() isChecked()"""
        try:
            self.ip_dhcp = self.Window.autoGetIp.isChecked()
            if self.ip_dhcp:
                self.enable_dhcp_ip()
            else:
                self.disable_dhcp_ip()
        except Exception as e:
            print(e)

    def set_dns_toggled(self):
        """setCheckable() isChecked()"""
        try:
            self.dns_dhcp = self.Window.autoGetDns.isChecked()
            if self.dns_dhcp:
                self.enable_dhcp_dns()
            else:
                self.disable_dhcp_dns()
        except Exception as e:
            print(e)

    def enable_dhcp_ip(self):
        """启用DHCP"""
        # ip提示框与输入框置灰并且清空
        # self.Window.ip.setText('')
        # self.Window.ip.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Window.ip.setStyleSheet("background-color:rgba(200,200,200,255)")
        self.Window.tipIp.setStyleSheet("color:rgba(200,200,200,255)")
        # 掩码提示框与输入框置灰并且清空
        # self.Window.mask.setText('')
        # self.Window.mask.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Window.mask.setStyleSheet("background-color:rgba(200,200,200,255)")
        self.Window.tipMask.setStyleSheet("color:rgba(200,200,200,255)")
        # 网关提示框与输入框置灰并且清空
        # self.Window.gateway.setText('')
        # self.Window.gateway.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Window.gateway.setStyleSheet("background-color:rgba(200,200,200,255)")
        self.Window.tipGateway.setStyleSheet("color:rgba(200,200,200,255)")

    def disable_dhcp_ip(self):
        """关闭DHCP"""
        # ip提示框与输入框置灰
        # self.Window.ip.setFocusPolicy(1)
        self.Window.ip.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Window.tipIp.setStyleSheet("color:rgba(0,0,0,255)")
        # 掩码提示框与输入框置灰
        # self.Window.mask.setFocusPolicy(1)
        self.Window.mask.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Window.tipMask.setStyleSheet("color:rgba(0,0,0,255)")
        # 网关提示框与输入框置灰
        # self.Window.gateway.setFocusPolicy(1)
        self.Window.gateway.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Window.tipGateway.setStyleSheet("color:rgba(0,0,0,255)")

    def enable_dhcp_dns(self):
        # dns提示框与输入框置灰并且清空
        # self.Window.mainDns.setText('')
        # self.Window.mainDns.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Window.mainDns.setStyleSheet("background-color:rgba(200,200,200,255)")
        self.Window.tipMainDns.setStyleSheet("color:rgba(200,200,200,255)")

        # dns提示框与输入框置灰并且清空
        # self.Window.minorDns.setText('')
        # self.Window.minorDns.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Window.minorDns.setStyleSheet("background-color:rgba(200,200,200,255)")
        self.Window.tipMinorDns.setStyleSheet("color:rgba(200,200,200,255)")

    def disable_dhcp_dns(self):
        # ip提示框与输入框置灰
        # self.Window.mainDns.setFocusPolicy(1)
        self.Window.mainDns.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Window.tipMainDns.setStyleSheet("color:rgba(0,0,0,255)")

        # ip提示框与输入框置灰
        # self.Window.minorDns.setFocusPolicy(1)
        self.Window.minorDns.setStyleSheet("background-color:rgba(255,255,255,255)")
        self.Window.tipMinorDns.setStyleSheet("color:rgba(0,0,0,255)")

    def load_net_card_data(self):
        """获取本机所有可用网卡"""
        info = psutil.net_if_addrs()
        for k, v in info.items():
            for item in v:
                if item[0] == 2 and not item[1] == '127.0.0.1':
                    self.net_card_data[k] = dict(card_name=k, card_ip=item[1])

    def load_net_card_data_to_combobox(self):
        """将网卡信息加载到网卡选择下拉框"""
        for i in self.net_card_data:
            self.Window.netcardComboBox.addItem(i)

        self.Window.selfIp.setText(self.net_card_data.get(self.Window.netcardComboBox.currentText())['card_ip'])

    def internet_and_gateway_status_monitor(self):
        """循环检查网络延迟"""
        while True:
            local_ip, gateway, dns, internet_ip = self.get_ip_config()
            self.is_valid_gateway(self.ping_ip(gateway))
            self.is_valid_dns(self.ping_ip(dns))
            self.is_internet(self.ping_ip(internet_ip))

    def get_ip_config(self):
        local_ip = self.net_card_data.get(self.Window.ipComboBox.currentText())
        gateway = self.Window.mainDns.text()
        dns = 'www.baidu.com'
        internet_ip = '114.114.114.114'
        return local_ip, gateway, dns, internet_ip

    def ping_ip(self, ip):
        delay = int()
        timeout = int()
        ping_success_count = int()
        res_list = self.exec_command(f'ping {ip}')[0]
        for item in res_list:
            match_obj = re.match(r'.*(\S\S)ms', item, re.M | re.I)
            # ping通了
            if match_obj:
                delay += int(match_obj.group(1).replace('<', '').replace('=', ''))
                ping_success_count += 1
            # 超时
            if '请求超时' in item or '无法访问目标主机' in item:
                timeout += 1
                continue
            # 全部超时
            if timeout == 4:
                return False, '超时！'
            # 无法解析主机
            if 'Ping 请求找不到主机' in item:
                return False, '找不到主机'
            # 100%丢失，不通
            if '数据包: 已发送 = 4' in item:
                if '(100% 丢失)' in item:
                    return delay, '100%丢包率'
        if not ping_success_count:
            return False, '超时！'
        tep = int("%.1d" % (delay / ping_success_count))
        delay = 1 if tep < 1 else tep
        return True, str(delay) + 'ms'

    def is_internet(self, delay):
        flag, msg = delay
        self.Window.internetStatus.setText(f"{msg}")
        if flag:
            self.Window.internetStatus.setStyleSheet("color:rgb(0,255,0,255)")
        else:
            self.Window.internetStatus.setStyleSheet("color:rgb(255,0,0,255)")

    def is_valid_gateway(self, delay):
        flag, msg = delay
        self.Window.gatewayStatus.setText(f"{msg}")
        if flag:
            self.Window.gatewayStatus.setStyleSheet("color:rgb(0,255,0,255)")
        else:
            self.Window.gatewayStatus.setStyleSheet("color:rgb(255,0,0,255)")

    def is_valid_dns(self, delay):
        flag, msg = delay
        self.Window.dnsStatus.setText(f"{msg}")
        if flag:
            self.Window.dnsStatus.setStyleSheet("color:rgb(0,255,0,255)")
        else:
            self.Window.dnsStatus.setStyleSheet("color:rgb(255,0,0,255)")

    # 加载历史设置IP记录到IP下拉框
    def load_ip(self):
        history_ip_list = self.read_history_ip()
        self.Window.ipComboBox.clear()
        for index in range(len(history_ip_list)):
            self.Window.ipComboBox.addItem(history_ip_list[index]['ip'])
            if index == 0:
                try:
                    self.Window.ip.setText(history_ip_list[index]['ip'])
                    self.Window.mask.setText(history_ip_list[index]['mask'])
                    self.Window.gateway.setText(history_ip_list[index]['gateway'])
                    self.Window.mainDns.setText(history_ip_list[index]['main_dns'])
                    self.Window.minorDns.setText(history_ip_list[index]['minor_dns'])
                except:
                    pass

    @staticmethod
    def read_history_ip():
        if not os.path.exists('static'):
            os.mkdir("static")
        if not os.path.exists('static/config.json'):
            return []
        return read_all_record().get('ip', [])

    def save_new_ip(self, **kwargs):
        # 去重
        for i in self.read_history_ip():
            if i['ip'] == kwargs['ip']:
                return
        if not self.Window.autoGetIp.isChecked() and not self.Window.autoGetDns.isChecked():
            history_ip_list = self.read_history_ip()
            history_ip_list.insert(0, kwargs)
            all_record = read_all_record()
            all_record['ip'] = history_ip_list
            write_all_record(all_record)
            self.load_ip()

    def show_network_window(self):
        self.exec_command("control.exe /name Microsoft.NetworkAndSharingCenter")

    # 执行windows命令
    def exec_command(self, commands) -> list:
        if not commands:
            return list()
        # 子进程的标准输出设置为管道对象
        if isinstance(commands, str):
            commands = [commands]
        return_list = []
        for i in commands:
            p = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            p.wait()
            return_list.append(p.stdout.readlines())
        return return_list

    # 设置网络为自动获取
    def set_dhcp(self):
        cur_card_name = self.net_card_data[self.Window.netCardList.currentText()]['card_name']
        if not cur_card_name:
            QMessageBox.warning(self.Window, '提示', '没有找到任何网卡')
        set_ip_command = [f'netsh interface ip set address "{cur_card_name}" source=dhcp',
                          f'netsh interface ip set dns name="{cur_card_name}" source=dhcp']
        self.exec_command(set_ip_command)

    # 设置ip
    def set_ip(self):
        ip = self.Window.ip.text()
        gateway = self.Window.gateway.text()
        if not gateway:
            # 此方式获取网关不合适，只能说是大部分默认为网规则
            gateway = '.'.join(ip.split('.')[:3]) + '.1'
        # 获取子网掩码，子网掩码应该可以根据ip计算出来的，方法还不知道
        mask = self.Window.mask.text()
        # 主副dns
        main_dns = self.Window.mainDns.text()
        minor_dns = self.Window.minorDns.text()
        # 获取当前选中的网卡名字
        cur_card_name = self.net_card_data.get(self.Window.netcardComboBox.currentText())['card_name']

        if not ip and not self.ip_dhcp:
            QMessageBox.warning(self.Window, '警告', 'ip地址为必填项')
            return
        if not mask and not self.dns_dhcp:
            QMessageBox.warning(self.Window, "警告", '子网掩码为必填项')
            return
        if not cur_card_name:
            QMessageBox.warning(self.Window, '提示', f"未找到任何网卡")
            return
        params = dict(
            ip=ip,
            mask=mask,
            gateway=gateway,
            card_name=cur_card_name,
            main_dns=main_dns,
            minor_dns=minor_dns,
            auto_get=self.Window.autoGetIp.isChecked(),
        )
        self.exec_command(self.generate_ip_command(**params))
        dns_list = [self.Window.mainDns.text(), self.Window.minorDns.text()]
        self.exec_command(self.generate_dns_command(cur_card_name, dns_list))
        # 保存设置记录
        self.save_new_ip(**params)
        self.Window.selfIp.setText(ip)
        QMessageBox.about(self.Window, '提示', '设置成功！')

    # 生成设置IP命令y
    @staticmethod
    def generate_ip_command(**kwargs):
        if kwargs['auto_get']:
            set_ip_command = f'netsh interface ip set address "{kwargs["card_name"]}" source=dhcp'
        else:
            set_ip_command = f'netsh interface ip set address "{kwargs["card_name"]}" ' \
                         f'static {kwargs["ip"]} {kwargs["mask"]} {kwargs["gateway"]}'
        return set_ip_command

    def generate_dns_command(self, card_name, dns_list):
        """设置dns"""
        auto_get = self.Window.autoGetDns.isChecked()
        set_dns_command = list()
        if auto_get:
            set_dns_command.append(f'netsh interface ip set dns "{card_name}" source=dhcp')
            return set_dns_command
        try:
            if dns_list[0]:
                set_dns_command.append(f'netsh interface ip set dns "{card_name}" static {dns_list[0]} register=primary')
            if dns_list[1]:
                set_dns_command.append(f'netsh interface ip add dns "{card_name}" addr={dns_list[1]} index=2')
        except:
            pass
        return set_dns_command

    # 更改IP槽函数
    def ip_list_index_changed(self, index):
        history_list = self.read_history_ip()
        self.Window.ip.setText(history_list[index].get("ip"))
        self.Window.gateway.setText(history_list[index].get("gateway"))
        self.Window.mainDns.setText(history_list[index].get("main_dns"))
        self.Window.minorDns.setText(history_list[index].get("minor_dns"))

    def net_card_list_index_changed(self, index):
        self.Window.selfIp.setText(self.net_card_data.get(self.Window.netcardComboBox.currentText())['card_ip'])

    # log
    def log(self, log):
        if log:
            log = log.replace("\n", "")
            pass
