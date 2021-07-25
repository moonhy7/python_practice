# 파일 입출력 관련 퀴즈
# 퀴즈7 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료
'''

# 단어 추가 함수
def addWord():
    print('\n[단어 추가]')
    with open('data/word.txt', 'a', encoding='utf-8') as f:
        word = input('두 글자로 구성된 단어를 입력하세요...').strip()
        if len(word) == 2:
            f.write(word+'\n')
            print('단어가 추가 되었습니다.\n')
            ans = input('단어를 계속 추가하시겠습니까? (추가시 y)...').strip()
            if ans == 'y': addWord()
        else:
            print('두 글자가 아닙니다.\n')

def readWord():
    print('\n[단어 모두 출력]')
    with open('data/word.txt', 'r', encoding='utf-8') as f:
        word_list = f.readlines()
        print(f'추가된 단어는  총 {len(word_list)}개 입니다.')
        for word in word_list:
            print(word)

def deleteWord() :
    print('\n[단어 모두 삭제]')
    with open('data/word.txt', 'w', encoding='utf-8') as f:
        print('단어 목록을 모두 삭제하였습니다.')


# 메인 메뉴 표시 함수 정의
def start():
    while True:
        ans = input('\n\n메뉴 번호를 입력하세요.  \n1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...')
        if ans == '1':
            addWord()
        elif ans == '2':
            readWord()
        elif ans == '3':
            deleteWord()
        elif ans == '4':
            print('프로그램을 종료합니다.')
            break
        else:
            print('올바른 입력 번호가 아닙니다.')


# 단어장 함수 호출
start()