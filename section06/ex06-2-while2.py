my_list = []
n = int(input('정수를 입력하세요 (종료는 0입니다.) >>>'))
#입력하는 숫자를 캐스팅해서 정수로 바꿈
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요 (종료는 0입니다.) >>>'))

print(my_list)