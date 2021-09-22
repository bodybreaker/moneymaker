import logging


def getLogger(name):
    # 로깅 설정 시작
    logger = logging.getLogger(name)
    # 로그의 출력 기준 설정
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s ::%(name)s[%(funcName)s][%(levelname)s] : %(message)s')
    # log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

