# 관련 함수를 바로 사용할 수 있게 모듈 임포트
from xml.etree.ElementTree import *
import csv
import pandas as pd

# xml 구조의  문자열 변수 => xml 객체 => 딕셔너리 리스트
# xml객체 = fromstring(문자열변수)

# xml 구조의 문자열 변수 정의
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
print(type(str_xml)) # <class 'str'>
print(str_xml)

# 문자열 => xml 객체화
# xml의 root 객체 = fromstring(문자열변수)
root = fromstring(str_xml)
print(root) # <Element 'breakfast_menu' at 0x000001CA49F428B0>
print(type(root)) # <class 'xml.etree.ElementTree.Element'>

food_list = []
for food in root.findall('food'):
    temp = {}
    temp['name'] = food.find('name').text
    temp['price'] = food.find('price').text
    temp['description'] = food.find('description').text.replace('\n','').strip()
    temp['calories'] = food.find('calories').text
    food_list.append(temp)
print(food_list)

df = pd.DataFrame(food_list, columns=['name', 'price', 'description', 'calories'])
print(df)
df.to_csv('output/breakfast_menu.csv', index=False)

# root 객체 =>  xml 파일로 저장하기
# ElementTree(root).write(xml경로, encoding='cp949/utf-8')
print(root)
print(root.tag)
ElementTree(root).write('output/breakfast_menu.xml', encoding='utf-8')