import os

# 파일 url, encoding(cp949, utf-8) 값을 매개변수로 전달받아서
# 파일 내용을 반환하는 함수 정의
def read_file(url, enc):
    f = open(url, 'r', encoding=enc)
    result = f.read()
    f.close()
    return  f'url = {url} \nencoding = {enc} \n {result}'

# print('=' * 50)
# print(os.getcwd()) # C:\pyclass
# print(read_file('data/national_anthem.txt','cp949'))
# print('=' * 50)
# print(read_file('data/coding.txt','utf-8'))


# 퀴즈
# 파일의 단어 전체갯수와 포함된 단어 중 5개만
# 표시되는 함수를 정의하여라. (중복 제거)
'''
def printWord(fileURL, op):
    #명령어 기입
'''
# >> 함수호출
# printWord('data/Yesterday.txt')
# >> 결과값
# 파일명 : data/Yesterday.txt
# 단어 갯수 : 134
# 단어 5개 출력
# ['Yesterday', 'All', 'my' ... ]

def printWord(url, enc):
    f = open(url, 'r', encoding=enc)
    result = f.read()
    f.close()
    result_list = list(set(result.split()))
    print('*'*50)
    print(f'파일명 : {url}')
    print(f'갯수 : {len(result_list)}')
    # print(f' 전체 리스트 : {result_list}')
    print(f'5개 출력 : {result_list[:5]}')

printWord('data/Yesterday.txt', 'cp949')
printWord('data/coding.txt','utf-8')

# 퀴즈
# data_eng.txt, data_kor.txt
# 파일에 삽입된 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
# 함수 정의 => 파일읽기 => 리스트화
# => 리스트의 값 더하기(숫자형데이터로 변환) : 합
# => 합 / 리스트갯수 : 평균

# '''
# # 함수 호출
# sumAvr('data/data_eng.txt', 'cp949')
# sumAvr('data/data_kor.txt', 'cp949')
#
# >> 결과
#
# 파일명 =  data/data_eng.txt
# 데이터 수 =  12
# 합 =  933
# 평균 = 77.75
#
# ----------
# 파일명 =  data/data_kor.txt
# 데이터 수 =  12
# 합 =  892
# 평균 = 74.33
#
# '''

def sumAvr(url, enc):
    f = open(url, 'r', encoding=enc)
    # 리스트화
    score_list = f.readlines()
    f.close()
    # 총합 구하기
    tot = 0
    for item in score_list:
        tot += int(item)
    print('*'*50)
    print(f'파일명 : {url}')
    print(f'데이터 수  : {len(score_list)}')
    # print(score_list)
    print(f'총합  : {tot}')
    print(f'평균  : {(tot/len(score_list)):.2f}')
sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')

# 파일 쓰기
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

print(os.getcwd()) # C:\pyclass

# 특정 위치에 빈 파일 생성하기
# f = open('data/sample_0.txt', 'w')
# f.close()
# 작업 위치 이동
os.chdir('data')
print(os.getcwd())
print(os.listdir(os.getcwd()))
if 'sample_0.txt' in os.listdir(os.getcwd()):
    print('파일이 생성되었습니다.')

# 특정 파일에 내용 쓰기
# 기존 파일 목록이 있다면 덮어쓴다.
print(os.getcwd()) # C:\pyclass\data
# 지정한 폴더가 없다면 에러 발생 : FileNotFoundError
f = open('sample_1.txt', 'w', encoding='utf-8')
f.write('='*50+'\n')
f.write('사과\n')
f.write('과수원\n')
f.write('원숭이\n')
f.close()

# 반복문 이용해서 파일에 내용추가하기
f = open('sample_2.txt', 'w', encoding='utf-8')
myFoodList = ['라면', '김치전', '모밀', '초밥', '샐러드']
count = 1
for item in myFoodList:
    f.write(str(count)+' => ' + item + '\n')
    count += 1
f.close()

if 'sample_2.txt' in os.listdir(os.getcwd()):
    print('파일이 생성되었습니다.')


# 퀴즈 :
# data/Yesterday.txt 파일에서 10줄만
# data/result_Yesterday.txt 파일에 저장하기
# 작업 과정
# 파일 읽기
# 리스트 구조로 저장
# 슬라이싱 = 리스트변수[0:10]
# 파일 쓰기

# print('-'*50)
# f1 = open('Yesterday.txt', 'r')
# f2 = open('result_Yesterday.txt', 'w', encoding='utf-8')
# resultList = f1.readlines() # 리스트에 저장
# print(f'resultList = {resultList}')
# # 리스트에서 '\n' 삭제
# for i in range(resultList.count("\n")):
#     resultList.remove('\n')
# print(f'resultList = {resultList}')
#
# # 파일 쓰기
# cnt = 1
# for row in resultList[0:10]:
#     dataLine = str(cnt) + '행 => ' + row
#     f2.write(dataLine)
#     cnt += 1
#     print('내용이 추가되었습니다.')
#
# f1.close()
# f2.close()


# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

# 빈 파일에 내용추가하기
# print(os.getcwd()) # C:\pyclass\data
# f = open('sample_a.txt', 'w', encoding='utf-8')
# f.write('========== Start 1 =============')
# f.close()

# f = open('sample_a.txt', 'a', encoding='utf-8')
# f.write('\n========== Start 2 =============')
# f.close()

# 기존 파일에 입력받은 내용 추가하기
# f = open('sample_a.txt', 'a', encoding='utf-8')
# while True:
#     item = input('데이타 삽입 (q 는 프로그램 종료) ===> ')
#     if item == 'q':
#         break
#     else:
#         f.write('\n' + item )
# print('테스트 종료')
# f.close()

# Delete 구현 1
# 파일변수.write() => 파일은 존재하고 안에 내용은 삭제
# 파일 내용 삭제 => 빈파일로 생성
# f = open('sample_a.txt', 'w', encoding='utf-8')
# f.close()

# Delete 구현 2 => 파일 삭제
# 삭제할 파일이 없으면 에러 발생
# FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다:
# 파일 삭제
# import os
# os.remove(삭제파일경로)
# ans = input('파일을 삭제하시겠습니까? ...')
# if ans.upper() == 'Y':
#     os.remove('sample_a.txt')

# 파일이 있다면 삭제
# 없다면 메세지 출력
print(os.listdir())
print('*'*50)
remove_file = 'sample_0.txt'
if remove_file in os.listdir():
    ans = input('파일을 삭제하시겠습니까? ...')
    if ans.upper() == 'Y':
        os.remove(remove_file)
        print('파일이 삭제되었습니다.')
else:
    print('파일 목록이 없습니다. 삭제가 불가능합니다.')




