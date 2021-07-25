# tsv 파일 다루기
# TSV 파일
# CSV 파일과 비슷하지만,
# 콤마 대신 Tab으로 컬럼을 분리하는 파일포맷
# TSV 파일은 컬럼 delimiter만 차이가 나므로,
# csv 모듈의 reader() 혹은 writer() 함수에서
# delimiter='\t' 옵션만 지정해 주면 나머지는 CSV와 동일하다.

# 파일변수 = open(url, 'r', encoding='cp949/utf-8')
# csv객체변수 = csv.reader(파일변수, delimiter='\t')
# 파일변수.close()

# 파일변수 = open(url, 'w', encoding='cp949/utf-8')
# csv객체변수 = csv.writer(파일변수)
# csv객체변수.writerow(리스트/튜플...)
# 파일변수.close()


# sample Data
# https://www.kaggle.com/gbahdeyboh/gapminder
# gapminder.tsv => 년도별 전세계 인구, 평균수명, GDP ... 데이타

import csv
import pandas as pd

# tsv 파일은 \t 가 데이타가 삽입된 구조
# delimiter='\t'
with open('data/gapminder.tsv', 'r', encoding='cp949') as f:
    # tsv_data = csv.reader(f, delimiter=',') # 한행에 하나씩 데이타
    tsv_data = csv.reader(f, delimiter='\t') # '\t' 로 데이타를 분리시킨 구조
    data_list = list(tsv_data)
    print(data_list)

# 나라명만 중복없이 리스트로 만들기
print(data_list[0])
# ['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']
country_list = []
for country, continent, year, lifeExp, pop, gdpPercap in data_list[1:]:
    country_list.append(country)
print('*'*50)
print(country_list)
# 중복 제거후 리스트화
country_list = list(set(country_list))
print(country_list)
print('#'*50)
# 정렬
country_list = sorted(country_list)
print(country_list)
print(len(country_list))

#  대한민국 나라명을  country_list에서 찾아서 출력하여라
# 힌트 Korea / korea / KOREA 가 들어가있다.
for item in country_list:
    if item.upper().find('KOREA') != -1:
        print(item)
'''
Korea, Dem. Rep.
Korea, Rep.
'''

# 대한민국 데이타만 찾아서 리스트로 저장하기
f = open('data/gapminder.tsv', 'r', encoding='cp949')
tsv_data = csv.reader(f, delimiter='\t') # '\t' 로 데이타를 분리시킨 구조
data_list = list(tsv_data)
f.close()

korea_list = []
for country, continent, year, lifeExp, pop, gdpPercap in data_list[1:]:
    if country == 'Korea, Rep.':
        korea_list.append([country, continent, year, lifeExp, pop, gdpPercap])
print(korea_list)
print('='*50)
# 맨앞에 필드행 추가하기
korea_list.insert(0, data_list[0])

for country, continent, year, lifeExp, pop, gdpPercap in korea_list:
    print(country, continent, year, lifeExp, pop, gdpPercap)

# tsv 파일로 저장하기
# output/korea.tsv
# 파일변수 = open(url, 'w', encoding='cp949/utf-8', newline='')
# tsv객체변수 = csv.writer(파일변수, delimiter='\t')
# 한행씩 저장하기
# tsv객체변수.writerow(리스트/튜플...)
# 모두 저장하기
# tsv객체변수.writerows(리스트/튜플...)
# 파일변수.close()

f = open('output/korea.tsv', 'w', encoding='utf-8', newline='')
tsv_data = csv.writer(f, delimiter='\t')
tsv_data.writerows(korea_list)
f.close()

# 2000년 이후의 데이타만 gapminder_2000.tsv 파일로 저장하여라.
with open('data/gapminder.tsv', 'r', encoding='cp949') as f:
    tsv_data = csv.reader(f, delimiter='\t')
    data_list = list(tsv_data)
    print(data_list[1])
    # ['Afghanistan', 'Asia', '1952', '28.801', '8425333', '779.4453145']

result2000 = []
for country, continent, year, lifeExp, pop, gdpPercap in data_list[1:]:
    if int(year) >= 2000:
        result2000.append([country, continent, year, lifeExp, pop, gdpPercap])

print(result2000)
for country, continent, year, lifeExp, pop, gdpPercap in result2000:
    print(country, continent, year, lifeExp, pop, gdpPercap)

# 맨앞에 필드행 추가하기
result2000.insert(0, data_list[0])

with open('output/gapminder_2000.tsv', 'w', encoding='utf-8', newline='') as f:
    tsv_data = csv.writer(f, delimiter='\t')
    tsv_data.writerows(result2000)
