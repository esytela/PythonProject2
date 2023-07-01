from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path = 'C:\Windows\Fonts\malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
data = [0.18, 0.3, 3.33, 3.75, 0.38, 2.5, 0.25, 2.75, 0.1]
vitamin = ['vitamin A','vitaminB1', 'vitamin B2', '나이아신', 'vitamin B6',
           'vitamin C', 'vitaminD', 'vitamin E', 'magnesium']
axes.pie(data, labels=vitamin, autopct='%0.1f%%')
plt.axis('equal')
plt.show()
