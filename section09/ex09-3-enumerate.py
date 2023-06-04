'''
enumerate() 함수
    list, tuple, string 등 자료형을 입력 받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다
'''

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print(f'{month+1}월 = {day}일')