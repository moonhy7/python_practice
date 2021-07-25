# 퀴즈 1
# 입력받은 수식에 관련된 결과계산값을 출력한다.
# eval() 이용
'''
result = input('계산식을 입력하세요?.... ')

3+4*20-100

결과 >>
3+4*20-100 = ?

'''

# result = input('계산식을 입력하세요?.... ')
# print('결과 >>')
# print(result, ' = ', eval(result))


# 퀴즈 2
# 7개의 입력받은 숫자 값을 리스트로 저장한 후
# 최대값과 최소값을 출력한다. (min, max 함수 이용)
# 입력값은 양의 정수로 제한한다.
'''
숫자 1? .... 56
숫자 2? .... 34
숫자 3? .... 100
숫자 4? .... 23
숫자 5? .... 78
숫자 6? .... 90
숫자 7? .... 3
입력 리스트 :  ['56', '34', '100', '23', '78', '90', '3']
최소값 :  100
최대값 :  90
'''

# numList = []
# for i in range(1,8):
#     num = int(input('숫자 ' + str(i) + '? .... '))
#     numList.append(num)
#
# print('입력 리스트 : ', numList)
# print('최소값 : ', min(numList))
# print('최대값 : ', max(numList))


# # 퀴즈3
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# 두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
'''
aList = [78,90,80,50]
bList = [8,100,34,60]

최소값 : 8
최대값 : 100
'''

# print('\n\n')
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# a_b_list = aList + bList
# print('최소값 : ', min(a_b_list))
# print('최대값 : ', max(a_b_list))
#



# 퀴즈 4
# enumerate(리스트/튜플, 초기값인덱스 )
# enumerate() 함수를 이용하여 아래 리스트를
# 시작 인덱스가 1이 되게 자료 구조를 생성하고
# 아래 형태로 출력한다.
'''
foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']

1 번째 메뉴: 감자탕
2 번째 메뉴: 떡국
3 번째 메뉴: 모밀냉면
4 번째 메뉴: 연어덮밥
5 번째 메뉴: 케이준 샐러드

'''

# foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']
# foodListTuple= enumerate(foodList, 1)
# for i, v in foodListTuple:
#     # print('{} 번째 메뉴: {}'.format(i,v))
#     print(f'{i} 번째 메뉴: {v}')
#
# foodListTuple= enumerate(foodList, 1)
# print(foodListTuple)
# print(list(foodListTuple))
#
# food_dict = dict(enumerate(foodList, 1))
# print(food_dict)

# 퀴즈 5
# 아래는 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍이다.
# 이때 딕셔너리 키는 'user숫자' 형태이다.
# map 함수를 이용한 구조로 변경하여라

# 리스트 => 딕셔너리 리스트로 변경 코드 
valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']

def makeDict(valueList):
    result = []
    for i in range(0, len(valueList)):
        temp = {}
        temp['user'+str(i+1)] = valueList[i]
        result.append(temp)
    return result

print(f'\n 결과 >> \n valueList = {valueList}')
print((f' \n 딕셔너리 리스트 구조로 변경 => \n {makeDict(valueList)}'))


'''
 결과 >>
 valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']
 
 딕셔너리 리스트 구조로 변경 => 
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

'''
 map함수 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''



def makeDict2(numKey, value):
    # result = {'user' + str(numKey): value}
    # return result
    return {'user' + str(numKey): value}

# print(makeDict2(100, '홍길동'))

valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']
keyList = list(range(1,len(valueList)+1))
print(keyList) # [1, 2, 3, 4, 5]

print(f'\n map함수 이용 결과 >> \n valuelist = {valueList}')
print(list(map(makeDict2, keyList, valueList)))



# 퀴즈 6
# 퀴즈5의 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍을
# map 함수안에 lambda 함수를 이용한 구조로 변경하여라

'''
 map함수와 lambda 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

f_make = lambda numKey, value: {'user' + str(numKey): value}
print(f_make(100, '은지원')) # {'user100': '은지원'}

valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']
keyList = list(range(1,len(valueList)+1))

print('\n map함수와 lambda 이용 결과 >> ')
print(list(map(f_make, keyList, valueList)))
print(list(map(lambda numKey, value:{'user' + str(numKey): value}, list(range(1,len(valueList)+1)), valueList)))


#  퀴즈7
# 아래의 2개의 리스트를 튜플 리스트(리스트안에 튜플 구조)로 zip() 함수를 이용하여 변경하여라
# mKind = ['발라드', '댄스', '클래식', 'OST']
# mTitle = ['거리에서', 'DNA', '소녀의 기도', '썸머']

'''
첫번째 리스트 = ['발라드', '댄스', '클래식', 'OST']
두번째 리스트 = ['거리에서', 'DNA', '소녀의 기도', '썸머']
튜플 리스트로 변경 
 [('발라드', '거리에서'), ('댄스', 'DNA'), ('클래식', '소녀의 기도'), ('OST', '썸머')]
 <class 'list'>

('발라드', '거리에서') <class 'tuple'>
('댄스', 'DNA') <class 'tuple'>
('클래식', '소녀의 기도') <class 'tuple'>
('OST', '썸머') <class 'tuple'>
'''

mKind = ['발라드', '댄스', '클래식', 'OST']
mTitle = ['거리에서', 'DNA', '소녀의 기도', '썸머']

print(f'\n\n첫번째 리스트 = {mKind}')
print(f'두번째 리스트 = {mTitle}')
result = list(zip(mKind, mTitle))
print(f'튜플 리스트로 변경 \n {result}\n {type(result)}\n')
for i in result:
    print(i,  type(i))

# 퀴즈 8
# time , datetime 모듈을 사용해서
# 1초에 한 번 현재 시간을 출력하는 코드를 작성하여라.
# 특정 시간마다 명령 실행은 time.sleep(초) 을 이용한다.
'''
결과 >> 
2021-01-04 20:00:15.259904
2021-01-04 20:00:16.260260
2021-01-04 20:00:17.260587
2021-01-04 20:00:18.260911
...
'''
# import time
# import datetime

# import time, datetime
#
# while True:
#     # 현재 시간 구한 후 변수로 저장
#     now = datetime.datetime.now()
#     print(now)
#     # time.sleep(초)
#     time.sleep(1)



# 퀴즈 9
# 아래는 5~10까지의 곱을 구하는 프로그래밍이다.
# lambda 함수, reduce()를 이용한 구조로 변경하여라
# reduce() 함수 임포트 명령어는?
# import functools as f

print('-'*20)
numList = list(range(5,11))
print(f'\n\nnumList = {numList}')

# 모든 리스트의 곱을 구하는 함수
def fact_f1(numList):
    result = 1
    txtList = []
    for i in numList:
        result *= i # 1*5*6..10
        txtList.append(str(i))
    return txtList, result

print(f'\n \n 함수 결과 => {fact_f1(numList)}')
#  함수 결과 => (['5', '6', '7', '8', '9', '10'], 151200)
print(f'\n \n numList = {numList}')
print(f'\n \n txtList = {fact_f1(numList)[0]}')
print(f' 5~10까지의 곱 >> \n {" * ".join(fact_f1(numList)[0])} = {fact_f1(numList)[1]}\n\n')
# 5 * 6 * 7 * 8 * 9 * 10 = 151200



'''
 numList = [5, 6, 7, 8, 9, 10]
 5~10까지의 곱 >> 
 5 * 6 * 7 * 8 * 9 * 10 = 151200
'''
'''
lambda 함수, reduce() 이용 >> 5~10까지의 곱 >> 
 numList = [5, 6, 7, 8, 9, 10]
5 X 6 X 7 X 8 X 9 X 10  =  151200
'''

print(f'\n\n lambda 함수, reduce() 이용 >> 5~10까지의 곱 >> ')
numList = list(range(5,11))
print(f' numList = {numList}')

import functools as f
print(" X ".join([str(i) for i in numList ]) , ' = ', f.reduce(lambda x,y:x*y , numList))


# 퀴즈 10
# 아래는 문자열 변수를 정의하고 숫자와 글자를 제외한 나머지 글자를 리스트로 변경하는 프로그래밍이다.
# filter() 함수를 이용한 구조로 변경하여라

# 숫자와 글자를 제외한 나머지 글자의 리스트화 
myString = 'a4+5b6&word*bn%~564^3'
def filterList(txt):
    result = []
    # and, or, not
    for i in range(len(txt)):
       #  숫자나 알파벳(한글포함)이 아니라면 리스트의 데이타로 추가
       if not (txt[i].isdigit() or txt[i].isalpha()) :
           result.append(txt[i])
    return result

print('-'*20)
print(f'\n\n myString = {myString}')
print(f' 숫자와 글자 제외 결과 리스트 = {filterList(myString)}')
print(f' 총 갯수 = {len(filterList(myString))}')


'''
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 = ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''

'''
 filter() 함수 활용 >> 
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 =  ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6

 filter()와 lambda 함수 활용 >> 
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 =  ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''

print('-'*20)
myString = 'a4+5b6&word*bn%~564^3'
print(f'\n filter() 함수 활용 >> \n myString = {myString}')
def filtering_f(c):
    if not (c.isdigit() or c.isalpha()):
       return True

# print(filtering_f('a')) # None
# print(filtering_f('&')) # True
print(' '.join(myString))
# 공백을 기준으로 문자열 => 리스트
print(' '.join(myString).split())
print(' 숫자와 글자 제외 결과 리스트 = ', list(filter(filtering_f, ' '.join(myString).split())))
print(f' 총 갯수 = {len(list(filter(filtering_f, " ".join(myString).split())))}')
#
#
print(f'\n filter()와 lambda 함수 활용 >> \n myString = {myString}')
# f = lambda x : not(x.isdigit()) and not(x.isalpha())
# # print(f('100'))
# # print(f('a'))
# # print(f('@'))
# '''
# False
# False
# True
# '''
# # ' '. join(myString).split()
#
# # lambda로 변경
print(' 숫자와 글자 제외 결과 리스트 = ', list(filter(lambda x : not(x.isdigit()) and not(x.isalpha()), ' '. join(myString).split() )))
print(f' 총 갯수 = {len(list(filter(lambda x : not(x.isdigit()) and not(x.isalpha()), " ". join(myString).split() )))}')