'''
파일 입출력 (I/O - Input/Output)
    입력(input) 기존 파일 읽어들이는 것
    출력(Output) 파일생성, 내용추가

open()함수
    파이썬에서 open()함수를 사용하여 파일을 열고 파일객체 생성,
    이를 통해 파일을 읽고 쓸 수 있다
'''

'''
file = open('myFile.txt', 'wt')
print('myFile.txt 파일이 생성되었습니다.')
file.close()
'''

# with 문 - 자동으로 close()를 해준다 (위에꺼랑 같음)
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')

