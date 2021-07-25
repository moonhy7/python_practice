# 입력문
# 변수명 = input(메세지)
# 입력받은 변수는 데이터형이 문자열이다.
# msg = input('메세지를 입력하세요 ....')
# print('msg = ', msg, type(msg))

# 자료형의 종류
# 기본 자료형 - 숫자형(float, int), 문자열, 논리형(True, False)
# 집합형 자료형 - 리스트, 집합, 튜플, 딕셔너리
# type()
x = 90.789
y = True
print('x = ', x, type(x)) # x =  90.789 <class 'float'>
print('y = ', y, type(y)) # y =  True <class 'bool'>

# 16진수 : 숫자0알파벳x16진수 ex => 17 0x11
# 8진수 : 숫자0알파벳o8진수   ex => 9 0o11
# 결과치는 10진수로 표시
print('0x11 =>', 0x11)
print('0o11 =>', 0o11)

# 자료형 변환 (Casting)
# int(값/수식/변수) : 정수형 데이터형으로 변환
# float(값/수식/변수) : 실수형 데이터형으로 변환
# str(값/수식/변수)  : 문자열 데이터형으로 변환
a = 100
b = 3.14
c = '100가나다'
print(a, float(a))
print(b, str(b), type(str(b)))
# ValueError
# print(c, int(c), type(int(c)))

# 퀴즈 : 2개의 숫자값을 입력받은 후 사칙 연산을 수행하여라
'''
첫번째 숫자를 입력하세요... 10
두번째 숫자를 입력하세요... 20
---------
10 + 20 = ?
10 - 20 = ?
10 * 20 = ?
10 / 20 = ?
'''
# myNum1 = int(input('첫번째 숫자를 입력하세요 ... '))
# myNum2 = int(input('두번째  숫자를 입력하세요 ... '))
# print(myNum1 , ' + ', myNum2, ' = ', myNum1+myNum2)
# print(myNum1 , ' - ', myNum2, ' = ', myNum1-myNum2)
# print(myNum1 , ' * ', myNum2, ' = ', myNum1*myNum2)
# print(myNum1 , ' / ', myNum2, ' = ', myNum1/myNum2)

# 연산자의 종류
# 산술연산자 => 숫자
# 대입연산자 => 숫자
# 관계연산자(비교연산자) => 논리형
# 논리연산자 => 논리형
# 문자열 연산자 => 문자열
# 조건 연산자 (삼항연산자)
# 증감연산자( ++, --) X

#  산술연산자
# +, - , *, /, //(정수형 몫), %(나머지), **(제곱)
print(1000/7) # 142.85714285714286
print(1000//7) # 142
print(1000%7) # 6
print(10**3) # 1000

# 연산자 우선순위
# 괄호()
# *, /
# +, -
print(100+20*40) # 900
print((100+20)*40) # 4800

# 대입 연산자
# 변수명 += , -= , *= , /=
n = 100
print('n = ', n)
n += 1 # n = n+1
print('n = ', n) # 101
n -= 10
print('n = ', n) # 91
n *= 5
print('n = ', n) # 455

# 관계 연산자
# 결과값이 True / False
# ==, !=, >, <, >=, <=
x = 100
y = 10
print(x > y) # True
print(x <= y) # False
print(x == y) # False
print(x != y) # True

# 논리 연산자
# 결과값이 True / False
# and, or, not
# 관계연산자를이용한수식1 논리 연산자 관계연산자를이용한수식2
# not(관계연산자를이용한수식)
# True and True => True
# True and False => False
# False or False => False
# True or False => True
# not(True) => False
# not(False) => True
print('========================')
userId = 'abcd'
pwd = 1234
age = 22
print((userId == 'abcd') or (pwd == 1234)) # T or T => True
print((userId != 'abcd') or (pwd == '1234')) # F or F => False
print((userId == 'abcd') and (age > 100)) # T and F => False
print((userId == 'abcd') and (age < 100)) # T and T => True
print(not(userId == 'abcd')) # False

# is, is not 연산자 => == , !=
# 값이 같은지 비교한다.
# 결과값이 True/ False
user1 = '홍길동'
user2 = '고길동'
print(user1 is user2) # False
print(user1 is not user2) # True

# 문자열 연산자
# 문자열 + 문자열 => 연결
# * 숫자 => 반복
msg1 = '12월24일'
msg2 = '크리스마스'
print('-'*50)
print(msg1+msg2) # 12월24일크리스마스
print(msg1*3) # 12월24일12월24일12월24일

# 문자열 생성 방법
# '' , "",
# ''' ''', """ ~ """ => 여러줄 문자열 변수 설정 가능
txt1 = '''
    파이썬 
    MySQL
    HTML
    CSS
    '''
txt2 = """
    FLASK
    판다스
    넘파이 
    시각화
    머신러닝 
    프로젝트
"""
print('-'*40)
print(txt1)
print('-'*40)
print(txt2)

# 문자열 인덱싱
# 인덱싱이란?  문자열의 위치를 숫자로 표시
# 인덱싱의 첫 위치는 0
# 인덱싱의 마지막 위치는 -1
# 문자열변수[인덱스값]

# 문자열 전체길이는?
# len(문자열이나 문자열변수)
# 정수형으로 반환
msg = '가나다라마바사아자차카타파하'
print('-'*40)
print('전체길이는?', len(msg))
print('msg[0] = ', msg[0])
print('msg[-1] = ', msg[-1])
print('msg[len(msg)-1] = ', msg[len(msg)-1])
print('msg[5] = ', msg[5])
print('msg[-5] = ', msg[-5])

# 문자열 슬라이싱이란?
# 문자열의 일부를 잘라서 표시
# 문자열변수[start:end:step]
# 문자열변수[start:end]
# 문자열변수[start:]
# 문자열변수[:end]
# start 부터 end-1 까지 step 수만큼 건너뛰기
msg = '0123456789'
print('-'*40)
print(msg, len(msg))
print('msg[0:5]',msg[0:5]) # 01234
print('msg[:5]',msg[:5]) # 01234
print('msg[5:10]',msg[5:10]) # 56789
print('msg[5:]',msg[5:]) # 56789
print('msg[::]',msg[::]) # 0123456789
print('msg[:]',msg[:]) # 0123456789
print('msg[::2]',msg[::2]) # 02468 # 홀수번째
print('msg[1::2]',msg[1::2]) # 13579 # 짝수번째
print('msg[-5:]',msg[-5:]) # 56789
print('msg[-7:-3]',msg[-7:-3]) # 3456
print('msg[::-1]',msg[::-1]) # 9876543210 # 역순정렬

# 출력포맷 방식
# %를 이용한 포맷팅
# format()를 이용한 포맷팅
# f'를 이용한 포맷팅. 파이썬 3.6 이상에서 사용 가능

# %자료형
# %d / %s / %전체자리수.소숫점자리이하숫자f / %o / %x
# print(' 문자열 %자료형 ' % 변수)
# print(' 문자열 %자료형1 %자료형2 ' % (변수1, 변수2))

today = '화요일'
yesterday = '월요일'
# 쉼표를 이용해서 출력
print('오늘은', today, '어제는', yesterday)
# % 포맷팅 이용
print('오늘은 %s 어제는 %s' % (today, yesterday))

# 10진수, 8진수, 16진수, 실수 로 출력하기
n = 100
print('10진수 = > %d' % n)
print('8진수 = > %o' % n) #  144
print('16진수 = > %x' % n) # 64
print('실수 = > %f' % n) # 100.000000 # 소숫점 6자리까지 표시

# %전체자릿수.소수점이하자릿수f
# %.소수점이하자릿수f
pi = 3.14156748
print('pi : %f' % pi )
print('pi : %.3f' % pi )
print('pi : %10.2f' % pi ) # pi :       3.14
print('pi : %3.5f' % pi )  # pi : 3.14157
print('pi : %15.1f' % pi ) # pi :             3.1

# % 퍼센트 기호 표시 : %%
# 오늘의 미세농도는 0.0005 % 입니다.
n = 0.0005
# TypeError: not enough arguments for format string
# print('오늘의 미세농도는 %f.4 % 입니다.' % n)
print('오늘의 미세농도는 %f %% 입니다.' % n)
print('오늘의 미세농도는 %.4f %% 입니다.' % n)

# %로 공백 지정
# %양수숫자Style(s/f/d/x/o) : 왼쪽에 공백 생성
# %음수숫자Style(s/f/d/x/o) : 오른쪽에 공백 생성
userName = '홍길동'
userNumber = 123.45
print('-'*30)
print('user Name : %10s ** ' % userName)
print('user Name : %-10s ** ' % userName)
print('userNumber : %10d ** ' % userNumber)
print('userNumber : %-15f ** ' % userNumber)

# format 을 이용한 출력방식
# ' 문자열1 {} {} 문자열2'.format(변수1, 변수2)
# ' 문자열1 {숫자나 변수} {숫자나 변수} 문자열2'
#   .format(변수1=값1, 변수2=값2)
color = 'Red'
myNumber = 7
# 인덱스가 생략된 문법 형태
print('좋아하는 색상은? {} 좋아하는 숫자는? {}' .format(color, myNumber))
# 인덱스가 있는 문법 형태
print('좋아하는 숫자는? {1} 좋아하는 색상은? {0} ' .format(color, myNumber))
# 변수와 초기값 설정 문법 형태
print('좋아하는 숫자는? {myNumber} 좋아하는 색상은? {color} ' . format(myNumber=100, color='Blue' ))


# format()으로 소숫점 처리하기
# "문자열 {위치인덱스:전체자릿수.소수점이하자릿수f}"
#   .format(값이나 변수)
pi = 3.14156748
print('pi 값은? {}'.format(pi))
print('pi 값은? {:.3f}'.format(pi))

# format 함수안에서 {} 표시하기
#  '{{ }}'.format()
# IndexError: Replacement index 1 out of range for positional args tuple
# print('pi 값은? {} {}'.format(pi))
print('pi 값은? {} {{}}'.format(pi))
# pi 값은? 3.14156748 {}


# f 문자열 포맷팅 : 3.6 이상 지원
# f' 문자열 {변수명이나 변수를이용한수식} '
# f 포맷팅 소수점 처리
# f' 문자열 {변수명:전체자릿수.소숫점이하자릿수f} '

user1 = '이몽룡'
user2 = '성춘향'
user1_age = 22
user2_age = 20.456
print(f'사용자1의 이름은 {user1} 나이는 {user1_age}')
print(f'사용자2의 이름은 {user2} 나이는 {user2_age:.1f}')


# f' 문자열 공백, 대체문자여백 지정
# f' 문자열 {변수명:>숫자} : 왼쪽여백생성
# f' 문자열 {변수명:<숫자} : 오른쪽여백생성
# f' 문자열 {변수명:^숫자} : 좌우여백생성
# f' 문자열 {변수명:대체문자>숫자} : 왼쪽에 대체문자반복
# f' 문자열 {변수명:대체문자<숫자} : 오른쪽에 대체문자반복
# f' 문자열 {변수명:대체문자^숫자} : 좌우 대체문자 반복

message = 'Hello world'
print(f' *** {message} ***')
print(f' *** {message:>30} ***')
print(f' *** {message:<30} ***')
print(f' *** {message:^30} ***')
print(f' *** {message:#^30} ***')
print(f' *** {message:!>30} ***')
print(f' *** {message:!<30} ***')
'''
 *** Hello world ***
 ***                    Hello world ***
 *** Hello world                    ***
 ***          Hello world           ***
 *** #########Hello world########## ***
 *** !!!!!!!!!!!!!!!!!!!Hello world ***
 *** Hello world!!!!!!!!!!!!!!!!!!! ***
'''

# 샘플 문자열 만들기
# https://www.lipsum.com/
sampleTxt = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing 
Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
PageMaker including versions of Lorem Ipsum.
'''
print(sampleTxt)

# 문자열 함수 스타일
# 문자열변수.함수명(옵션)
# 문자열.함수명(옵션)

# 특정 문자열의 갯수 출력
# 문자열변수.count(찾고자하는문자열)
print(f'Lorem의 빈도수는? => { sampleTxt.count("Lorem") }')
# print('Lorem의 빈도수는? =>', sampleTxt.count("Lorem"))


# 특정 문자열의 시작인덱스 위치 반환
# 문자열변수.find(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 -1 반환
# 문자열변수.index(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 에러 발생
print(f' 첫번째 t의 시작 위치는? {sampleTxt.find("t")}') # 29
print(f' 첫번째 t의 시작 위치는? {sampleTxt.index("t")}') # 29
print(f' 첫번째 t의 시작 위치는? {sampleTxt.find("가")}') # -1
# ValueError: substring not found
# print(f' 첫번째 t의 시작 위치는? {sampleTxt.index("가")}')

# 대소문자 변환 함수
# 문자열변수.upper()
# 문자열변수.lower()
# 문자열변수.title()
print('-'*30)
print(sampleTxt.lower())
print('-'*30)
print(sampleTxt.upper())
print('-'*30)
print(sampleTxt.title())

# 체이닝 방식으로 문자열 함수 연결하기
# 문자열변수.함수1(옵션).함수2(옵션)...
print(sampleTxt.upper().count('IT')) # 5
print(sampleTxt.lower().count('it')) # 5
print(sampleTxt.count('IT')) # 0
print(sampleTxt.count('it')) # 3
print(sampleTxt.count('It')) # 2

# 문자열 교체하기
# 문자열변수.replace(찾고자하는문자열, 교체문자열)
# is => was
print('-'*30)
print(sampleTxt.count('is'))
print(sampleTxt.replace('is','was'))
# 원본에 적용하기
sampleTxt = sampleTxt.replace('is','was')
print(sampleTxt.count('is'))
print(sampleTxt.count('was'))


# '연결문자'.join(문자열변수)
print('-'*30)
sample = 'Python'
print('...'.join(sample))

# 좌우 공백 제거하기
# 문자열변수.strip()
# 문자열변수.rstrip()
# 문자열변수.lstrip()
sample = '    파   이    썬    '
print('***',sample,'***')
print('***',sample.strip(),'***')
print('***',sample.rstrip(),'***')
print('***',sample.lstrip(),'***')
print('***',sample.strip().replace(' ',''),'***')