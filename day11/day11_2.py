# RSS 정보 이용하기
# https://ko.wikipedia.org/wiki/RSS
# RSS(Really Simple Syndication, Rich Site Summary)란
# 블로그처럼 컨텐츠 업데이트가 자주 일어나는 웹사이트에서,
# 업데이트된 정보를 쉽게 구독자들에게 제공하기 위해 XML을 기초로 만들어진 데이터 형식이다.

# 예) 동네예보 > 시간별예보
# http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp

# 예 ) 기상청 전국날씨 RSS
# description :
# http://www.weather.go.kr/images/weather/lifenindustry/midtermforecast_rss.pdf
# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

# 웹상의 URL 데이타읽기
# urllib.request
# https://docs.python.org/3.8/library/urllib.html
# 모듈 임포트
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# request객체 = urlopen(url경로)
# data = request객체.read()

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urlopen(url)
xml_data = request.read()
print(type(xml_data)) # <class 'bytes'>
print(xml_data)

# xml 파싱 : soup 객체
soup = BeautifulSoup(xml_data, 'xml')
print('\n\n=== soup 객체')
print(soup)

print('\n\n=== title 태그')
title_tags = soup.find_all('title')
print(title_tags[0])
print(len(title_tags))
for tag in title_tags:
    print(tag.text)

print('\n\n=== wf 태그 : 기상전망')
# <![CDATA[ => 자바스크립트 주석
wf_tags = soup.find_all('wf')
print('갯수는?', len(wf_tags))
for i in range(3):
    print(wf_tags[i].text)

print('\n\n=== province 태그 :  지역코드에 따른 지역명(서울ㆍ인천ㆍ경기도)')
print('=== city 태그 :  예보구역코드에 따른 지역명')
province_tags = soup.find_all('province')
city_tags = soup.find_all('city')
print('province, city 갯수는?', len(province_tags), len(city_tags))
# province, city 갯수는? 41 41
for tag1, tag2 in zip(province_tags, city_tags):
    print(tag1.text,' :: ', tag2.text)


print('\n\n=== 서울ㆍ인천ㆍ경기도  ::  서울 지역의 데이타만 출력하기')
seoul_data = soup.find_all('location')[0]
# print(seoul_data)
data_tags = seoul_data.find_all('data')
data_list = []
for tag in data_tags:
    data_list.append(['서울', tag.find('tmEf').text,
                      tag.find('wf').text, tag.find('tmn').text,
                      tag.find('tmx').text, tag.find('rnSt').text])
print(data_list)
df = pd.DataFrame(data_list,
                  columns=['지역', '년월일 시분', '날씨예보', '최저온도', '최고온도', '강수확률'])
print(df)

'''
<mode>A02</mode>
<tmEf>2021-01-16 00:00</tmEf>
<wf>맑음</wf>
<tmn>-7</tmn>
<tmx>-2</tmx>
<reliability/>
<rnSt>0</rnSt>
'''