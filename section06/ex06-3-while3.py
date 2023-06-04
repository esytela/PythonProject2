my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요 (종료는 0입니다) >>>'))
    my_list.append(n)

my_list.pop()
#my list에 0이 추가가 되지만 pop을 통해 마지막 값인 0이 빠짐
print(my_list)
