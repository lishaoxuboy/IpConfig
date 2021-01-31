import sys
from PyQt5.Qt import *

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.btn = QPushButton("选择字体",self)
        self.color_btn = QPushButton("选择颜色",self)
        self.color_btn.move(100,0)
        self.fd = QFontDialog(self)
        self.qfc = QColorDialog(self)
        self.fd.fontSelected.connect(self.font_select)
        self.fd.currentFontChanged.connect(self.font_select)
        self.qfc.colorSelected.connect(self.color_select)
        self.label = QLabel("天佑中华！",self)
        self.label.move(100,100)
        self.btn.clicked.connect(self.open_choose)
        self.color_btn.clicked.connect(self.open_color_choose)

    def color_select(self,color):
        red,green,blue,_ = color.getRgb()
        print(red, green, blue)
        self.label.setStyleSheet("color:rgb({},{},{},255)".format(red,green,blue))

    def open_color_choose(self):
        self.qfc.open()

    def open_choose(self):
        self.fd.open()

    def font_select(self,font):
        self.label.setFont(font)
        self.label.adjustSize()



if __name__ == "__main__":
    app = QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())