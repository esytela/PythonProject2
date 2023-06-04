total = 0
for a in range (1,101):
    if a % 3 == 0: #3의 배수
        continue
    total += a
    print('a: {}, total'.format())

print(total)