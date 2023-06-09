'''
조건문
    특정 조건을 만족하는지 여부에 따라
    실행하는 코드가 달라야 할 떄 사용하는 명렁어

방법 1
    if 조건식:
        조건식이 참일 경우 실행할 코드
    else:
        조건식이 거짓일 경우 실행할 코드

3.
    if 조건식1:
        조건식1 참 실행할 코드
    elif 조건식2:
        조건식2 참 실행할 코드
    elif 조건식3:
        조건식3 참 실행할 코드
    else:
        모든 조건식 거짓일 떄 실행할 코드
'''
#아까랑 다른 것은 if가 먼저 나온 다음 조건이 나옴
#전에는 조건식이 먼저 나오고 그 다음에 if가 나옴

a = 100
b = 200
if b > a:
    print('b는 a보다 크다.')

a = 4
b = 7
if b >= a:
    print('b는 a보다 크거나 같다.')
else:
    print('b는 a보다 작다')

#if ~ elif ~ else
b = 5
if b == 1:
    print('1')
elif b == 2:
    print('2')
elif b == 3:
    print('3')
else:
    print('1,2,3 모두 아니다.')