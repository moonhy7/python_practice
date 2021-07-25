# BeautifulSoup를 이용한 xml 파싱
# BeautifulSoup 이란?
# HTML 및 XML 파일에서 원하는 데이터를
# Parsing 할 수 있는 Python 라이브러리
# 별도 설치 과정이 필요
# pip install BeautifulSoup4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# 모듈 임포트
from bs4 import BeautifulSoup
import pandas as pd

# xml 문자열 변수 =>  BeautifulSoup 파싱  => 2차원 리스트
# xml 구조의 문자열 변수 정의
# 소스 : https://www.w3schools.com/Xml/
str_xml = '''
<breakfast_menu>
    <food>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>
       Two of our famous Belgian Waffles with plenty of real maple syrup
       </description>
        <calories>650</calories>
    </food>
    <food>
        <name>Strawberry Belgian Waffles</name>
        <price>$7.95</price>
        <description>
        Light Belgian waffles covered with strawberries and whipped cream
        </description>
        <calories>900</calories>
    </food>
    <food>
        <name>Berry-Berry Belgian Waffles</name>
        <price>$8.95</price>
        <description>
        Belgian waffles covered with assorted fresh berries and whipped cream
        </description>
        <calories>900</calories>
    </food>
</breakfast_menu>
'''

# Beautifulsoup을 이용한 xml 객체화
# soup객체변수 = BeautifulSoup(xml문자열변수, "html.parser/xml/lxml/html5lib")
# soup = BeautifulSoup(str_xml, 'html.parser')
# 에러 발생시 pip install lxml
soup = BeautifulSoup(str_xml, 'xml')
# <?xml version="1.0" encoding="utf-8"?> 가 최상단에 자동 삽입
# soup = BeautifulSoup(str_xml, 'lxml')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
print(soup)

# Tag 찾기
# soup객체.find(태그명) => 최초태그객체
# soup객체.find_all(태그명) => 모든태그객체. 리스트반환
# find(태그명).text
# find(태그명).get_text()

food_tag1 = soup.find('food')
food_tags= soup.find_all('food')
print('== 첫번째 food')
print(food_tag1)
print('== 모든 food')
print(food_tags)

print('== 첫번째 name 태그안의 글자 ')
print(soup.find('name').text)
print('== 모든 name 태그안의 글자')
name_tags = soup.find_all('name')
for tag in name_tags:
    print(tag.text)

print('== 3번째 위치한 name 태그안의 글자 ')
print(soup.find_all('name')[2].text)

print('== food 태그안의 name, price, description 태그안의 글자만 출력 ')
food_tags = soup.find_all('food')
cnt = 1
for food in food_tags:
    print('Menu'+ str(cnt) + ' => ', \
          food.find('name').text, food.find('price').text, \
          food.find('description').text.replace('/n','').strip())
    cnt += 1

#======================
# 별도의 xml 파일 => xml 객체화  => 태그 찾기
# data/books.xml
# https://www.w3schools.com/xml/books.xml

# xml파일 내용 => 문자열변수로 저장
with open('data/books.xml', 'r', encoding='utf-8') as f:
    xml_books = f.read()
    print('\n======== xml_books')
    print(type(xml_books)) # <class 'str'>
    print(xml_books)

# xml 객체화
soup = BeautifulSoup(xml_books, 'xml')
print('\n======== soup')
print(type(soup)) # <class 'bs4.BeautifulSoup'>
print(soup)
print('\n======== title 태그안의 텍스트만 출력')
title_tags = soup.find_all('title')
print(len(title_tags))
for tag in title_tags:
    print(tag.text)

print('\n======== 속성으로 찾기 ')
# <태그 속성1=값1, 속성2=값2...> 내용 </태그>
# category 속성값이 children 으로 지정된 book 태그 찾기
# 숩객체.find_all(태그명, {속성1:값1, 속성2:값2...})
book_children = soup.find_all('book', {'category':'children'})
print(book_children)
print(type(book_children))
print('='*50)
for tag in book_children:
    print(tag)
print('='*50)
for tag in book_children:
    print(tag.text)
print('='*50)
# author 태그와 price 태그안의 텍스트만 출력
for tag in book_children:
    print('author : ', tag.find('author').text)
    print('price : ', tag.find('price').text)

print('\n======== 2차원 리스트로 저장 ')
soup = BeautifulSoup(xml_books, 'xml')
books_tag = soup.find_all('book')
bookstore_list = []
for book in books_tag:
    temp = []
    temp.append(book.find('title').text)
    temp.append(book.find('author').text)
    temp.append(book.find('year').text)
    temp.append(book.find('price').text)
    bookstore_list.append(temp)
print(bookstore_list)

print('\n======== 데이타프레임 구조로 확인 ')
df = pd.DataFrame(bookstore_list, columns=['title', 'author', 'year', 'price'])
print(df)