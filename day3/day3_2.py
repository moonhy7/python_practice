# 반복문 : while
# while 조건:
#      실행명령
# 조건이 True 이면 명령을 실행해라.
# 조건을 False로 만드는 명령이 필요하다

# 특정 메세지를 5번만 출력하여라
txt = 'Hello world'
count = 1
while count<=5:
    print(count, txt)
    count += 1
print('='*50)


# 10, 9, 8 ... 1 까지 출력하여라
cnt = 10
while cnt > 0:
    print(cnt, end=' ')
    cnt -= 1 # cnt = cnt - 1
print()
print('-'*50)

# 1~100까지의 합 출력하기
# 1 + 2+ 3+ ... + 100
cnt = 1
total = 0
while cnt<= 100:
    # print(cnt)
    total += cnt
    cnt += 1
print(f'1~100까지의 합 = {total}')
print('-'*50)

# 별찍기 1
cnt = 1
while cnt<=5:
    print(cnt, '*'*10)
    cnt += 1
print('-'*50)

'''
*
**
***
****
*****
'''
# 별찍기 2
cnt = 1
while cnt<=5:
    print(cnt, '*'*cnt)
    cnt += 1
print('-'*50)

# 퀴즈 - 별찍기 3
'''
*****
****
***
**
*
'''
cnt = 5
while cnt>0:
    print(cnt, '*'*cnt)
    cnt -= 1
print('-'*50)

# 반복문 + 조건문
# 1~50까지 짝수만 출력하기
cnt = 1
while cnt<=50:
    if cnt%2 == 0:
        print(cnt, end=' ')
    cnt += 1
print()
print('-'*50)

# 1~100 사이의 숫자중에서 3이나 5의 배수를 출력하여라
# n = 16
# print((n % 3 == 0) or (n % 5 == 0))
cnt = 1
while cnt<=100:
    if (cnt % 3 == 0) or (cnt % 5 == 0):
        print(cnt, end=' ')
    cnt += 1
print()
print('-'*50)

# 입력받은 숫자로 구구단 출력하기
'''
3 X 1 = 3
3 X 2 = 6
...
3 X 9 = 27
'''
# n = int(input('출력할 구구단의 숫자를 입력하세요...'))
# cnt = 1
# while cnt<10:
#     print(f'{n} X {cnt} = {n*cnt}')
#     cnt += 1
# print('-'*50)

# while문과 집합형 자료(리스트, 튜플)+문자
# while 문 이용해서 리스트 요소 출력하기
fruit = ['사과', '바나나', '수박', '포도']
print('첫번째 리스트값은? ', fruit[0])
print('리스트 전체 갯수는? ', len(fruit))
cnt = 0
while cnt<len(fruit):
    print(cnt, fruit[cnt])
    cnt += 1
print('-'*50)

# 짝수번째 글자만 출력하기
txt1 = '가나다라마바사'
print(txt1)
print(txt1[1::2])
cnt = 0
while cnt<len(txt1):
    if cnt%2 != 0:
        print(cnt, txt1[cnt])
    cnt += 1
print('-'*50)

# 가장 큰 수를 삭제하여라
# 리스트명.remove(값)
myNumList = [100, 200, 50, -30, 999, 10]
max_num =  myNumList[0]
cnt = 0
while cnt<len(myNumList):
    if myNumList[cnt] > max_num:
        max_num = myNumList[cnt]
    # print(myNumList[cnt])
    cnt += 1
print('-'*50)
print(myNumList)
print(f'최대값은? {max_num}')
myNumList.remove(max_num)
print(myNumList)

# 다중 while 문
# while 조건1:
#   while 조건2:
#       명령문2
#   명령문1

# 점선 출력후 문단 3번찍기 반복하기
cnt1 = 1
# cnt2 = 1
while cnt1<=3:
    print(cnt1, '-'*50)
    cnt2 = 1
    while cnt2<=3:
        print('\t\t', cnt2, 'Hello world')
        cnt2 += 1

    cnt1 += 1

print('다중 while문 테스트 종료 ')

# break
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용

# 입력값으로 리스트에 추가하기
# n 입력시 종료
# myList = []
# while True:
#     ans = input('데이타 종료를 원하시면 n을 입력하세요...')
#     if ans == 'n':
#         # while 문 탈출
#         break
#     item = input('데이타 => ')
#     myList.append(item)
#     # print(myList)
# print('테스트 종료')
# print(myList)


# continue
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 1~10사이의 숫자 출력 (7은 제외)
cnt = 0
while cnt<=9:
    cnt += 1
    if cnt == 7:
        # 아래의 명령은 실행되지 않는다.
        continue
    print(cnt)

print('테스트 종료')


# 퀴즈 : 1~30까지 숫자중에서 3의 배수만 제외하고 출력하여라.
# continue 문과 if 조건, while문 이용
cnt = 0
while cnt < 30:
    cnt += 1
    if cnt%3 == 0:
        continue
    print(cnt, end=' ')
print('\ncontinue Test 종료')

# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

# list( range(start, end , step) )
# : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) )
# : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) )
# : 순차적으로 숫자로 구성된 집합

# 1 ~ 10 으로 구성된 리스트/튜플/집합 을 생성하여라
# myList = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
# range(start, end , step) : start ~ end-1 까지의 숫자를 생성하는 객체
print(range(1, 11)) # range(1, 11)
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(range(1, 11))) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(set(range(1, 11))) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 1~50사이의 홀수만 리스트로 생성
result = list(range(1, 51, 2))
print(result, len(result))
# 10~1로 구성된  리스트로 생성
result = list(range(10, 0, -1))
print(result)

# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문
# 다른 언어들 => for(초기값; 조건식; 증감치) {}

# 1~10까지 출력하기
for i in range(1,11):
    print(i, end=' ')
print('\n 테스트 종료1')

cnt = 1
while cnt<=10:
    print(cnt, end=' ')
    cnt += 1
print('\n 테스트 종료2')

# 1~10까지 홀수만 출력하기
for i in range(1,11,2):
    print(i, end=' ')
print('\n 홀수만 찍기 테스트 종료')


# 1~100사이의 합 구하기
total = 0
for i in range(1,101):
    # print(i, end=' ')
    total += i
print(f'1~100 까지의 합은? {total} ')
print('\n 1~100사이의 합 구하기 테스트 종료')

# for 문에서 조건문 실행
# 1~25 까지 한줄에  5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''
for i in range(1,26):
    print(i, end=' ')
    if i%5 == 0:
        print()
print('\n 1~25 까지 한줄에  5개씩 출력하기 테스트 종료')

# 1~27 에서 5의 배수만 빼고 출력하기
# for + if + continue
for i in range(1,28):
    if i%5 == 0:
        continue
    print(i, end=' ')
print('\n 1~27 에서 5의 배수만 빼고 출력하기 테스트 종료')

# 다중 for 문
# while 문 이중 반복문 예
# cnt1 = 1
# while cnt1<=3:
#     print(cnt1, '-'*50)
#     cnt2 = 1
#     while cnt2<=3:
#         print('\t\t', cnt2, 'Hello world')
#         cnt2 += 1
#     cnt1 += 1

# 다중 for 문  예
for i in range(1,4):
    print(i, '-' * 50)
    for j in range(1,4):
        print('\t\t', j, 'Hello world')
print('다중 for 문 테스트 종료 ')


# 입력받은 숫자에 해당하는 구구단 출력
# n = int(input('구구단 n 입력 => '))
# print(f'{n} 단 출력')
# for i in range(1,10):
#     print(f'{n} X {i} = {n*i}')
# print('입력받은 숫자에 해당하는 구구단 출력 테스트 종료 ')

# 퀴즈 : 다중 for 문을 이용하여 구구단 출력
#  아래의 while 반복문을 for 문을 이용하여 수정하여라.
# cnt1 = 2
# while cnt1<=9:
#     print(f' { cnt1 } 단')
#
#     cnt2 = 1
#     while cnt2<=9:
#         print(f' {cnt1} X {cnt2} = {cnt1*cnt2}')
#         cnt2 += 1
#
#     print('-'*20)
#     cnt1 += 1


for i in range(2,10):
    print(f' {i} 단')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
    print('-'*20)

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

# 1~10 으로 구성된 리스트를 생성하여라 1
# 빈리스트를 만들고  for 문을 이용해서 생성된 숫자를 리스트 삽입한다.
numList1 = []
for i in range(1,11):
    numList1.append(i)
print(f' numList1 ={numList1}')

# 리스트 for문을 이용하여 1~10 으로 구성된 리스트를 생성하여라 2
# 리스트변수 = [ 결과값 for 명령문 ]
numList2 = [i for i in range(1,11)]
print(f' numList2 ={numList2}')

# 3단의 결과값으로 리스트를 만들어라
result1 = []
n = 3
for i in range(1,10):
    result1.append(n*i)
print(f' result1 ={result1}')

# 리스트 for 이용
# 리스트변수 = [ 결과값 for 명령문 ]
n = 3
result2 = [n*i for i in range(1,10)]
print(f' result2 ={result2}')

# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라
result1 = []
n = 3
for i in range(1,10):
    result1.append(n*i-1)
print(f' result1 ={result1}')

# 리스트 for 이용
# 리스트변수 = [ 결과값 for 명령문 ]
n = 3
result2 = [n*i-1 for i in range(1,10)]
print(f' result2 ={result2}')

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']
print('-'*50)
result1 = []
for i in range(1,11):
    result1.append('*'*i)
print(f' result1 ={result1}')

# 리스트 for 이용
# 리스트변수 = [ 결과값 for 명령문 ]
result2 = [ '*'*i for i in range(1,11) ]
print(f' result2 ={result2}')


# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 리스트변수 = [ 결과값 for 명령문1 for 명령문2 ]

# 구구단의 결과값으로 리스트를 생성하여라.
result_gugu1 = []
for i in range(2,10):
    for j in range(1,10):
        result_gugu1.append(i*j)
print(f' result_gugu1 ={result_gugu1}')

# 리스트 다중 for를 이용한 리스트 생성
# 리스트변수 = [ 결과값 for 명령문1 for 명령문2 ]
result_gugu2 = [i*j for i in range(2,10) for j in range(1,10)]
print(f' result_gugu2 ={result_gugu2}')

# 리스트 for 문 + 조건문
# 리스트변수 = [ 결과값 for 명령문 if 조건식 ]
# 1~30 사이의 숫자중에서 5의 배수를 제외하고 리스트를 생성하여라
print('-'*50)
result1 = []
for i in range(1,31):
    if i%5 != 0:
        result1.append(i)
print(f' result1 ={result1}')

# if문이 적용된 리스트 for를 이용한 리스트 생성
result2 = [i for i in range(1,31) if i%5 != 0 ]
print(f' result2 ={result2}')

# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

# 리스트를 생성하고 아이템을 출력하여라
myList = ['구로동', '신림동', '서초동', '역삼동']
for item in myList:
    print(item)

# 문자열을 세로로 출력하여라
txt = '도레미파솔라시도'
for item in txt:
    print(item)

# 튜플 아이템을 출력하여라
myTuple = (10, 600, -90, 500)
for item in myTuple:
    print(f' ====> {item}')

# 퀴즈 - 아래의 튜플 리스트의 모든 합을 구하여라
# for item in ... 이용
myTuple = (10, 600, -90, 500)
sum = 0
for item in myTuple:
    sum += item
print(f' {myTuple} 의 총합은?  {sum}')
# (10, 600, -90, 500) 의 총합은?  1020


# for 를 이용한 딕셔너리 요소 출력
# for 키변수(key) in 딕셔너리:
#   명령문
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}
print(myDict[100]) # '백'

for key in myDict:
    print(f'{key} 의 값은? {myDict[key]} ')


# 2차원 리스트와 for
# 조건 : 2차원 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문

list2d = [[1, 2], ['a', 'b'], ['홍길동', '춘향이']]
print(list2d[0]) # [1, 2]
print(list2d[2][0])  # '홍길동'
for (i, j) in list2d:
    print(f' i => {i} , j => {j}')

'''
 i => 1 , j => 2
 i => a , j => b
 i => 홍길동 , j => 춘향이

'''

# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균
김태희     30   40   100   ?     ?
...

'''

stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

# 2차원 리스트 출력하기
print('-'*50)
print('학생이름  국어  영어  수학   합계   평균')
print('-'*50)
for (stName, kor, eng, math) in stGradeList:
    tot = kor+eng+math
    avg = tot/3
    print(f'{stName}    {kor}   {eng}   {math}     {tot}  {avg:.2f}')
print('-'*50)

# 위의 stGradeList 에서 평균이 70점 이상의 학생의 데이타만 출력하여라
print('-'*50)
print('학생이름  국어  영어  수학   합계   평균')
print('-'*50)
for (stName, kor, eng, math) in stGradeList:
    tot = kor+eng+math
    avg = tot/3
    if avg >= 70:
        print(f'{stName}    {kor}   {eng}   {math}     {tot}  {avg:.2f}')
print('-'*50)

# 위의 stGradeList 에서 김 으로 시작하는 학생의 데이타만 출력하여라
print('-'*50)
print('학생이름  국어  영어  수학   합계   평균')
print('-'*50)
for (stName, kor, eng, math) in stGradeList:
    tot = kor+eng+math
    avg = tot/3
    # if stName[0] == '김':
    if stName[-1] == '희':
        print(f'{stName}    {kor}   {eng}   {math}     {tot}  {avg:.2f}')
print('-'*50)