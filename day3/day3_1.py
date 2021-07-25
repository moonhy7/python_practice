'''
집합형 자료구조
- 리스트 CRUD
- 튜플 CRUD
- 퀴즈 2-1
- 딕셔너리 CRUD
- 집합 CRUD
- 캐스팅
- 퀴즈 2-2
'''

# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~elif~else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다

# 조건문 if

# 조건문 1 - 단순 if 문
# if 조건:
#   명령문

# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

# if 문
# if True조건식:
#    실행할 문장

# 조건식이 True가 되는 경우는?
# True/0이아닌 숫자/''가 아닌문자열
# ([],(),{})아닌 집합형 자료. 길이가 0이 아닌 집합형 자료
# flag = True
# flag = False
flag = -100
if flag:
    print('if 테스트')
print('테스트 종료')


# 비교 연산자나 논리연산자를 이용한  if 문
# 비교연산자 : >, <, <=, >=, !=, ==
# 논리 연산자 : and, or, not
# 수의 비교
x = 10
y = 10
if x>y:
    print('x가 크다')
if x<y:
    print('y가 크다')
if x==y:
    print('x와 y가 같다')

# 두수를 입력받아서 큰수만 출력하기
# x = int(input('x ? ...'))
# y = int(input('y ? ...'))
# if x>y:
#     print(x)
# if x<y:
#     print(y)
# if x==y:
#     print('x와 y가 같다')

# 짝수? 홀수?
# 숫자%2 나머지가 0이면 짝수
# x = int(input('x ? ...'))
# if x%2==0:
#     print(f'{x} => 짝수')
# if x%2!=0:
#     print(f'{x} => 홀수')


# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 3의 배수인지 메세지 출력
x = 99
print('-'*50)
if x%3 == 0:
    print(f'{x} => 3의 배수이다')
else:
    print(f'{x} => 3의 배수가 아니다.')
print('-'*50)

# 돈이 있으면(0이 아닌 숫자) 택시를 타고,
# 돈이 없으면(0) 걸어 간다
money = 100
if money:
    print('택시를 타고 간다.')
else:
    print('걸어간다')


# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

# 숫자값이 0, 음수, 양수 인지 출력
x = 10
if x>0:
    print(f'{x}는 양수')
elif x<0:
    print(f'{x}는 음수')
else:
    print(f'{x}는 0')


# 퀴즈 :
# 나이를 입력받는다.
# 나이에 따라서 서로 다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...
~7 : 영유아
8 ~ 13 : 초등학생
14 ~ 16 : 중학생
17 ~ 19 : 고등학생
20 ~ : 성인
'''
# print('-'*50)
# userAge = int(input('당신의 나이를 입력해 주세요? ...'))
# if (userAge <= 7):
#     print('영유아')
# elif (userAge <= 13):
#     print('초등학생')
# elif (userAge <= 16):
#     print('중학생')
# elif (userAge <= 19):
#     print('고등학생')
# else:
#     print('성인')
# print('테스트 종료')

# 조건식에서 True가 되는 조건 =
# True, 0빼고 나머지숫자, 길이가 0이 아닌 (문자열, 튜플, 리스트, 딕셔너리)
# 조건식에서 False가 되는 조건
# = False, 0, '', None, [], (), {}

flag = None
if flag:
    print('실행 테스트1')
else:
    print('실행 테스트2')

# 퀴즈
# 태어난 년도를 입력받아 관련된 띠를 출력한다.
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
'''
태어난 년도를 입력하세요? 2009
당신은 소띠 입니다.
'''
print(2009%12)

print( '-'*10, '\n\n' )

# birth = int(input('태어난 년도를 입력하세요 ...?  '))
# animalList2 = ['원숭이띠', '닭띠', '개띠', '돼지띠', '쥐띠', '소띠', '범띠', '토끼띠', '용띠', '뱀띠', '말띠', '양띠']
# animal = birth%12
#
# if animal == 0:
#     print(f'당신은 {animalList2[0]}띠 입니다.')
#     print('당신은 원숭이띠 입니다.')
# elif animal == 1:
#     print(animalList2[1])
# elif animal == 2:
#     print(animalList2[2])
# elif animal == 3:
#     print(animalList2[3])
# elif animal == 4:
#     print(animalList2[4])
# elif animal == 5:
#     print(animalList2[5])
# elif animal == 6:
#     print(animalList2[6])
# elif animal == 7:
#     print(animalList2[7])
# elif animal == 8:
#     print(animalList2[8])
# elif animal == 9:
#     print(animalList2[9])
# elif animal == 10:
#     print(animalList2[10])
# elif animal == 11:
#     print(animalList2[11])

# 조건문안에 조건문

# 문자열이 숫자,영문형태?
# 문자열.isdigit() : 문자열이 숫자이면 True
# 문자열.isdecimal() : 문자열이 숫자이면 True
# 문자열.isalpha() : 문자열이 영문글자이면 True
# 문자열.isalnum() : 문자열이 영문글자 또는 숫자 형태이면 True
txt1 = '123'
txt2 = 'python33'
txt3 = '!!**345'
print(txt1.isdigit()) # True
print(txt2.isdigit()) # False
print(txt1.isdecimal()) # True
print(txt1.isalpha()) # False
print(txt2.isalnum())  # True
print(txt3.isalnum()) # False


# 숫자를 입력받아서
# 0, 양수, 숫자가 아니다.
# 입력받은 데이타가 숫자이면 데이터형 변경.
# 그렇지 않으면 메세지 출력

# ans = input('데이타 입력 => ')
# if ans.isdigit():
#     if int(ans) > 0:
#         print(f'{ans} => 양수')
#     else:
#         print(0)
# else:
#     print(f'{ans} => 숫자가 아니다.')

#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False

cityList = ['서울', '부산', '대구']
txt = 'abcdefg'
print('서울' in cityList) # True
print('대전' in cityList) # False
print('대전' not in cityList) # True
print('a' not in txt) # False
print('a' in txt) # True

# 조건문 + in/not in 연산자

# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3

twise = ['나연', '채영', '쯔위']
# member = '조이'
member = '쯔위'
if member in twise:
    print(f'{member} 은(는) 트와이스이다.')
else:
    print(f'{member} 은(는) 트와이스 멤버가 아니다.')


# pass 키워드 이용하기
# 명령문의 일종으로 비실행
# 함수, 클래스 생성시 등록만 시킬때 사용
print('-'*30)
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

