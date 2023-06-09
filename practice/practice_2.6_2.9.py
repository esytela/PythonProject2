thistuple = ('피카츄', '라이츄', '파이리')
print(thistuple)

thisset = {'오빠', '바보', '똥꼬'}
print(thisset)

for x in thisset:
    print(x)

a, b = 10, 20
print('a = %d, b = %d' % (a, b)) #여기 왜 % (a,b)

my_list = []
n = int(input('정수를 입력하세요 (종료는 0입니다.) >>>'))
#입력하는 숫자를 캐스팅해서 정수로 바꿈
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요 (종료는 0입니다.) >>>'))

print(my_list)

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요 (종료는 0입니다) >>>'))
    my_list.append(n)

my_list.pop()
#my list에 0이 추가가 되지만 pop을 통해 마지막 값인 0이 빠짐
print(my_list)

'''
 6-2와 6-3이 같은 결과를 보임. 왜 6-2에 리스트에 마지막에 0이 안 들어갔지
'''