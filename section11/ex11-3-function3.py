# 반환 (return) 값이 있는 함수

def address(): #매개변수 x, 리턴 o
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str #address이 리턴 값을 받음

result = address()
print(result)

#매개변수 o, 리턴 o
def plus(num1, num2):
    return num1 + num2 #plus에 return값이 들어감

result = plus(5,7)
print(result)
print(plus(2,3)) #함수 안에 함수도 가능함

