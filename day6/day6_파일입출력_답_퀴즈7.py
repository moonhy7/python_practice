# 퀴즈7 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
** 퀴즈7 **

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요송아지
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요사과
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요자두
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 2 입니다.
사과

자두



메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   3

[파일 내용 모두 삭제]
단어 목록을 모두 삭제하였습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 0 입니다.


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   4


프로그램을 종료합니다.
'''


def continueAddWord():
    while True:
        ans = input('\n단어를 계속 추가하시겠습니까? (y/n)... ').strip()
        if ans == 'n':
            break
            start()
            break
        elif ans == 'y':
            addWord()
            break
        else:
            print('잘못된 입력입니다. y나 n을 입력하셔야 합니다\n')



def addWord():
    print('\n[단어 추가]')
    with open('data/wordResult.txt', 'a', encoding='utf-8') as f:
        while True :
            word = input('두 글자로 구성된 단어를 입력하세요...').strip()
            if len(word) == 2:
                f.write(word+'\n')
                print('단어가 추가 되었습니다.\n')
                continueAddWord()
                break
            else:
                print('두글자가 아닙니다.\n')

def readWord():
    print('\n[단어 모두 출력]')
    with open('data/wordResult.txt', 'r', encoding='utf-8') as f:
        dataList = f.readlines()
        print(f'\n추가된 단어는 총 {len(dataList)} 개 입니다.')
        for i in dataList:
            print(i, end='')
        print('\n')

def clearWord():
    print('\n[파일 내용 모두 삭제]')
    with open('data/wordResult.txt', 'w', encoding='utf-8') as f:
        f.write('')
        print(f'단어 목록을 모두 삭제하였습니다.\n')


def start():
    while True:
        ans = input('\n메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...')
        if ans == '1':
            addWord()
        elif ans == '2':
            readWord()
        elif ans == '3':
            clearWord()
        elif ans == '4':
            print('\n프로그램을 종료합니다.')
            break


print('-' * 30)
start()

        
