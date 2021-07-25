# dir(자료형) => Reference 기능
# 사용가능한 속성과 함수를 리스트 구조로 표시
print(dir('String'))
# print(dir(True))
print(dir(100))
# print(dir([1,2,3,4,5]))
# print(dir((1,2,3,4,5)))
print(dir({1:'하나', 2:'둘'}))
# print(dir({1,2,3,4,5}))


# zip(리스트1, 리스트2 .. )
# zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# list(zip 객체): [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.

p1 = ['길동', '동미', '미영', '영철']
p1Gender= ['남','여','여','남']
zipObj = zip(p1, p1Gender)
print(zipObj, type(zipObj))
# <zip object at 0x0000017B05770BC0> <class 'zip'>
# for 문 이용해서 구성요소 출력 1
for item in zipObj:
    print(item)
'''
('길동', '남')
('동미', '여')
('미영', '여')
('영철', '남')
'''
print('-'*50)
# for 문 이용해서 구성요소 출력 2
zipObj = zip(p1, p1Gender)
for i, j in zipObj:
    print(i, j)
'''
길동 남
동미 여
미영 여
영철 남
'''
# 리스트화  => 튜플리스트
print(list(zip(p1, p1Gender)))
# [('길동', '남'), ('동미', '여'), ('미영', '여'), ('영철', '남')]

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 결과물은 같은 인덱스의 값만 튜플로 다시 생성
# 리스트 튜플 정의
tupleList = [('a','apple'),('b','banana'),('c','cat')]
print(tupleList, type(tupleList))
# 변수를 지정한 후 zip 함수 적용
x,y = zip(*tupleList)
print(x) # ('a', 'b', 'c')
print(y) # ('apple', 'banana', 'cat')


# random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

import random
# 특정 범위에서 정수 난수 출력하기
# random.randint(start, end) : start~end 사이의 정수 난수
print(random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5))

# 로또번호 뽑기 : 1~46 중 중복없이 6개를 뽑아 로또번호 리스트를 출력하여라
# 아래의 코딩 소스에서 로또 번호가 중복없이 표시되도록 프로그래밍하여라.

# 중복 허용
# def make_lotto():
#     lotto_list = []
#     for i in range(6):
#         temp = random.randint(1, 46)
#         lotto_list.append(temp)
#     return print('로또 리스트 => ' , lotto_list)
# make_lotto()
# make_lotto()
# make_lotto()
# make_lotto()
# make_lotto()
# make_lotto()
# make_lotto()
# '''
# 로또 리스트 =>  [40, 14, 40, 32, 41, 9]
# 로또 리스트 =>  [10, 11, 18, 45, 24, 23]
# 로또 리스트 =>  [28, 1, 16, 41, 45, 21]
# 로또 리스트 =>  [3, 20, 42, 38, 36, 34]
# 로또 리스트 =>  [43, 23, 36, 19, 41, 42]
# 로또 리스트 =>  [41, 31, 39, 29, 10, 17]
# 로또 리스트 =>  [9, 14, 26, 2, 20, 13]
# '''

# 중복 허용 X
def make_lotto():
    lotto_list = []
    while True:
        temp = random.randint(1, 46)
        # lotto_list 에 없다면 리스트에 추가한다.
        if temp not in lotto_list:
            lotto_list.append(temp)
        if len(lotto_list) == 6:
            break
    return print('로또 리스트 => ' , lotto_list)

for i in range(10):
    make_lotto()

# not in 과 in 연산자
# 값 in/not in 리스트/문자열/튜플... => True/False
print(123 in [123, 456, 789]) # True
print(123 not in [123, 456, 789]) # False
print(56 in [123, 456, 789]) # False
print(56 not in [123, 456, 789]) # True

# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
eventList = ['꽝', '미니쿠퍼', '1억원(세금없음)', '금 10돈',
             '스타벅스 10만원 상품권', '캠핑카', '초코파이 1상자']

# 중복 있음
for i in range(5):
    print('상품 뽑기', i+1, random.choice(eventList))

print('-'*50)
# 중복 없음
print(eventList)
for i in range(5):
    temp = random.choice(eventList)
    print('상품 뽑기', i+1, temp)
    # 뽑은 상품은 리스트에서 삭제
    eventList.remove(temp)
    print(eventList)
    print('='*30)

# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.
stList = ['김철수', '홍길동', '기대주', '이동백', '하민수']
print(stList)
# print(random.shuffle(stList)) # None
random.shuffle(stList)
print(stList)
random.shuffle(stList)
print(stList)

# 퀴즈 : 학생중에서 2명을 오늘의 청소 당번으로 하려고 한다.
# random.shuffle() 함수를 이용하여 2명만 출력하여라.
print('-'*50)
def choice_student(stList):
    random.shuffle(stList)
    # print(stList)
    return print(f'청소 당번 => {stList[0]}, {stList[1]}')

choice_student(['김철수', '홍길동', '기대주', '이동백', '하민수', '고길동', '임영웅'])
stList = ['김철수', '홍길동', '기대주', '이동백', '하민수', '고길동', '임영웅']
choice_student(stList)

# filter(함수명/lambda 함수, 리스트/튜플),
# map(함수명/lambda 함수, 리스트/튜플),
# reduce(함수명/lambda 함수, 리스트/튜플)
# 정의된 사용자정의함수, 람다함수를  리스트 데이타 각각에 적용한다.

# filter()
# filter(함수명/lambda 함수, 리스트/튜플)
# 사용할 함수는 결과값이 True/False
# 함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
# => 참인조건의 리스트만 출력

# 리스트에서 짝수만 출력하여라
# 일반 함수 이용
def make_odd(numList):
    result = []
    for item in numList:
        if item%2 == 0:
            result.append(item)
    return result

print('\n== 일반 함수 이용')
numList = [10, 56, -90, 45, 300, 23, 11]
print(numList, '=>', make_odd(numList))

print('\n== filter + 함수 이용')
# 순서
# 1) 리스트 원소 한개에 해당하는 함수 생성 => True/False 반환
# 2) filter 함수 적용 filter(함수, 리스트)
# 3) 리스트화
# 숫자가 짝수이면 True 반환
def check_number(n):
    if n % 2 == 0:
        return True
print(check_number(100)) # True
print(check_number(55)) # None

# filter() 함수 적용 => filter 객체
numList = [10, 56, -90, 45, 300, 23, 11]
print(filter(check_number, numList))
# <filter object at 0x000001D4A489EA30>

# 리스트화
# print(list(filter(check_number, numList)))
print(numList, '=>', list(filter(check_number, numList)))


print('\n== filter + 람다 함수 이용')
# 순서
# 1) 리스트 원소 한개에 적용되는 람다 함수 생성 => 값 반환
# 2) filter 함수 적용 filter(람다함수, 리스트)
# 3) 리스트화

# 짝수일때 값 반환
# 함수변수 = lambda 인자:명령
# 호출은? 함수변수(인자)

# 짝수이면 True를 반환하는 람다함수 정의
f1 = lambda n: n % 2 == 0
print(f1(100)) # True
print(f1(33)) # False

# filter 적용
numList = [10, 56, -90, 45, 300, 23, 11]
print(filter(f1, numList))
# <filter object at 0x000002DD6652BA60>

# filter 적용 후 리스트화
print(list(filter(f1, numList)))
# [10, 56, -90, 300]

'''
# filter를 적용하지 않고 특정 리스트에서 짝수만 표시
def make_odd(numList):
    result = []
    for item in numList:
        if item%2 == 0:
            result.append(item)
    return result
print(make_odd([10, 56, -90, 45, 300, 23, 11]))
'''
# 람다함수를 filter 함수에 바로 적용한 경우
print(list(filter(lambda n: n % 2 == 0, [10, 56, -90, 45, 300, 23, 11])))

# 리스트에서 양수만 출력하여라

# 일반함수 사용
def positive_list(myList):
    result = []
    for item in myList:
        if item > 0:
            result.append(item)
    return result
print([10, -44, 78, -90, -5], ' => ', positive_list([10, -44, 78, -90, -5]))

# filter + 함수 : filter(함수, 리스트)
# 1) 리스트 원소 한개에 해당하는 함수 생성 => True/False 반환
def check_positive(n):
    # if n > 0:
    #     return True
    return n>0
print('-'*60)
print(check_positive(-100)) # False
print(check_positive(40)) # True

# 2) filter 함수 적용 filter(함수, 리스트) + 리스트화
result = list(filter(check_positive, [10, -44, 78, -90, -5]))
print([10, -44, 78, -90, -5], ' => ', result)

print('-'*60)
# filter + 람다함수 : filter(람다함수, 리스트)
# 1) 람다함수 정의
f_positive = lambda n:n>0
print(f_positive(90)) # True
print(f_positive(-90)) # False

# 2) filter함수에 람다함수 적용 filter(람다함수, 리스트) + 리스트화
result = list(filter(f_positive, [10, -44, 78, -90, -5]))
print([10, -44, 78, -90, -5], ' => ', result)
# [10, -44, 78, -90, -5]  =>  [10, 78]

# 한줄로 filter+labda
print('-'*60)
print([10, -44, 78, -90, -5], ' => ', list(filter(lambda n:n>0, [10, -44, 78, -90, -5])))


# 퀴즈 :문자열에서 숫자만 리스트로 만들기
message = 'ab4690cfvg342가1나1다0'
print('*'*60)
# 일반 함수 이용
def make_numberlist(txt):
    result = []
    for i in range(len(txt)):
        if txt[i].isdigit():
            result.append(txt[i])
    return result
print(message, ' => ', make_numberlist(message))

# filter + 함수
print('*'*60)
def check_c(c):
    return c.isdigit()
print(check_c('t')) # False
print(check_c('9')) # True
message = 'ab4690cfvg342가1나1다0'
print(message, ' => ', list(filter(check_c, message)))

# filter + 람다함수
print('*'*60)
f_c = lambda c:c.isdigit()
print(f_c('t')) # False
print(f_c('9')) # True
message = 'ab4690cfvg342가1나1다0'
print(message, ' => ', list(filter(f_c, message)))
print(message, ' => ', list(filter(lambda c:c.isdigit(), message)))
# ab4690cfvg342가1나1다0  =>  ['4', '6', '9', '0', '3', '4', '2', '1', '1', '0']

# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된 함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가
#
# 리스트의 제곱을 구해서 새로운 리스트로 만들기  ')
# numlist = [1,2,3,4]  결과 => [1, 4, 9, 16]

# 일반 함수 이용
def power_list(myList):
    result = []
    for item in myList:
        result.append(item**2)
    return result
numlist = [1,2,3,4]
print('일반 함수 이용 : ', numlist, ' => ', power_list(numlist))

# map() 이용
# 순서
# 1) 리스트 원소 한개에 적용되는 일반 함수나 람다함수 생성 => 값 반환
# 2) map 함수 적용 => list(map(람다함수/일반함수, 리스트))
def power_one(n):
    return n**2
# print(power_one(5)) # 25
numlist = [1,2,3,4]
print('map 함수 이용1 : ', numlist, ' => ', map(power_one, numlist))
print('map 함수 이용2 : ', numlist, ' => ', list(map(power_one, numlist )))

# 람다함수 정의
f_power = lambda n:n**2
# print(f_power(5)) # 25
numlist = [1,2,3,4]
print('map 함수 + 람다 이용1 : ', numlist, ' => ', map(f_power, numlist))
print('map 함수 + 람다 이용2 : ', numlist, ' => ', list(map(f_power, numlist )))

# 한줄로 코딩화
print('map 함수 + 람다 이용3 : ', numlist, ' => ', list(map(lambda n:n**2, [1,2,3,4] )))

print('#'*60)
# 두 리스트에서 같은 위치의 데이타 값을 서로 곱하여라
listA = [10, 20, 5, 78, 33]
listB = [4, 6, 23, 56, 11]

# TypeError
# print(listA*listB)
# 리스트 반복
print(listA*3)
# [10, 20, 5, 78, 33, 10, 20, 5, 78, 33, 10, 20, 5, 78, 33]

# 일반 함수 이용
def make_multylist(list_a, list_b):
    result = []
    for i in range(0, len(list_a)):
        temp = list_a[i]*list_b[i]
        result.append(temp)
    return result

listA = [10, 20, 5, 78, 33]
listB = [4, 6, 23, 56, 11]
print('='*50)
print(listA,' * ', listB)
print('일반 함수 이용 :  => ', make_multylist(listA, listB ))

# map() + 일반함수 이용
def mul(x,y):
    return x*y
print('='*50)
print(listA,' * ', listB)
print('map() + 일반함수 이용 :  => ', map(mul, listA, listB))
print('map() + 일반함수 이용 :  => ', list(map(mul, listA, listB)))

# map() + 람다함수 이용
print('='*50)
print(listA,' * ', listB)
print('map() + 람다함수 이용 :  => ', list(map(lambda x,y:x*y, listA, listB)))

print('======== reduce')
# reduce()
# 리스트의 요소에 함수를 적용해 1개의 결과를 리턴한다.
# reduce(람다나 정의한 함수, 리스트나 튜플)
# 외장함수로 import functools 모듈 임포트 명령 필요
# 모듈내의 함수 사용1?
# import functools
# functools.reduce(옵션)
# 모듈내의 함수 사용2? = 별칭 지정
# import functools as f
# f.reduce(옵션)

# 리스트의 모든 합을 구하여라
# 일반함수
def sum_list(myList):
    tot = 0
    for item in myList:
        tot += item
    return tot
numList = [10, 56, 23, 45, 77]
print('일반함수를 이용한 리스트의 모든 합 ', numList, ' => ', sum_list(numList))

# reduce()  적용 순서
# 1) 리스트 원소 2개에 적용되는 일반 함수나 람다함수 생성 => 값 반환
# 2)
# reduce 함수 적용1 => functools.reduce(람다함수/일반함수, 리스트))
# reduce 함수 적용2 => 별칭.reduce(람다함수/일반함수, 리스트))

# 모듈 임포트
import functools as f

def add_two(x, y):
    return x+y
numList = [10, 56, 23, 45, 77]
print('reduct를 이용한 리스트의 모든 합1', numList, ' => ', f.reduce(add_two, numList))
print('reduct를 이용한 리스트의 모든 합2', numList, ' => ', f.reduce(lambda x, y:x+y, numList))

# 딕셔너리 리스트란?
# 리스트안에 딕셔너리가 있는 구조
users = [   {'mail': 'gregory@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},
            {'mail': 'hinton@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},
            {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},
            {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},
            {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42} ]
print('*'*80)
for row in users:
    # print(row)
    for key in row:
        print(row[key], end='\t\t')
    print()
    print('-'*80)

# 딕셔너리 리스트에서 나이의 합 구하기
# 일반함수 이용
def sum_age(users):
    tot = 0
    for dict in users:
        tot += dict['age']
    return tot

print('일반함수 이용 : 나이의 총합은?  => ', sum_age(users))

# reduce() + 함수 이용
def add_age(acc, dict):
    return acc + dict['age']
# TypeError: unsupported operand type(s) for +: 'dict' and 'int'
# print('reduce() + 함수 이용  : 나이의 총합은?  => ', f.reduce(add_age, users))

# 딕셔너리의 합을 구하는 경우에는 모듈명.reduce(함수/람다, 딕셔너리리스트명, 초기값)
print('reduce() + 함수 이용  : 나이의 총합은?  => ', f.reduce(add_age, users, 0))

# reduce + 람다
print('reduce() + 람다 이용  : 나이의 총합은?  => ', \
      f.reduce(lambda acc, dict:acc + dict['age'], users, 0))

print('*'*80)
for row in users:
    # print(row)
    for key in row:
        print(row[key], end='\t\t')
    print()
    print('-'*80)

# 이메일 리스트 만들기
# TypeError: can only concatenate list (not "str") to list
# print('reduce() + 람다 이용  : 이메일 리스트  => ', \
#       f.reduce(lambda acc, dict:acc + dict['mail'], users, []))

print('reduce() + 람다 이용  : 이메일 리스트  => ', \
      f.reduce(lambda acc, dict:acc + [dict['mail']], users, []))

'''
reduce() + 람다 이용  : 이메일 리스트  =>  ['gregory@gmail.com', 'hinton@hotmail.com', 'wwagner@gmail.com', 'daniel79@gmail.com', 'ujackson@gmail.com']

'''

import pandas as pd
df = pd.DataFrame(users)
print(df)
print(df.dtypes)