# CSV
# data 폴더에서 csv 파일 확인
# population.csv / data.csv /
# 한국교통안전공단_대중교통 이용자유형별 이용인원(2017년).csv
# => traffic_2017.csv (encoding:utf-8)

import os, csv

# 경로 확인
print(os.getcwd()) # C:\pyclass
# 현재 경로의 파일과 폴더를 리스트 반환
print(os.listdir(os.getcwd()))
# data 폴더로 위치 이동
os.chdir('data')
print(os.getcwd()) # C:\pyclass\data
print(os.listdir(os.getcwd()))

# 외부 데이타 : txt, csv, tsv, dat 엑셀, open-api(json, xml), 스크래핑(bs4, 셀레니움)

# CSV란?
# Comma Seperate Value
# 콤마(,)로 데이타가 분리된 파일

# 내장 모듈 임포트
# import csv

# CSV 파일 읽기1
# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.reader(파일변수)

print(os.getcwd()) # C:\pyclass\data
# f = open('data/data.csv', 'r', encoding='utf-8')
f = open('data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
print('csv_data = ', csv_data, type(csv_data))
# csv_data =  <_csv.reader object at 0x0000017E5DB35E80> <class '_csv.reader'>
# for 문 이용해서 출력하기
# for row in csv_data:
#     print(row)

# 리스트로 저장하기 => 2차원 리스트
data_list = []
for row in csv_data:
    data_list.append(row)

print(f'data_list 의 전체 길이는? {len(data_list)}')
print(data_list)

# 1행은 제목행 => Header
print(data_list[0]) # ['class', 'name', 'kor', 'eng', 'mat', 'bio']

# 제목행을 제외하고 출력하기
print('-'*50)
for row in data_list[1:]:
    print(row)

# 인덱스 변수 이용해서 출력하기
for (cls, name, kor, eng, mat, bio) in data_list:
    print(cls , name, kor, eng, mat, bio)

f.close()
print('\n\n'+'='*50)

# with문을 이용하여 CSV 파일 읽기
# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
#   csv객체변수 = csv.reader(파일변수)

# population.csv
with open('population.csv', 'r', encoding='utf-8') as f:
    csv_data = csv.reader(f)
    pop_list = []
    for row in csv_data:
        pop_list.append(row)

print(f'행의 갯수는? {len(pop_list)}')
print('1~10행 출력하기')
cnt = 1
for row in pop_list[:10]:
    print(cnt, row)
    cnt += 1
print('-'*50)
print('State', '\t\t\t\t\t\t', 'Population')
print('-'*50)
for s,p in pop_list[1:]:
    print(s, '\t\t\t\t\t\t', p)





