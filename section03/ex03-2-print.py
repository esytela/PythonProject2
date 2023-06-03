'''
print()함수 사용법
sep : 출력할 value의 구분 문자
end : value 출력 후 출력할 문자 (기본값 '\n')
file : 출력 방향 지정
'''
print('재미있는', '파이썬')
print('Python', 'Java', 'C', sep=', ')

print('안녕', end='')
print('하세요')

fos = open('sample.py', mode='wt') #wt = write text
print('print("HelloWorld")', file=fos)
fos.close()