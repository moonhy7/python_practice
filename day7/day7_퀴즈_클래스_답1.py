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


