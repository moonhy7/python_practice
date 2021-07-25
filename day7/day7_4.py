# 모듈의 종류
# - 내부모듈
# : 파이썬에서 기본적으로 제공
# : datetime, time, math, random ....
# - 외부 모듈
# : pip/pip3(파이썬), conda(아나콘다)를 이용해서 별도 설치
# : 파이참에서는 [File]-[Settings]
#       [Project Interpreter]에서 확인
# : pandas, numpy, mathplotlib, seaborn, flask ...
# - 사용자정의 모듈
# : 필요에 의해서 직접 모듈로 등록한 후 사용


# 모듈의 호출방법 1
# import 모듈이름
# 모듈이름.함수(인자)

# 모듈의 호출방법 2
# import 모듈이름 as 별칭
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)

# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)

# math 모듈안의 수학함수(sin(), cos(), tan(), pi...) 이용하기

# 방법1
# import 모듈이름
# 모듈이름.함수(인자) / 모듈이름.속성
# import math
# print(math.pi) # 3.141592653589793
# print(math.cos(10)) # -0.8390715290764524

# 방법2 - 별칭 이용
# import 모듈이름 as 별칭
# 별칭.함수(인자) / 별칭.속성
# import math as m
# print(m.pi) # 3.141592653589793
# print(m.cos(10)) # -0.8390715290764524

# 방법3 - from 사용. 모듈명 없이 함수만 바로 호출 가능
# from 모듈이름 import 모듈함수/속성
from math import pi, cos
print(pi)
print(cos(10))

# 사용자 정의 모듈
# 기본자료형 < 집합 < 함수 < 클래스 < 모듈 (파일단위) < 패키지(폴더)

# sample1.py 파일안에 1~10 출력하는 함수 정의
# 현재 문서에서 test1.py의 함수를 호출한다.

# sample1.py 모듈을 임포트
import sample1
sample1.print_10()
print(sample1.sum_100())

# 구구단 모듈
# Step1. gugu.py로 입력한 숫자에 대한 구구단을 출력하는 모듈파일 생성
# Step2. import gugu로 모듈을 임포트 한 후 모듈이 실행되는지 확인
import gugu
gugu.gugu()






