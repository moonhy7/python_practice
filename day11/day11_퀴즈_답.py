
# 퀴즈1 : 웹상의 json 파일을 파이썬의 딕셔너리 리스트로 생성하고 총 몇개인지 출력하여라.
# url - http://jsonplaceholder.typicode.com/photos

import json

# url 데이타 획득1 : urllib.request
# from urllib.request import urlopen
# url = 'http://jsonplaceholder.typicode.com/photos'

# request = urlopen(url)
# photos_list = json.loads(request.read())
# print(photos_list)
# print(f'총 갯수 = {len(photos_list)}')

# url 데이타 획득2 : requests
# requests 는 외장 모듈
# pip install requests
import requests
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
photos_list = json.loads(response.text)
print(photos_list [:2])
print(f'총 갯수 = {len(photos_list )}')


# # 퀴즈2 : 퀴즈 1의 딕셔너리 리스트에서 마지막 딕셔너리 리스트를 아래와 같은 형식으로
# # 출력하여라
'''
albumId => 100
id => 5000
title => error quasi sunt cupiditate voluptate ea odit beatae
url => https://via.placeholder.com/600/6dd9cb
thumbnailUrl => https://via.placeholder.com/150/6dd9cb
'''

print('\n'*3)
for key in photos_list[-1]:
  print(f'{key} => {photos_list[-1][key]}')


# # 퀴즈3 : 퀴즈 1의 딕셔너리 리스트에서 albumId 가 22인 딕셔너리 리스트에서
# # title 과 url 값만 모두 출력하여라

print('\n'*3)
cnt = 0
for i in range(len(photos_list)):
  if photos_list[i]['albumId']==22:
    print('-'*30,'\n','title : ', photos_list[i]['title'],'\n','url : ', \
          photos_list[i]['url'] )
    cnt += 1
print('-' * 70)
print(f'총 갯수 - {cnt}')



# # 퀴즈4 : 퀴즈 1의 딕셔너리 리스트에서 10개만 json 파일로 저장하여라.

with open('output/photos10.json', 'w') as f:
  json.dump(photos_list[:10], f, indent='\t')


#
# # 퀴즈5 : 퀴즈4에서 생성된 json 파일을 이용하여 딕셔너리 리스트를 생성하고
# # 출력하여라.

'''
key = albumId, value = 1
key = id, value = 1
key = title, value = accusamus beatae ad facilis cum similique qui sunt
key = url, value = https://via.placeholder.com/600/92c952
key = thumbnailUrl, value = https://via.placeholder.com/150/92c952

...
'''

print('\n'*5)
with open('output/photos10.json') as f:
  datalist_dict = json.load(f)
  print(datalist_dict)
  for item in datalist_dict:
    print('$'*30)
    for key in item:
      print(f'key = {key}, value = {item[key]}')


# 퀴즈 6 : 아래 주소를 참조하여 기상청 육상 중기예보 RSS 데이타에서
# 부산 지역과 관련된 데이타만 출력하여라.
# https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


print('\n\n 퀴즈6====')
url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
request = urlopen(url)

xml_str = request.read()
soup = BeautifulSoup(xml_str ,'xml')
location_tags = soup.find_all('location')
# print(len(location_tags))


pusan_list = []
for location in location_tags:
    if location.find('city').text == '부산':
        for data in location.find_all('data'):\
            pusan_list.append([ data.find('mode').text, data.find('tmEf').text,
                                data.find('wf').text, data.find('tmn').text,
                                data.find('tmx').text, data.find('rnSt').text ])

print(pusan_list)
field_list = ['mode', 'tmEf', 'wf', 'tmn', 'tmx', 'rnSt']
print(pd.DataFrame(pusan_list, columns=field_list))



# 퀴즈 7 : 아래 주소를 참조하여 기상청 육상 장기예보 1개월 전망 데이타에서
# '강원도 영서'와 '강원서 영동' 지역과 관련된 데이타만 csv 파일로 저장하여라.
# https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20210107.xml

from bs4 import BeautifulSoup
import pandas as pd

print('\n\n 퀴즈7====')
url = "https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20210107.xml"
request = urlopen(url)
xml_data = request.read()
soup = BeautifulSoup(xml_data, 'xml')
# 강원도 영서
local_ta_data1 = soup.find_all('local_ta')[2]
print(local_ta_data1)
# 강원도 영동
local_ta_data2 = soup.find_all('local_ta')[3]
print(local_ta_data2)

location_list = ['강원도 영서', '강원도 영동']
result_list = []
idx = 0
for i in range(2,4):
    local_ta_data = soup.find_all('local_ta')[i]
    print(local_ta_data)
    data_tags = local_ta_data.find_all('week_local_ta')
    temp = []
    for data in data_tags:
        print(data.text)
        temp.append(data.text.split('\n'))
    print('======')
    print(temp)
    for row in temp:
        row.remove('')
        row.remove('')
        row.insert(0, location_list[idx])
    idx += 1
    result_list.extend(temp)
print(result_list)

df = pd.DataFrame(result_list)
print(df)
df.to_csv('output/kangwon.csv', encoding='utf-8', index=False)


# 퀴즈 8 : 아래 주소를 참조하여 구글 뉴스의 RSS 에서 item태그와 관련된 데이타만  저장하여라.
# 구글 뉴스 RSS : https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko

print('\n\n 퀴즈8====')
url = 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko'
request = urlopen(url)
soup = BeautifulSoup(request.read(),'xml')

temp = []
for data in soup.find_all('item'):
    temp.append([data.find('title').text.replace('\'','').replace('\"','').replace('“','')[:20],
                 data.find('pubDate').text[:-7],data.find('source').text])
df = pd.DataFrame(temp,columns=['title','pubDate','source'])
print(df)
df.to_csv('output/news.csv', encoding='utf-8', index=False)



# 퀴즈 9 : 퀴즈 6의 부산지역 데이타를 json 구조로 변경하고 json 파일로 저장하여라.
print('\n\n 퀴즈9====')
field_list = ['mode', 'tmEf', 'wf', 'tmn', 'tmx', 'rnSt']

from bs4 import BeautifulSoup
url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
request = urlopen(url)

xml_str = request.read()
soup = BeautifulSoup(xml_str ,'xml')
location_tags = soup.find_all('location')

pusan_list = []
for location in location_tags:
    if location.find('city').text == '부산':
        for data in location.find_all('data'):
            pusan_list.append({ 'mode':data.find('mode').text,
                                'tmEf':data.find('tmEf').text,
                                'wf':data.find('wf').text,
                                'tmn':data.find('tmn').text,
                                'tmx':data.find('tmx').text,
                                'rnSt':data.find('rnSt').text })

print(pusan_list[0])

with open('output/location_busan.json','w', encoding='utf-8') as f:
    json.dump(pusan_list, f, indent='\t', ensure_ascii=False)
