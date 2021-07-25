
# 퀴즈 1:
# 아래와 같이 3줄로 글자를 출력하는 4가지 방법은?
'''
파이썬
파이썬
파이썬
'''

# 방법1
print('파이썬')
print('파이썬')
print('파이썬')
print('*'*30)

# 방법2
print('파이썬\n'*3)
print('*'*30)

# 방법3
print('파이썬\n파이썬\n파이썬')
print('*'*30)

# 방법4
multiLine = '''
파이썬
파이썬
파이썬
'''
print(multiLine)
print('*'*30)


# 퀴즈 2
# 홍길동 씨의 과목별 점수는 다음과 같다.
# 홍길동 씨의 평균 점수를 소숫점 둘째자리까지 출력하여라
'''
국어 : 86
영어 : 77
수학 : 55
평균 : ?
'''

class1 = 86
class2 = 77
class3 = 55
print('국어 : ', class1)
print('영어 : ', class2)
print('수학 : ', class3)
print('평균 : ', (class1+class2+class3)/3)
print('평균 :  %.2f' % ((class1+class2+class3)/3) )
print('*'*30)

# 퀴즈 3
# 변수 a,b를 입력문을 이용하여 데이터를 저장한다.
# == 을 이용하여 a,b 가 같은지 True, False 로
# 출력하여라
'''
a값 입력 => 10
b값 입력 => 10
True
'''

# a = input('a ? ')
# b = input('b ? ')
# print(a == b)
# print('*'*30)


# 퀴즈 4
# 2개의 숫자를 입력받아 다음과 같이 출력하여라
# % 포맷 이용

# '''
# 숫자1을 입력하세요... 12
# 숫자2를 입력하세요... 12.345
#
# 입력받은 숫자1은 12 입니다.
# 입력받은 숫자1은 8진수로 14 입니다.
# 입력받은 숫자1은 16진수로 c 입니다.
# 입력받은 숫자2는 12.3 입니다.
# '''

# myNum1 = int(input('숫자를 입력하세요....'))
# myNum2 = float(input('숫자를 입력하세요... '))
# print('입력받은 숫자1은 %d 입니다.' % myNum1 )
# print('입력받은 숫자1은 8진수로 %o 입니다.' % myNum1 )
# print('입력받은 숫자1은 16진수로 %x 입니다.' % myNum1 )
# print('입력받은 숫자2는 %.1f 입니다.' % myNum2 )
#
# print('*'*30)


# 퀴즈 5
# 홍길동씨의 주민등록번호는 881120-1068234
# 연월일과 숫자 부분을 나누어서 출력하여라.
'''
연월일 : 881120
숫자 : 1068234
'''

pin = '881120-1068234'
# yyyymmdd = pin[0:6]
yyyymmdd = pin[:6]
num = pin[7:]
print('연월일 : ',yyyymmdd)
print('숫자 : ',num)

print('*'*30)



# 퀴즈 6
# 2개의 변수를 정의하고 아래와 같이 출력한다.
# format 또는 % 또는 f'' 이용

'''
movie1 = '알라딘'
movie2 = '스파이더맨'

--------------
오늘의 영화 => 스파이더맨 , 알라딘

'''

movie1 = '알라딘'
movie2 = '스파이더맨'
print('오늘의 영화 : {} : {}'.format(movie1,movie2))
print('오늘의 영화 : %s, %s' % (movie1, movie2))
print(f'오늘의 영화 : {movie1}, {movie2}')

print('-'*30)


# 퀴즈 7
# 다음과 같이 문자열 변수를 정의하고 결과값이 출력되도록 한다.
'''
Let thy speech be short, comprehending much in few words.

결과 >> 
첫번째 t의 위치 : ?
첫번째 m의 위치 : ?
s 의 갯수 : ?

= 이 모든 글자 사이에 연결되게 표시 : ?
 
모두 대문자로 표시 : ? 

'''

message = 'Let thy speech be short, comprehending much in few words.'
print(message)
print('첫번째 t의 위치 인덱스 : ', message.find('t'))
print('첫번째 m의 위치 인덱스 : ', message.find('m'))
print('s 의 갯수 : ', message.count('s'))
print('\n= 으로 연결 : \n')
print('='.join(message))
print('\n대문자로 변경 :  \n')
print(message.upper())

print('-'*30)


# 퀴즈 8
# 아래와 같이 변수를 지정하고
# humidity = 82
# temperature = -1.8
# % 포맷, format(), f' 포맷 3가지 방식을 이용하여 다음과 같이 출력하여라

'''
오늘의 날씨 : 맑음, 습도 82%, 현재기온 -1.8
'''

humidity = 82
temperature = 1.878

print('오늘의 날씨 : 맑음, 습도 %d%%, 현재기온 %.1f' % (humidity, temperature))
print('오늘의 날씨 : 맑음, 습도 {0}%, 현재기온 {1:.1f}'.format(humidity, temperature))
# print(f'오늘의 날씨 : 맑음, 습도 {humidity}%, 현재기온 {round(temperature,1)}')
print(f'오늘의 날씨 : 맑음, 습도 {humidity}%, 현재기온 {temperature:.1f}')
