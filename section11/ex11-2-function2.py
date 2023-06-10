
#매개변수 o, 리턴 x
def introduce(name,age):
   print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name,age))

introduce('홍길동',25)

# 가변 매개변수 함수
def show(*args):
    print(type(args)) #튜플로 값이 들어감
    for item in args:
        print(item)
show('pythons')
show('python','java','c++')

