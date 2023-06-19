'''
소멸자
    인스턴스가 소멸될 떄 자동으로 호출된다

소멸자 선언 방법
    __del__()


'''
class Service:
    def __init__(self,service): #생성자
        self.service = service
        print('{} Service가 시작되었습니다'.format(self.service))

    def __del__(self): #소멸자
        print('{} Service가 종료되었습니다.'.format(self.service))

#실행코드
s = Service('길 안내')
del s

s2 = Service('커피 주문')

print('프로그램 종료')
#프로그램이 끝난 후에야 del됨.