# 출력문
# 변수와 자료형
# 입력문
# 집합 자료형
# 제어문 ( 조건문과 반복문)
# 오늘은? 함수

# 사용자정의함수 정의
# 함수정의 문법
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 호출시
# 함수명(값1, 값2 ...)

# 인자(매개변수=파라미터) : 함수에 값을 전달할때 사용하는 변수
# 반환값 : return문을 이용해서 반환하는 최종 함수의 결과치

# 함수 정의 1 : 인자도 없고 return문도 없음
'''
def 함수명():
    명령문

# 호출
# 함수명()
'''

# 함수 호출시 특정 메세지 출력
# 함수 정의
def hello():
    print('hello 함수호출')
    print('Hello world')
    print('Hello Python')
    print('Hello MySQL')

# 함수 호출
hello()
hello()

# 함수 정의 2
# 인자가 있다. return이 없다.
'''
def 함수명(인자1,인자2..):
    인자가 있는 명령문

# 호출
# 함수명(값1, 값2...)
'''
def hello_params(m1, m2, m3):
    print('\n\nhello_params 함수호출')
    print('1. Hello', m1)
    print('2. Hello', m2)
    print('3. Hello', m3)

# 함수 호출
hello_params('Python', 'C', 'C++')
# TypeError: hello_params() missing 1 required positional argument: 'm3'
# hello_params('자바', '머신러닝')


# 함수 정의 3
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
# 함수의 최종 결과치를 반환한다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문

# 호출
함수명()
'''

# 두수를 입력받은 후 합을 반환하는 함수 정의
# 출력문이 없는 경우
def addNumber():
    x = int( input('x => '))
    y = int( input('y => '))
    return x+y

# 함수 호출
# print(f'함수 호출 => {addNumber()}')
# print(f'함수 호출 => {addNumber()}')

# 두수를 입력받은 후 곱을 반환하는 함수 정의
# 출력문이 있는 경우
def multyNumber():
    x = int( input('x => '))
    y = int( input('y => '))
    return print(x, ' * ', y , ' = ', x*y)

# 함수 호출
# multyNumber()
# print() 문안에 print문이 삽입된 함수 호출시 None 반환
# print(multyNumber()) # None

# 입력받은 값이 숫자이면 출력한다.
# 입력받은 값이 숫자가 아니면 아무것도 출력하지 않게 한다.
def printNumber():
    data = input('데이타 입력 => ')
    if data.isdigit():
        return print(f'data = {data}')
    else:
        return
    print('함수 호출 테스트')

# printNumber()
# printNumber()


# 함수 정의 4
# 인자가 있다. return이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문

# 호출
함수명(값1, 값2...)
'''

# 메세지 출력
def message(person):
    return 'Happy New Year.. ' + person + '님'

print(f'함수 호출1 => {message("홍길동")}')
print(f'함수 호출2 => {message("고길동")}')

# f'' 포맷팅을 return 문에 사용하는 경우
def message2(n, person):
    return f'함수 호출 {n} => Happy New Year.. {person} 님'
print(message2(1, '김수철'))
print(message2(2, '박수철'))

# 아래 소스를 이용하여 숫자를 받아서 1~숫자까지의 합을 구하는 함수 정의후 호출
# 1~100까지의 합 구하기
sum = 0
for i in range(1,101):
    sum += i
print(f'1~100까지의 합은? {sum}')

# 함수 정의
def sum_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return print(f'1 ~ {n} 까지의 합은? {sum}')

sum_n(100)
sum_n(30)


'''
퀴즈 1:
2개의 수 x, y를 인자로 전달하여 누적합 구하기
x~y까지의 합 함수로 변경
'''
#sum2(10,20) : 10~20까지의 합 반환

# 함수 정의
def sum2(x, y):
    sum = 0
    for i in range(x, y+1):
        sum += i
    return print(f'{x} ~ {y} 까지의 합은? {sum}')
print('-'*50)
sum2(10,20)
sum2(1,100)



'''
퀴즈 2:
n개를 입력 받아서 리스트에 저장하는 함수 정의

printList(5) # 5개로 구성된 리스트 반환
printList(3) # 3개로 구성된 리스트 반환
'''
# range(start:end:step)
# range(end)
# range(start:end)
# range(:end:step)

# start가 생략되면 0 부터 시작
def make_list(n):
    result = []
    # for i in range(n): # 0, 1, ... n-1
    # for i in range(0, n): # 0, 1, ... n-1
    for i in range(1, n+1): # 1, 2, ... n
        item = input('Data => ')
        result.append(item)
    return print(f'\n\n\t {n} 개의 리스트 => {result}')

# make_list(3)
# make_list(2)


# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값1, 결과값2 ....

# 호출
함수명(값1, 값2...)
'''

# 2개의 숫자를 인자로 전달한 후 합과 차의 값을 리턴한다.
def plus_minus(x, y):
    return x+y, x-y

print('-'*50)
result = plus_minus(100, 50)
print(result, type(result), result[0], result[1])
# (150, 50) <class 'tuple'> 150 50



