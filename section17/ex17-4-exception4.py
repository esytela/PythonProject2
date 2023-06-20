'''
try:
    정상코드 영역
except:
    예외 발생시 처리영역
else:
    예외가 발생하지 않으면 처리되는 영역
finally:
    항상 실행되는 영역
'''

try:
    print('서버에 접속 합니다.')
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))

    result = a/b

except:
    print('예외가 발생했습니다')
else:
    print('{} / {} = {}'.format(a,b,result))
finally:
    print('서버 접속 종료합니다.')