# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예 : p_t___
p = 'python'
print(p[0], p[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예 : 2210
car = "24가 2210"
print(car[-4:])

# 023 문자열 인덱싱
# 아래의 문자에서 '홀'만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예 : 홀홀홀
string = "홀짝홀짝홀짝"
print(string[::2])
# 슬라이싱 때 "시작인덱스:끝인덱스:오프셋" 지정 가능

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예 : NOHTYP
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예 : 010 1111 2222
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
# replace 메서드를 사용하면 문자열 일부를 치환할 수 있음, 문자열은 수정할 수 없는 자료형이기 때문에 치환된 새로운 문자열이 리턴

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예 : 01011112222
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-', '')
print(phone_number1)

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예 : kr
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
# 문자열로 표현된 url에서 "."을 기준으로 분리

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
# 문자열은 수정할 수 없어서 문자열이 할당(assignment) 메서드를 지원하지 않음

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예 : Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
# abcd : 문자열은 변경할 수 없기에 replace 메서드를 사용하면 원본은 그대로며 변경된 새로운 문자열 객체를 리턴