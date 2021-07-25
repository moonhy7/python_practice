# 캐스팅
# 문자열 => 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# 문자열변수.split(sep=구분문자) : 구분문자를 기준으로 해서 리스트화
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경

txt1 = '가 나 다 라 마'
txt2 = '가/나/다/라/마'
print(txt1, type(txt1))
print(txt2, type(txt2))
result1 = txt1.split()
result2 = txt2.split('/')
print(result1, type(result1))
print(result2, type(result2))
print(list(txt1), type(list(txt1)))
print(list(txt2), type(list(txt2)))


# 문자열리스트 => 문자열
# str(리스트이름)
# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화
myList = ['100', '200', '300']
result1 = str(myList)
result2 = ' '.join(myList)
print('-'*50)
print(f'myList = {myList}')
print(f'result1 = {result1}, {len(result1)}')
# result1 = ['100', '200', '300'], 21
print(f'result1[0] = {result1[0]}')
print(f'result2 = {result2}, {len(result2)}')
# result2 = 100 200 300, 11

# 중첩리스트
# 중첩 리스트 구조
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]
myList2d = [[100, 200, 300], ['가','나'], 'Python']
print(myList2d , type(myList2d), len(myList2d))
# [[100, 200, 300], ['가', '나'], 'Python'] <class 'list'> 3
print(myList2d[0]) # [100, 200, 300]
print(myList2d[0][0]) # 100
print(myList2d[1][-1]) # 나
print(myList2d[-1]) # 'Python'

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
grade = [kor, math, eng, python]
print('-'*50)
print(grade)
print('국어점수 = ', grade[0])
print(grade[-1][-1]) # 88
print(grade[3][2]) # 88
print(grade[2][-1])

# 퀴즈 :
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''
kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
grade = [kor, math, eng, python]
kor_tot = grade[0][0] + grade[0][1] + grade[0][2]
math_tot = grade[1][0] + grade[1][1] + grade[1][2]
eng_tot = grade[2][0] + grade[2][1] + grade[2][2]
python_tot = grade[3][0] + grade[3][1] + grade[3][2]
print(f'kor : 합계 = {kor_tot} , 평균 = {(kor_tot/3):.2f}')
print(f'math : 합계 = {math_tot} , 평균 = {(math_tot/3):.2f}')
print(f'eng : 합계 = {eng_tot} , 평균 = {(eng_tot/3):.2f}')
print(f'python : 합계 = {python_tot} , 평균 = {(python_tot/3):.2f}')


# 튜플
# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정)
# 튜플변수 = (값1, 값2...)

# 튜플 생성2 (초기값 지정)
# 튜플변수 = 값1, 값2...

# 튜플 생성3 (빈 튜플)
# 튜플변수 = ()

t1 = (100, 200, 'Python', 'MySQL', True)
t2 = 1, 56, '파이썬'
t3 = ()
# 갯수 1개인 튜플 생성
# 튜플변수 = (값,)
t4 = (1000)
t5 = (1000,)

print(t1, type(t1), len(t1))
print(t2, type(t2), len(t2))
print(t3, type(t3), len(t3))
print(t4, type(t4)) # 1000 <class 'int'>
print(t5, type(t5)) # (1000,) <class 'tuple'>

# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]
t1 = (100, 200, 'Python', 'MySQL', True)
print(t1)
print(t1[0], t1[-1])
print(t1[0:2], t1[2:4], t1[::2], t1[::-1])

# 튜플의 값은 교체가 가능한가?
# TypeError , 내용 교체가 불가능하다.
# TypeError: 'tuple' object does not support item assignment
# t1[0] = '백'

# 튜플은 값을 새로 추가할 수 있는가?
# 튜플변수 += (값1,)
# 한개 추가시에는 쉼표(,) 주의
# 튜플변수 += (값1, 값2...)
myTuple = ()
print(f'myTuple = {myTuple}')
# 1개 삽입시에는 쉼표 주의
myTuple += (10,)
print(f'myTuple = {myTuple}')
myTuple += (99, 88, 77)
print(f'myTuple = {myTuple}')

# 튜플의 값은 삭제가 가능한가?
# 튜플 요소 각각의 값 삭제는 불가능
# 튜플변수 전체 삭제는 가능
# del 튜플변수
myTuple = (100, 200, 'Python', 'MySQL', True)
print(f'myTuple = {myTuple}')
del myTuple
# NameError: name 'myTuple' is not defined
# print(f'myTuple = {myTuple}')

# 튜플의 연산자 + : 튜플끼리 더하기 => 연결
# 튜플의 연산자 * 숫자 : 튜플 요소 반복
myTuple1 = (100, 200)
myTuple2 = ('Python', 'MySQL', True)
print(myTuple1 + myTuple2)
print(myTuple1*3)

# 각각 튜플 변수 정의하기
# 튜플전체변수 = (변수1, 변수2...) = (값1, 값2...)
myTuple = (t1, t2, t3) = (100, 200, 300)
print('-'*50)
print(myTuple)
print(t1, myTuple[0])
print(t2, myTuple[1])
print(t3, myTuple[2])

# 튜플 함수
# 튜플변수.count(값)
# 튜플변수.index(값)
myTuple = (100, 200, 100, 'Python', 'MySQL', True, 100)
print(myTuple)
print('100의 빈도수는? ', myTuple.count(100))
print('첫번째 100값의 위치 인덱스값은? ', myTuple.index(100))

# 캐스팅
# 문자열 => 튜플 : tuple(문자열변수나 값)
# 리스트 => 튜플 : tuple(리스트변수나 값)
# 튜플 => 리스트 : list(튜플변수나 값)
txt = 'abcd'
myList = [10, 20, 30]
myTuple = ('강아지', '고양이', '코끼리')
result1 = tuple(txt)
result2 = tuple(myList)
result3 = list(myTuple)
print(result1, type(result1))
print(result2, type(result2))
print(result3, type(result3))


# 튜플 => 문자열
# : str(튜플변수나 값)
# : 구분자.join(튜플변수나 값)
#  주의사항은 join() 사용시에는 튜플의 자료형이 문자열이어야 한다.
myTuple = ('강아지', '고양이', '코끼리')
# txt = "('강아지', '고양이', '코끼리')"
txt1 = ' ** '.join(myTuple)
txt2 = str(myTuple)
print('-'*50)
print(txt1, type(txt1), len(txt1))
print(txt2, type(txt2), len(txt2))

# 튜플 리스트란?
# 리스트안에 튜플이 삽입되어 있는 구조
# 이중 튜플 = 중첩튜플
# 튜플안에 튜플이 삽입되어 있는 구조
t1 = [(10, 20, 30),(40, 50, 60)]
t2 = ((10, 20, 30),(40, 50, 60))
print(t1, type(t1))
print(t2, type(t3))
print(t1[0],t1[0][0])
print(t2[0],t2[0][0])

# 딕셔너리
# CRUD : Create Read Update Delete
# 딕셔너리 생성 1 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능

# 딕셔너리 생성 2 - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키값]=값

# 문자열키
dict1 = {'a':'apple', 'b':'banana', 'c':'cat'}
# 숫자키
dict2 = {100:'일백', 200:'이백', 300:'삼백'}
print(dict1, type(dict1), len(dict1))
print(dict2, type(dict2), len(dict2))

dict3 = {}
dict3['가'] = '가지'
dict3['나'] = '나라'
print(dict3, type(dict3), len(dict3))

# 딕셔너리 요소 조회 : 키인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시
dict1 = {'a':'apple', 100:'banana', 'c':'cat'}
print(dict1)
print(dict1['a'])
print(dict1[100])

# 리스트, 튜플처럼 숫자 인덱싱이 가능할까?
# KeyError : 딕셔너리는 키값으로만 호출가능
# 리스트, 튜플처럼 슬라이싱이 가능할까?
# TypeError 딕셔너리는 슬라이싱이 불가능
# print(dict1[2])

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
dict1 = {'a':'apple', 'b':'banana', 'c':'cat', 'a':'apart', 'cc':'cat'}
print(dict1['a']) # apart
print(dict1['c']) #'cat'
print(dict1['cc']) #'cat'

# 딕셔너리 값 교체
# 딕셔너리[키값]=값
print('-'*50)
print(dict1)
dict1['b'] = 'base'
print(dict1)

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수
# del 딕셔너리변수[키값]
dict1 = {'a':'apple', 'b':'banana', 'c':'cat', 'cc':'cat'}
print('-'*50)
print(dict1)
dict1.pop('cc')
print(dict1)
del dict1['a']
print(dict1)
dict1.clear()
print(dict1)

# 딕셔너리 함수
# 딕셔너리변수.values() : 값 만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)...
sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print('-'*50)
print(sports)
print(sports.values())
print(sports.keys())
print(sports.items())
# dict_values(['박지성', '강정호', '손연제'])
# dict_keys(['축구', '야구', '체조'])
# dict_items([('축구', '박지성'), ('야구', '강정호'), ('체조', '손연제')])
# 딕셔너리의 값 리스트
print(list(sports.values()))
# 딕셔너리의 키 리스트
print(list(sports.keys()))
# 딕셔너리에서 키와 값으로 구성된 튜플의 리스트
print(list(sports.items()))

# 리스트 => 딕셔너리(인덱스숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시
menuList = ['만두', '순두부', '제육볶음']
print('-'*50)
print(menuList)
# enumerate object화
print(enumerate(menuList)) # <enumerate object at 0x0000029768553300>
# enumerate object => 딕셔너리
result = dict(enumerate(menuList))
print(result, type(result))
# {0: '만두', 1: '순두부', 2: '제육볶음'} <class 'dict'>


# 튜플 => 딕셔너리
menuTuple = ('만두', '순두부', '제육볶음')
print(menuTuple)
print(dict(enumerate(menuTuple)))

# 딕셔너리 => 문자열
# str(딕셔너리변수) => {...}
# 구분자.join(딕셔너리변수) => 키값으로 생성된 문자열
sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print('-'*50)
print(' '.join(sports)) # 축구 야구 체조
print('/'.join(list(sports.values()))) # 박지성/강정호/손연제

# 딕셔너리 => 튜플/리스트
# tuple(딕셔너리) => 키값으로 구성된 튜플 생성
sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print(tuple(sports)) # ('축구', '야구', '체조')
print(list(sports)) # ['축구', '야구', '체조']
print(tuple(sports.values())) # ('박지성', '강정호', '손연제')
print(list(sports.values())) # ['박지성', '강정호', '손연제']

# 딕셔너리 리스트
# 리스트안에 딕셔너리가 있는 구조
dictList = [{'a':'apple', 'v':'victory'},
            {100:'백', 200:'이백'},
            {'user1':'김철수', 'user2':'고소영'}]
print('-'*50)
print(dictList, type(dictList))
print(dictList[0]) # {'a': 'apple', 'v': 'victory'}
print(dictList[0]['a']) # apple
# KeyError: 0
# print(dictList[0][0])


# 집합
# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 집합변수 = {값1, 값2, 값3....}
# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# 중복 데이타는 허용하지 않는다.
s1 = set([-90, 34, 45, 56, 100, 100, 100 ])
s2 = { 'a', 'b', 'c', 'd', 'e' }
print(s1, type(s1))
print(s2, type(s2))

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])
# 집합의 요소 삭제
# 집합변수.remove(값)
# del 집합변수 => 메모리에서 삭제

# [] () {}
# 비어있는 집합 정의
s3 = {}
# s4 = set([])
s4 = set()
print(s3, type(s3)) # {} <class 'dict'>
print(s4, type(s4)) # set() <class 'set'>
# 집합 요소 추가 1
s4.add('python')
s4.add('pandas')
print(s4, type(s4)) # {'python', 'pandas'} <class 'set'>
# 집합 요소 추가 2
s4.update([100, 200, 300])
print(s4, type(s4))
# {100, 'pandas', 200, 300, 'python'} <class 'set'>
# 집합 요소 삭제 remove(값)
s4.remove(300)
print(s4, type(s4))

# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)
s1 = { '최', '김', '선우', '박', '이'}
s2 = { '신', '왕', '선우', '윤', '이'}
print('='*50)
print(f' s1 = {s1}')
print(f' s2 = {s2}')
print(f' 합집합 = {s1|s2}')
print(f' 합집합 = {s1.union(s2)}')

# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)
print(f' 교집합 = {s1&s2}')
print(f' 교집합 = {s1.intersection(s2)}')

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)
print(f' 차집합 = {s1-s2}')
print(f' 차집합 = {s1.difference(s2)}')

# 대칭차집합
# 집합1^집합2
print(f' s1 = {s1}')
print(f' s2 = {s2}')
print(f' 대칭차집합 = {s1^s2}')

# 캐스팅
# 집합 => 리스트
# list(집합변수)
# 집합 => 튜플
# tuple(집합변수)
# 리스트,문자열,튜플 => 집합
# set(리스트,문자열,튜플)
myList = [100, 200, 300, 400]
myTuple = ('최', '김', '선우', '박', '이')
mySet = { '신', '왕', '윤'}
myTxt = '가나다라마바사'
myDict = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print('집합 => ', mySet)
print('집합 => 튜플', tuple(mySet))
print('집합 => 리스트', list(mySet))
print('집합 => 문자열', '!'.join(mySet))
# ValueError
# print('집합 => 딕셔너리', dict(mySet))
print('집합 => enumerate => 딕셔너리', dict(enumerate(mySet)))