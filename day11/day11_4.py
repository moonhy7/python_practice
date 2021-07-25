# JSON(제이슨, JavaScript Object Notation) 란?
# 경량의 DATA-교환 형식
# 속성-값 쌍 또는 "키-값 쌍"으로 이루어진 데이터 오브젝트를
# 전달하기 위해 사용하는 개방형 표준 포맷이다.
# 자바스크립트의 데이터 객체 표현 방식 으로 데이터 교환의 표준 이용


# JSON 예시 - 키와 값의 구조
# {
#     "이름": "서태웅",
#     "성별": "남",
#     "학교": "북산 고등학교 1학년 10반 22번",
#     "특기": "농구",
#     "포지션": "스몰 포워드(SF)",
#     "별명": "여우",
#     "체격": {"키": "187 ㎝", "몸무게": " 75 ㎏", "혈액형": " AB형(Rh+)"},
#     "라이벌": ["윤대협", "정우성"]
#  }

# json 파이썬 레퍼런스
# https://docs.python.org/3/library/json.html

# 관련 모듈 임포트
import json

# json 구조의 문자열 변수 => 딕셔너리 구조
# json.loads(json문자열변수)


person_str = '{"name":"홍길동", "language":["영어", "한국어", "일어"]}'
print('\n\n === 문자열 데이타  ')
print(person_str)
print(person_str[0]) # {
print(type(person_str))
print('\n\n === 딕셔너리 데이타  ')
person_dict = json.loads(person_str)
print(person_dict)
# print(person_dict[0]) # KeyError: 0
print(type(person_dict))
print(person_dict['name']) # 홍길동
print(person_dict['language'][0]) # 영어

# json 파일읽기 => 딕셔너리 데이타
# data/person.json 파일 생성
'''
with open(jsonURL, 'r', encoding='utf-8/cp949') as 파일변수:
    json데이타변수 = json.load(파일변수)
'''
with open('data/person.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print('\n\n === json 파일 읽기  ')
print(type(data))
print(data)
# <class 'dict'>
# {'name': '홍길동', 'language': ['영어', '한국어', '일어'], 'contact': {'mobile': '010-1234-7890', 'email': 'hong@naver.com'}}
print(data['contact'])
print(data['contact']['email'])

# 딕셔너리 => json문자열로 변경
# json.dumps(딕셔너리)
person_dict = {"name":"홍길동", "language":["영어", "한국어", "일어"]}
print('\n\n === 딕셔너리 데이타  ')
print(type(person_dict))
print(person_dict)

print('\n\n === json 문자열  ')
# ensure_ascii=False 는 한글인 경우 아스키코드로 변경하지 않고 글자 자체를 그대로 유지시켜준다.
# indent='\t' 들여쓰기 모드 사용
json_string = json.dumps(person_dict , ensure_ascii=False, indent='\t')
print(type(json_string))
print(json_string)
'''
<class 'str'>
{
	"name": "홍길동",
	"language": [
		"영어",
		"한국어",
		"일어"
	]
}
'''
'''
# ensure_ascii=False 옵션을 지정하지 않은 경우 
{"name": "\ud64d\uae38\ub3d9", "language": ["\uc601\uc5b4", "\ud55c\uad6d\uc5b4", "\uc77c\uc5b4"]}
'''

# ===============
# json 파일로 저장하기
'''
with open(jsonURL, 'w', encoding='utf-8/cp949') as 파일변수:
    json.dump(딕셔너리, 파일변수, ensure_ascii=False, indent='\t')
'''
# 딕셔너리 정의
person_dict = {"name":"홍길동", "language":["영어", "한국어", "일어"]}
with open('output/person_sample.json', 'w', encoding='utf-8') as f:
    json.dump(person_dict, f, ensure_ascii=False, indent='\t')

person_dict2 = {
  "name":"홍길동",
  "language":["영어", "한국어", "일어"],
  "contact":{"mobile":"010-1234-7890", "email": "hong@naver.com"}
}
with open('output/person_sample2.json', 'w', encoding='utf-8') as f:
    json.dump(person_dict2, f, ensure_ascii=False, indent='\t')


