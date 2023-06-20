'''
URL(Uniform Resource Locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을수 있는 주소

    ex) https://news.nate.com:443/rank?mid=n1000

프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 표준화된
    규칙, 절차 혹은 통신 프로세스를 의미

    ex)
        http/https - 웹서버 프로토콜
        ftp - 파일서버 프로토콜
        mailto - 메일 서버 프로토콜
        telnet - 원격지 프로토콜

호스트(host)
    리소스가 위치한 서버의 이름
    ex) news.nate.com, naver, google

포트(Port)
    서버에서 사용하는 방번호
    ex) http - 80, https - 443

경로(path)
    웹서버에서 자원에 대한 경로(물리적 또는 추상적 경로)
    ex) /rank

쿼리(query) - 추가로 서버에 보내는 데이터(파라미터)
    ex) mid=n1000
        key1=value1&key2=value2
'''
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
news_list = soup.find_all('div', class_='list_content')

for news in news_list:
    news_title = news.text.strip().split('\n')[0]
    print(news_title)








