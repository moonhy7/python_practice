# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949') as 파일변수:
#   명령문
import  os
print('='*50)
print(os.getcwd()) # C:\pyclass

# 특정 파일에서 3줄만 출력하기
with open('data/national_anthem.txt', 'r', encoding='cp949') as f:
    data_list = f.readlines()
    for row in data_list[:3]:
        print(row)

# 10~1 까지 특정파일에 쓰기
print('='*50)
with open('data/sample_100.txt', 'w', encoding='utf-8') as f:
    for i in range(10, 0, -1):
        f.write(str(i)+'\n')

# 특정파일에 내용 추가하기
# 구구단
print('='*50)
with open('data/sample_100.txt', 'a', encoding='utf-8') as f:
    f.write('\n\t\t구구단 출력하기')
    for i in range(2, 10):
        f.write(f'\n\t{i}단 \n')
        for j in range(1,10):
            f.write(f'{i} X {j} = {i*j} \n')
        f.write('\n')
        f.write('-'*50)
