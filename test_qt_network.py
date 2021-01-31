#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
Created by PyCharm.
File:               LinuxBashShellScriptForOps:getNetworkStatus.py
User:               Guodong
Create Date:        2016/11/2
Create Time:        16:20

show Windows or Linux network Nic status, such as MAC address, Gateway, IP address, etc

# python getNetworkStatus.py
Routing Gateway:               10.6.28.254
Routing NIC Name:              eth0
Routing NIC MAC Address:       06:7f:12:00:00:15
Routing IP Address:            10.6.28.28
Routing IP Netmask:            255.255.255.0
 """
import os
import sys
import wmi

# import netifaces
#
# routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
# routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]
#
# for interface in netifaces.interfaces():
#
#     if interface == routingNicName:
#         # print netifaces.ifaddresses(interface)
#         routingNicMacAddr = netifaces.ifaddresses(interfce)[netifaces.AF_LINK][0]['addr']
#         try:
#             routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
#             # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
#             routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
#         except KeyError:
#             pass
#     ret

# display_format = '%-30s %-20s'
# print display_format % ("Routing Gateway:", routingGateway)
# print display_format % ("Routing NIC Name:", routingNicName)
# print display_format % ("Routing NIC MAC Address:", routingNicMacAddr)
# print display_format % ("Routing IP Address:", routingIPAddr)
# print display_format % ("Routing IP Netmask:", routingIPNetmask)


def set_ip():
    import wmi

    # Obtain network adaptors configurations
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]

    # IP address, subnetmask and gateway values should be unicode objects
    ip = u'192.168.0.11'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])


import psutil
def get_netcard():
    netcard_list = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_list.append(k)
                return netcard_list

# 执行windows命令
import subprocess
def exec_command(commands) -> list:
    if not commands:
        return list()
    # 子进程的标准输出设置为管道对象
    if isinstance(commands, str):
        commands = [commands]
    return_list = []
    for i in commands:
        p = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        p.wait()
        # stdout = p.stdout.readlines()
        # return_list.append(stdout)
    return return_list


def set_dns(card_name, dns_list):
    """设置dns"""
    set_dns_command = list()
    set_dns_command.append(f'netsh interface ip set dns name="{card_name}" source=static addr={dns_list[0]} register=primary')
    set_dns_command.append(f'netsh interface ip add dns name="{card_name}" addr={dns_list[1]} index=2')
    exec_command(set_dns_command)


# set_dns("本地连接", ['3.3.3.3', '4.4.4.4'])

nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)