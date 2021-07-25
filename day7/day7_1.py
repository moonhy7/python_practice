# 클래스 : 특별한 자료구조
# 관련 키워드 => OOP, 인스턴스=객체
# 기본자료형(숫자, 문자열, 불른)
# 콜렉션형 (리스트, 집합, 튜플, 딕셔너리)
# 클래스 ( 속성, 함수 ...) => 틀
# 인스턴스=객체=Object
#   => 클래스에 의해서 만들어진 산출물
# 클래스란? 설계도/틀 -> 붕어빵틀
# => 인스턴스(객체) -> 붕어빵

# 클래스 생성 문법
# 클래스이름은 첫글자는 대문자로 지정
# class 클래스이름:
#   명령문

# pass :
# 명령어가 필요할때 삽입. 실행은 없음

# 기본자료형 (실수, 정수, 문자열, 논리형) < 집합형 < 함수 < 클래스(속성+메서드(함수)) < 모듈 < 패키지

# 자동차 클래스 생성 => 설계도
class Car:
    pass

print(Car, type(Car))
# <class '__main__.Car'> <class 'type'>

# 자동차 생성 => 인스턴스
# 인스턴스 생성하기
# 인스턴스명은 첫글자는 소문자로 지정
# 인스턴스변수 = 클래스이름()
car1 = Car()
car2 = Car()
print(car1, type(car1))
print(car2, type(car2))
# <__main__.Car object at 0x0000012944689640> <class '__main__.Car'>
# <__main__.Car object at 0x000001B1ACD68FD0> <class '__main__.Car'>

# Bus 클래스 생성
class Bus:
    pass

bus1 = Bus()

# isinstance(인스턴스변수, 클래스이름)
# 특정클래스에 의해서 생성된 인스턴스가 맞는지 출력
# True / False 로 출력
print('bus1은 Bus 클래스에 의해서 생성된 객체인가?', isinstance(bus1, Bus)) # True
print('car1은 Bus 클래스에 의해서 생성된 객체인가?', isinstance(car1, Bus)) # False
print('car2는 Car 클래스에 의해서 생성된 객체인가?', isinstance(car2, Car)) # True

# 생성자 함수 (Constructor)
# => 속성값 정의
# 사각형에 관련된 클래스 속성 => 가로, 세로, 색상, 무늬
# 사람에 대한 클래스 속성 => 이름, 성별, 키, 몸무게, 출신지
# 붕어빵에 대한 클래스 속성 => 재료, 칼로리, 크기, 생성날짜

# 생성자함수 문법
# class 클래스명:
#   def __init__(self, 인자):
#       self.인자 = 인자
#       self.인자 = 값
#       self.인자 = (인자값1, 인자값2,...) # 튜플형태

# 인스턴스 생성
# 인스턴스명 = 클래스이름(인자값,..)

# 실제 속성값 출력
# 인스턴스명.속성

# 사각형에 대한 클래스 생성
# 속성 = 가로, 세로, 만든사람(영희, 철수)
class Square:
    # 생성자 메서드(=함수) 정의
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maker = ('영희', '철수')

# 객체 인스턴스화
# TypeError: __init__() missing 2 required positional arguments: 'width' and 'height'
# s1 = Square()
s1 = Square(10, 10)
s2 = Square(50, 30)
print(s1) # <__main__.Square object at 0x000002030BD3C100>
# 생성자 메서드에서 정의한 인스턴스명.속성으로 접근 가능
print(f's1의 가로 : {s1.width}, 세로 {s1.height}, 만든이 {s1.maker}')
print(f's2의 가로 : {s2.width}, 세로 {s2.height}, 만든이 {s2.maker}')


# 클래스 메소드란? => 동작/ 기능
# def 메소드이름(self,인자):
#   명령어
#   return 값

# 메소드 호출
# 인스턴스명.메소드이름(인자)

# Bread 클래스
# 속성 => 빵종류 , 가격, 칼로리, 재료, 브랜드
# 메서드 => 정보출력, 주문한 빵에 대한 가격 계산

class Bread:
    # 생성자 메서드 정의
    def __init__(self, kind, price, kcal, src):
        self.kind = kind
        self.price = price
        self.kcal = kcal
        self.src = src
        self.brand = '파리바게뜨'

    # 빵 속성 출력과 관련된 메서드 정의
    def print_info(self):
        print('='*50)
        print(f' 종류 = {self.kind}')
        print(f' 가격 = {self.price}')
        print(f' 칼로리 = {self.kcal}')
        print(f' 재료 = {self.src}')
        print(f' 브랜드 = {self.brand}')
        print()

    # 주문한 빵에 대한 가격 계산 메서드 (빵 갯수)
    def print_price(self, count):
        print('='*50)
        print(f'{self.kind} 을(를) {count} 개 주문하셨습니다.')
        print(f' 주문 가격은? {self.price*count}')


# Bread 인스턴스 생성
bread1 = Bread('팥빵', 3000, 350, ('밀가루', '팥', '설탕' ))
bread2 = Bread('마늘 바게뜨', 5500, 200, ('밀가루', '마늘', '버터' ))

# 빵 종류만 출력 - 인스턴스명.속성
print(f'오늘의 빵 = {bread1.kind}, {bread2.kind}')
# 오늘의 빵 = 팥빵, 마늘 바게뜨

# 각 인스턴스의 모든 속성 출력
# 인스턴스명.print_info()
bread1.print_info()
bread2.print_info()

# 주문 가격에 대한 메서드 호출
bread1.print_price(10)
bread2.print_price(3)

'''
==================================================
팥빵 을(를) 10 개 주문하셨습니다.
 주문 가격은? 30000
==================================================
마늘 바게뜨 을(를) 3 개 주문하셨습니다.
 주문 가격은? 16500
'''

# Cat 클래스
# 속성 : kind, name, age, gender, animal_kind(고양이)
# 메서드 :  속성출력(print_info), 동작 : run, sleep(어디서), eat(무엇을)

class Cat:
    # 생성자 함수 정의
    def __init__(self, kind, name, age, gender):
        self.animal_kind = '고양이'
        self.kind = kind
        self.name = name
        self.age = age
        self.gender = gender

    # 속성 출력 메서드
    def print_info(self):
        print(f'\n\n {self.animal_kind} 정보 출력 ')
        print('='*50)
        print(f' 종류 = {self.kind}')
        print(f' 이름 = {self.name}')
        print(f' 나이 = {self.age}')
        print(f' 성별 = {self.gender}')
        print()

    # 동작 메서드 정의
    def run(self):
        print(f'{self.animal_kind} {self.name} 가 달린다.')

    def sleep(self, where):
        print(f'{self.animal_kind} {self.name}가 {where}에서 잔다.')

    def eat(self, food):
        print(f'{self.animal_kind} {self.name}가 {food}을(를) 먹는다.')

    # 정의 메서드를 이용해서 새로운 메서드 정의
    def action_print(self):
        print('$'*40)
        print(f'{self.animal_kind} {self.name} 의 아침 일상')
        self.eat('물')
        self.eat('사료')
        self.run()
        self.eat('간식')
        self.sleep('쇼파')
        print()

# Cat 클래스의 인스턴스화
cat1 = Cat('코캣', '덩치', 1, '남')
cat2 = Cat('러시안블루', '나비', 5, '여')

# 메서드 호출
cat1.print_info()
cat2.print_info()
cat1.run()
cat2.run()
cat1.sleep('캣타워')
cat2.sleep('택배 박스')
cat1.eat('사료')
cat2.eat('춥스')

cat1.action_print()
cat2.action_print()

# 퀴즈1 - 삼각형 클래스를 다음과 같은 속성과 메서드로 정의하여라
# 속성(이름, 밑변, 높이, 도형의종류)
# 메서드1 - 속성 출력
# 메서드2 - 삼각형의 넓이 출력
# 삼각형의 면적 구하는 공식 = (밑변의길이 * 높이)/2

# 퀴즈2 - 정의한 삼각형 클래스를 이용하여
# 인스턴스 객체를 생성하고 메서드를 호출하여라

class Triangle:
    def __init__(self, objName, base, height):
        self.objName = objName
        self.base = base
        self.height = height
        self.type = '삼각형'

    def info(self):
        print('\n','-'*20)
        print('종류 : ', self.type)
        print('이름 : ', self.objName)
        print('밑변 : ', self.base)
        print('높이 : ', self.height)

    def area(self):
        print('삼각형의 면적 : ', (self.base*self.height)/2)

triangle1 = Triangle('triangle1', 10, 5)
triangle2 = Triangle('triangle2', 10, 8)
triangle1.info()
triangle1.area()
triangle2.info()
triangle2.area()

'''
--------------------
종류 :  삼각형
이름 :  triangle1
밑변 :  10
높이 :  5
삼각형의 면적 :  25.0

 --------------------
종류 :  삼각형
이름 :  triangle2
밑변 :  10
높이 :  8
삼각형의 면적 :  40.0

'''