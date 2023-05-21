'''
문자열(string)
    하나 이상 연속된 문자(character)들의 나열
    파이썬에서는 문자열 자료형은 큰따옴표 ("")
    또는 작은 따옴표 ('') 사이에 위치
'''
#'Hello'와 "Hello"는 동일
print('Hello' == "Hello") #값이 다르면 false라 뜨고 값이 같으면 true라고 뜸

'''
변수에 문자열 할당
'''

str = "Hello"
print(str)

'''
여러줄 문자열
    세개의 따옴표를 사용하여 변수에 여러줄 문자열 할당
'''

str = """피카츄, 라이츄, 파이리, 꼬부기
버터플 야도란, 피존투, 또가스"""
print(str)

'''
문자 배열 => 문자열
    문자열 인덱싱 (indexing)
    h   e   l   l   o    <-- 문자열
    0   1   2   3   4    <-- 이렇게 인덱스 번호가 있음. 파이썬은 마이너스 인덱스도 있음
    -5 -4  -3  -2  -1    <-- 마이너스 인덱스
'''

str = 'hello'
print(str[-5])
print(str[1])
print(str[3])
print(str[-2])
print(str[4])
print(str[1] == str[-4])

'''
문자열 슬라이싱
    슬라이스 구문을 사용하여 문자를 반환할 수 있다
    문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분
'''
str = "Hello, World"
print(str[2:5]) #2번째글자부터 4번째 글짜까지 (인덱스 번호가 0부터 시작)

# 처음부터 인덱스번호 앞까지 슬라이스
print(str[:5]) #아무것도 안 쓰면 default으로 0
#인덱스번호부터 끝까지 슬라이스
print(str[2:]) #뒤에 안 적으면 끝까지 감

str = "Hello, World"
# 대문자
print(str.upper())
#소문자
print(str.lower())

#문자열 바꾸기
str = "hello, world"
print(str.replace("h","J"))

print('git test')
