# 데이타 수집
# 동네예보 > 시간별예보
# http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp

# 지역 검색 후 xml 정보 페이지로 이동하기
# 예시 - https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1154551000
# Reference : http://www.weather.go.kr/images/weather/lifenindustry/dongnaeforecast_rss.pdf


# 모듈 임포트
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# url 획득
# http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# 지역 검색후 url 복사
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1154551000'
request = urlopen(url)
data = request.read()
print('\n\n data => String')
print(data)

# xml 파싱 => soup 객체
soup = BeautifulSoup(data, 'xml')
print('\n\n soup data => ')
print(soup)

print('\n\n  pubdate, category ')
print('오늘날짜 => ', soup.find('pubDate').text)
print('지역 => ', soup.find('category').text)
location = soup.find('category').text
today = soup.find('pubDate').text
'''
오늘날짜 =>  2021년 01월 13일 (수)요일 14:00
지역 =>  서울특별시 금천구 가산동
'''

print('\n\n  data 태그의 seq 속성값이 0')
data_0 = soup.find_all('data', {'seq':0})
print(data_0)
for tag in data_0:
    print('시간 => ', tag.find('hour').text)
    print('평균 온도 => ',tag.find('temp').text)
    print('기상 예보 => ' , tag.find('wfKor').text)


print('\n\n  2차원 데이타 구조로 저장하기 ')
location = soup.find('category').text
today = soup.find('pubDate').text
data_tags = soup.find_all('data')
data_list = []
for tag in data_tags:
    data_list.append([today[:-6],location, tag.find('hour').text,
                      tag.find('temp').text, tag.find('tmx').text,
                      tag.find('tmn').text, tag.find('wfKor').text])
print(data_list)

'''
<hour>3</hour>
<day>1</day>
<temp>-3.0</temp>
<tmx>7.0</tmx>
<tmn>-4.0</tmn>
<sky>1</sky>
<pty>0</pty>
<wfKor>맑음</wfKor>
<wfEn>Clear</wfEn>
<pop>0</pop>
<r12>0.0</r12>
<s12>0.0</s12>
<ws>1.1</ws>
<wd>0</wd>
<wdKor>북</wdKor>
<wdEn>N</wdEn>
<reh>80</reh>
<r06>0.0</r06>
<s06>0.0</s06>
'''

print('\n\n  데이타프레임으로 구조 변경 ')
df = pd.DataFrame(data_list, columns=['날짜', '지역', '시간', '평균온도', '최고온도', '최저온도', '예보'])
print(df)

df.to_csv('output/2021년01월13일_가산동.csv', index=False, encoding='utf-8')

# 엑셀로 저장하기
# 데이타프레임변수.to_excel(엑셀파일경로, index=False, encoding='utf-8')
df.to_excel('output/2021년01월13일_가산동.xlsx', index=False, encoding='utf-8')



