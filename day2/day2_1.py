'''
== REVIEW
아나콘다 + 파이참 작업환경 설정
주석
출력문 print()
변수
기본자료형
입력문 input()
자료형 변환
연산자
문자열 인덱싱과 슬라이싱
문자열 함수
퀴즈1
'''

# 파이썬의 자료형의 종류
# - 기본 자료형(정수,실수,논리형,문자열), 집합형 자료형
# 집합 자료형 - 리스트, 튜플, 딕셔너리, 집합...
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }
# CRUD : Create Read Update Delete

# 리스트 []
# 다른 데이터형 가능
# 순차적으로 생성
# 빈 리스트, 초기값 설정 방식

# 초기값 설정 방식을 이용한 리스트 정의
# 리스트변수 = [값1, 값2...]
# type() , len()
list1 = [100, 3.14, True, 'Python']
print(list1, type(list1), len(list1))
# [100, 3.14, True, 'Python'] <class 'list'> 4

# 빈 리스트를 이용한 리스트 정의
# 리스트변수 = []
list2 = []
print(list2, type(list2), len(list2))
# [] <class 'list'> 0
# 아이템 추가는?
# 리스트변수.append(아이템값)
list2.append('부산')
list2.append('대구')
list2.append('서울')
list2.append('대전')
print(list2, len(list2))

# 리스트 인덱싱
# 리스트 인덱싱
# 리스트이름[숫자] : 0부터 시작, 숫자값이 -1 마지막 요소 표시
list3 = [100, 200, 300, 400, 500, 600, 700]
print(list3[:])
print(f'첫번째 리스트값은? {list3[0]}')
print(f'마지막 리스트값은? {list3[6]}')
print(f'마지막 리스트값은? {list3[-1]}')

# 리스트 슬라이싱
# 리스트이름[start:end:step]
# 리스트이름[start:end]
# 리스트이름[start:]
# 리스트이름[:end]
# 리스트이름[::step]
# 리스트이름[:] = 리스트이름[::] = 전체리스트
print(f'list3[1:5] =>  {list3[1:5]}')
print(f'list3[:5] =>  {list3[:5]}')
print(f'list3[5:] =>  {list3[5:]}')
print(f'list3[::2] =>  {list3[::2]}')
print(f'list3[1::2] =>  {list3[1::2]}')
print(f'list3[::-1] =>  {list3[::-1]}')

# 리스트 값 변경하기
# 리스트변수[인덱스] = 값
print(f'list3 =>  {list3}')
list3[0] = '백'
print(f'list3 =>  {list3}')

# 리스트 연산자 => +, *
# 리스트1 + 리스트2 : 같이 표시
# 리스트이름*숫자 : 반복
listA = ['라면', '짬뽕', '김밥']
listB = ['사과', '포도']
print(f'listA =>  {listA}')
print(f'listB =>  {listB}')
print(f'listA + listB =>  {listA+listB}')
print(f'listA*3 =>  {listA*3}')

# 리스트 함수
# 리스트변수.함수명(옵션)


# 정의된 리스트에 새로운 값을 추가
# 리스트변수.append(값) : 마지막에 아이템이 추가
# 리스트변수.insert(삽입위치, 값) : 삽입위치에 아이템이 추가
# 여러개의 요소를 한꺼번에 리스트에 추가 싶다면?
# 리스트변수.extend([값1,값2...])
myList = [10, 20, 30]
print(f'myList =>  {myList}')
myList.append('Python')
print(f'myList =>  {myList}')
myList.insert(0, '판다스')
print(f'myList =>  {myList}')
myList.extend([True, False])
print(f'myList =>  {myList}')
myList.insert(0, ['가', '나', '다'])
print(f'myList =>  {myList}')
# myList =>  [['가', '나', '다'], '판다스', 10, 20, 30, 'Python', True, False]

# 리스트 삭제와 관련된 함수와 명령어
# 리스트변수.remove(값) : 값으로 삭제하기
# 리스트변수.pop() : 마지막 요소가 삭제되면서 값이 반환된다.
# 리스트변수.pop(위치값)
# : 위치에 해당하는 요소가 삭제되면서 값이 반환된다.
# 리스트변수.clear() : 리스트안의 값이 모두 삭제. 빈리스트로 된다.
# del 리스트변수 : 리스트 자체가 삭제된다.
myList = [100, 200, 300, 400, 500, 600, 700]
print(f'myList =>  {myList}')
myList.remove(500)
print(f'myList =>  {myList}')
print(f'삭제요소 => {myList.pop()}')
print(f'myList =>  {myList}')
print(f'삭제요소 => {myList.pop(0)}')
print(f'myList =>  {myList}')
myList.clear()
print(f'myList =>  {myList}')
del myList
# NameError: name 'myList' is not defined
# print(f'myList =>  {myList}')

# 입력받은 값으로 리스트를 생성하여라 (리스트 갯수 3개)
# input()
# myList = []
# item = input('아이템1 값은? ...')
# myList.append(item)
# item = input('아이템2 값은? ...')
# myList.append(item)
# item = input('아이템3 값은? ...')
# myList.append(item)
# print(f'myList = {myList}')


# 리스트 값 정렬하기
# 리스트변수.reverse()
# 리스트변수.sort()
# 주의사항은 리스트변수.sort()의 경우
# 리스트를 이루는 구성요소의 데이터형은 같아야한다
# TypeError 발생
myList = [88, 67, 77, 34, 1, 109, 50]
print(f'myList = {myList}')
myList.sort()
print(f'myList = {myList}')
myList.reverse()
print(f'myList = {myList}')

# 주의사항은 리스트변수.sort()의 경우
# 리스트를 이루는 구성요소의 데이터형은 같아야한다
# TypeError 발생
myList2 = [88, 67, 'Python', 1, 109, 50]
print(f'myList2 = {myList2}')
# TypeError: '<' not supported between instances of 'str' and 'int'
# myList2.sort()

# reverse()의 경우에는 결과 X 에러 X
myList2.reverse()
print(f'myList2 = {myList2}')

# 리스트변수.count(값)
# 중복값이 몇개인가?
# 리스트변수.index(값)
# 값에 해당하는 요소가 몇번째에 위치하고 있는가?
myList = [88, 50, 67, 'Python', 1, 109, 50, 50]
print(f'myList = {myList}')
print(f'myList에서 50의 빈도수는? {myList.count(50)}') # 3
print(f'myList에서 50의 인덱스값은? {myList.index(50)}') # 1

# 리스트 퀴즈 - 2문제 이상 코딩해서 채팅창또는 메일로 전송해주세요
# coderecipe@naver.com

# 퀴즈 1

'''
2개의 리스트를 정의하고 다음과 같이 출력한다.
myList1 : ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
myList2 : ['토끼', '거북이', '물개', '펭귄']

1. 2개의 리스트 합(+ 연산자 이용)  : ?
2. 1번의 리스트에서 앞에서 순차적으로 4개만 출력 : ? 
3. 1번의 리스트에서 짝수번째만 출력 : ?
4. 1번의 리스트에서 홀수번째만 출력 : ?
5. 1번의 리스트에서 전체 길이 :  ?
'''

# 퀴즈 2
'''
리스트를 정의한 후 리스트 요소를 편집한다.
(변경, 삭제, 추가)
['사과', '배', '망고']
첫번째 요소 변경 후 : ['포도', '배', '망고']
마지막 위치에 요소 추가후 : ['포도', '배', '망고', '오렌지']
2번째 위치에 요소 추가후 : ['포도', '수박', '배', '망고', 
                        '오렌지']
마지막 위치 삭제 : ['포도', '수박', '배', '망고']
배 삭제 : ['포도', '수박', '망고']
'''

# 퀴즈 3
'''
데이터를 입력받은 후 리스트에 추가하는 예제입니다.
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산
당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''

# 퀴즈 4
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']

'''
