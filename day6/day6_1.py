
# import os # os 관련 함수() 사용이 가능한 모듈
# os.getcwd()
# 현재 작업폴더 위치 확인하기
# 인터프리터 python.exe 파일 위치 정보와 현재 파일 위치 정보가 출력
# os.listdir(경로)
# 경로로 지정된 폴더의 파일 목록등 표시
# os.mkdir(폴더명)
# os.chdir(경로)
# 지정된 경로로 폴더 이동


import os
# 현재 작업폴더 위치 확인
print(os.getcwd())
# C:\Users\lkiop\.conda\envs\pyclass\python.exe C:/pyclass/day6_1.py
# C:\pyclass

# 작업폴더안의 파일과 목록 => 리스트화
print(os.listdir(os.getcwd()))

# 폴더 탐색
os.chdir('data')
print(os.getcwd()) # C:\pyclass\data
# data 폴더안의 파일 목록 확인 => 리스트 반환
print(os.listdir(os.getcwd()))

# 파일입출력
# 파일변수  = open(파일경로, 'r'/'w'/'a',
#                    encoding='utf-8/cp949')
# 파일변수.파일입출력함수(옵션)

# 파일읽기
# 파일변수 생성
# 파일변수  = open(파일경로, 'r',
#                     encoding='utf-8/cp949')
# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트

# 현재 위치 확인
print(os.getcwd()) # C:\pyclass\data
# 폴더 경로 변경
os.chdir('../')
print(os.getcwd()) # C:\pyclass

# Yesterday.txt 파일 읽기
# FileNotFoundError
# f = open('Yesterday.txt', 'r')

f = open('data/Yesterday.txt', 'r')
print(f, type(f))
# <_io.TextIOWrapper name='Yesterday.txt' mode='r' encoding='cp949'>
# <class '_io.TextIOWrapper'>

# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
result1 = f.read()
print(type(result1))  # <class 'str'>
print(result1)
# 파일 닫기 : 파일변수.close()
f.close()

# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
print('='*50)
f = open('data/Yesterday.txt', 'r')
result2 = f.readline()
print(result2)
f.close()

# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트
print('='*50)
f = open('data/Yesterday.txt', 'r')
result3 = f.readlines()
print(type(result3))
print(result3)
f.close()

# 3줄만 출력하기
for i in range(3):
    print(f'{i+1} 행 => {result3[i]}')
print('*'*50)

# 2~4 범위 지정해서 출력하기
for i in range(1, 4):
    print(f'{i+1} 행 => {result3[i]}')

print('*'*50)
count = 2
for row in result3[1:4]:
    print(f'{count} 행 => {row}')
    count += 1


print('*'*50)
print(result3)
# '\n' 요소 삭제
print("\\n의 갯수는?", result3.count("\n")) # 5
# 값으로 하나만 삭제
# result3.remove('\n')
# print("\\n의 갯수는?", result3.count("\n")) # 4
# print(result3)
# 리스트에서 모두 삭제 '\n'
for i in range(5):
    result3.remove('\n')
print("\\n의 갯수는?", result3.count("\n"))
print(result3)

# 리스트 요소안의 '\n' 삭제하기
# 문자열변수.replace(old, new)
temp = []
for row in result3:
    # print(row)
    temp.append(row.replace('\n', ''))
print(temp)
result3 = temp
print(result3)

# 5줄만 출력하기
for i in range(5):
    print(f'{i+1} 행 => {result3[i]}')
print('*'*50)

# 'Yesterday.txt'는 몇개의 어구로 구성되어 있을까?
# 공백을 기준으로 단어별로 리스트 저장
f = open('data/Yesterday.txt', 'r')
result1 = f.read()
print(type(result1))  # <class 'str'>
print(result1)
# 파일 닫기 : 파일변수.close()
f.close()

result_list = result1.split()
print(result_list)
print(f'단어 갯수 = {len(result_list)}')

# 중복 제거하기
result_list2 = list(set(result_list))
print(result_list2)
print(f'단어 갯수 = {len(result_list2)}')