# https://wikidocs.net/21866
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QAction
from PyQt5.QtGui import QIcon

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MoneyMaker - Login')  # 타이틀 설정
        # self.move(300, 300)  # 스크린 위치로 이동
        self.center()
        self.setWindowIcon(QIcon('./login/web.png'))  # 아이콘 설정
        self.resize(500, 500)  # 위젯 크기 설정
        self.showStatusMessage('로그인하여주세요')
        menubar = self.menuBar()
        settingMenu = menubar.addMenu('&설정')
        settingMenu.addAction(self.settingAction())
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showStatusMessage(self, message):
        self.statusBar().showMessage(message)

    def settingAction(self):
        action = QAction('라이선스 등록', self)
        # action.setShortcut('Ctrl+S')
        action.setStatusTip('Exit application')
        # action.triggered.connect(qApp.quit)
        return action


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())
