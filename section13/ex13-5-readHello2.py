'''
file 객체 read() 함수
    read() -> 전체 읽어오기
    read(인자값) -> 인자값 크기 만큼 읽어오기

'''
file = open('hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5) #공백과 \n 을 포함해서 5문자씩 읽음
    if not str: #읽을 값이 없으면 True 된다
        break
    print(str)
file.close()


