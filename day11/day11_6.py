# =========================================
# 외장모듈인 xmltodict를 이용한 xml 파서방법
# 설치 : pip install xmltodict
# xml string => OrderedDict => json => dict
# import xmltodict

# 객체 = xmltodict.parse(xml텍스트변수) : OrderedDict
# json객체 = json.dumps(xml객체))
# 딕셔너리변수 = json.loads(json객체)


import xmltodict
import json
import pandas as pd
from bs4 import BeautifulSoup

# xml 문자열 변수 정의
str_xml = '''
<animals>
    <animal>
      <name>lion</name>
      <lifespan>13</lifespan>
    </animal>
    <animal>
      <name>tiger</name>
      <lifespan>17</lifespan>
    </animal>
</animals>
'''

print(type(str_xml)) # <class 'str'>
print('='*50)
# 객체변수 = xmltodict.parse(xml텍스트변수) : OrderedDict
data = xmltodict.parse(str_xml)
print('\n\n OrderedDict 구조 ')
print(type(data)) # <class 'collections.OrderedDict'>
print(data)
# OrderedDict([('animals', OrderedDict([('animal', [OrderedDict([('name', 'lion'), ('lifespan', '13')]), OrderedDict([('name', 'tiger'), ('lifespan', '17')])])]))])
print('\n\n json string 구조 ')
json_data = json.dumps(data)
print(type(json_data))
print(json_data)
'''
<class 'str'>
{"animals": {"animal": [{"name": "lion", "lifespan": "13"}, {"name": "tiger", "lifespan": "17"}]}}

'''
print('\n\n 딕셔너리 구조 ')
dict = json.loads(json.dumps(data))
print(type(dict))
print(dict)
# <class 'dict'>
# {'animals': {'animal': [{'name': 'lion', 'lifespan': '13'}, {'name': 'tiger', 'lifespan': '17'}]}}

# json 파일로 저장
with open('output/animals.json', 'w') as f:
    json.dump(dict, f, indent='\t')

# 데이타프레임화 : 조건=> 딕셔너리 리스트/2차원데이타
print(dict['animals']) # {'animal': [{'name': 'lion', 'lifespan': '13'}, {'name': 'tiger', 'lifespan': '17'}]}
print(dict['animals']['animal'])
# [{'name': 'lion', 'lifespan': '13'}, {'name': 'tiger', 'lifespan': '17'}]
df = pd.DataFrame(dict['animals']['animal'])
print(df)




