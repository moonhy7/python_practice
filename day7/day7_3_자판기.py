# 클래스를 이용한 자판기 메뉴를 표시하는 프로그램을 프로그래밍 하려고 한다.
# 다음과 같이 속성과 메서드를 정의하여라.
# 속성
# :  지역, 메뉴(튜플형태), 가격(튜플형태)
# 메소드
# : 메뉴 표시
# : 머신 실행

class Vending_machine:
    # 생성자 메서드 정의
    def __init__(self, v_name, product, price):
        self.v_name = v_name
        self.product = product
        self.price = price

    # 메뉴와 가격표시 메서드 정의
    def show_menu(self):
        print(f'\n\t\t {self.v_name}')
        for i in range(len(self.product)):
            print(f'메뉴{i+1} : {self.product[i]} / 가격 : {self.price[i]}  원 ')

    # 금액 투입 메서드
    def input_money(self):
        print('주문하실 메뉴의 금액을 삽입구에 넣어주세요')
        self.in_money = input('투입 => ').strip()
        # 숫자만 입력되는지 유효성 검사
        if self.in_money.isdigit():
            print('OK')
        else:
            print('투입한 금액이 올바르지 않습니다. 주문이 불가능합니다.')

    # 자판기 실행 메서드
    def start(self):
        while True:
            # 메뉴 표시 메서드 호출
            self.show_menu()
            # 금액 투입 메서드 호출
            self.input_money()
            break

# 인스턴스화
vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
# vm1.start()

vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
# vm2.start()

vm3 = Vending_machine('부산역점',
                      ('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'),
                      (2000, 700, 1500, 1300))
vm3.start()

