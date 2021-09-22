from kiwoom.kiwoom import *
import sys
from PyQt5.QtWidgets import *
from gui.login.loginWindow import *
from util.logUtil import *

class Main():
    def __init__(self):
        # 로깅 설정
        self.logger = getLogger(__name__)

        self.logger.info("Main() Start")
        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()

        # LoginWindow 인스턴스 생성
        loginWindow = LoginWindow(self.kiwoom)
        # LoginWindow 보여주기
        loginWindow.show()

        sys.exit(self.app.exec_())


if __name__=="__main__":
    Main()