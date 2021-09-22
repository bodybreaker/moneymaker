from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *
from util.logUtil import *
import platform


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        # 로깅 설정
        self.logger = getLogger(__name__)
        self.logger.info("Kiwoom() class start.")

        self.get_ocx_instance()  # OCX 방식을 파이썬에 사용할 수 있게 반환해 주는 함수 실행
        self.event_slots()  # 키움과 연결하기 위한 시그널/슬롯 모음

        self.login_event_loop = QEventLoop()  # 로그인 요청용 이벤트 루프

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")  # 레지스트리에 저장된 API 모듈 불러오기
        self.logger.info("[get_ocx_instance] 완료")

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")  # 로그인 요청 시그널
        self.login_event_loop.exec_()  # 이벤트 루프 실행
        self.logger.info("[signal_login_commConnect] 완료")

    #  슬롯과 관련된 함수들
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, err_code):
        self.logger.info(errors(err_code)[1])
        # 로그인 처리가 완료됐으면 이벤트 루프를 종료한다.
        self.login_event_loop.exit()
        print(platform.architecture())
        print(1/0)

    def showPwSaveWindow(self):
        self.dynamicCall("KOA_Functions(QString,QString)", "ShowAccountWindow", "")  # 계좌 비밀번호 자동저장 설정창 띄우기
