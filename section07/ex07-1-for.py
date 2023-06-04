'''
for문
    값의 범위나 횟수가 정해져 있을때 사용
    while문보다 사용빈도 높다

for 변수 in 반복가능한 객치:
    반복실행문

'''

pwd = input ('비밀번호를 입력하세요 >>>')

ch_count = 0
num_count = 0

for ch in pwd:
    if ch.isalpha(): #ch.isalpha = ch변수에 문자여부
        ch_count += 1
    elif ch.isnumeric(): #숫자여부
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다')
else:
    print('불가능한 비밀번호 입니다')