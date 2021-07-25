# 클래스 퀴즈

# 퀴즈 1
# 삼각형 클래스를 다음과 같은 속성과 메서드로 정의하여라
# 속성(이름, 밑변, 높이)
# 메서드1 - 속성 출력
# 메서드2 - 삼각형의 넓이 출력
# 삼각형의 면적 구하는 공식 = (밑변의길이 * 높이)/2

# print('퀴즈1')
class Triangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
    def printInfo(self):
        print(f'이름 = {self.name}')
        print(f'밑변 = {self.width}')
        print(f'높이 = {self.height}')
        print('====================')
    def printArea(self):
        print(f'삼각형 넓이 = {(self.width*self.height)/2:.2f}')
        print('====================')


# 퀴즈 2
# 퀴즈1의 삼각형 클래스를 이용하여 인스턴스 객체를 생성하고 메서드를 호출하여라


'''
이름 = triangle1
밑변 = 10
높이 = 5
====================
삼각형 넓이 = 25.00
====================


이름 = triangle2
밑변 = 35
높이 = 27
====================
삼각형 넓이 = 472.50
====================


'''

print('퀴즈2')
triangle1 = Triangle('triangle1', 10, 5)
triangle1.printInfo()
triangle1.printArea()
triangle2 = Triangle('triangle2', 35, 27)
triangle2.printInfo()
triangle2.printArea()




# 퀴즈 3
# 클래스 Animal과  Animal 클래스를 상속받는 Dog 클래스를
# 정의하여라. 아래는 참고 코딩이다.


# class Animal:
#     def __init__(self, objName, leg):
#         명령 입력
#
#     def info(self, objName, leg):
#         명령 입력
#
#     def run(self):
#         명령 입력
#
#     def (self, food):
#         명령 입력


#
# class Dog(?):
#
#   def printName(self, name):
#         명령 입력
#     def shout(self, sound):
#         명령 입력
#


# print('퀴즈 3')
class Animal:
    def __init__(self, objName, leg):
        self.objName = objName
        self.leg = leg

    def info(self):
        print(f'종류 : {self.objName}')
        print(f'다리수 : {self.leg}')

    def run(self):
        print(f'{self.objName} 이(가) 달린다. ')

    def eat(self, food):
        print(f'{self.objName} 이(가) {food}을(를) 먹는다.')


class Dog(Animal):
    def printName(self, name):
        print(f'{self.objName}의 이름은 {name}이다.')

    def shout(self, sound):
        print(f'{self.objName} 이(가) {sound} 짖는다.(소리를 낸다) ')





# 퀴즈 4
# 퀴즈 3에서 정의한 클래스를 이용하여 다음과 같이 출력되도록
# 객체 인스턴스화하고 메서드를 호출하여라.
'''
종류 : 동물
다리수 : 4
동물 이(가) 달린다. 
동물 이(가) 물을(를) 먹는다.
==============================
종류 : 강아지
다리수 : 4
강아지 이(가) 달린다. 
강아지 이(가) 뼈다귀을(를) 먹는다.
강아지의 이름은 행운이이다.
강아지 이(가) 멍멍 짖는다.(소리를 낸다) 
'''


print('='*30)
print('\n\n 퀴즈4 결과 >> ')
animal1 = Animal('동물', 4)
animal1.info()
animal1.run()
animal1.eat('물')
print('='*30)
dog1 = Dog('강아지', 4)
dog1.info()
dog1.run()
dog1.eat('뼈다귀')
dog1.printName('행운이')
dog1.shout('멍멍')


# 퀴즈 5
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정된다.
# Account 클래스를 생성한 후 객체 인스턴스를 구현하도록 프로그래밍하여라.
# 객체 인스턴스는 예금주와 초기 잔액만 입력 받으며
# 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성한다.
# random 모듈 이용
'''
고객명 김민수
잔액 100
은행 SC은행
계좌 375-85-239565
'''

import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        # self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

kim = Account("김민수", 100)
print('고객명', kim.name)
print('잔액', kim.balance)
print('은행',kim.bank)
print('계좌', kim.account_number)


# 퀴즈 6
# 퀴즈 5의 클래스에 클래스 변수를 사용해서
# Account 클래스로부터 생성된 계좌 객체와 관련된 변수를 정의하고
# 출력하도록 get_account_num() 메서드를 추가하여라.
'''
# 계좌를 3개 인스턴스화 한 경우 
chio = Account("최진수", 100)
kim = Account("김민수", 100)
lee = Account("이민수", 100)
Account.get_account_num()

결과>>
총 계좌수 :  3

'''


# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     # @classmethod
#     def get_account_num():
#         # print(cls.account_count)     # Account.account_count
#         print('총 계좌수 : ',Account.account_count)     # Account.account_count
#
# chio = Account("최진수", 100)
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# Account.get_account_num()

# 퀴즈 7
# 위에서 정의한 Account 클래스에
# 입금을 위한 deposit 메서드와
# 출금을 위한 withdraw 메서드를 하여라.
# 출금은 계좌의 잔고 이상으로 출금할 수는 없으며
# 입금은 최소 1원 이상만 가능하다.
'''
# 객체 인스턴스 참고코드. 
k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print('잔액 => ',k.balance)

# 잔액 =>  110
'''


# import random
#
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count +=1
#
#     # @classmethod
#     def get_account_num():
#         # print(cls.account_count)     # Account.account_count
#         print('총 계좌수 : ',Account.account_count)     # Account.account_count
#
#     def deposit(self, amount):
#             if amount >= 1:
#                 self.balance += amount
#
#     def withdraw(self, amount):
#             if self.balance > amount:
#                 self.balance -= amount
#
# print('#'*70)                                                      *70)
# k = Account("kim", 100)
# k.deposit(100)
# k.withdraw(90)
# print('잔액 => ',k.balance)

# 잔액 =>  110


# 퀴즈 8
# 위에서 정의한 Account 클래스에
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를
# 추가하여라.
'''
# 객체 인스턴스 참고 소스 
print('$'*70)
p = Account("홍길동", 10000)
p.display_info()

#  >> 결과 
은행이름:  SC은행
예금주:  홍길동
계좌번호:  098-29-285603
잔고:  10000
'''

import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count +=1

    # @classmethod
    def get_account_num():
        # print(cls.account_count)     # Account.account_count
        print('총 계좌수 : ',Account.account_count)     # Account.account_count

    def deposit(self, amount):
            if amount >= 1:
                self.balance += amount

    def withdraw(self, amount):
            if self.balance > amount:
                self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

print('$'*70)
p = Account("홍길동", 10000)
p.display_info()


# 퀴즈 9
# 클래스를 이용한 자판기 메뉴를 표시하는 프로그램을 프로그래밍 하려고 한다.
# 다음과 같이 속성과 메서드를 정의하여라.
# 속성
# :  지역, 메뉴(튜플형태), 가격(튜플형태)
# 메소드
# : 메뉴 표시
# : 머신 실행


'''
# vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
# vm1.start()

		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
'''


'''
# vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
# vm2.start()
		 분당점 
메뉴1 : 아메리카노 /  가격 800 원
메뉴2 : 핫초코 /  가격 1000 원
메뉴3 : 버블티 /  가격 2500 원

'''


'''
# vm3 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
# vm3.start()

		 부산역점 
메뉴1 : 수박쥬스 /  가격 2000 원
메뉴2 : 아이스아메리카노 /  가격 700 원
메뉴3 : 카푸치노 /  가격 1500 원
메뉴4 : 탄산수 /  가격 1300 원

'''


# 퀴즈 10 :
# 퀴즈 9의 자판기 머신 클래스에 금액을 투입하여
# 투입한 금액에 따라 메세지를 출력하는
# 메서드를 추가하고 실행되도록 프로그램하여라.

'''
		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => Yes
투입한 금액이 올바르지 않습니다. 주문이 불가능합니다.
투입 => 

'''

'''
# 예시 

		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

'''

'''
		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 500
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 500원

'''


# 퀴즈 7 :
# 퀴즈 6의 자판기 머신 클래스에서 아래 출력 화면을
# 참조하여 메서드를 추가하고 실행되도록 하여라.
# - 투입금액에 따른 메뉴 선택
# - 메뉴 선택에 따른 메시지 출력
# - 잔돈 메시지

'''


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 1500
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 2
투입 금액이 부족하여 주문이 불가능합니다.


========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 567
선택 번호의 메뉴가 없습니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => hhh
잘못된 입력입니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => q
투입구를 확인하여 주세요(금액 환불) => 1500원


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 900
투입 금액이 부족하여 주문이 불가능합니다.
투입구를 확인하여 주세요(환불) => 900원


		 강남점 
메뉴1 : 아메리카노 /  가격 1200 원
메뉴2 : 라떼 /  가격 2000 원
주문하실 메뉴의 금액을 삽입구에 넣어주세요
투입 => 2000
주문이 가능합니다.

========== 메뉴를 선택하세요 ==========
1.아메리카노   2.라떼    (환불 및 다시 시작 q)
======================================
선택 => 1

=====================================
주문하신 아메리카노가 나왔습니다.
잔돈은 800원 입니다.


'''





