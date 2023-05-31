'''

변수(variable) = 어떤 데이터를 저장하고자 할 떄 사용하는 메모리 저장공간. 저장공간의 이름을 붙여준것이 변수

변수명 = 값

변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성
    특수문자 사용할 수 없음
    대문자와 소문자 구분
    변수명의 첫 글자를 숫자로 사용 못함
    키워드 (list, dict, if, for, and, 등) 사용 못함

'''

name = 'Alice'
print(name)
age = 25
print(age)
address = '''우편번호 123456
서울시 서대문구 신폰 123-45
''' # 여러줄 문장으로 저장 됨. 줄바꿈까지 그대로 나옴

print(address)

'''
잘못된 변수명 예시
'''
# 2mybar = 'Python1' #숫자안됨
# my-var = 'Python2' #특수문자 안됨
# my var = 'Python3' #공백 있으면 안됨


'''
여러값 할당
'''

x, y, z = '피카츄', '라이츄', '파이리'
print(x)
print(y)
print(z)

'''
여러변수에 대한 하나의 값
'''

a = b = c = '꼬부기'
print(a)
print(b)
print(c)



