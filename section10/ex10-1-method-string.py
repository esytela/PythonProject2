'''
메소드(method)
    특정 객체가 가지고 있는 함수를 의미한다
     - 아직 class 객체 안 배움
    객체.메소드()
'''

#string 객체 format method
print("10자리 폭 왼 쪽 정렬 '{:<10d}'".format(123))
    #:<10d 왼쪽정렬 + 10칸 만듬
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
    #빈칸 별표로 채우기
print("10자리 폭 왼 쪽 정렬 채움 문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움 문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움 문자 '{:*^10d}'".format(123))

# count() 메소드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)
#인덱스 5부터 best라는 단어 찾아 달라는 뜻

#find() 메소드 - 위치한 인덱스 번호 반환
s = 'apple' #처음에 나오는 p가 2번 인덱스번호
result = s.find('p')
print(result)
result = s.find('z')
if result == -1:
    print('존재하지 않은 문자입니다.')
print(result) #없는 값을 find 하면 -1이 뜸

s = 'best of best'
result = s.find('best', 5)
print(result)
# 인덱스 번호 5 이후 문자를 찾아줌
result = s.find('best', -7)
print(result)


# index() - find() 메소드와 같지만 문자열이 존재하지 않을 경우 에러 발생
s = 'apple'
result = s.index('p')
print(result)
'''
result = s.index('z')
print(result) 
#없는 값을 index하면 에러 뜸
'''






