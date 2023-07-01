# 구름 형태 문자
import wordcloud
import matplotlib.pyplot as plt

words = {
    'Python':10,
    'Java':5,
    'C':7,
    'C++':9,
    'JSP':12
}

wc = wordcloud.WordCloud()
cloud = wc.generate_from_frequencies(words)
plt.figure()
plt.imshow(cloud)
plt.show()