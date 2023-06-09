'''
continue
    while 문이나 for문과 같은 반복문을 강제로 건너뛰게 한다
'''


total = 0
for a in range (1,101):
    if a % 3 == 0: #3의 배수
        continue
    total += a
    print('a: {}, total {}'.format(a, total))
#3의 배수 빼고 1부터 100까지 다 더하겠다는 뜻이다

print(total)