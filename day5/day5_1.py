# 함수의 종류
'''
- 사용자 정의 함수
- 빌트인함수 : 외장함수 , 내장함수
'''
# 수학관련 내장 함수
# 절대값 리턴 : abs(숫자)
# 최대값 리턴 : max(리스트/튜플/집합...)
# 최소값 리턴 : min(리스트/튜플/집합...)
x = -800
y = 900
print(f'x의 절대값 = {abs(x)} , y의 절대값 = {abs(y)}')
# x의 절대값 = 800 , y의 절대값 = 900
# 리스트의 절대값 반환
numList = [100, 0, -90, 80, -55, -500]
temp = []
for item in numList:
    print(abs(item), end=' ')
    temp.append(abs(item))
print('\n',temp)

# 집합형 자료의 최댓값, 최솟값
# TypeError
# numList = [100, 0, -90, 80, -55, -500, '파이썬']
numList = [100, 0, -90, 80, -55, -500]
numSet = {100, 0, -90, 80, -55, -500}
print(max(numList), min(numSet))


# 나누기 연산자 /(실수), //(정수형몫)
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플
x = 100
y = 7
print(x/y, x//y, x%y) # 14.285714285714286 14 2
print(divmod(x, y), type(divmod(x, y))) # (14, 2) <class 'tuple'>

# enumerate(리스트/튜플/문자열 , 인덱스숫자 )
# 인덱스 숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)
myList = ['도', '레', '미', '파']
result = enumerate(myList)
print(result, type(result))
# <enumerate object at 0x000002128F380B40> <class 'enumerate'>
for item in result:
    print(item)
'''
# 튜플로 반환 (인덱스, 값)
(0, '도')
(1, '레')
(2, '미')
(3, '파')
'''
# 다시 enumerate 객체 생성후 리스트화 => 리스트 튜플
result = enumerate(myList)
print(list(result))
# [(0, '도'), (1, '레'), (2, '미'), (3, '파')]

# 인덱스를 특정 숫자로 설정
result = enumerate(myList, 11)
for item in result:
    print(item)
'''
(11, '도')
(12, '레')
(13, '미')
(14, '파')
'''
result = enumerate(myList, 11)
print(list(result))
# [(11, '도'), (12, '레'), (13, '미'), (14, '파')]


# 리스트/튜플/집합 => 딕셔너리 구조로 변경
# dict(enumerate(리스트/문자열/튜플, 인덱싱번호))
myList = ['도', '레', '미', '파']
myDict = dict(enumerate(myList, 1))
print(myDict)
for key in myDict:
    print(key, ' => ', myDict[key] )

print('-'*50)
# eval(문자열계산식)
# 입력받은 수식을 계산하여라
# result1 = input('1. 수식을 입력하세요? ... ')
# result2 = eval(input('2. 수식을 입력하세요? ... '))
# print(result1, ' = ', result2)
'''
1. 수식을 입력하세요? ... 34+89-4
2. 수식을 입력하세요? ... 34+89-4
34+89-4  =  119
'''

print('-'*10, '\n'*2)
# 내장함수 : 아스키(American Standard Code for Information Interchange)
#           코드와 관련된 함수
# chr() , ord()
# chr(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# ord(관련 문자나 숫자) => 아스키코드값
# chr()과 반대되는 함수
# 대응시켜 놓은 코드표
# https://ko.wikipedia.org/wiki/ASCII

print(ord('A')) # 65
print(ord('Z')) # 90
print(ord('z')) # 122
print(chr(65)) # A
print(chr(48)) # 0

# A ~ Z 알파벳 문자로 구성된 리스트를 생성하여라
alphaList = []
for i in range(65, 91):
    alphaList.append(chr(i))
print(f'alphaList = {alphaList}')

print('#'*50)
# z ~ a 소문자로 구성된 리스트를 생성하여라
alphaList = []
for i in range(ord('z'), ord('a')-1, -1):
    alphaList.append(chr(i))
print(f'alphaList = {alphaList}')
print('#'*50)

# sort(), reverse()
alphaList = []
num1 = ord('a')
num2 = ord('z')
print(num1, num2)
# for i in range(ord('a'), ord('z')+1):
for i in range(num1, num2+1):
    alphaList.append(chr(i))
print(f'alphaList = {alphaList}')
alphaList.reverse()
print(f'alphaList = {alphaList}')

print('-'*50)
# 리스트/튜플 등의 원소값이 False 값인지 True 값인지
# Boolean 형(True/False)로 표시
# all(리스트/튜플/집합) :  값이 모두 True 조건이면 True
# any(리스트/튜플/집합) : 값중 하나라도 True 조건이면 True
# False 조건값 : None, 0, 0.0, '', False, [], {}, ()

listA = [0, False, '', ' ']
setB = {0, False, '', None, 0.0} # 모두 False
tupleC = (1, 2, 3, True, 'Yes') # 모두 True
print(any(listA)) # True
print(any(setB)) # False
print(any(tupleC)) # True
print(all(listA)) # False
print(all(setB)) # False
print(all(tupleC)) # True

# 유효성 검사?
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha()
# : 모두 문자(알파벳,한글..)인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() , 문자열변수.isnumeric()
# : 모두 숫자문자인가?  , True/Fasle
# 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
# islower(), isupper() : 대문자/ 소문자 검사
# isdecimal() : 모두 10진수인가?
str1 = 'fkfkfk가나다'
str2 = '12345'
str3 = '1fdkjfsl2345'
str4 = 'BANANA'
str5 = '#&^=+'
print(str1.isalpha()) # True
print(str2.isalpha()) # False
print(str3.isdigit()) # False
print(str1.isdigit()) # False
print(str2.isdigit()) # True
print(str3.isalnum()) # True
print(str4.isupper()) # True
print(str1.islower()) # True
print(str2.isdecimal()) # True
print(str3.isdecimal()) # False
print(str5.isalpha()) # False
print('-'*10, '\n'*2)

# 퀴즈 : 숫자로 구성된 리스트 생성 (길이는 5)
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

# # 결과값을 저장할 빈 리스트 생성
# resultList = []
# while True:
#     data = input('데이타 입력 => ')
#     # 숫자이면 리스트에 추가한다.
#     if data.isdigit():
#         resultList.append(int(data))
#         print('리스트에 추가되었습니다')
#     # 음수 조건 -100
#     # 음수 문자열 => (data[0] == '-') and (data[1:].isdigit())
#     elif (data[0] == '-') and (data[1:].isdigit()):
#         resultList.append(int(data[1:])*-1)
#         print('리스트에 추가되었습니다')
#     else:
#         print('숫자가 아닙니다. 다시 입력해주세요')
#
#     # 리스트 길이가 5이면 while 종료
#     if len(resultList) == 5:
#         break
# print(f' 결과 리스트 = {resultList} ')


# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라.
# 특수문자는 제외한다.
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''

result1 = []
result2 = []
testWord = 'Python1234Java4!$$$774'
for item in testWord:
    if item.isdigit():
        result1.append(item)
    elif item.isalpha():
        result2.append(item)

print("결과 >>")
print(f'숫자 갯수 : {len(result1)}')
print(f'문자 갯수 : {len(result2)}')


# 함수 이용
def count_word(testWord):
    result1 = []
    result2 = []
    for item in testWord:
        if item.isdigit():
            result1.append(item)
        elif item.isalpha():
            result2.append(item)

    print(f'테스트 글자 => {testWord} ')
    print(f'숫자 갯수 : {len(result1)}')
    print(f'문자 갯수 : {len(result2)}')
    print('-'*50)

# 함수 호출
count_word('Python1234Java4!$$$774')
count_word('yudhd67427109')


print('-'*10, '\n'*2)
# 정렬과 관련된 내장 함수
# sorted(리스트/튜플/집합..)
# : 바로 인쇄 가능. 튜플과 집합은 정렬된 형태의 리스트로 변경
# : 데이타 정렬
# : 결과값을 리턴한다. => print()문안에 삽입 가능

# 리스트이름.sort() : 리스트정렬
# 리스트이름.reverse() : 리스트 역정렬
# print() 문안에 삽입시 None이 반환


myList = ['b', 'a','c','x']
myTuple = ('b', 'a','c','x')
mySet = {'b', 'a','c','x'}
print(f'myList = {myList}') # myList = ['b', 'a', 'c', 'x']
# 원본은 적용되지 않는다.
print(sorted(myList)) # ['a', 'b', 'c', 'x']
print(f'sorted() 적용후 1 ... myList = {myList}')
# sorted() 적용후... myList = ['b', 'a', 'c', 'x']
myList = sorted(myList)
print(f'sorted() 적용후 2... myList = {myList}')
print(myList.sort()) # None
# 튜플의 정렬
print(f'myTuple = {myTuple}')
# TypeError: 'NoneType' object is not iterable
# print(tuple(list(myTuple).sort()))
temp = list(myTuple)
temp.sort()
myTuple = tuple(temp)
print(f'myTuple = {myTuple}')
print('-'*50)
print(f'mySet = {mySet}')
# 리스트화한 후 정렬
print(sorted(mySet))
print(f'mySet = {mySet}')
mySet = set(sorted(mySet))
print(f'mySet = {mySet}')