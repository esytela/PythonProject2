'''
크롤링
- 이전에 되던게 안될수도 있음, 왜냐면 주기적으로 html을 바꿔주거나 못 알아보게 바꿈
'''

import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p',class_='title') #BeautifulSoup이 p태그를 찾고 p태그중 class_가 title인것만 찾음
artist_list = soup.find_all('p', class_='artist')

for idx, title in enumerate(music_list):
    print(idx+1, end='\t') #인덱스가 0부터니까 +1한것
    print(title.text.strip(), end='-') #실제 텍스트 값만 가져옴
    print(artist_list[idx].find_all('a')[0].text.strip()) #text.strip 실제 텍스트 값만 가져옴
    #find_all[0] -> 아티스트 이름이 구대인 가수들이 있어서 첫번째만 나오게 하기 위해서 find_all[0]을 쓴것

