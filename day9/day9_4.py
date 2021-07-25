# dat 파일 다루기
# .dat 파일 확장자를 가진 파일은
# 파일을 만든 프로그램과 관련된 특정 정보를 저장하는 일반 데이터 파일
# 일반 텍스트 파일과 같이 메모장에서 열기가 가능하다.
# dat 구분자가 | 나 ||

# contacts.dat => 주소록(번호|이름|단축번호|주소|그룹번호)
import csv

# dat 파일 읽기
with open('data/contacts.dat', 'r', encoding='cp949') as f:
    data_list = f.readlines()
    print(data_list) # 1차원
    print(data_list[0]) # 000|Mom|3|New Bark Town|0
    # 2차원 구조 변경, /n 없애기, | 를 기준으로 리스트 분리
    temp_list = []
    for row in data_list:
        temp = row.replace('\n', '').split('|')
        temp_list.append(temp)
    data_list = temp_list

print(data_list)
for row in data_list:
    print(row)


# 제목행 삽입하기
# 3열 값이 숫자가 아닌경우에는 -999 또는 None 으로 처리하기
# csv 파일로 저장하기
field_list = ['No', 'Name', 'Speed Dial', 'Address', 'Group No']
data_list.insert(0, field_list)
print('#'*50)
for row in data_list:
    print(row)

# 3열 값이 숫자가 아닌경우에는 -999 또는 None 으로 처리하기
print('='*50)
for No, Name, SpeedDial, Address, GroupNo in data_list:
    if SpeedDial.isalpha():
        print([No, Name, SpeedDial, Address, GroupNo])

print('*-'*50)
temp_list = []
for No, Name, SpeedDial, Address, GroupNo in data_list:
    if SpeedDial.isalpha():
        # SpeedDial = '-999'
        SpeedDial = None
    temp_list.append([No, Name, SpeedDial, Address, GroupNo])
data_list = temp_list
print(data_list)

# csv 파일로 저장하기
with open('output/contacts.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f)
    csv_data.writerows(data_list)


# movies.dat => 영화번호::영화제목(년도)::장르1|장르|..
# http://files.grouplens.org/datasets/movielens/ml-1m-README.txt
# 1::Toy Story (1995)::Animation|Children's|Comedy

with open('data/movies.dat', 'r', encoding='ISO-8859-1') as f:
    data_list = f.readlines()
    # 2차원 데이타로 구조 변경
    temp_list = []
    for row in data_list:
        temp = row.replace('\n', '').split('::')
        temp_list.append(temp)
    data_list = temp_list

print(data_list[0])
# ['1', 'Toy Story (1995)', "Animation|Children's|Comedy"]

# 영화번호, 제목, 년도, 장르 구조로 변경하기
temp_list = []
for n, t, g in data_list:
    # 제목과 년도 분리하기
    # 맨마지막을 기준으로 7번째까지 자르고 공백제거
    t1 = t[:-6].strip()
    t2 = int(t[-5:-1])
    temp_list.append([int(n), t1, t2, g])
print(temp_list[0])

# 1995년대 이후만 영화만 저장하기
# output/movies_1995.csv
print(len(temp_list)) # 3883
for n, t, y, g in temp_list[:10]:
    print(n, t, y, g)

print('='*50)
movies_1995 = []
for n, t, y, g in temp_list:
    if y >= 1995:
        movies_1995.append([n, t, y, g])

for n, t, y, g in movies_1995[:10]:
    print(n, t, y, g)

# csv 파일로 저장하기
with open('output/movies_1995.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f)
    csv_data.writerow(['No', 'Title', 'Year', 'Genres'])
    csv_data.writerows(movies_1995)


