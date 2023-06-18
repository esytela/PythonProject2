file = open('hello.txt', 'wt', encoding='UTF-8')
#encoding = 'UTF-9'은 한국어를 출력함
file.write('안녕하세요')
file.write('\n')
file.write('반갑습니다')
file.write('\n ')
print('hello.txt 파일이 생성되었습니다')
file.close()