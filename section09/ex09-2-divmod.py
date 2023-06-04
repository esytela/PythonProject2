'''
divmod() 함수
    두 숫자를 인자로 전달 받아
    첫번째 인자를 두번째 인자로
    나눈 몫과 나머지를 tuple 형식으로 반환
'''

money = 10000
price = 3000
result = divmod(money,price)
print(f'빵을 {result[0]}개 사고 {result[1]}원이 남았습니다')