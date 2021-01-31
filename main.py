from PyQt5.QtWidgets import QApplication, QWidget

from window import Ui_MainWindow
import sys


from api import Api
from network import SetNetWork


class MainWindow(QWidget, Ui_MainWindow):
    """
    主窗口
    """
    def __init__(self):
        """
        这里完成窗口组建的信号与槽的绑定
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)                                                                          # 初始化主窗口
        self.NetWork = SetNetWork(self)                                                             # 初始化网络对象
        self.Api = Api(self)                                                                        # 初始化接口请求对象
        self.setIp.clicked.connect(self.NetWork.set_ip)                                             # 绑定设置IP槽函数
        self.ipComboBox.currentIndexChanged.connect(self.NetWork.ip_list_index_changed)             # 绑定选中IP槽函数
        self.netcardComboBox.currentIndexChanged.connect(self.NetWork.net_card_list_index_changed)  # 绑定选中IP槽函数
        self.networkSet.clicked.connect(self.NetWork.show_network_window)                           # 绑定打开网络配置槽函数
        self.request.clicked.connect(self.Api.requests)                                             # 绑定请求接口函数
        self.requestRecord.clicked.connect(self.Api.select_record)                                  # 绑定点击记录操作函数
        self.autoGetIp.toggled.connect(self.NetWork.set_ip_toggled)                                 # 自动获取IP复选框
        self.autoGetDns.toggled.connect(self.NetWork.set_dns_toggled)                               # 自用获取DNS复选框
    
    def closeEvent(self, event):
        import os
        event.accept()
        os._exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
