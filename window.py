# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 572)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 191, 431))
        self.groupBox_5.setObjectName("groupBox_5")
        self.requestRecord = QtWidgets.QListView(self.groupBox_5)
        self.requestRecord.setGeometry(QtCore.QRect(10, 20, 171, 401))
        self.requestRecord.setObjectName("requestRecord")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(220, 200, 461, 251))
        self.groupBox_6.setObjectName("groupBox_6")
        self.response = QtWidgets.QPlainTextEdit(self.groupBox_6)
        self.response.setGeometry(QtCore.QRect(20, 20, 421, 221))
        self.response.setObjectName("response")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(220, 20, 461, 181))
        self.groupBox_7.setObjectName("groupBox_7")
        self.method = QtWidgets.QComboBox(self.groupBox_7)
        self.method.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.method.addItem("")
        self.url = QtWidgets.QLineEdit(self.groupBox_7)
        self.url.setGeometry(QtCore.QRect(90, 20, 281, 21))
        self.url.setText("")
        self.url.setObjectName("url")
        self.request = QtWidgets.QPushButton(self.groupBox_7)
        self.request.setGeometry(QtCore.QRect(380, 20, 71, 21))
        self.request.setObjectName("request")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_7)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 60, 421, 111))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.params = QtWidgets.QPlainTextEdit(self.tab_5)
        self.params.setGeometry(QtCore.QRect(10, 10, 391, 71))
        self.params.setObjectName("params")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.headers = QtWidgets.QPlainTextEdit(self.tab_6)
        self.headers.setGeometry(QtCore.QRect(10, 10, 391, 71))
        self.headers.setObjectName("headers")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab, "")
        self.netWorkSettings = QtWidgets.QWidget()
        self.netWorkSettings.setObjectName("netWorkSettings")
        self.setIp = QtWidgets.QPushButton(self.netWorkSettings)
        self.setIp.setGeometry(QtCore.QRect(490, 510, 101, 21))
        self.setIp.setObjectName("setIp")
        self.groupBox_4 = QtWidgets.QGroupBox(self.netWorkSettings)
        self.groupBox_4.setGeometry(QtCore.QRect(110, 10, 481, 491))
        self.groupBox_4.setObjectName("groupBox_4")
        self.IpSettings = QtWidgets.QGroupBox(self.groupBox_4)
        self.IpSettings.setGeometry(QtCore.QRect(30, 20, 431, 231))
        self.IpSettings.setObjectName("IpSettings")
        self.netcardComboBox = QtWidgets.QComboBox(self.IpSettings)
        self.netcardComboBox.setGeometry(QtCore.QRect(110, 20, 211, 21))
        self.netcardComboBox.setObjectName("netcardComboBox")
        self.tipSelectNetCard = QtWidgets.QLabel(self.IpSettings)
        self.tipSelectNetCard.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.tipSelectNetCard.setObjectName("tipSelectNetCard")
        self.autoGetIp = QtWidgets.QRadioButton(self.IpSettings)
        self.autoGetIp.setGeometry(QtCore.QRect(120, 100, 111, 21))
        self.autoGetIp.setObjectName("autoGetIp")
        self.manualSetIp = QtWidgets.QRadioButton(self.IpSettings)
        self.manualSetIp.setGeometry(QtCore.QRect(250, 100, 121, 21))
        self.manualSetIp.setObjectName("manualSetIp")
        self.tipIp = QtWidgets.QLabel(self.IpSettings)
        self.tipIp.setGeometry(QtCore.QRect(60, 130, 41, 21))
        self.tipIp.setObjectName("tipIp")
        self.tipMask = QtWidgets.QLabel(self.IpSettings)
        self.tipMask.setGeometry(QtCore.QRect(50, 160, 61, 21))
        self.tipMask.setObjectName("tipMask")
        self.tipGateway = QtWidgets.QLabel(self.IpSettings)
        self.tipGateway.setGeometry(QtCore.QRect(50, 190, 51, 21))
        self.tipGateway.setObjectName("tipGateway")
        self.ip = QtWidgets.QLineEdit(self.IpSettings)
        self.ip.setGeometry(QtCore.QRect(120, 130, 241, 21))
        self.ip.setObjectName("ip")
        self.mask = QtWidgets.QLineEdit(self.IpSettings)
        self.mask.setGeometry(QtCore.QRect(120, 160, 241, 21))
        self.mask.setObjectName("mask")
        self.gateway = QtWidgets.QLineEdit(self.IpSettings)
        self.gateway.setGeometry(QtCore.QRect(120, 190, 241, 21))
        self.gateway.setObjectName("gateway")
        self.ipComboBox = QtWidgets.QComboBox(self.IpSettings)
        self.ipComboBox.setGeometry(QtCore.QRect(110, 60, 211, 21))
        self.ipComboBox.setObjectName("ipComboBox")
        self.tipSettingsHisory = QtWidgets.QLabel(self.IpSettings)
        self.tipSettingsHisory.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.tipSettingsHisory.setObjectName("tipSettingsHisory")
        self.networkSet = QtWidgets.QPushButton(self.IpSettings)
        self.networkSet.setGeometry(QtCore.QRect(330, 20, 81, 21))
        self.networkSet.setObjectName("networkSet")
        self.autoGetIp.raise_()
        self.netcardComboBox.raise_()
        self.tipSelectNetCard.raise_()
        self.manualSetIp.raise_()
        self.tipIp.raise_()
        self.tipMask.raise_()
        self.tipGateway.raise_()
        self.ip.raise_()
        self.mask.raise_()
        self.gateway.raise_()
        self.ipComboBox.raise_()
        self.tipSettingsHisory.raise_()
        self.networkSet.raise_()
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 260, 431, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.autoGetDns = QtWidgets.QRadioButton(self.groupBox_3)
        self.autoGetDns.setGeometry(QtCore.QRect(120, 20, 121, 21))
        self.autoGetDns.setObjectName("autoGetDns")
        self.manualSetDns = QtWidgets.QRadioButton(self.groupBox_3)
        self.manualSetDns.setGeometry(QtCore.QRect(260, 20, 121, 21))
        self.manualSetDns.setObjectName("manualSetDns")
        self.mainDns = QtWidgets.QLineEdit(self.groupBox_3)
        self.mainDns.setGeometry(QtCore.QRect(120, 50, 241, 21))
        self.mainDns.setObjectName("mainDns")
        self.minorDns = QtWidgets.QLineEdit(self.groupBox_3)
        self.minorDns.setGeometry(QtCore.QRect(120, 80, 241, 21))
        self.minorDns.setObjectName("minorDns")
        self.tipMainDns = QtWidgets.QLabel(self.groupBox_3)
        self.tipMainDns.setGeometry(QtCore.QRect(60, 50, 51, 21))
        self.tipMainDns.setObjectName("tipMainDns")
        self.tipMinorDns = QtWidgets.QLabel(self.groupBox_3)
        self.tipMinorDns.setGeometry(QtCore.QRect(60, 80, 51, 21))
        self.tipMinorDns.setObjectName("tipMinorDns")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(30, 390, 431, 81))
        self.groupBox.setObjectName("groupBox")
        self.gatewayStatus_2 = QtWidgets.QLabel(self.groupBox)
        self.gatewayStatus_2.setGeometry(QtCore.QRect(40, 50, 51, 16))
        self.gatewayStatus_2.setObjectName("gatewayStatus_2")
        self.internetStatus_2 = QtWidgets.QLabel(self.groupBox)
        self.internetStatus_2.setGeometry(QtCore.QRect(240, 20, 61, 21))
        self.internetStatus_2.setObjectName("internetStatus_2")
        self.dnsStatus_2 = QtWidgets.QLabel(self.groupBox)
        self.dnsStatus_2.setGeometry(QtCore.QRect(250, 50, 51, 21))
        self.dnsStatus_2.setObjectName("dnsStatus_2")
        self.selfIp_2 = QtWidgets.QLabel(self.groupBox)
        self.selfIp_2.setGeometry(QtCore.QRect(50, 20, 41, 21))
        self.selfIp_2.setObjectName("selfIp_2")
        self.selfIp = QtWidgets.QLabel(self.groupBox)
        self.selfIp.setGeometry(QtCore.QRect(100, 20, 101, 21))
        self.selfIp.setText("")
        self.selfIp.setObjectName("selfIp")
        self.gatewayStatus = QtWidgets.QLabel(self.groupBox)
        self.gatewayStatus.setGeometry(QtCore.QRect(100, 50, 121, 16))
        self.gatewayStatus.setText("")
        self.gatewayStatus.setObjectName("gatewayStatus")
        self.internetStatus = QtWidgets.QLabel(self.groupBox)
        self.internetStatus.setGeometry(QtCore.QRect(310, 20, 101, 21))
        self.internetStatus.setText("")
        self.internetStatus.setObjectName("internetStatus")
        self.dnsStatus = QtWidgets.QLabel(self.groupBox)
        self.dnsStatus.setGeometry(QtCore.QRect(310, 50, 101, 21))
        self.dnsStatus.setText("")
        self.dnsStatus.setObjectName("dnsStatus")
        self.tabWidget.addTab(self.netWorkSettings, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 30, 191, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 80, 281, 271))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.tab_3)
        self.listView.setGeometry(QtCore.QRect(80, 70, 191, 271))
        self.listView.setObjectName("listView")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.groupBox_5.setTitle(_translate("MainWindow", "请求历史"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Response"))
        self.groupBox_7.setTitle(_translate("MainWindow", "GroupBox"))
        self.method.setItemText(0, _translate("MainWindow", "GET"))
        self.method.setItemText(1, _translate("MainWindow", "POST"))
        self.method.setItemText(2, _translate("MainWindow", "PUT"))
        self.method.setItemText(3, _translate("MainWindow", "DELETE"))
        self.url.setToolTip(_translate("MainWindow", "<html><head/><body><p>url:port/path</p></body></html>"))
        self.url.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>请求地址</p></body></html>"))
        self.request.setText(_translate("MainWindow", "发送"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Params"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Headers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "接口调用"))
        self.setIp.setText(_translate("MainWindow", "应用设置"))
        self.groupBox_4.setTitle(_translate("MainWindow", "网络设置"))
        self.IpSettings.setTitle(_translate("MainWindow", "IP地址设置"))
        self.tipSelectNetCard.setText(_translate("MainWindow", "选择网卡"))
        self.autoGetIp.setText(_translate("MainWindow", "自动获取IP地址"))
        self.manualSetIp.setText(_translate("MainWindow", "使用指定IP地址"))
        self.tipIp.setText(_translate("MainWindow", "IP地址"))
        self.tipMask.setText(_translate("MainWindow", "子网掩码"))
        self.tipGateway.setText(_translate("MainWindow", "默认网关"))
        self.tipSettingsHisory.setText(_translate("MainWindow", "设置历史"))
        self.networkSet.setText(_translate("MainWindow", "网络设置"))
        self.groupBox_3.setTitle(_translate("MainWindow", "DNS服务器设置"))
        self.autoGetDns.setText(_translate("MainWindow", "自动获取DNS服务器"))
        self.manualSetDns.setText(_translate("MainWindow", "使用指定DNS服务器"))
        self.tipMainDns.setText(_translate("MainWindow", "主DNS"))
        self.tipMinorDns.setText(_translate("MainWindow", "副DNS"))
        self.groupBox.setTitle(_translate("MainWindow", "本机当前网络信息及状态"))
        self.gatewayStatus_2.setText(_translate("MainWindow", "网关延迟"))
        self.internetStatus_2.setText(_translate("MainWindow", " 外网延迟"))
        self.dnsStatus_2.setText(_translate("MainWindow", "DNS延迟"))
        self.selfIp_2.setText(_translate("MainWindow", "本机IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.netWorkSettings), _translate("MainWindow", "网络设置"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "预留一"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "预留二"))
