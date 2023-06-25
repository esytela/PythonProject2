num = 2
while num < 10:
    n = 1
    while n < 10:
        print((f'{num} * {n} = {num*n}\t'), end='')
        n += 1
    num += 1
    print()

a = int(input('숫자 입력>>'))
b = int(input('숫자 입력>>'))
result = a*b
print('{}와{}를 곱하면 {}입니다'.format(a,b,result))
