a = int(input('숫자 입력 >>'))
b = int(input('숫자2 입력 >>'))

result = a + b

if result <=10:
    print('{}는 10보다 작은 숫자'.format(result))
elif result > 10 and result < 20:
    print('{}는 10보다 크고 20 보다 작다'.format(result))
elif result > 20 and result < 30:
    print('{}는 20보다 크고 30보다 작다'.format(result))
else:
    print('{}는 30보다 큰 숫자'.format(result))