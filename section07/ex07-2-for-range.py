'''
for 문과 range 함수
    range()
        연속된 숫자를 만들어주는 함수
'''

dan = int(input('출력할 구구단을 입력하세요 >>>'))

'''
range(stop)
'''

#0~9 range
for n in range(10):
    print(f'{dan}x{n}={dan*n} ', end='')
print()

'''
range(start, stop)
'''
#1~9
for n in range(1,10):
    print(f'{dan}x{n}={dan*n} ', end='')
print()

'''
range(start, stop, step)
'''
#1부터 2씩 증가 그러나 10보다 작음
for n in range(1, 10, 2):
    print(f'{dan}x{n}={dan * n} ', end='')
print()