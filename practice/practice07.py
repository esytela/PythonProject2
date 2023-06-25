'''
가계부
- int(input)을 이용
- for dict 을 이용하여 사용내역 보기
- class 를 이용하여 어디에 사용했는지 지정
'''

food = int(input('음식 금액>>'))
date = int(input('데이트 금액>>'))
movie = int(input('영화 금액>>'))
cafe = int(input('카페 금액>>'))

use_dict = {
    '음식': food,
    '데이트': date,
    '영화': movie,
    '카페': cafe,
}

total = food + date + movie + cafe
for use in use_dict:
    print('{}의 사용 금액은 {}입니다'.format(use))
    print('총 사용 금액은 {}입니다'.format(total))