try:
    a = int(input('제수를 입력하세요 >>>'))
    b = int(input('피제수를 입력하세요 >>>'))
    print('{} / {} = {}'.format(a, b, a/b))
    print('정상종료')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다')
except:
    print('예외가 발생했습니다')