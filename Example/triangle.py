# 삼각형 클래스 정의
# triangle.py

class Triangle:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def printInfo(self):
        print(f'이름 = {self.name}')
        print(f'밑변 = {self.width}')
        print(f'높이 = {self.height}')
        print('='*50)

    def printArea(self):
        print(f'삼각형 넓이 = {(self.width*self.height)/2:.2f}')
        print('='*50)

# t1 = Triangle('삼각형1', 30, 30)
# t1.printInfo()
# t1.printArea()