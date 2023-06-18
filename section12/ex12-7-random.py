'''
random - 난수 생성 모듈
'''

import random

# 두 인자 사이 난수
print(random.randint(1,10)) #1 ~ 10 사이 랜덤 숫자 생성

#range 함수 비슷
print(random.randrange(10))
print(random.randrange(1,10))
print(random.randrange(1,10,2)) #1에서 2를 더한 값들만 나옴

print(random.random())
if random.random() < 0.5:
    print('안녕하세요')
# 50%확률로 print 안녕하세요

#choice 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

#shuffle() 함수 - 임의로 섞는 함수
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

