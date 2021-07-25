
# 1 ~ 10 출력하는 함수 정의
def print_10():
    print('sample1.py 안의 print_10 함수 호출 ')
    for i in range(1,11):
        print(i)

# print_10()

# 1~100까지 구하는 함수 정의
def sum_100():
    print('sample1.py 안의 sum_100 함수 호출 ')
    result = 0
    for i in range(1, 101):
        result += i
    return f'1~100까지의 합은? {result}'

# print(sum_100())