import random
import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(121)
axes2 = figure.add_subplot(122)

x = [n for n in range(101)] # 0부터 100까지 다 넣음 [0,1,2,3,...100] 와 같음
y1 = []
y2 = []

for i in range(101):
    y1.append(random.randint(0,100)) #0에서 100사이 난수 값을 append 함
    y2.append(random.randint(0,100))

axes.plot(x, y1, color='r', marker='.')
axes2.bar(x, y2, color='g')
plt.show()

