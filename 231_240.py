# 231
# 아래 코드를 실행한 결과를 예상하라.
'''
def n_plus_1 (n) :
    result = n + 1
n_plus_1(3)
print (result)
'''
# 에러 발생, 함수 내부에서 사용한 변수는 밖에서 접근할 수 없음
# 함수 내부 계산값을 전달하기 위해선 return을 사용

# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def make_url(string) :
    url = "www." + string + ".com"
    return url
result = make_url("naver")
print(result)

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(string):
    my_list = []
    for 변수 in string:
        my_list.append(변수)
    return my_list
result = make_list("abcd")
print(result)

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result
result = pickup_even([3, 4, 5, 6, 7, 8])
print(result)

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567
def convert_int (string) :
    return int(string.replace(',', ''))
result = convert_int("1,234,567")
print(result)

# 236
# 아래 코드의 실행 결과를 예측하라.
def 함수(num) :
    return num + 4
a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
# 10 - 14 - a변수 14저장
# 14 - 18 - b변수 18저장
# 18 - 22 - c변수 22저장, 따라서 22출력

# 237
# 아래 코드의 실행 결과를 예측하라.
def 함수(num) :
    return num + 4
c = 함수(함수(함수(10)))
print(c)
# 안쪽 괄호부터 14, 18, 22 따라서 22출력됨

# 238
# 아래 코드의 실행 결과를 예측하라.
def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10)
c = 함수2(a)
print(c)
# 함수 1이 10+4가 되어서 14반환
# 함수 2는 14*10을 통해 140반환 c에 바인딩
# 따라서 출력값은 140

# 239
# 아래 코드의 실행 결과를 예측하라.
def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)
# c를 통해 10이 바인딩 되어서 num에 12로 업데이트
# 12로 업데이트 된 함수1은 +4가 되어서 12+4를 통해 16이 출력됨

# 240
# 아래 코드의 실행 결과를 예측하라.
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)
c = 함수2(2)
print(c)
# 2+10을 통해 함수1에 12로 업데이트
# 12+2를 통해 함수2에 14로 업데이트
# 최종적으로 함수0은 14*2로 28출력