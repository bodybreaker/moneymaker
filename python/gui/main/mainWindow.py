# https://wikidocs.net/21866
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QAction
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import getmac

if __name__ == 'gui.main.mainWindow':
    form_class = uic.loadUiType("gui/main/main.ui")[0]
else:
    # UI 파일 연결
    form_class = uic.loadUiType("main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self, kiwoom):
        super().__init__()
        self.setupUi(self)
        self.kiwoom = kiwoom
        self.setWindowIcon(QIcon('web.png'))  # 아이콘 설정
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(None)
    mainWindow.show()
    sys.exit(app.exec_())
