# 사용자정의 에러
# 에러코드 + 에러 메세지 등록
# Exception 클래스 상속받아서 에러코드 등록

# 1단계 : 사용자 에러코드 + 에러메세지 등록
# Exception 내장 클래스를 상속받아
# 임의의 에러명으로 클래스 생성
# class 에러명클래스(Exception):
#   def __str__(self):
#       return 에러메세지

# 에러 코드 + 에러 메세지 등록
# 에러코드클래스 등록
class MyError(Exception):
    # pass
    # 에러 메세지 메서드
    def __str__(self):
        return '에러 메세지 : MyError => 사용자정의 에러 발생 '

# 2단계
# 에러 발생시 에러코드 호출
# raise 에러코드클래스명()

# 입력값이 0이면 오류 발생
# x = input('0이 아닌 문자를 입력하세요...')
# if x == '0':
#     raise MyError()
# else:
#     print(f' x = {x}')
# print('사용자정의 에러 테스트')
# # __main__.MyError: 에러 메세지 : MyError => 사용자정의 에러 발생

# try ~ except 에러코드 as e 에 적용하기
# try:
#     x = input('0이 아닌 문자를 입력하세요...')
#     if x == '0':
#         raise MyError()
# except MyError as e:
#     print(e)
# else:
#     print(f' x = {x}')
# finally:
#     print('사용자 정의 에러 테스트 종료')


# 닉네임 금칙어 에러 코드 만들기
# 닉네임 금칙어 - ['바보', '히틀러', '무솔리니']

# 에러 코드 클래스 생성
class NicknameError(Exception):
    def __str__(self):
        return '닉네임 금칙어 에러 - 닉네임으로 사용할 수 없습니다.'

# 함수 정의
def check_nickname(nickname):
    stop_nickname_list = ['바보', '히틀러', '무솔리니']
    if nickname in stop_nickname_list:
        raise NicknameError()
    else:
        return f' {nickname} 승인 완료'

# 함수 호출
# nickname = input('닉네임 입력 => ')
# print(check_nickname(nickname))

# try .. except ...
try:
    print(check_nickname('스머프'))
    print(check_nickname('무솔리니'))
except NicknameError as e:
    print(e)

