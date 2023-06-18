'''
파일복사
    원본 읽기 -> 버퍼 (Memory 저장) -> 복사본 쓰기

open 함수 모드
    b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력
'''

buffer_size = 1024 # 1024 byte -> 1kb
with open('../section13/hello.txt','rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)

print('hello2.txt 파일이 복사 되었습니다')
