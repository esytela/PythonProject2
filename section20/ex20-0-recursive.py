'''
재귀함수 (Recursive function)
    함수 내부에서 자기자신 호출하는 것을 말한다
'''

def count_number(n):
    while n > 0:
        print(n)
        n -= 1

def recursive_count_number(n):
    print(n)
    if(n <= 0):
        return
    recursive_count_number(n - 1)


#실행코드
#count_number(5)
recursive_count_number(5)