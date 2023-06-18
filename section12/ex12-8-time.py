'''
time 모듈
    시간 처리에 관련된
'''

import time
#1970년1월1일부터 1일1시부터 시간을 계산 (timestamp)
print(time.time())

#ctime() 함수 - 인수로 전달된 time을 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

# 인수로 전달된 날짜와 지시지를 이용하여 형식을 갖춘
# 날짜 데이터를 문자열로 반환
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y년 %m월 %d일 %H:%M:%S'))

#인코딩 문제 발생시 아래와 같이 사용하면 된다
print(time.strftime (
'%Y년 %m월 %d일'
    . encode('unicode-escape')
    . decode()
.encode() .decode('unicode-escape')
))

#인자 초만큼 시스템 일시중지
time.sleep(1)

sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
