# 기본자료형 < 집합자료형 < 함수 < 클래스 < 모듈(파일단위) < 패키지(폴더단위)

# 패키지(Package)
# 모듈 파일(함수가 정의된 파이썬 파일) 을 별도의 폴더에 저장하여 쓰는 기능
# 폴더는 패키지명으로 이용

# 파이참에서 패키지용도의 폴더만들기
# [Project] 창에서 폴더 마우스우측버튼
# [New]-[python package]
# 패키지폴더가 생성되고 자동으로 __init__.py 파일 생성
# __init__.py
# : 패키지폴더임을 알려주는 파일

# 별도패키지폴더명 - AAA
# 패키지안의 모듈 파일 - AAA/a.py
# 모듈파일안에 함수 정의 - testPrint()

# 패키지안의 모듈안의 함수 호출 방법 1
# import 패키지명.모듈명
# 패키지명.모듈명.함수(인자)
# import AAA.a
# AAA.a.testPrint()

# 패키지안의 모듈안의 함수 호출 방법 2
# import 패키지명.모듈명 as 별칭
# 별칭.함수(인자)
# import AAA.a as aa
# aa.testPrint()


# 패키지안의 모듈안의 함수 호출 방법 3
# from 패키지명.모듈명 import 함수
# 함수(인자)
from AAA.a import testPrint
testPrint()

# 패키지안의 패키지안의 모듈과 함수 테스트
# 별도패키지폴더명 - AAA/BBB
# 패키지안의 모듈 파일 - AAA/BBB/b.py
# 모듈파일안에 함수 정의 - testPrint_B()

# import 패키지명.패키지명.모듈명 as 별칭
import AAA.BBB.b as bb
bb.testPrint_b()

# 다른 패키지의 모듈이나 모듈안의 클래스 호출하기
# 같은 폴더안의 triangle.py 삼각형 클래스 정의
import triangle

# 객체 생성
# 모듈명.클래스명(값)
t1 = triangle.Triangle('삼각형A', 50, 30)
t1.printInfo()
t1.printArea()

# CCC 패키지폴더안의 모듈안의 클래스 정의해서 테스트
# CCC 패키지(폴더) / account 모듈(파일) / Account 클래스 정의
# import 패키지명.모듈명
# 패키지명.모듈명.함수(인자)
import CCC.account
hong = CCC.account.Account('홍길동', 3000)
hong.display_info()

# * 명령으로 특정 패키지(폴더)안의 모든 모듈 임포트하기

# 패키지로 정의된 폴더안의 __init__.py
# __all__ = [모듈명1, 모듈명2...]
# CCC/__init__.py
# __all__ = ['c1', 'c2']

# from 패키지명 import *
# 함수 호출
# 모듈명.함수명으로 호출가능

# 작업 과정
# CCC 패키지안의 account.py, triangle.py, helloworld.py 생성
# account.py, triangle.py, helloworld.py 파일안에는 클래스나 함수가 정의되어 있어야 한다.

# CCC 패키지안의 __init__.py
# 임포트할 수 있는 모듈명 리스트 정의
# __all__ = [모듈명1, 모듈2 ... ]
# __all__ = ['account', 'triangle', 'helloworld']

# CCC 패키지안의 모든 모듈을 임포트
from CCC import *

# 모듈명.함수명() 또는 모듈명.클래스명() 으로 호출가능

helloworld.hello_world()

t1 = triangle.Triangle('삼각형1', 30, 30)
t1.printInfo()
t1.printArea()

user1 = account.Account('박수철', 3000)
user1.display_info()
user1.deposit(3000)
user1.display_info()
user1.withdraw(500)
user1.display_info()







