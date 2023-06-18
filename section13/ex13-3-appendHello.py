'''
open함수 모드
    a(append mode) : 추가 모드
'''

file = open('hello.txt', 'at', encoding='UTF-8')
file.write('Hello\n')
file.write('Nice to meet you\n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')
file.close()

