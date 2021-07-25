# 웹상의 json 데이타 => 문자열 데이타 =>  딕셔너리

# 데이타 획득
# json sample site
# http://jsonplaceholder.typicode.com/
# http://jsonplaceholder.typicode.com/todos

from urllib.request import urlopen
import json
import pandas as pd

# 웹상의 데이타 저장
url = 'http://jsonplaceholder.typicode.com/todos'
request = urlopen(url)
json_str = request.read()
print('\n\n 문자열 데이타 => ')
print(type(json_str))
print(json_str)

# json.loads() 함수 적용
todos = json.loads(json_str)
print('\n\n todos 데이타 => ')
print(type(todos)) # <class 'list'>
print(todos)

print('\n\n todos 첫번째 데이타 => ')
print(todos[0])

print('\n\n todos 마지막 데이타 => ')
print(todos[-1])

print('\n\n todos 전체 출력  => ')
for item in todos:
    for key in item:
        print(key,'=>', item[key], end=' / ')
    print()

print('\n\n = userId 키가 1이고 completed 키값이 True 인 목록과 총 갯수 표시')
cnt = 0
for i in range(len(todos)):
    if (todos[i]['userId'] == 1) and (todos[i]['completed'] == True):
        print(todos[i])
        cnt += 1
print('총갯수는? ', cnt)

# 데이타 프레임화
# 딕셔너리리스트 => 데이타프레임
# columns 속성값이 없는 경우 컬럼명은 딕셔너리의 키로 지정된다.
df = pd.DataFrame(todos)
print(df)

# 엑셀 파일로 저장하기
df.to_excel('output/todos.xlsx', index=False)