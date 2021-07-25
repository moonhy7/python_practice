# 함수

# 사용자정의함수
# 빌트인 함수 => 파이썬에서 제공하는 함수

# 내장함수 : 별도의 import 명령이 필요없다
#           함수(옵션) ex) abs(), enumerate(), len(), int(), float(), type()...
# 외장함수 : 별도의 import 명령이 필요
#           모듈.함수(옵션) ex) datetime 함수

# 시계열 데이타 다루기 - datetime , time 모듈 사용

# 시간과 관련된 모듈 임포트
import datetime

# 현재 시간을 기준으로 년,월,일,시,분,초 변수 생성
# datetime.함수(옵션)
# datetime.속성
now = datetime.datetime.now()
print(now) # 2021-01-04 16:53:37.955876
print(' 년도 : ', now.year) # 2021
print(' 월 : ', now.month) # 1
print(' 날짜 : ', now.day) # 4
print(' 시간 : ', now.hour) # 16
print(' 분 : ', now.minute) # 53
print(' 초 : ', now.second) # 53

print('-'*30, '\n'*2)

# 아래와 같이 출력하여 보세요
# 오늘은 ?년 ?월 ?일 입니다.
# 현재시간은 ()시 ()분입니다
now = datetime.datetime.now()
print(f'오늘은 {now.year}년 {now.month}월 {now.day}일 입니다.')
print(f'현재 시간은 {now.hour}시 {now.minute}분입니다.')

# 퀴즈 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 출력한다. - 오전 또는 오후 출력
# 현재 시간은 오후 3시 () 분입니다.

now = datetime.datetime.now()
# 오전 구분
if now.hour < 12:
    print(f'현재 시간은 오전 {now.hour}시 {now.minute} 분입니다.')
# 오후
else:
    print(f'현재 시간은 오후 {now.hour-12}시 {now.minute} 분입니다.')

# 퀴즈 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 12월은 겨울입니다.

now = datetime.datetime.now()
# if + 비교 연산자
if 3 <= now.month <= 5:
    print(f'{now.month} 월은 봄입니다.')
elif 6 <= now.month <= 8:
    print(f'{now.month} 월은 여름입니다.')
elif 9 <= now.month <= 11:
    print(f'{now.month} 월은 가을입니다.')
else:
    print(f'{now.month} 월은 겨울입니다.')

# if + in 연산자
if now.month in (3, 4, 5):
    print(f'{now.month} 월은 봄입니다.')
elif now.month in (6, 7, 8):
    print(f'{now.month} 월은 여름입니다.')
elif now.month in (9, 10, 11):
    print(f'{now.month} 월은 가을입니다.')
else:
    print(f'{now.month} 월은 겨울입니다.')

# 요일 데이타
# 요일은 (월요일)0 ~ 6(일요일)
today = datetime.datetime.today().weekday()
print(today, type(today)) # 0 <class 'int'>
now = datetime.datetime.now()
if today == 0:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 월요일입니다.')
elif today == 1:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 화요일입니다.')
elif today == 2:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 수요일입니다.')
elif today == 3:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 목요일입니다.')
elif today == 4:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 금요일입니다.')
elif today == 5:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 토요일입니다.')
else:
    print(f'오늘은 {now.year}년 {now.month}월 {now.day} 일요일입니다.')

# 요일 리스트 이용
dayList = ['월', '화', '수', '목', '금', '토', '일']
today = datetime.datetime.today().weekday()
now = datetime.datetime.now()
print(f'오늘은 {now.year}년 {now.month}월 {now.day} {dayList[today]}요일입니다.')

# time 모듈 이용하기

# time 모듈 임포트
import time

# time.time()
# : 현재 시간을 실수 형태로 리턴한다.

# time.localtime(time.time())
# : time.time()의 값을 년도, 월, 일, 시, 분, 초로 변경
# : 튜플 자료 구조 형태

print(time.time()) # 1609749515.172064
print(time.localtime(time.time()))
# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=4, tm_hour=17, tm_min=38, tm_sec=35, tm_wday=0, tm_yday=4, tm_isdst=0)

temp = time.localtime(time.time())
print(type(temp)) # <class 'time.struct_time'>
# 리스트화
timeList = list(time.localtime(time.time()))
print(timeList, type(timeList))
dayList1 = ['년', '월', '일', '시', '분', '초']
dayList2 = ['월', '화', '수', '목', '금', '토', '일']

for i in range(len(dayList1)):
    print(timeList[i], dayList1[i], end=' ' )
print(dayList2[timeList[6]], '요일')


# 여러가지 출력 포맷 이용하기
# time.strftime('포맷코드1 포맷코드2', time.localtime(time.time()))
# 출력할 형식 포맷코드
# %a / %A  : 요일
# %b / %B  :  달
# %c : 날짜와 시간
# %d : 날(day)
# %H :24시간 기준의 시간
# %I :12시간 기준의 시간
# %j :1년중 누적 날짜 표시
# %x : 지역 기반 날짜 출력
# %X : 지역 기반 시간 출력
# %w : 숫자로된 요일 출력. 0은 일요일
# %Y : 년도 출력
# %Z : 시간대 출력
# %p : AM/PM

print('-'*30)
print(time.strftime('%x', time.localtime(time.time()))) # 01/04/21
print(time.strftime('%X', time.localtime(time.time()))) # 17:50:48
print(time.strftime('%c', time.localtime(time.time()))) # Mon Jan  4 17:50:48 2021
print(time.strftime('%a %A', time.localtime(time.time()))) # Mon Monday
print(time.strftime('%p %I', time.localtime(time.time()))) # PM 05
