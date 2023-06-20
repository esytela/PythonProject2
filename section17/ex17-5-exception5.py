try:
    raise Exception('강제로 발생시킨 예외')
except Exception as e: #Exception은 위 에러 정보를 갖고 있음
    print('발생한 예외 메시지는 다음과 같습니다.')
    print(e)