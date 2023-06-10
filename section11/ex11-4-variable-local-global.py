'''
지역변수 (local)
    함수 내부에 선언
    함수 내부에서만 사용 가능
    함수 종료시 같이 소멸

전역변수 (global)
    함수외부선언
    함수내부 외부 모두 사용 가능
'''

gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal()

def globalAndLocal2():
    lVar = '지역' #여기에 있는 지역 변수 삭제하면 에러. 왜냐면 내부에 없기 때문에
    #그러나 전역변수가 없어도 사용 가능. 밖에서 define했기 때문에
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal2()


gVar = '전역'
def globalAndLocal3():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역' #이름만 같지 새로운 지역변수이다
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal3()

# 전역변수 선언
total = 0
def gift(dic, who, money): #변수명이 dic라고 dictionary가 되는 것이 아님
    global total # 전역변수 total를 사용하겠다
    total += money
    dic[who] = money #여기도 dictionary 정의

wedding = {} #이렇게 정의하기 때문에 dictionary가 된것
gift(wedding, '영희', 5) #wedding: {'영희':5}, total = 5
gift(wedding, '철수', 6) #total = 11
gift(wedding, '이모', 10) #total =21

print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))


'''
컴퓨터 메모리 구조
코드 영역 -> 데이터 영역 -> 입형역 -> 스택영역
'''