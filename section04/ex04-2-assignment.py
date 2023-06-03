'''
대입연산
    변수에 값을 저장하기 위해 사용하는 연산자

print 형식문자
%d: 숫자 데이터
%f : 실수 데이터
%o : 8진수 데이터
%x: 16진수 데이터
%s : 문자열 데이터
%c : 문자 하나 데이터
'''

a, b = 10, 20
print('a = %d, b = %d' %(a,b))
'''
변수 값 바꾸기 (다른 언어들)
tmp = a #a값을 tmp에 넣음
a = b #b의 값을 a에 넣음
b = tmp #b에 값에 a값 넣음
'''
#파이썬에서 변수 값 바꾸기

a, b = b, a
print('a = %d, b = %d' %(a,b))

'''
복합 대입연산자
    +=
        ex) x += 3 -> x = x + 3 같다
    -=
        ex) x -= 3 -> x = x - 3 같다
'''

piggy_bank = 0
money = 10000
piggy_bank += money
print(f'저금통에 용돈 {money}원을 넣었습니다')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다')

snack = 2000
piggy_bank -= snack
print(f'저금통에서 스낵 구입비 {snack}원을 뺏습니다')
print(f'지금 저금통에는 {piggy_bank}원이 있습니다')


