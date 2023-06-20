'''
BeautifulSoup
    HTML, XML 등의 마크업 (<>) 언어를 파싱하는 (해석하고 분석하는) 라이브러리
    ex) <html>텍스트</html>

BeautifulSoup 설치방법
pip install beautifulsoup4

https://news.nate.com/rank?mid=n1000

'''
import requests
from bs4 import BeautifulSoup

url = 'https://news.nate.com/rank'
param = {'mid': 'n1000'}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('h2')
for tit in tit_list:
    print(tit.text.strip())

#랭킹 뉴스의 제목들만 따로 골랐음
# h2 class에 있는 것들을 다 골라서 tit_list에 넣어서 프린트함