from tkinter import *
import time

tk = Tk()
#canvas 위젯 생성 및 크기 설정
canvas = Canvas (tk, width=500, height=500) # 그림 그릴 수 있는 객체
canvas.pack()

# 다각형 그리기
canvas.create_polygon(250, 400, 275, 450, 225, 450) # (x1, y1, x2, y2, x3, y3) 삼각형의 좌표
canvas.create_polygon(250, 400, 275, 450, 225, 450)

for i in range(0, 70):
    canvas.move(1, -5, -5)
    canvas.move(2, 5, -5)

    tk.update() #for 문 돌때마다 움직임. update가 움직임의 정보를 넣음
    time.sleep(0.05)

