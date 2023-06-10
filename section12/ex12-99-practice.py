import random
import time

pot = [n for n in range(1,46)] #1부터 45까지 for문으로 돌아서 리스트 만듬

jackpot = []

for n in range(1,7):
    random.shuffle(pot) #리스트 순서를 섞음

    pick = pot.pop()
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick)
    time.sleep(1) #1초 동안 프로그램 일시정지

jackpot.sort()
print('이번 당첨번호는 {}입니다.'.format(jackpot))
