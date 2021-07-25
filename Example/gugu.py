
# 특정 숫자에 대한 구구단 출력 함수 정의
def gugu():
    print('gugu.py 안의 gugu 함수 호출 ')
    n = int(input('숫자 입력 => '))
    for i in range(1,10):
        print(f'{n} * {i} = {n*i}')