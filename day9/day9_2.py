# 딕셔너리 => csv 파일로 저장하기

# csv 파일 쓰기3
# 파일변수 = open('csv파일경로', 'w', encoding='utf-8/cp949', newline='')
# field_list = 리스트(딕셔너리의 키로 생성된 리스트)
# csv객체변수 = csv.DictWriter(파일변수, fieldnames=field_list)
# csv객체변수.writerheader()
# csv객체변수.writerow(딕셔너리)
# csv객체변수.writerows(딕셔너리 리스트)
# 파일변수.close()

# csv 파일 쓰기4
# with open('csv파일경로', 'w', encoding='utf-8/cp949', newline='') as 파일변수:
# field_list = 리스트(딕셔너리의 키로 생성된 리스트)
# csv객체변수 = csv.DictWriter(파일변수, fieldnames=field_list)
# csv객체변수.writerheader()
# csv객체변수.writerow(딕셔너리)
# csv객체변수.writerows(딕셔너리 리스트)


data_list = [   ['이름','주소','전화번호'],
                ['김영희','부산시','010-6374-90874'],
                ['홍길동','춘천시','010-5463-9403'],
                ['성은희','서울시','010-4646-9403']   ]

# 딕셔너리 리스트 정의 => 각 딕셔너리의 키값은 동일
dict_list = [   {'name':'김영희','address':'부산시','mobile':'010-6374-90874'},
                {'name':'홍길동','address':'춘천시','mobile':'010-5463-9403'},
                {'name':'성은희','address':'서울시','mobile':'010-4646-9403'}   ]

import csv

with open('output/address4.csv', 'w', encoding='utf-8', newline='') as f:
    # 키값으로 구성된 리스트 생성
    field_list = ['name', 'address', 'mobile']

    # csv 객체 생성
    # csv객체변수 = csv.DictWriter(파일변수, fieldnames=키리스트)
    csv_data = csv.DictWriter(f, fieldnames=field_list)

    # 제목행과 관련된 필드 쓰기
    csv_data.writeheader()

    # 1행씩 쓰기
    # csv_data.writerow(dict_list[0])
    # csv_data.writerow(dict_list[1])

    # 전체 쓰기
    for dict in dict_list:
        csv_data.writerow(dict)

#  writerows() 함수를 이용한 전체 쓰기
with open('output/address5.csv', 'w', encoding='utf-8', newline='') as f:
    # 키값으로 구성된 리스트 생성
    field_list = ['name', 'address', 'mobile']
    csv_data = csv.DictWriter(f, fieldnames=field_list)
    csv_data.writeheader()
    csv_data.writerows(dict_list)

# 판다스를 이용해서 csv 파일 읽기와 쓰기
# 판다스란? 파이썬계의 엑셀 라이브러리
# https://pandas.pydata.org/
# 파이참에서 판다스가 설치되어 있는지 확인하기
# [File]-[Settings] 에서 Project 목록에서 확인하기
# 없으면 설치 : [+] 설치하고자 하는 pandas 입력후 설치

# 수동 설치는?
# [Terminal] 탭을 클릭한 후
# 명령어 입력
# pip install pandas
# 확인은?
# pip list

# 넘파이 설치
# pip install numpy

# 임포트
import pandas as pd

# pandas 이용해서 csv 파일 읽기와 쓰기
# 데이타프레임변수 = pd.read_csv('파일경로', encoding='cp949/utf-8')
# 데이타프레임변수.to_csv('파일경로', encoding='cp949/utf-8', index=False)

# 2018.csv => 2018년도 전국별 대학교 취업자수 데이타
df = pd.read_csv('data/2018.csv', encoding='cp949')
print(type(df)) # <class 'pandas.core.frame.DataFrame'>
print(df)

# utf-8 포맷으로 저장하기
# index=False 1열의 인덱스 숫자 제외하고 쓰기
df.to_csv('output/2018_college1.csv', encoding='utf-8', index=False)

