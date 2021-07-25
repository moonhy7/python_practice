# 클래스 변수
# 클래스 정의시 지정된 공용 변수
# 생성자 함수 위에 정의
# 동일한 주소값을 가지고 있다.
# id(객체이름.속성) : 주소 표시
# 인스턴스 생성후 접근
# - 인스턴스명.클래스변수명
# - 클래스명.클래스변수명

class Test:
    # 공용변수, 클래스 변수
    msg = 'Test 클래스입니다.'

    # 생성자 메서드
    def __init__(self, name):
        # 속성 정의
        self.name = name

    # 일반 메서드
    def print_info(self):
        print('name => ',self.name)

# 객체 인스턴스화
test1 = Test('test1')
# 객체 메서드 호출
test1.print_info()
# 객체 속성 호출
print('name 속성은?', test1.name)
# AttributeError: type object 'Test' has no attribute 'name'
# 클래스명으로는 호출 불가능
# print('name 속성은?', Test.name)

# 클래스 변수 호출 - 인스턴스명.클래스변수명
print('test1.msg 속성은?', test1.msg)

# 클래스 변수 호출 - 클래스명.클래스변수명
print('Test.msg 속성은?', Test.msg)

# 인스턴스 속성과 클래스 변수는 동일한 주소값을 가지고 있을까?
# id(객체이름.속성) : 주소 표시
print(id(test1.msg), id(Test.msg))
print(id(test1.msg) == id(Test.msg))

# 상속(Inheritance)이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1,부모클래스2...)
# 부모 클래스 = 조상 클래스 = 슈퍼 클래스
# 자식 클래스 = 파생 클래스 = 서브 클래스

# 부모 클래스 => Country
# 자식 클래스 => Korea

# 부모 클래스 정의
class Country:
    # 클래스 변수 정의
    name_title = '국가명'
    population_title = '인구'
    capital_title = '수도'

    # 일반 메서드 정의
    def show(self):
        print('국가 클래스의 메서드 show 입니다. ')

# Country 클래스를 상속받는 자식 클래스 정의
class Korea(Country):

    # 생성자 메서드 정의
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    # 속성 출력 메서드 정의
    def show_info(self):
        # name_title, capital_title, population_title 속성은
        # 부모 클래스 Country에서 받은 속성이다.
        print('\n'*2+'$'*50)
        print(self.name_title ,self.name)
        print(self.capital_title, self.capital)
        print(self.population_title, self.population)
        print()

# 인스턴스화
kor = Korea('대한민국', '서울', '5164만')
kor.show_info()
# 부모 클래스에서 상속받은 메서드 호출
kor.show()

# 다중 클래스 상속
# 부모클래스1 Papa - 아파트, 차, 김철수
# 부모클래스2 Mama - 오피스텔, 전동스쿠터, 이영희
# 자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터, 로봇청소기, ?은주

# 부모클래스를 상속해서 자식 클래스 만들기
# class 자식클래스명(부모클래스명1, 부모클래스명2....):
#   명령문

# 부모 클래스 1
class Papa:
    # 클래스 변수
    family_name = '김'
    name = '철수'
    # 생성자 메서드
    # def __init__(self, name):
    #     self.name = name

    # 일반 메서드
    def asset_info1(self):
        print('아파트', '차')

    def print_info(self):
        print(f'Papa 이름 => {self.family_name} {self.name}')


# 부모 클래스 2
class Mama:
    # 클래스 변수
    family_name = '이'
    name = '영희'
    # # 생성자 메서드
    # def __init__(self):
    #     self.name = name

    # 일반 메서드
    def asset_info2(self):
        print('오피스텔', '전동스쿠터')

    def print_info(self):
        print(f'Mama 이름 => {self.family_name} {self.name}')

# 자식 클래스 <= Papa, Mama
# 우선순위 : 메서드 이름과 속성 이름이 같은 경우
# Child > Papa > Mama
class Child(Papa, Mama):
    def __init__(self, name):
        self.name = name

    def asset_info3(self):
        print('로봇 청소기')

    # 메서드 오버라이딩 :
    # 부모클래스에서 미리 정의된 메서드 이름과 동일한 메서드를 재정의하는 기능
    def print_info(self):
        print(f'child 이름 => {self.family_name} {self.name}')

# 부모 클래스 인스턴스화
print('='*50)
papa = Papa()
papa.print_info()  # 이름 => 김 철수
papa.asset_info1() # 아파트 차

print('='*50)
mama = Mama()
mama.print_info()  # 이름 => 이 영희
mama.asset_info2() # 오피스텔 전동스쿠터

print('='*50)
# 자식 클래스의 인스턴스화
child = Child('은주')
# 부모 클래스의 메서드 호출
child.asset_info1() # 아파트 차
child.asset_info2() # 오피스텔 전동스쿠터

# Papa 클래스의 print_info() X
# Child 클래스의 print_info() O
print('='*50 )
child.print_info() # child 이름 => 김 은주

# Child 클래스의 메서드 호출
child.asset_info3()

# 상속된 속성 확인
print('-'*50)
print('child.name => ', child.name)
# child.name =>  은주
print('family_name => ', child.family_name)
# family_name =>  김


# 부모 클래스와 자식 클래스의 관계 확인
# issubclass(자식클래스,부모클래스)
# : 자식클래스와 부모 클래스와의 관계 표시 (True / False)
# 부모 클래스 정보 표시
# 클래스명.__bases__ => 튜플 형태
print('='*50)
print(issubclass(Child, Papa)) # True
print(issubclass(Child, Mama)) # True
print(issubclass(Papa, Mama)) # False
print(f'Child 클래스의 부모 클래스는? {Child.__bases__}')
# Child 클래스의 부모 클래스는? (<class '__main__.Papa'>, <class '__main__.Mama'>)


# 부모 클래스 : Tiger , Lion
# 자식 클래스 : Liger

class Tiger:
    kind = '호랑이'
    def jump(self):
        print('호랑이처럼 멀리 점프하기')
    def cry(self):
        print('호랑이 : 어흥 ~ ')

class Lion:
    kind = '사자'
    def bite(self):
        print('사자처럼 한입에 꿀꺽하기')
    def cry(self):
        print('사자 : 으르렁 ~ ')

# 자식 클래스
class Liger(Lion, Tiger):
    kind = '라이거'
    def play(self):
        print('라이거만의 사육사와 재미있게 놀기')

    # 메서드 오버라이딩(method overriding)
    def cry(self):
        print('라이거 : 어흥~ 으르렁~')

    # 첫번째로 상속받은 부모클래스의 cry() 메서드를 사용하고 싶다면?
    # super() 이용
    def cry1(self):
        super().cry()



# 부모 클래스 인스턴스화
print('\n\n========tiger========')
tiger = Tiger()
print(tiger.kind, Tiger.kind)
tiger.cry()
tiger.jump()
'''
호랑이 호랑이
호랑이 : 어흥 ~ 
호랑이처럼 멀리 점프하기
'''
print('\n\n========lion========')
lion = Lion()
print(lion.kind, Lion.kind)
lion.bite()
lion.cry()
'''
사자 사자
사자처럼 한입에 꿀꺽하기
사자 : 으르렁 ~ 
'''
print('\n\n========liger========')
liger = Liger()
print(liger.kind, Liger.kind) # 라이거 라이거
# 클래스명.클래스변수 로도 호출 가능
print(Tiger.kind, Lion.kind) # 호랑이 사자
liger.bite() # 사자처럼 한입에 꿀꺽하기
liger.jump() # 호랑이처럼 멀리 점프하기
liger.play() # 라이거만의 사육사와 재미있게 놀기
liger.cry() # 라이거 : 어흥~ 으르렁~
# 부모 클래스의 상속받은 메서드를 재정의 super() 이용
liger.cry1() # 사자 : 으르렁 ~







