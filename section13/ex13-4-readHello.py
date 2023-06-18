
# open 함수 모드
    # r(read mode): 읽기 전용 모드 / 파일 없으면 에러

# 경로(path)
   # 파일 시스템에서 파일이나 디렉터리 위치를 나타내는 문자열

    # 1. 절대경로 (absolute path)
      #  파일 시스템 루트 디렉터리부터 출발하여 파일이나 디렉터리를 찾는 경로
       # ex) "C:\Users\estel\PythonProject2\section13\hello.txt"
        #루트경로
         #   1. C:\ - Window
          #  2. / - Linux, Mac

    # 2. 상대경로 (relative path)
      #  현재 작업 디렉터리를 기준으로 파일이나 디렉터리를 찾는 경로
       # ex) ./hello.txt
        # . -> 현재 폴더


#file = open('절대경로, 상대경로 넣어도 됨', 'rt', encoding='UTF-8')
file = open('hello.txt', 'rt', encoding='UTF-8')
str = file.read()
print(str, end='')
file.close()

with open('./hello.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')



