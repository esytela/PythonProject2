'''
반복문
    어떤 수행 작업을 한번이 아니라 계속해서 수행해야할 떄 사용

1. while 문
    특정 조건을 만족하는 동안 반복해서 수행하는 명령어

    while 조건식:
        반복 실행코드
'''

n = 10
while n==0:
    print(n)
    n -= 1 # n = n-1

print('while문 끝나고 n의 값:{}' .format(n))