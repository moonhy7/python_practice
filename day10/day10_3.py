# xml 이란?
# eXtensible Markup Language
# 데이타 전송 목적. 다목적 마크업 언어.
# Open API
# https://www.w3schools.com/Xml/

# XML 문법
# 여는 태그와 닫는 태그로 구성 => 요소(Element)
# 1. <태그> ... </태그>
# 2. <태그 />

# 예시 : 노트의 XML 구조
'''
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
'''

# person xml 구조 => name, id, age, address
'''
<person>
    <name>홍길동</name>
    <id>hong100</id>
    <age>22</age>
    <address>서울</address>
</person>
'''
# 트리구조
# 루트태그는 하나이다.
# 부모태그(parent), 자식태그(child)
# 속성 atrribute
# 1. <태그 속성1=값1 속성2=값2 속성3=값3 ...>...</태그>
# 2. <태그 속성1=값1 속성2=값2 속성3=값3 ... /태그>

# xml.etree.ElementTree 모듈
# xml 처리 모듈 - 파이썬의 내장모듈
# https://docs.python.org/3/library/xml.etree.elementtree.html
# 파싱(Parsing)이란 가공되지 않은 데이터에서 원하는 특정한 문자열을 빼내는 작업

# 관련 함수를 바로 사용할 수 있게 모듈 임포트
from xml.etree.ElementTree import *
import csv
import pandas as pd

# 외부 xml 파일 불러오기
'''
샘플 xml 파일 생성하기 
data/country_data.xml 
소스는 아래 참조 
https://docs.python.org/3/library/xml.etree.elementtree.html
'''
# xml객체 = parse(xmlURL)
tree = parse('data/country_data.xml')
print(tree, type(tree))
# <xml.etree.ElementTree.ElementTree object at 0x0000027E8BD09FD0>
# <class 'xml.etree.ElementTree.ElementTree'>

# 루트 찾기 getroot()
# 루트객체 = xml객체.getroot()
root = tree.getroot()
print(root, type(root))
# <Element 'data' at 0x0000025337AA14F0> <class 'xml.etree.ElementTree.Element'>
# tag : 객체의 태그명 표시
# attrib : 객체의 태그 속성 , 딕셔너리
print(root.tag) # data
print(root.attrib) # {}

# root의 자식요소 찾기
for child in root:
    print(child.tag, child.attrib)
'''
    country {'name': 'Liechtenstein'}
    country {'name': 'Singapore'}
    country {'name': 'Panama'}
'''

# root의 자식요소의 자식요소 찾기
for child in root:
    print('step1', child.tag, child.attrib)
    for child_sub in child:
        print('\tstep2', child_sub.tag, child_sub.attrib)
    print('='*50)

# 특정 태그의 정보 확인하기
# 루트객체.iter(자식요소의태그)
# 모든 neighbor 태그의 속성 출력하기
print('=== neighbor 태그의 모든 속성  ')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print('=== country 태그의 모든 속성  ')
for country in root.iter('country'):
    print(country.attrib)

# text : <태그>..</태그> 태그안에 삽입된 문자열 부분
# find(태그명) : 첫번째 태그만 반환
# findall(태그명) : 모든 태그 반환 => 집합형
print('=== country 태그의 하위 태그 정보  ')
for country in root.findall('country'):
    print('rank => ', country.find('rank').text)
    print('year => ', country.find('year').text)
    print('gdppc => ', country.find('gdppc').text)
    print('\n')

# find, findall
print(root.findall('country'))
# [<Element 'country' at 0x000001C96ABC2540>, <Element 'country' at 0x000001C96AD104A0>, <Element 'country' at 0x000001C96AD10630>]
# print(root.findall('country').text)
print(root.find('country'))
# <Element 'country' at 0x000001C96ABC2540>

# .(도트)를 이용한 체이닝
# root.find(태그1).find(태그2).text
# 첫번째 country 요소안의 rank에 삽입된 글자는?
print(root.find('country').find('rank').text) # 1
print(root.find('country').find('gdppc').text) # 141100

# 두번째 삽입된 country 요소안의 year 태그안에 글자 출력?
print(root.findall('country')[1].find('year').text) # 2011

# 태그안의 속성값 반환 = get(속성명)
print('=========모든 country 태그의 name 속성값만 출력하기')
for country in root.findall('country'):
    print(country.get('name'), end=' ')

# xml => 딕셔너리 리스트 => csv 저장
print('=== 딕셔너리 리스트 구조화')
country_list = []
for country in root.findall('country'):
    temp = {}
    temp['rank'] = country.find('rank').text
    temp['year'] = country.find('year').text
    temp['gdppc'] = country.find('gdppc').text
    country_list.append(temp)
print(country_list)

with open('output/country_result1.csv', 'w', encoding='utf-8', newline='') as f:
    field_list = ['rank', 'year', 'gdppc']
    csv_data = csv.DictWriter(f, fieldnames=field_list)
    csv_data.writeheader()
    csv_data.writerows(country_list)

df = pd.DataFrame(country_list, columns=['rank', 'year', 'gdppc'])
print(df)
df.to_csv('output/country_result2.csv', index=False)

# 퀴즈 :
# 아래 주소를 이용하여 books.xml 파일을 생성한 후
# bookstore.csv 파일로 저장하기
# xml => 딕셔너리 리스트 => csv 저장
# https://www.w3schools.com/xml/books.xml
# author 태그의 텍스트가 여러개인 경우 첫번째만 저장한다.
#  title  author  year  price

tree = parse('data/books.xml')
# print(tree, type(tree))

root = tree.getroot()
# print(root, type(root))

books_list = []
for book in root.findall('book'):
    temp = {}
    temp['title'] = book.find('title').text
    temp['author'] = book.find('author').text
    temp['year'] = book.find('year').text
    temp['price'] = book.find('price').text
    books_list.append(temp)
print(books_list)

df = pd.DataFrame(books_list, columns=['title', 'author', 'year', 'price'])
print(df)
df.to_csv('output/bookstore.csv', index=False)


# 여러개의 태그가 있는 경우 리스트화 한 후 텍스트로 변경하여 저장
# 예) James McGovern/Per Bothner...

# for book in root.findall('book'):
#     authors_list = []
#     for item in book.findall('author'):
#         authors_list.append(item.text)
#     print(authors_list)
#     # 리스트 => 텍스트
#     print(' / '.join(authors_list))

books_list = []
for book in root.findall('book'):
    temp = {}
    temp['title'] = book.find('title').text
    authors_list = []
    for item in book.findall('author'):
        authors_list.append(item.text)
    temp['author'] = '/'.join(authors_list)

    temp['year'] = book.find('year').text
    temp['price'] = book.find('price').text
    books_list.append(temp)
print(books_list)

df = pd.DataFrame(books_list, columns=['title', 'author', 'year', 'price'])
print(df)
df.to_csv('output/bookstore2.csv', index=False)




