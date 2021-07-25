# 정규표현식 (Regular Expression)
# 유효성 검사
# 문자열에서 특정 조건(패턴)에 맞는 문자열 찾기
# 회원가입시 주민등록번호 형식이 맞는가?
# ???... - ????...
# 핸드폰번호 형식이 맞는가?
# 01(0|1|7|9)-????-????
# 회원가입시 비밀번호 설정 형식이 맞는가?
# 자릿수
# 특수문자 + 숫자 + 영문대문자 + 영문소문자

# 파이썬에서 정규표현식 모듈 => re (내장모듈)
import re

# re 객체의 속성과 메소드 확인
print(dir(re))
for i in dir(re):
    print(i)

# 정규표현식 패턴1 - 대문자, 소문자, 숫자, 한글
# [문자클래스스타일]  => 한글씩
# [문자클래스스타일]+ => 단어단위
# [a-z] : 영어소문자
# [A-Z] : 영어대문자
# [0-9] : 숫자
# [가-흫] / [가-힣]: 한글

# 정규표현식 패턴2 - 대문자, 소문자, 숫자 : \지원문자
# [\d] : 10진수, [0-9]와같음
# [\D]: 10진수외 [^0-9]
# [\s] :공백문자, [ \t\n\r\f\v]
# [\S]: 공백 문자 외, [ \t\n\r\f\v]
# [\w] : 영문자숫자 , [a-zA-Z0-9]
# [\W]: 영문자숫자외 , [^a-zA-Z0-9]

# 정규표현식메소드
# match(문자열) : 문자열 처음부터 검색 => 문자열 / None
# search(문자열) : 문자열 전체 검색 => 문자열 / None
# findall(문자열) : 정규식과 매치되는 문자열을 리스트로 반환
# => 리스트 / []
# finditer(문자열)
# : 정규식과 매치되는 문자열을 반복가능한 객체로 반환
# => 반복가능한객체. for문으로 개별 결과 확인


# 적용 방식1
# 패턴식변수 = re.compile(패턴식)
# 패턴식변수.정규표현식메소드(문자열)

# 적용방식2
# 문자열변수 = 문자열값
# re.정규표현식메소드(패턴식, 문자열변수)
# re.match(패턴식, 문자열변수) => 문자열
# re.search(패턴식, 문자열변수) => 문자열
# re.findall(패턴식, 문자열변수) => 리스트
# re.finditer(패턴식, 문자열변수) => 반복가능객체

# ===============
# 적용 방식1
# 패턴식변수 = re.compile(패턴식)
# 패턴식변수.정규표현식메소드(문자열)

txt = 'JAVA 도레미 파솔라 시도 </%$#@ Python mysql 파이썬 1234 67^공**'
# 낱글자 단위
pattern1 = re.compile('[A-Z]')
pattern2 = re.compile('[a-zA-Z]')
pattern3 = re.compile('[가-힣]')
pattern4 = re.compile('[0-9]')
# 단어단위
pattern5 = re.compile('[A-Z]+')
pattern6 = re.compile('[a-zA-Z]+')
pattern7 = re.compile('[가-힣]+')
pattern8 = re.compile('[0-9]+')

print(pattern1, type(pattern1))
# re.compile('[A-Z]') <class 're.Pattern'>

# 패턴식에 맞는 문자열을 리스트로 반환
# 패턴식변수.findall(문자열)
print('== 글자 단위 필터링')
print(pattern1.findall(txt)) # ['J', 'A', 'V', 'A', 'P']
print(pattern2.findall(txt)) # ['J', 'A', 'V', 'A', 'P', 'y', 't', 'h', 'o', 'n', 'm', 'y', 's', 'q', 'l']
print(pattern3.findall(txt)) # ['도', '레', '미', '파', '솔', '라', '시', '도', '파', '이', '썬', '공']
print(pattern4.findall(txt)) # ['1', '2', '3', '4', '6', '7']
print('== 단어 단위 필터링')
print(txt)
print(pattern5.findall(txt))
print(pattern6.findall(txt))
print(pattern7.findall(txt))
print(pattern8.findall(txt))
'''
['JAVA', 'P']
['JAVA', 'Python', 'mysql']
['도레미', '파솔라', '시도', '파이썬', '공']
['1234', '67']
'''

pattern_a = re.compile('[\w]+')
pattern_b = re.compile('[\D]+')
pattern_c = re.compile('[\s]')
print(txt)
print(pattern_a.findall(txt))
print(pattern_b.findall(txt))
print(pattern_c.findall(txt))
'''
['JAVA', '도레미', '파솔라', '시도', 'Python', 'mysql', '파이썬', '1234', '67', '공']
['JAVA 도레미 파솔라 시도 </%$#@ Python mysql 파이썬 ', ' ', '^공**']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
'''

print('\n\n finditer() 테스트 ')
# finditer(문자열)
# : 정규식과 매치되는 문자열을 반복가능한 객체로 반환
# => 반복가능한객체(Match 객체로 반환). for문으로 개별 결과 확인
print(pattern_a.finditer(txt))
# <callable_iterator object at 0x0000021BE82EEAF0>
pattern_a = re.compile('[\w]+') # 알파벳대문자+알파벳소문자+숫자 [a-zA-Z0-9]+
result = pattern_a.finditer(txt)
print(txt)
for item in result:
    print(item)
'''
<re.Match object; span=(0, 4), match='JAVA'>
<re.Match object; span=(5, 8), match='도레미'>
<re.Match object; span=(9, 12), match='파솔라'>
<re.Match object; span=(13, 15), match='시도'>
<re.Match object; span=(23, 29), match='Python'>
<re.Match object; span=(30, 35), match='mysql'>
<re.Match object; span=(36, 39), match='파이썬'>
<re.Match object; span=(40, 44), match='1234'>
<re.Match object; span=(45, 47), match='67'>
<re.Match object; span=(48, 49), match='공'>
'''

# 패턴식과 맞는 결과값을 1개만 반환 => Mathch 객체
# match(문자열) : 문자열 처음부터 검색 => 문자열 / None
# search(문자열) : 문자열 전체 검색 => 문자열 / None
pattern = re.compile('[a-z]+')
print(txt)
print(pattern.match(txt)) # None
print(pattern.search(txt)) # <re.Match object; span=(24, 29), match='ython'>


# Match object 메서드
# group() : 매치된 문자열을 리턴한다.
# start() : 매치된 문자열의 시작 위치를 돌려준다.
# end() : 매치된 문자열의 끝 위치를 돌려준다.
# span() : 매치된 문자열의 시작,끝 위치를 튜플 형태로 돌려준다.
print('n'*3)
pattern = re.compile('[가-힣]+')
result = pattern.finditer(txt)
print(txt)
for item in result:
    print(item)
    print(item.group())
    print(item.start())
    print(item.end())
    print(item.span())
    print('='*50)

print('n'*3)
pattern = re.compile('[가-힣]+')
print(pattern.search(txt))
print(pattern.search(txt).span())
print(pattern.search(txt).group())
# <re.Match object; span=(5, 8), match='도레미'>
# (5, 8)
# 도레미

# =================
# 패턴식 사용방식2 - re.정규표현식메소드(패턴식, 문자열변수)
# re.match(패턴식, 문자열변수) => match객체/None
# re.search(패턴식, 문자열변수) => match객체/None
# re.findall(패턴식, 문자열변수) => 리스트
# re.finditer(패턴식, 문자열변수) => 반복가능객체
txt = '도레미 JAVA 파솔라 시도 </%$#@ Python mysql 파이썬 1234 67^공**'
pattern = '[가-힣]+'
print(re.findall(pattern, txt))
print(re.search(pattern, txt))
print(re.match(pattern, txt))
print(re.finditer(pattern, txt))

# 자릿수 지정 패턴 {}
# [문자열]{n} n번 반복됨
# {n,} n번 이상 반복됨
# {n, m} 최소 n번 이상 최대 m 번 이하로 반복됨
# x* : 문자열X가 0번이상 반복

print('\n'*3)
txt = "abc 00ab 000abcd 00000abcd 012340abcd 00가나다 078376!!! 000BANHF78765 도라지0"
pat1 = '[0]{1}[a-zA-Z]+'
pat2 = '[0]{1,}[a-zA-Z]+'
pat3 = '[0]{1,}[가-힣]+'
pat4 = '[0]{1,3}[a-zA-Z]+'
print(re.findall(pat1, txt)) # ['0ab', '0abcd', '0abcd', '0abcd', '0BANHF']
print(re.findall(pat2, txt)) # ['00ab', '000abcd', '00000abcd', '0abcd', '000BANHF']
print(re.findall(pat3, txt)) # ['00가나다']
print(re.findall(pat4, txt)) # ['00ab', '000abcd', '000abcd', '0abcd', '000BANHF']

# 정규표현식 메타문자
# | : OR 또는
# +:바로 앞의 문자가 하나 이상 있음
# ^:문자열의 처음을 나타냄
# $:문자열의 끝
# . :임의의 문자가 와도 됨
# *:바로 앞의 문자가 없거나 하나 이상 있음
# ?:앞의 문자가 없거나 하나임

txt = '''
        010-7777-1234 00-6785-가나다 
        011-5678-8989 01156788989
        333-123 abc-9990-0000 554-8488-7878 
        045-5678-4567 016-8888-9090
        017-7785-7775
        '''

# 휴대폰번호 유효성검사
# 숫자3자리-숫자4자리-숫자4자리
# 010-숫자4자리-숫자4자리
# 01[0|1|6|7]-숫자4자리-숫자4자리
pattern1 = '[0-9]{3}-[0-9]{4}-[0-9]{4}'
pattern2 = '010-[0-9]{4}-[0-9]{4}'
pattern3 = '01[0|1|6|7]-[0-9]{4}-[0-9]{4}'
print('\n'*3)
print(txt)
print(re.findall(pattern1, txt))
print(re.findall(pattern2, txt))
print(re.findall(pattern3, txt))
'''
['010-7777-1234', '011-5678-8989', '554-8488-7878', '045-5678-4567', '016-8888-9090', '017-7785-7775']
['010-7777-1234']
['010-7777-1234', '011-5678-8989', '016-8888-9090', '017-7785-7775']
'''