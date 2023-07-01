'''
데이터 시각화 (data visualization)

matplotlib.org에 들어가서 그래프 코드들 보기
'''

import matplotlib.pyplot as plt

#figure 객체 생성
figure = plt.figure() #그래프가 나오는 창을 figure이라 함

axes = figure.add_subplot(111) #행, 열, 번호 (222)입력해서 보기
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',]
y = [1200, 800, 500, 400, 700, 800]
axes.plot(x, y, linestyle='dotted', marker='^', color='red')
plt.show()

