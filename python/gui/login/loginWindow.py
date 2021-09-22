# https://wikidocs.net/21866
from gui.main.mainWindow import *
import getmac
from util.logUtil import *

if __name__ == 'gui.login.loginWindow':
    form_class = uic.loadUiType("gui/login/login.ui")[0]
else:
    # UI 파일 연결
    form_class = uic.loadUiType("login.ui")[0]


class LoginWindow(QMainWindow, form_class):
    def __init__(self, kiwoom):
        super().__init__()
        self.logger = getLogger(__name__)
        self.setupUi(self)
        self.macAddress = getmac.get_mac_address()  # 추후 mac 별 ID 부여
        self.setWindowIcon(QIcon('web.png'))  # 아이콘 설정
        self.bt_login.clicked.connect(self.loginFunction)
        self.showStatusMessage("로그인 하여 주세요>>" + self.macAddress)
        self.kiwoom = kiwoom

    # bt_login 클릭시 로그인 수행하는 함수
    def loginFunction(self):
        id = self.le_kiwoom_id.text()
        pw = self.le_kiwoom_pw.text()

        if len(id) != 0 and len(pw) != 0:
            self.logger.info("로그인 수행")
            self.kiwoom.signal_login_commConnect()
            self.goToMainWindow()
        else:
            self.showStatusMessage("아이디와 비밀번호를 입력해주세요")

    # 상태표시줄 메시지 표시하는 함수
    def showStatusMessage(self, message):
        self.statusBar().showMessage(message)

    def goToMainWindow(self):
        self.mainWindow = MainWindow(self.kiwoom)
        self.mainWindow.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # LoginWindow 인스턴스 생성
    loginWindow = LoginWindow(None)  # 본 화면만 테스트,
    # LoginWindow 보여주기
    loginWindow.show()
    sys.exit(app.exec_())
