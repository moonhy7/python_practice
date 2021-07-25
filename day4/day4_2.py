# 함수 정의 6
# 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)
'''

# 두수의 합 리턴. 초기값 있음 - 인자, return
def sum_plus(x=0, y=0):
    return f'{x} + {y} = {x+y}'

print(sum_plus()) # 0 + 0 = 0
print(sum_plus(10)) # 10 + 0 = 10
print(sum_plus(20, 30)) # 20 + 30 = 50


# 세수의 곱 리턴. 초기값 있음 - 인자, return
def three_number_mul(x=1, y=1, z=1):
    return f'{x} * {y} * {z} = {x*y*z}'
print(three_number_mul())
print(three_number_mul(50))
print(three_number_mul(3, 4))
print(three_number_mul(10, 20, 80))


# 함수 정의 7
# 인자의 초기값 설정 (인자의 일부만 초기값이 있는 경우)
# 주의 사항은 마지막 인자부터 초기값이 지정되어 있어야 한다.
'''
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(값1)
# 함수명(값1, 값2)
'''

# 세수의 곱 리턴. x는 초기값 없음. y,z는 초기값이 있음 - 인자, return
def three_number_mul2(x, y=1, z=1):
    return f'{x} * {y} * {z} = {x*y*z}'
print('!'*50)
# TypeError:
# print(three_number_mul2())
print(three_number_mul2(5)) # 5 * 1 * 1 = 5
print(three_number_mul2(5, 6)) # 5 * 6 * 1 = 30
print(three_number_mul2(5, 6, 7)) # 5 * 6 * 7 = 210

# x,z는 초기값 있음. y는 초기값이 없음
# SyntaxError
# def three_number_mul3(x=1, y, z=1):
#     return f'{x} * {y} * {z} = {x*y*z}'
# print('!'*50)
# print(three_number_mul3(100))

# 아래와 같이 수정해야한다.
def three_number_mul3(y, x=1, z=1):
    return f'{x} * {y} * {z} = {x*y*z}'
print('!'*50)
print(three_number_mul3(100))


# 함수 정의 8
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)
'''

# 가변인자 스타일로 인자를 받아서 여러줄로 각각 출력한다.
def student_print(*args):
    print('-'*50)
    print(args, type(args))
    cnt = 1
    for item in args:
        print(f'{cnt} 번 => {item}')
        cnt += 1

student_print()
# (), <class 'tuple'>
student_print('고길동', '박길동')
# ('고길동', '박길동') <class 'tuple'>
student_print('홍길동', '박길동', '고길동', '윤길동')
# ('홍길동', '박길동', '고길동', '윤길동') <class 'tuple'>

# 퀴즈. 인자 모두의 합을 구하는 가변함수를 정의하여라
'''
sumNumber(1,2) => 1+2=?
sumNumber(4,5,6) => 4+5+6=?
'''

def sumNumber(*args):
    result = 0
    for item in args:
        result += item
    return f'{args} 의 모든 합은? {result}'

print('-'*50)
print(sumNumber(1,2)) # (1, 2) 의 모든 합은? 3
print(sumNumber(4,5,6)) # (4, 5, 6) 의 모든 합은? 15


# 구분자문자열.join(문자열/리스트/튜플)
def sumNumber2(*args):
    result = 0
    tempList = []
    for item in args:
        result += item
        # 리스트에 숫자값을 문자열로 변경한 후 리스트에 삽입한다.
        tempList.append(str(item))
    # return print(tempList, result)
    return print(' + '.join(tempList),' = ', result)

sumNumber2(1,2) # 1 + 2  =  3
sumNumber2(4,5,6) # 4 + 5 + 6  =  15
sumNumber2(1, 2, 3, 4, 5) # 1 + 2 + 3 + 4 + 5  =  15

# 함수 정의 9
# 일반인자랑 가변인자랑 함께 있는 경우
# 주의 사항: 일반 인자는 앞쪽으로 배치. 가변 인자 *args는 뒷편에 배치
'''
def 함수명(인자, *args):
    인자와 args를 이용한 명령문...
    return 값/변수/수식/명령문
    
# 호출
# 함수명(인자값, 가변값1)
# 함수명(인자값, 가변값1, 가변값2...)
'''

# 가변인자의 합 또는 곱을 구하는 함수 정의
# symbol(add, mul) 값에 따라 합 또는 곱의 결과값이 반환된다.
# TypeError
# def sum_mul(*args, symbol):
def sum_mul(symbol, *args):
    if symbol == 'add':
        result = 0
        for item in args:
            result += item
        return f'{args} 의 합은? {result}'
    elif symbol == 'mul':
        result = 1
        for item in args:
            result *= item
        return f'{args} 의 곱은? {result}'
    else:
        return
print('-'*50)
# print(sum_mul(10, 20, 30, 'add'))
print(sum_mul('add', 10, 20, 30))
print(sum_mul('mul', 10, 20, 30))


# 함수 정의 10
# 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리
# kwargs = Keyword Arguments

'''
def 함수명(**kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
'''
# 딕셔너리 가변 함수 테스트
def dict_print(**kwargs):
    return print(kwargs, type(kwargs))

# 호출시 키=값 형태로 삽입
dict_print(x=100) # {'x': 100} <class 'dict'>
dict_print(x=100, y=200, z=300) # {'x': 100, 'y': 200, 'z': 300} <class 'dict'>

# 딕셔너리 가변 함수 테스트2
def dict_print2(**kwargs):
    print('\n\t\t Student Info')
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

dict_print2(stName='심순애', stAge=25)
dict_print2(stName='심순애', stAge=25, contact='010-1234-7897')
# TypeError: dict_print2() takes 0 positional arguments but 2 were given
# dict_print2('심순애', 25)


# 함수 정의 11
# 초기값이 있는 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리

'''
def 함수명(**kwargs):
    # 초기값 지정
    kwargs[키값] = 값
    kwargs를 명령문...
    return 값/변수/수식/명령문

# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
'''

# nationality 값이 고정
'''
user1 = {'nationality':'USA', 'age':33, 'name':'Jackson'}
user2 = {'nationality':'USA', 'age':22, 'name':'Maria', 'gender':'female'}
'''
def makePerson(**kwargs):
    # 초기값 지정
    kwargs['nationality'] = 'USA'
    print('\n\n')
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

# 함수 호출
makePerson(age=33, name='Jackson')
'''
age = 33
name = Jackson
nationality = USA
'''
makePerson(age=22, name='Maria', gender='female')
'''
age = 22
name = Maria
gender = female
nationality = USA
'''

# 초기값으로 정의된 키와 값을 인자로 정의해서 함수를 호출한다면?
makePerson(age=25, name='Julia', gender='female', nationality = 'Spain')
# nationality = 'Spain' (X)
# 함수내에서 정의한 초기값이 우선순위가 높다.
# nationality = USA (O)
'''
age = 25
name = Julia
gender = female
nationality = USA
'''

# nationality 값이 없다면 초기값으로 표시
def makePerson2(**kwargs):
    if 'nationality' not in kwargs:
        # 초기값 지정
        kwargs['nationality'] = 'USA'
    print('\n\n')
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')

makePerson2(age=22, name='Maria', gender='female')
makePerson2(age=25, name='Julia', gender='female', nationality = 'Spain')

# 함수 정의 12
# 람다 함수
# def 로 정의하지 않다.
# 한줄로 정의한다.
# return 문이 없다.
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''

# 메세지 출력하기 - 일반함수
def hello_msg(user):
    return print(user, ' 님 환영합니다')

hello_msg('홍길동')

# 메세지 출력하기 - 람다함수
# 함수변수 = lambda 인자:명령
f1 = lambda user:print(user, ' 님 환영합니다')
f1('둘리')

# 두수의 합을 구하는 일반함수
def sum(x,y):
    return f'{x} + {y} = {x+y}'
print(sum(45, 77))

# 두수의 합을 구하는 람다함수
f2 = lambda x,y:f'{x} + {y} = {x+y}'

print(f2(45, 77))

# 함수의 변수 영역
# 스코프(Scope)
# 전역변수(문서 전체의 공통변수) ?
# 지역변수(함수내부에만 유효한 변수)?

# 함수내에서 정의한 지역변수를 전역변수로 정의
# global 변수명

# print('-'*50)
# print('전역변수와 지역변수 테스트')
# # 전역변수
# v = 10
# w = 200
#
# def scopeTest():
#     # 지역변수 : 함수안에서만 유효한 변수
#     v = 100
#     w = 400
#     print(f'함수안의 v = {v}') # 100
#     print(f'함수안의 w = {w}') # 400
#
# scopeTest()
# print(f'함수밖의 v = {v}') # 10
# print(f'함수밖의 w = {w}') # 200

print('-'*50)
print('전역변수와 지역변수 테스트2')
# 전역변수
v = 10
w = 200
def scopeTest():
    v = 100
    # 전역변수로 정의
    global w
    print(f'함수안의 v = {v}') # 100
    w = 300
    print(f'함수안의 w = {w}') # 300
    w = 400

scopeTest()
print(f'함수밖의 v = {v}') # 10
print(f'함수밖의 w = {w}') # 400





