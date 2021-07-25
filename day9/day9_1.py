# csv, tsv, dat, xls, json, xml, html => 2차원리스트, 딕셔너리 리스트
# openAPI => json, xml
# 데이타수집 => 데이타가공 => 데이타분석 => 예측(머신러닝)

# csv 란? 쉼표로 분리된 데이타

# import csv

# CSV 파일 읽기 1
# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.reader(파일변수)
# 파일변수.close()

# CSV 파일 읽기 2
# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수
#   csv객체변수 = csv.reader(파일변수)


# data/data.csv 파일 읽기
# 'kor' 과목의 총점, 평균, 최고점, 최하점은?
# 국어 점수의 최고점을 받은 학생의 이름은?

import csv, os
print(os.getcwd()) # C:\pyclass
with open('data/data.csv', 'r', encoding='utf-8') as f:
  csv_data = csv.reader(f)
  print(csv_data)

  # 리스트로 저장하기 => 2차원 리스트
  # data_list = []
  # for row in csv_data:
  #     data_list.append(row)

  # 2차원 리스트  구조로 변경
  data_list = list(csv_data)

  print(data_list)

# 첫행 리스트만 출력하기
print(data_list[0]) # ['class', 'name', 'kor', 'eng', 'mat', 'bio']

# 1행 제외 나머지 데이타만 출력하기
print('='*50)
for c, n, k, e, m, b in data_list[1:]:
    print(c, n, k, e, m, b)


# 'kor' 과목의 총점, 평균, 최고점, 최하점은?
print('='*50)
kor_data_list = []
# ValueError: invalid literal for int() with base 10: 'kor'
# for c, n, k, e, m, b in data_list:
# 1행(인덱스 0)는 제목행(Header, field)은 제외
for c, n, k, e, m, b in data_list[1:]:
    # 문자열  => 정수형
    kor_data_list.append(int(k))
print('국어 점수 리스트 = ', kor_data_list)
print('국어 총점 = ', sum(kor_data_list))
print('국어 평균 = ', sum(kor_data_list)/len(kor_data_list))
print('국어 최고점 = ', max(kor_data_list))
print('국어 최하점 = ', min(kor_data_list))

# 국어 점수의 최고점을 받은 학생의 이름은?
# if 문 이용
for c, n, k, e, m, b in data_list[1:]:
    if int(k) == max(kor_data_list):
        print(f'국어 점수의 최고점 학생은? {n}')

# 국어 점수의 최고점 학생은? oscar

# 전체 총점이 가장 높은 학생의 이름은?
tot_data_list = []
for c, n, k, e, m, b in data_list[1:]:
    temp = int(k) + int(e) + int(m) + int(b)
    tot_data_list.append(temp)
print(tot_data_list)
print('총점 최고점 ',max(tot_data_list))

# 1등은 누구인가?
# 총점 최고점의 인덱스 구하기
# 리스트명.index(값)
temp = max(tot_data_list)
temp_index = tot_data_list.index(temp)
print(temp_index) # 9


print('='*50)
for c, n, k, e, m, b in data_list:
    print(c, n, k, e, m, b)
print(data_list[1])

# 최고 총점을 구한다.
temp = max(tot_data_list)
# 최고 총점의 인덱스를 구한다.
temp_index = tot_data_list.index(temp)
# 실제 원본 리스트의 인덱스 + 1로 대입한다.
print(data_list[temp_index+1])
# 이름만 표시
print('전체 총점이 가장 높은 학생의 이름은', data_list[temp_index+1][1])

# ==============================
# ordered dict 형태로 데이터 불러오기

# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.DictReader(파일변수)

# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
#   csv객체변수 = csv.DictReader(파일변수)


# traffic_2017.csv 파일 => 딕셔너리 리스트
# 1행은 키값으로 지정
# 2행부터가 실제 데이타
# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.DictReader(파일변수)
print('\n'*5)
f = open('data/traffic_2017.csv','r', encoding='cp949')
csv_data = csv.DictReader(f)
print(csv_data, type(csv_data))
# 리스트화 => 리스트안의 딕셔너리 구조
data_list = list(csv_data)
print(data_list)
print(data_list[0], type(data_list[0]))
# {'구분': '서울', '일반인': '3711168', '어린이': '36098', '청소년': '259128', '기타': '417539'} <class 'dict'>
f.close()

# 전체 출력하기 1
for row in data_list:
    # 딕셔너리
    print(row)

# 전체 출력하기 2
print('='*50)
for row in data_list:
    for key in row:
        # row[key]는 string
        print(row[key], end="\t")
    print()

# 데이타 접근 - 1행의 '구분' 값은?
print(data_list[0])
# KeyError: 0
# print(data_list[0][0])
# 리스트명[위치인덱스][키값]
print(data_list[0]['구분']) # 서울

# 제주 데이타 출력하기
for row in data_list:
    if row['구분'] == '제주':
        print(f'제주 데이타는? {row}')

# 지역을 매개변수로 지정해서 함수화
def get_city_data(city):
    for row in data_list:
        if row['구분'] == city:
            print('%'*50)
            print(f'{city} 데이타는? {row}')
            for key in row:
                print(key, '=>', row[key])


get_city_data('서울')
get_city_data('부산')

# 제주 사용자의 총 데이타값 출력 ?
print('$'*50)
for row in data_list:
    if row['구분'] == '제주':
        print(f'제주 데이타는? {row}')
        # ValueError: invalid literal for int() with base 10: ''
        # result = int(row['일반인']) + int(row['어린이']) + int(row['청소년']) + int(row['기타'])
        result = 0
        for key in row:
            try:
                result += int(row[key])
            except:
                pass

        print(f'제주 대중교통 총 사용자는? {result}')


# csv 파일 쓰기1
# 파일변수 = open('csv파일경로', 'w', encoding='utf-8/cp949', newline='')
# csv객체변수 = csv.writer(파일변수)
# csv객체변수.writerow(리스트/튜플...)
# 파일변수.close()

# csv 파일 쓰기2
# with open('csv파일경로', 'w', encoding='utf-8/cp949', newline='') as 파일변수:
    # csv객체변수 = csv.writer(파일변수)
    # csv객체변수.writerow(리스트/튜플...)


# 2차원 리스트 => csv 파일로 저장하기
# 현재폴더를 기준으로 output 폴더 생성
# os.mkdir(폴더명)

print(os.getcwd())
# os.mkdir('output')
print(os.listdir(os.getcwd()))

# 2차원 리스트
data_list = [   ['이름','주소','전화번호'],
                ['김영희','부산시','010-6374-90874'],
                ['홍길동','춘천시','010-5463-9403'],
                ['성은희','서울시','010-4646-9403']   ]

# newline='' 공백줄 없이 삽입하는 옵션
with open('output/address1.csv', 'w', encoding='utf-8', newline='') as f:
    # csv 객체 생성
    csv_data = csv.writer(f)
    # 1~2행만 쓰기
    csv_data.writerow(data_list[0])
    csv_data.writerow(data_list[1])

# 2차원 리스트 전체 데이타 csv 파일로 저장하기 1 - for문 + writerow(리스트/튜플...)
with open('output/address2.csv', 'w', encoding='utf-8', newline='') as f:
    # csv 객체 생성
    csv_data = csv.writer(f)
    # 전체쓰기
    for row in data_list:
        csv_data.writerow(row)

# 2차원 리스트 전체 데이타 csv 파일로 저장하기 2 - writerows(2차원리스트)
with open('output/address3.csv', 'w', encoding='utf-8', newline='') as f:
    # csv 객체 생성
    csv_data = csv.writer(f)
    # 1행만 삽입
    csv_data.writerow(['주소'])

    # 전체쓰기
    csv_data.writerows(data_list)

