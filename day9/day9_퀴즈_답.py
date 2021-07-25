
# 퀴즈1 :
# data.csv 파일을 이용하여
# 4과목('kor', 'eng', 'mat', 'bio')의 총점과 전체 평균을 구하여라.
'''
 kor 총점 = ... ?
 eng 총점 = ... ?
 mat 총점 = ... ?
 bio 총점 = ... ?
4과목의 총점은 ... ?
전체 평균은 ... ?
'''

# import csv
#
# with open('data/data.csv', 'r', encoding='utf-8') as f:
#     csv_data = csv.reader(f)
#     data_list = list(csv_data)
#
#     # 리스트 초기화
#     korList = []
#     engList = []
#     matList = []
#     bioList = []
#
#     for i in range(1, len(data_list)):
#         korList.append(int(data_list[i][2]))
#         engList.append(int(data_list[i][3]))
#         matList.append(int(data_list[i][4]))
#         bioList.append(int(data_list[i][5]))
#
#     print(f' kor 총점 = {sum(korList)}')
#     print(f' eng 총점 = {sum(engList)}')
#     print(f' mat 총점 = {sum(matList)}')
#     print(f' bio 총점 = {sum(bioList)}')
#
#     print(f'4과목의 총점은? {sum(korList)+sum(engList)+sum(matList)+sum(bioList)}')
#     print(f'전체 평균은? {(sum(korList)+sum(engList)+sum(matList)+sum(bioList))/((len(data_list)-1)*4):.2f}')

'''
 kor 총점 = 933
 eng 총점 = 892
 mat 총점 = 936
 bio 총점 = 987
4과목의 총점은? 3748
전체 평균은? 78.08

'''


# 퀴즈2 :
# 미국 주별 인구수 population.csv 파일을 이용하여 리스트 구조로 변경하고
# 출력하여라
# 이때 인구와 관련된 데이타는 정수 리스트로 변환해야 한다.
'''
State Population
Alabama 4780131
Alaska 710249
Arizona 6392301
  ...
'''

# import csv
#
# # print(int('4,780,131'.replace(',',''))) # 4780131
#
# # 미국 주별 인구수
# # data/population.csv
# with open('data/population.csv', 'r', encoding='utf-8') as f:
#     csv_data = csv.reader(f)
#     data_list = list(csv_data)
#     # print(data_list)
#
#     population_list = []
#     for s, p in data_list[1:]:
#        #  형변환
#        population_list.append([s, int(p.replace(',', ''))])
#
#     population_list.insert(0, data_list[0] )
#     print(population_list)
#     for s, p in population_list:
#         print(s, p)



# 퀴즈3 :
# 퀴즈2의 리스트에서
# 가장 인구가 많은 주(State)와 가장 인구가 적은 주(state)는?

# 인구수의 max(), min()
# 인구수의 max(), min()에 해당하는 index 값 구하기
# 데이타리스트에서 index 삽입하여 결과 반환

# print(f'가장 인구가 많은 주(State)? {population_list.index(max(population_list))}')
# print(f'가장 인구가 많은 주(State)? {data_list[population_list.index(max(population_list))]}')
# print(f'가장 인구가 많은 주(State)? {data_list[population_list.index(max(population_list))][0]}')
#
# print(f'가장 인구가 적은 주(State)? {population_list.index(min(population_list))}')
# print(f'가장 인구가 적은 주(State)? {data_list[population_list.index(min(population_list))]}')
# print(f'가장 인구가 적은 주(State)? {data_list[population_list.index(min(population_list))][0]}')
#



# 퀴즈5 :
# traffic_2017.csv 각 지역별 대중교통 파일을 이용하여
# 아래와 같은 딕셔너리 구조로 대중교통총사용자수를 출력하여라

'''
{'서울': 4423933, '부산': 952394, '대구': 547568, ... }

'''
# import csv
# with open('data/traffic_2017.csv', 'r') as f:
#     csv_data = csv.DictReader(f)
#     list_city = []
#     list_user = []
#
#     for row in csv_data:
#         list_city.append(row['구분'])
#         if row['기타'] == '':
#             temp = '0'
#         else:
#             temp = row['기타']
#         list_user.append(int(row['일반인'])+
#                          int(row['어린이'])+
#                          int(row['청소년'])+int(temp))
#
#     # print(list_city)
#     # print(list_user)
#     korea_traffic_dict = {}
#     for i in range(0, len(list_city)):
#         # 딕셔너리변수[키] = 값
#         korea_traffic_dict[list_city[i]] = list_user[i]
#     print(korea_traffic_dict)




# 퀴즈6 :
# 퀴즈 5번의 데이타 리스트에서 가장 낮은 대중교통 사용자수와 관련된 도시는?
# temp = min(list(korea_traffic_dict.values()))
# print(temp)
# for key in korea_traffic_dict:
#     if korea_traffic_dict[key] == temp:
#         print(f'가장 낮은 대중교통 사용자수에 해당하는 도시는? {key}')




# 퀴즈7 :
# 2018.csv 파일을 이용하여 다음을 구하여라.

# 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
# 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?

# import csv
# # 딕셔너리 리스트
# with open('data/2018.csv', 'r') as f:
#     csv_data2 = csv.DictReader(f)
#     # 리스트화1
#     # data_list2 = []
#     # for item in csv_data2:
#     #     data_list2.append(item)
#
#     # 리스트화2
#     data_list2 = [item for item in csv_data2]
#     print(data_list2)
#
#     # 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
#     # 지역 필드를 리스트로 만들기
#     # city_list = []
#     # for item in data_list2:
#     #     city_list.append(item['지역'])
#
#     city_list = [item['지역'] for item in data_list2]
#     print(f'city_list = {city_list}')
#
#     # 1000명이상 필드를 정수 리스트로 만들기
#     # employ1000_list = []
#     # for item in data_list2:
#     #     temp = int(item['1000명이상'].replace(',',''))
#     #     employ1000_list.append(temp)
#
#     employ1000_list = [int(item['1000명이상'].replace(',','')) for item in data_list2]
#     print(f'employ1000_list = {employ1000_list}')
#     # print(type(employ1000_list[0])) #<class 'str'>
#
#     # 1000명이상 필드에서 최대값은?
#     print(max(employ1000_list))
#
#     # 1000명이상 필드에서 최대값을 갖는 인덱스 번호는?
#     print(employ1000_list.index(max(employ1000_list)))
#
#     # 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
#     num = employ1000_list.index(max(employ1000_list))
#     print(f' 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?  {city_list[num]}' )
#

# 퀴즈 => 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?

# 3개의 필드에서 리스트 각각 생성하기
# employ_list1 = [int(item['1-5인미만'].replace(',', '')) for item in data_list2]
# employ_list2 = [int(item['6-50인미만'].replace(',', '')) for item in data_list2]
# employ_list3 = [int(item['51-100인미만'].replace(',', '')) for item in data_list2]
# print(employ_list1)
# print(employ_list2)
# print(employ_list3)
# # print(employ_list1+employ_list2+employ_list3)
# employ_list4 = []
# for i in range(len(employ_list1)):
#     temp = employ_list1[i] + employ_list2[i] + employ_list3[i]
#     employ_list4.append(temp)
# print(employ_list4)
#
# print(min(employ_list4))
# print(employ_list4.index(min(employ_list4)))
# num = employ_list4.index(min(employ_list4))
# print(f' 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?  {city_list[num]}')


# 퀴즈8 :
# 2018.csv 파일에서 '학제', '분석대상자수'  컬럼만 제외한 후
# output 폴더안에 2018_result.csv
# 파일로 저장하여라.

# import csv
# with open('data/2018.csv', 'r') as f:
#     csv_data = csv.reader(f)
#     # for item in csv_data1:
#     #     print(item)
#     data_list = []
#     for item in csv_data:
#         data_list.append(item)
#     print(data_list)
#
#     # 첫번째 리스트 제외
#     data_list2 = data_list[1:]
#     print(data_list2)
#     print(len(data_list2))
#
#     # for 문으로 각 리스트 별로 출력하기
#     for rows in data_list:
#         print(rows)

# 학제, 분석대상자수 제외하고 csv 파일쓰기
# output/2018_result1.csv

# with open('output/2018_result1.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#
#     # 전체 쓰기
#     for row in data_list:
#         writer.writerow([row[1]]+row[3:])




# 퀴즈9 :
# gapminder.tsv 파일을 이용하여 Asia 대륙의 데이타만 저장하여 별도 파일로 저장하여라.
# output 폴더안의 asia.tsv
# import csv
# with open('data/gapminder.tsv', 'r', encoding='cp949') as f:
#     tsv_data = csv.reader(f, delimiter='\t')
#     data_list = list(tsv_data)
#     # Asia 대륙의 데이타만 출력하기
#     asia_list = []
#     for (country, continent, year, lifeExp, pop, gdpPercap) in data_list[1:]:
#         if continent == 'Asia':
#             asia_list.append(
#                 [country, continent, int(year), round(float(lifeExp), 2), int(pop), round(float(gdpPercap), 2)])
#     print(asia_list)
#     print(len(asia_list))
#
# # Asia 대륙의 데이타만 tsv 파일로 저장하기
# with open('output/asia.tsv', 'w', encoding='utf-8', newline='') as f:
#     tsv_data = csv.writer(f, delimiter='\t')
#     tsv_data.writerows(asia_list)



# 퀴즈 10:
# gapminder.tsv 파일의 데이타를 이용하여 다음과 같이 출력하여라.
'''
 평균 수명이 가장 길었던 데이타 : ? 년도의 ? 
 평균 수명이 가장 짧았던 데이타 : ? 년도의 ?
'''

# with open('data/gapminder.tsv', 'r', encoding='cp949') as f:
#     tsv_data = csv.reader(f, delimiter='\t')
#     data_list = list(tsv_data)
#
#     # 평균수명(lifeExp)이 가장 높은 데이타만 출력하기
#     lifeExp_list = []
#     for (country, continent, year, lifeExp, pop, gdpPercap) in data_list[1:]:
#         lifeExp_list.append(float(lifeExp))
#
#     print(lifeExp_list)
#     print(min(lifeExp_list), max(lifeExp_list))
#
#     for (country, continent, year, lifeExp, pop, gdpPercap) in data_list[1:]:
#         if lifeExp == str(max(lifeExp_list)):
#             print(f' 평균 수명이 가장 길었던 데이타 : {year} 년도의 {country} ')
#         if lifeExp == str(min(lifeExp_list)):
#             print(f' 평균 수명이 가장 짧았던 데이타 : {year} 년도의 {country} ')
'''
 평균 수명이 가장 길었던 데이타 : 2007 년도의 Japan 
 평균 수명이 가장 짧았던 데이타 : 1992 년도의 Rwanda 
'''

# 퀴즈 11:
# movies.dat 파일을 이용하여
# 1980년도 (1980~1989) 영화만
# movies_1980_1989.csv 파일로 저장하여라.

'''
MovieID,Title,Year,Genres
142,Shadows (Cienie),1988,Drama
541,Blade Runner,1982,Film-Noir|Sci-Fi
592,Batman,1989,Action|Adventure|Crime|Drama
 ... 
'''

# import csv
# with open("data/movies.dat", 'r', encoding='ISO-8859-1') as f:
#     # print(f.readline())
#     data = f.readlines()
#     # print(data)
#     data_list = []
#     for row in data:
#         temp = row.replace('\n', '')
#         # print(temp)
#         data_list.append(temp.split('::'))
#
# # print(data_list)
# print(data_list[0])
#
# # 자료형 변환 및 년도 분리시키기
# temp_list = []
# for m, t, g in data_list:
#     t1 = t[:-6].rstrip()
#     t2 = int(t[-5:-1])
#
#     temp_list.append([int(m), t1, t2, g])
#
# # 1980년도 (1980~1989) 영화만 movies_1980 으로 저장하기
# print(temp_list[1]) # [1, 'Toy Story', 1995, "Animation|Children's|Comedy"]
# movie1980_list = []
# for m, t, y, g in temp_list[1:]:
#     if 1980 <= y < 1990:
#         movie1980_list.append([m, t, y, g])
# print(movie1980_list)
#
# field_list = ['MovieID','Title','Year','Genres']
# movie1980_list.insert(0, field_list)
# with open('output/movies_1980_1989.csv', 'w', encoding='utf-8', newline='') as f:
#     csv_data = csv.writer(f, delimiter=',')
#     csv_data.writerows(movie1980_list)




# 퀴즈 12:
# movies.dat 파일을 이용하여
# Animation 장르의 데이타만 animation_movies.csv 파일로 저장하여라.
'''
MovieID,Title,Year,Genres
1,Toy Story,1995,Animation|Children's|Comedy
13,Balto,1995,Animation|Children's
48,Pocahontas,1995,Animation|Children's|Musical|Romance
...

'''
import csv
with open("data/movies.dat", 'r', encoding='ISO-8859-1') as f:
    # print(f.readline())
    data = f.readlines()
    # print(data)
    data_list = []
    for row in data:
        temp = row.replace('\n', '')
        # print(temp)
        data_list.append(temp.split('::'))


# 자료형 변환 및 년도 분리시키기
temp_list = []
for m, t, g in data_list:
    t1 = t[:-6].rstrip()
    t2 = int(t[-5:-1])

    temp_list.append([int(m), t1, t2, g])

print(temp_list[0])

field_list = ['MovieID','Title','Year','Genres']
temp_list.insert(0, field_list)
print(temp_list)


# print(temp_list[1])
# # [1, 'Toy Story', 1995, "Animation|Children's|Comedy"]
# print(temp_list[1][-1]) # Animation|Children's|Comedy
# print(temp_list[1][-1].count('Animation')) # 1


# Animation 무비만 animation_movies.csv 파일로 저장하기
animation_list = []
for m, t, y, g in temp_list[1:]:
    if 'Animation' in g.split('|'):
        animation_list.append([m, t, y, g])
print(animation_list)


# csv 파일로 저장하기
field_list = ['MovieID','Title','Year','Genres']
animation_list.insert(0, field_list)
with open('output/animation_movies.csv', 'w', encoding='utf-8', newline='') as f:
    csv_data = csv.writer(f, delimiter=',')
    csv_data.writerows(animation_list)
