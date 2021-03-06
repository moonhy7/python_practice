
#  함수 퀴즈 : 5문제만 코딩해보세요

# 퀴즈1 : 별찍기
# 지정한 숫자 만큼 다음과 같은 형태로 출력하는
# 함수를 정의한 후 호출하여라.

'''
starPrint(5)

결과 :
*
**
***
****
*****

starPrint(3)

결과 :
*
**
***
'''




# 퀴즈2
# 인자값을 받아서 출력하는 구구단 함수를 정의한 후
# 호출하여 출력하여라
'''
def gugu(n):
    ?

gugu(9)

출력 >>
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81

'''





# 퀴즈 3:
# 리스트를 호출하면 각각의
# 구성 아이템이 다음과 같이 출력되도록 함수를 정의하여라
'''
# printList(['라면', '빙수'])

   오늘의 메뉴   
1  :  라면
2  :  빙수

# printList(['모밀', '탕수육', '육계장'])
   오늘의 메뉴   
1  :  모밀
2  :  탕수육
3  :  육계장
'''




# 퀴즈 4
# 키와 몸무게를 인자로 입력하여
# 메세지가 출력되도록 함수를 정의하고
# bmi 값에 따라 출력한다.
#
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
#
# bmi = (체중(kg)/키(m)의제곱)*1000
#
# bmi 값에 따라 다음과 출력한다.
#
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

'''
# 함수 호출 
Bmi(170, 68)


키 :  170
몸무게 :  68
과체중
BMI : 23.53

'''







# 퀴즈 5
# 아래의 예제를 참조하여 함수를 호출하면 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 
say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 결과값 1
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
--------------------------------------------------
# 결과값 2
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''





# 퀴즈 6
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하고 호출하여라
'''
# 함수 호출 
addList(1,2,3,4)
addList('가','나','다','라','마')

결과1 >>>
총 갯수 : 3
데이타형 : <class 'list'>
0 번째 => 1
1 번째 => 2
2 번째 => 3

결과2 >>>
총 갯수 : 5
데이타형 : <class 'list'>
0 번째 => 가
1 번째 => 나
2 번째 => 다
3 번째 => 라
4 번째 => 마


'''




# 퀴즈 7
# 첫번째 인자의 값이 'min'이면 다음 인자의 숫자 중
# 최대값을 출력하고
# 첫번째 인자의 값이 'max'이면 다음 인자의 숫자중
# 최소값을 출력하여라
# 이 때 전달하는 숫자의 갯수는 가변으로 한다.

'''
min_max_number('min', 100, 20, 40)
min_max_number('min', 100, 20, 40, 500, 1)
min_max_number('max', 100, 20, 40)
min_max_number('max', 100, 20, 40, 500, 1)

# 결과 
최소값은?  20
최소값은?  1
최대값은?  100
최대값은?  500

'''




# 퀴즈 8
# **kwargs 인자 가변 함수를 이용하여
# 함수 호출시 결과값이 다음과 같이 딕셔너리 형태로
# 출력되도록 하여라
'''
# 함수 호출 
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

결과1 >>>

{'a': 'apple', 'b': 'banana', 'n': 'nano'}
a : apple
b : banana
n : nano

결과2 >>>
{'b': 'banana', 'n': 'nano', 's': 'soup', 'd': 'dress', 'q': 'quit'}
b : banana
n : nano
s : soup
d : dress
q : quit

'''




# 퀴즈 9
# 첫글자를 제외한 나머지 글자를 '*'로 표시하는
# 람다함수를 정의하여라. 입력되는 문자열은 3글자로 한다.
# 변수 = lambda 인자:명령문

'''
# 함수 호출 
# f1('홍길동')
# f1('김철수')

결과: >>
홍**
김**
'''




# 퀴즈 10
# 국어,영어,수학 3과목의 합과 평균을 구하는
# 람다 함수를 정의하여라
'''
# 람다 호출 
# f2(100,80,90)

결과 >>
국어:100, 영어:80, 수학:90 , 총점:270, 평균90.00

'''


