# 클래스 구조의 자판기 프로그램
# 속성 :  메뉴, 가격, 이름
# 메소드
# : 메뉴 표시
# : 금액 투입
# : 메뉴 선택과 선택한 메뉴 배달 완료
# : 남은 금액 표시

class Vending_machine:
    def __init__(self, v_name, product, price):
        self.v_name = v_name
        self.product = product
        self.price = price

    # 메뉴 표시
    def show_menu(self):
        print(f'\n\n\t\t {self.v_name} ')
        # print(f'메뉴1 : {self.product[0]} 가격 {self.price[0]}')
        for i in range(0, len(self.product)):
            print(f'메뉴{i+1} : {self.product[i]} /  가격 {self.price[i]} 원')

    # 금액 투입
    def input_money(self):
        print('주문하실 메뉴의 금액을 삽입구에 넣어주세요')
        while True:
            self.in_money = input('투입 => ').strip()
            # 숫자만 입력되는 확인
            if self.in_money.isdigit():
                # 자료형 변경
                self.in_money = int(self.in_money)
                break
            else:
                print('투입한 금액이 올바르지 않습니다. 주문이 불가능합니다.')


    # : 메뉴 선택과 선택한 메뉴 배달 완료
    def get_drink(self):
        # 메뉴 선택 변수
        print('========== 메뉴를 선택하세요 ==========')
        for i in range(0, len(self.product)):
            print(str(i+1)+'.' + self.product[i], end='   ')
        print(' (환불 및 다시 시작 q)')
        print('======================================')
        sel = (input('선택 => ').strip())
        if sel == 'q':
            print(f'투입구를 확인하여 주세요(금액 환불) => {self.in_money}원')
            self.start()
        else:
            sel = int(sel)
            if 0< sel <= len(self.product):
                if self.in_money >= self.price[int(sel) - 1]:
                    print('=====================================')
                    print(f'주문하신 {self.product[int(sel) - 1]}가 나왔습니다.')
                    print(f'잔돈은 {self.in_money-self.price[int(sel) - 1]}원 입니다.')
                    self.start()
                else:
                    print('투입 금액이 부족하여 주문이 불가능합니다.')
                    self.get_drink()
            else:
                print('선택 번호의 메뉴가 없습니다.')



    def start(self):
        while True:
            # 메뉴 표시
            self.show_menu()
            # 금액 삽입 메세지
            self.input_money()
            # 투입금액이 가장 낮은 메뉴의 가격보다 큰지 확인
            if self.in_money >= int(min(self.price)):
                print('주문이 가능합니다.')
                # 메뉴 선택과 주문 완료
                self.get_drink()
                break
            else:
                print('투입 금액이 부족하여 주문이 불가능합니다.')
                print(f'투입구를 확인하여 주세요(환불) => {self.in_money}원')




# vm1 = Vending_machine('강남점',('아메리카노', '라떼', '마끼아또'), (800, 1200, 2000))
# vm1.start()

# vm2 = Vending_machine('분당점',('아메리카노', '핫초코', '버블티'), (800, 1000, 2500))
# vm2.start()


vm3 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
vm3.start()






