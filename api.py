"""
接口测试请求
"""
from requests import sessions
from threading import Thread
from comment import read_all_record, write_all_record
from PyQt5.QtCore import QStringListModel, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QMessageBox
import time


class Api(object):
    def __init__(self, main_widow):
        self.MainWindow = main_widow
        self.method = str()
        self.url = str()
        self.params = dict()
        self.record_index = list()
        self.record_data = list()
        self.load_request_record()

    def get_url(self):
        self.url = self.MainWindow.url.text()
        if "http://" not in self.url:
            self.url = "http://" + self.url

    def get_method(self):
        self.method = self.MainWindow.method.currentText()

    def get_parameter(self):
        try:
            base_str = self.MainWindow.parameter.toPlainText()
            if base_str:
                for i in base_str.split("&"):
                    key, value = i.split("=")
                    self.params[key] = value
        except Exception as e:
            self.log(f"解析参数错误 {e}")

    def requests(self):
        self.get_parameter()
        self.get_url()
        self.get_method()
        self.save_request()
        response = self.request()
        self.reset_request_params()
        if response:
            self.log(f"状态码: {response.status_code}\n结果: {response.text}")

    def request(self):
        with sessions.Session() as session:
            try:
                response = session.request(method=self.method, url=self.url, data=self.params, timeout=2)
                return response
            except Exception as e:
                self.log(f"请求错误:{e}")
                return None

    def reset_request_params(self):
        self.method = None
        self.url = None
        self.params = dict()

    def save_request(self):
        """保存请求记录"""
        # 读取请求记录
        all_record = read_all_record()
        # 生成此次请求的唯一ID
        uuid = self.method + "_" + self.url + "_" + self.MainWindow.parameter.toPlainText()
        # 相同的请求不保存
        if all_record['api'].get(uuid):
            return
        # 保存新请求
        all_record['api'][uuid] = dict(
            method=self.method,
            url=self.url,
            params=self.MainWindow.parameter.toPlainText()
        )
        # 添加至索引列表
        self.record_index.insert(0, uuid)
        # 更新保存的请求记录
        write_all_record(all_record)
        self.MainWindow.requestRecord.model().setData(1, self.url, 0)

    def clear_record(self, url) -> bool:
        """清空请求记录"""
        a = QStringListModel()
        a.setStringList([url])
        self.MainWindow.requestRecord.setModel(a)
        self.record_index = []
        return True

    def load_request_record(self):
        """将请求记录重新加载到ListView"""
        all_recode = read_all_record()
        if all_recode.get('api'):
            for i in all_recode['api']:
                url = all_recode['api'][i]['url']
                method = all_recode['api'][i]['method']
                params = all_recode['api'][i]['params']
                # 保存加载到ListView中的索引
                self.record_index.append(method + '_' + url + "_" + params)
                # 索引对应的数据
                self.record_data.append(dict(url=url, method=method, params=params))

        # 创建列表字符串对象，跟QListView配合使用
        listModel = QStringListModel()
        listModel.setStringList(self.record_index)
        self.MainWindow.requestRecord.setContextMenuPolicy(3)
        self.MainWindow.requestRecord.setModel(listModel)
        # 未每个item加入右键功能
        self.MainWindow.requestRecord.customContextMenuRequested[QPoint].connect(self.list_widget_menu)

    def list_widget_menu(self, point):
        index = self.MainWindow.requestRecord.currentIndex().row()
        list_view_menu = QMenu()
        list_view_menu.addAction('删除')
        res = list_view_menu.exec_(QCursor.pos())
        print(f"当前选中行{index} {point}")
        if res:
            if res.text() == '删除':
                self.delete_record(index)

    def delete_record(self, index):
        res = QMessageBox.question(self.MainWindow, '确认', '确认删除?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            self.MainWindow.requestRecord.model().removeRow(index)
            uuid = self.record_index.pop(index)
            self.record_data.pop(index)
            all_record = read_all_record()
            if all_record:
                del all_record['api'][uuid]
            write_all_record(all_record)

        else:
            QMessageBox.warning(self.MainWindow, '警告', '小伙子，不要乱搞哦！')

    def select_record(self, index):
        """将选中的item信息加载到输入框"""
        record = self.record_data[index.row()]
        self.MainWindow.method.setCurrentText(record['method'])
        self.MainWindow.url.setText(record['url'])
        self.MainWindow.parameter.setPlainText(record['params'])

    def delete_all_record(self):
        listModel = QStringListModel()
        listModel.setStringList([])
        self.MainWindow.requestRecord.setModel(listModel)
        all_record = read_all_record()
        all_record['api'] = {}
        write_all_record(all_record)

    def log(self, log):
        log = log.encode("utf-8").decode()
        self.MainWindow.response.appendPlainText(log)