# 오류?
# 오류의 종류
# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# IndexError :  튜플,리스트의 잘못된 인덱스 접근
# ZeroDivisionError : 0으로 나눈 경우
# FileNotFoundError : 잘못된 파일 경로
# ValueError => 잘못된 값
# TypeError => 잘못된 데이터형
# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외


# 튜플, 리스트 인덱스 접근시 발생 - IndexError
# IndexError: list index out of range
# IndexError: tuple index out of range

# myTuple = (1,)
# print(myTuple[3]) # IndexError: tuple index out of range
# myList = []
# print(myList[0])  # IndexError: list index out of range

# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# print(a) # NameError: name 'a' is not defined
# print(hello()) # NameError: name 'hello' is not defined

# ZeroDivisionError : 0으로 나눈 경우
# print(100/0) # ZeroDivisionError: division by zero

# FileNotFoundError : 잘못된 파일 경로
# import os
# os.remove('테스트.py')
# FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다: '테스트.py'


# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외
# print('abcde) # SyntaxError: EOL while scanning string literal


# ValueError : ValueError: invalid literal for int() with base 10: 'ghghghg'
# ans = int(input('숫자 입력 => '))

# TypeError: sequence item 0: expected str instance, int found
# myList = [100, 56, 77]
# print(' '.join(myList))


# try..except 명령
# try..except..else 명령
# try..except..else..finally 명령
# raise Exception : 사용자정의 에러
#  ex) 금칙어, 특별한 값 지정. 데이타 유효성

# ---------------------------------

# 에러처리 문법 1
# ## try..except 명령1
# - 에러코드를 알고있어야 한다.
# - e는 에러메세지
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# 0으로 나누면 에러발생 : ZeroDivisionError
# n = int(input('숫자 입력 => '))
# try:
#     print(100/n)
# except ZeroDivisionError as e:
#     print('에러 메세지 = ', e, '0으로 나눌수 없어요')
# print('에러 테스트 종료')

# ValueError : ValueError: invalid literal for int() with base 10: 'ghghghg'
# try:
#     ans = int(input('숫자 입력 => '))
# except ValueError as e:
#     print('에러 메세지 = ', e, '입력된 값이 숫자가 아닙니다.')
# print('에러 테스트 종료')

# try..except 명령2
# 모든 예외의 에러 코드를 출력할 때는 Exception 키워드
# 에러코드를 몰라도 된다. => Exception
# try:
#     명령
# except Exception as e:
#     print(e)

# try:
#     n = int(input('숫자 입력 => '))
#     print(100/n)
# except Exception as e:
#     print('에러 메세지 = ', e)
# print('에러 테스트 종료')


# ##  try..except 명령3
# try:
#   명령어
# except:
#   에러처리명령

# try:
#     # f = open('파일.txt', 'r', encoding='cp949')
#     f = open('data/Yesterday.txt', 'r', encoding='cp949')
#     print(f.readline())
# except:
#     print('파일이 없습니다.')
#
# print('에러 테스트 종료')

# ##  try..except..else 명령4
# try:
#   명령어
# except 에러코드 as e:
# except Exception as e:
# except:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

# try:
#     # f = open('파일.txt', 'r', encoding='cp949')
#     f = open('data/Yesterday.txt', 'r', encoding='cp949')
# except Exception as e:
#     print(e, ' => 파일이 없습니다.')
# else:
#     print(f.readline())


# ##  try..except..else..finally.. 명령5
# try:
#   명령어

# except 에러코드 as e:
# except Exception as e:
# except:

#   e 출력 ,에러처리명령

# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어
# x = 100
# try:
#     y = int(input('숫자 입력 => '))
#     result = x/y
# except Exception as e:
#     print('에러 메세지 = ', e)
# else:
#     print(f'{x} / {y} = {result}')
# finally:
#     print('에러 테스트 종료')


# 오류 회피
# 에러 무시 : pass 키워드 사용

# try:
#   명령어1
# except: / except Exception: / except 에러코드:
#   pass
# else:
#   명령어2
# finally:
#   명령어3
#
# myList = [1, 2, 3]
# try:
#     result = myList[100]
# except:
#     pass
# else:
#     print(result)
# finally:
#     print('테스트 종료')



# 여러개의 오류 처리하기
# 먼저 발생한 오류 우선: 뒤에 오류는 실행되지 않음
# 에러코드를 알고 있는 경우에 사용

# try:
#     명령실행 1
#     명령실행 2
#       ...
# except 오류코드1:
#     에러메세지 출력1
# except 오류코드2:
#     에러메세지 출력2
# finally:
#     테스트완료명령

# 먼저 발생한 오류 우선: 뒤에 오류는 실행되지 않음


# x = 100
# try:
#     y = int(input('숫자 입력 => '))
#     result = x/y
# except ZeroDivisionError as e:
#     print('에러 메세지 = ', e, '0으로 나눌수 없어요')
# except ValueError as e:
#     print('에러 메세지 = ', e, '숫자값만 입력하세요')
# else:
#     print(f'{x} / {y} = {result}')
# finally:
#     print('에러 테스트 종료')

# print(user1) # NameError

# 먼저 발생한 오류 우선: 뒤에 오류는 실행되지 않음
# try:
#     print(user1)
#     print(100/0)
# except NameError as e:
#     print(f' NameError => {e}')
# except ZeroDivisionError as e:
#     print(f' ZeroDivisionError => {e}')
# finally:
#     print('테스트 종료')


# 사용자정의 에러
#  raise 문 이용
# 일부러 에러 발생
# if 조건식:
#   raise Exception(오류 메세지)

# 입력값이 0이면 오류 발생
x = input('0이 아닌 문자를 입력하세요')
if x == '0':
    raise Exception('입력 에러 => 입력값이 0입니다. ')
else:
    print(f' x = {x}')
print('사용자정의 에러 테스트')

# try..except.. + raise Exception
# 사용자정의 에러에 대해서도 예외처리하기

# 입력값이 0이면 오류 발생
# try:
#     x = input('0이 아닌 문자를 입력하세요...')
#     if x == '0':
#         raise Exception('입력 에러 => 입력값이 0입니다. ')
# except Exception as e:
#     print(e)
# else:
#     print(f' x = {x}')
# print('사용자정의 에러 테스트 종료')



# data = input('데이타 입력 => ')
# if (data[0] == '-') and (data[1:].isdigit()):
#     # print(f'{data} => 음수')
#     raise Exception('입력 에러')



# 입력값이 음수이면 에러발생
# 음수는 - 와 나머지는 0이 아닌 숫자
# -0 은 0으로 출력
# try:
#     data = input('데이타 입력 => ')
#     if (data[0] == '-') and (data[1:].isdigit()) and (data[1] != '0' ):
#         raise Exception('입력 에러')
#     elif (data[0] == '-') and (data[1:] == '0'):
#         data = 0
# except Exception as e:
#     print(e)
# else:
#     print(f' x = {data}')
# print('사용자정의 에러 테스트 종료')


# try:
#     data1 = input('숫자1입력 ? .... ')
#     if (data1[0] == '-') and (data1[1:].isdigit()) and (data1[1] != '0' ):
#         data1 = int(data1[1:]) * -1
#     elif (data1[0] == '-') and (data1[1] == '0'):
#         data1 = 0
#     else:
#         data1 = int(data1)
#     data2 = input('숫자2입력 ? ....  ')
#     if (data2[0] == '-') and (data1[2:].isdigit()) and (data2[1] != '0' ):
#         data2 = int(data2[1:]) * -1
#     elif (data2[0] == '-') and (data2[1] == '0'):
#         data2 = 0
#     else:
#         data2 = int(data2)
# except Exception as e:
#     print(e)
# else:
#     print(f' {data1} + {data2} = {data1+data2}')
# print('사용자정의 에러 테스트 종료\n\n')


# 함수 활용
def check_digit(n):
    if (n == '-') and (n.isdigit()) and (n != '0' ):
        n = int(n[1:]) * -1
    elif (n[0] == '-') and (n[1] == '0'):
        n = 0
    else:
        n = int(n)
    return n

try:
    data1 = check_digit(input('숫자1입력 ? .... '))
    data2 = check_digit(input('숫자2입력 ? .... '))
except Exception as e:
    print(e)
else:
    print(f' {data1} + {data2} = {data1+data2}')
print('사용자정의 에러 테스트 종료')


