# 1. a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과
# 마지막 번째 튜플값을 출력하세요.


myTuple = ('a', 'b', 'c', 'd', 'e')
print('myTuple = {0}'.format(myTuple))
print('myTuple[0] = {0}, myTuple[-1] = {1}'.format(myTuple[0], myTuple[-1]))


# 2. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

fruits = ["Banana", "Apple", "Orange"]
print(f'fruits = {fruits}')
fruits.remove("Apple")
# fruits.pop(1)
print(f'fruits = {fruits}')


# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding0' 데이터를 첫번째에 추가하고,
#    다시 튜플 데이터로 변환하세요.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
print(f'tupledata = {tupledata}')
temp = list(tupledata)
temp.insert(0, 'fun-coding0' )
print(f'temp = {temp}')
tupledata = tuple(temp)
print(f'tupledata = {tupledata}')



# 4. 다음 항목을 딕셔너리(dict)으로 선언해보세요.
# : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
fare = {'성인':100000 , '청소년':70000 , '아동':30000}
print(f'fare = {fare}')

# 5. 4번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
fare['소아'] = 0
print(f'fare = {fare}')


# 6. 5번의 딕셔너리(dict)에서 Key 항목만 리스트로 저장하여 정렬한 후 튜플로 변경하여라.
#  결과 => ('성인', '소아', '아동', '청소년')
temp = list(fare.keys())
print(temp)
temp.sort()
print(temp)
print('결과 => ' , tuple(temp))



# 7. number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
#  number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
print('-'*20)
print(number_list)
print(list(set(number_list)))


# 8. 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '월E', '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
result = list(set1 & set2)
print('-'*20)
print(result)

# 9. 8의 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
#  아이템1 / 아이템2 / ....
print('-'*20)
print( ' / '.join(result))

# 10. 빈 집합을 생성하고 값을 입력받아 집합의 원소를 삽입하여라.
# 집합 원소의 갯수는 5개로 한다.
'''
 mySet = set() <class 'set'>
첫번째 아이템 값 => 갈비탕 
두번째 아이템 값 => 소머리국밥
세번째 아이템 값 => 삼계탕
네번째 아이템 값 => 순두부
다섯번째 아이템 값 => 김치찌게
 mySet = {'김치찌게', '소머리국밥', '갈비탕 ', '순두부', '삼계탕'} <class 'set'>
'''
mySet = set([])
print('-'*20)
print( ' mySet ', mySet, type(mySet))
mySet.add(input('첫번째 아이템 값 => '))
mySet.add(input('두번째 아이템 값 => '))
mySet.add(input('세번째 아이템 값 => '))
mySet.add(input('네번째 아이템 값 => '))
mySet.add(input('다섯번째 아이템 값 => '))
print( ' mySet = ', mySet, type(mySet))

# 11. 10의 집합을 다음과 같은 딕셔너리 구조로 변환하여라.
#  mydict =  {0: '소머리국밥', 1: '갈비탕', 2: '순두부', 3: '김치찌게', 4: '삼계탕'}
#  <class 'dict'>

mydict = dict(enumerate(mySet))
print('-'*20)
print( ' mydict = ', mydict, type(mydict))