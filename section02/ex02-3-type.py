'''
내장데이터 유형
python 변수는 다른 유형의 데이터르르 저장할 수 있으며
다른 유형은 다른 작업을 수행할 수 있다

텍스트 유형 : str (string의 약자)
숫자 유형: int (정수형), float (실수형), comple(복소수)
시퀀스 유형: list, tuple, range
매핑 유형: dict
세트 유형: set
논리 유형: bool
바이너리 유형: bytes, bytearray
없음 유형: none
'''

# str
x = 'hello world'
print(type(x))
#이걸 실행 시키면 <class 'str'>이라 뜸. x가 어느 유형의 텍스트인지 알려주는 것

# int
x = 20
print(type(x))

#float
x = 20.5
print(type(x))

#list
x = ['피카츄', '라이츄', '파이리']
print(type(x))
    #list는 여러 값은 가질 수 있음

# tuple
x = ('피카츄', '라이츄', '파이리')
print(type(x))
    #수정이 안됨

# range
x = range(6)
print(type(x))

# dict
x = {"name" : "피카츄", "기술":"백만볼트!"}
print(type(x))

# set
x = {"피카츄", "라이츄", "파이리"}
print(type(x))

# bool
x = True
#또는 false 값이 들어감
print(type(x))

x = None
print(type(x))

'''
변수명 = 값

숫자 + 숫자 = 숫자
문자 + 문자 = 문자 연결
문자 + 숫자 = 문자숫자 연결 

'''

num1 = 10
num2 = 20
result = num1 + num2
print(result)

#문자 + 숫자 쓰는 두가지 방법
name = 'Alice'
age = '15' #이렇게 '' 쓰기
result = name + ' / ' + age
print(result)

name = 'Pedro'
age = 27
result = name + str(age) #숫자 앞에 str 추가하기
print(result)