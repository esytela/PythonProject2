'''
죽음의 다이아몬드
'''

class A:
    def greeting(self):
        print('안녕하세요, A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요, B입니다.')

class C(A):
    def greeting(self):
        print("안녕하세요. C입니다")

class D(B,C):
    pass # 내부동작 필요없고 빈껍데기만 필요할 때 pass 사용

# 실행 코드
x = D()
x.greeting()
print(D.mro()) #mro() - 다중상속시 메서드 호출 순서 결정
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# D의 부모 class인 B가 프린트 된것






