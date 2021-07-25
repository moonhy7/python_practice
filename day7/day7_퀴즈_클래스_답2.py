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

# 계좌번호는 3자리-2자리-6자리
# print(random.randint(100,999),'-',random.randint(10,99), '-', random.randint(100000,999999))
# account_number = str(random.randint(100,999))+'-'+str(random.randint(10,99))+'-'+str(random.randint(100000,999999))
# print(account_number)

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#         self.account_number = str(random.randint(100,999)) + '-' \
#                               + str(random.randint(10,99)) + '-' \
#                               + str(random.randint(100000,999999))
#
# # 인스턴스 생성
# kim = Account("김민수", 100)
# print('고객명 :', kim.name)
# print('잔액 : ', kim.balance)
# print('은행 : ',kim.bank)
# print('계좌 : ', kim.account_number)


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

class Account:
    # 클래스 변수
    account_count = 0

    # 생성자 메서드
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.account_number = str(random.randint(100,999)) + '-' \
                              + str(random.randint(10,99)) + '-' \
                              + str(random.randint(100000,999999))
        # 계좌 생성시 누적 카운트
        # 클래스.클래스변수 로 접근 가능
        Account.account_count += 1

    # 생성된 인스턴스를 출력하는 메서드
    def get_account_num(self):
        print(f'총 계좌수 : {Account.account_count}')

    # self 값이 없는 메서드 => 클래스 메서드
    # 클래스명.메서드() 접근 가능
    def get_account_num2():
        print(f'총 계좌수 : {Account.account_count}')

    # 입금 메서드
    # 입금 금액은 1보다 커야한다.
    # 입금 금액은 잔액(balance)에 누적된다.
    def deposit(self, amount):
            if amount >= 1:
                self.balance += amount
            else:
                print('입금 오류')

    # 출금 메서드
    # 잔액에서 출금만큼 금액은 인출되어야 한다.
    # 출금 금액은 잔액보다 작아야한다.
    def withdraw(self, amount):
            if self.balance > amount:
                self.balance -= amount
            else:
                print('출금 오류')

    # 계좌 정보 출력 메서드
    def display_info(self):
        print("은행이름 : ", self.bank)
        print("예금주 : ", self.name)
        print("계좌번호 : ", self.account_number)
        print("잔고 : ", self.balance)


# 인스턴스 생성
# chio = Account("최진수", 100)
# print('계좌수는? ', Account.account_count)
# kim = Account("김민수", 100)
# print('계좌수는? ', Account.account_count)
# lee = Account("이민수", 100)
# print('계좌수는? ', Account.account_count)

# 총 계좌수
# 마지막으로 생성된 인스턴스.get_account_num()
# lee.get_account_num()
# 클래스명.get_account_num()
# Account.get_account_num2()


print('#'*70)
# chio = Account("최진수", 100)
# print('잔액 => ',chio.balance) # 잔액 =>  100
# chio.deposit(100)
# print('잔액 => ',chio.balance) # 잔액 =>  200
# chio.withdraw(90)
# print('잔액 => ',chio.balance) # 잔액 =>  110
# chio.deposit(0.5) # 입금 오류
# chio.withdraw(300) # 출금 오류

chio = Account("최진수", 100)
chio.display_info()
