# 퀴즈 1: FileNotFoundError
#  data/test.txt 가 없다면
#  에러메세지(e)와 함께 '파일이 없습니다.' 메세지 출력
#  있다면 파일의 내용을 출력한다.

# try:
#     f = open('data/result.txt', 'r', encoding='cp949')
#     # f = open('data/없는파일.txt', 'r')
#     print(f.readline())
#     f.close()
# except FileNotFoundError as e:
#     print(f'파일이 없습니다. \n\t\t {e}')


# 퀴즈 2: ValueError
# 2개의 숫자글자를 입력받아서 더한다.
# 입력된 글자가 숫자가 아니라면 에러 메세지 출력
# 입력된 글자가 숫자라면  더한후 출력한다.

# try:
#   n1 = int(input('숫자1입력 ? .... '))
#   n2 = int(input('숫자2입력 ? .... '))
# # except ValueError as e:
# except Exception as e:
#   # print('입력 데이터가 숫자가 아닙니다.\n\t\t %s' %e)
#   print(f'입력 데이터가 숫자가 아닙니다.\n\t\t {e}')
# else:
#     print(f'{n1} + {n2} = {n1+n2}')



# 퀴즈 3 : ValueError, ZeroDivisionError
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?

# def plusNum():
#     try:
#         num1 = int(input('첫번째 값을 입력하세요...'))
#         num2 = int(input('두번째 값을 입력하세요...'))
#         result = num1/num2
#
#     except ZeroDivisionError as e:
#         print(f'ZeroDivisionError 데이타 오류 ... - {e}')
#     except ValueError as e:
#         print(f'ValueError 데이타 오류 ... - {e}')
#
#     else:
#         print(f'{num1} / {num2} = {result}')
#
# plusNum()



# 퀴즈 4
# data_eng.txt 파일을 파일 변수로 저장한다.
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.

def total_sum(url, op):
    try:
        sum=0
        i=0
        with open(url,'r',encoding=op) as f:
            data_list = f.readlines()
            for item in data_list:
                sum+=int(item)
                i+=1
            print(f'sum={sum}')
            print(f'avg={sum/len(data_list)}')

    except:
        print('파일 없음')

print('-'*50)

# total_sum('data/data_eng.txt', 'cp949')
# total_sum('data_eng.txt', 'cp949')



# 퀴즈 5
# 함수의 매개변수값에 따라 다음과 같은 메세지를 출력한다.
# 0과 같거나 0보다 작다
# 0보다 크다
# 매개변수값이 숫자가 아닌경우에는 오류를 무시하도록
# try...except 문을 작성하여라

def numCompare(x):
    try:
        if (x[0] == '-') and x[1:].isdigit():
            x = int(x[1:])*-1
        else:
            x = int(x)

        if x <= 0:
            print(f'매개변수는 0과 같거나 0보다 작다.')
        else:
            print(f'0보다 크다.')
    except Exception:
        pass

# x = input('값을 입력하세요... ')
# numCompare(x)



# 퀴즈6
# 학생의 학년을 저장하는 변수 classYear값은
# 1학년, 2학년, 3학년, 4학년 이어야한다.
# 나머지 값은  raise Exception 을
# 이용하여 오류를 발생시켜라

# def classYear():
#     classYear = int(input('classYear = '))
#     if 1<=classYear<=4:
#         print(f'{classYear}학년 입니다.')
#     else:
#         raise Exception('학년 정보가 올바르지 않습니다.\n 올바른 값은 1학년~4학년 입니다.')
#
# classYear()

def classYear():
    classYear=['1학년','2학년','3학년','4학년']
    ans = input('학년을 입력하시요...(1~4학년)')
    if ans not in (classYear):
        raise Exception('해당학년은 존재하지 않습니다')
    else:
        print(ans)
classYear()