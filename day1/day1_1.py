


# 실행은? [Run]-[Run]
print('Hello world')

# 혹 실행이 안된다 ?
# => [File]-[Settings]
# [Project]-[Python Interpreter] 화면에서
# 인터프리터 설정해주셔야 합니다.



# 교재 부분은 온라인 참조
# https://wikidocs.net/book/1

# 한줄주석  (ctrl+/)
# 인용부호 3개 이용
'''
 여러줄 주석1
 여러줄 주석2
'''

# 출력문
# print(값/수식/변수, end='대체문자나 공백') 문
# ctrl + d => 행 복제
print('가나다라마바사')
print(10+20+500)
x = 100
print(x)

# 같은 행에 출력하기 - end 옵션 이용
print('동해물과 ', end='')
print('백두산이 ')
print('무궁화 ', end='***')
print('꽃이 피었습니다')
print()
print()
print('영희야', end=' ')
print('철수야')
print('길동아')


# 쉼표를 이용한 출력문
x = 100
y = 200
print('x 값은?',x)
print('y 값은?',y)

# 이스케이프 코드
# \n 개행, \t 왼쪽 여백
print('오늘도 \n\n \t\t\t좋은 하루!!!')

# 변수 할당 방법
# 자료형 설정 X
# 변수 = 수식 또는 값
# 서로 다른 변수에 동일한 값 할당
# type(변수) : 자료형 확인 함수
userAge = 300
userName = '홍길동'
print(userAge, type(userAge)) # 300 <class 'int'>
print(userName, type(userName)) # 홍길동 <class 'str'>

# 쉼표(,)를 이용한 변수 할당
# 변수1, 변수2 = 값1, 값2
x , y = 100, 200
print('x 값은?',x)
print('y 값은?',y)

# 숫자로 시작하는 변수 설정은?
# SyntaxError
# 100abc = 100

# 파이썬의 예약어 확인
# len(리스트/문자열...) => 길이 확인
import keyword
print(keyword.kwlist)
print('키워드 갯수 = ', len(keyword.kwlist))

# 변수 삭제
# del 변수명
myWord = 'Python'
print(myWord)
del myWord
# print(myWord)
# NameError: name 'myWord' is not defined


# 퀴즈 : user1, user2의 변수값을 서로 변경하여라
user1 = "영희"
user2 = "철수"
print('user1 = ', user1)
print('user2 = ', user2)
print('----------------')
# 중간변수 설정
temp = user1
user1 = user2
user2 = temp
print('user1 = ', user1)
print('user2 = ', user2)
print('----------------')
# 쉼표를 이용한 변수 교체
user1, user2 = user2, user1
print('user1 = ', user1)
print('user2 = ', user2)
print('----------------')