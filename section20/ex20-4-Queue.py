'''
큐(Queue)
    컴퓨터 기본적인 자료구조의 한가지로,
    먼저 집어 넣은 데이터가 먼저 나오는
    FIFO (First in First outpout)
    저장하는 형식을 말한다

    데이터를 가져오면서 데이터가 살아진다

Stack = 가장 먼저 들어온게 제일 마지막에 들어옴
'''

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    while queue:
        print('Get Value: ', queue.pop(0))


#실행코드
Queue()