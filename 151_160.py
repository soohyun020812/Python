# 151
# 리스트에는 네 개의 정수가 저장돼 있다.
리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
# -20
# -3
for 변수 in 리스트: 
  if 변수 < 0:
    print(변수)

# 152
# for문을 사용해서 3의 배수만을 출력하라.
리스트 = [3, 100, 23, 44]
# 3
for 변수 in 리스트:
  if 변수 % 3 == 0:
    print(변수)

# 153
# 리스트에서 20 보다 작은 3의 배수를 출력하라
리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18
for 변수 in 리스트:
  if (변수 < 20) and (변수 % 3 == 0):
    print(변수)

# 154
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language
for 변수 in 리스트:
  if len(변수) >= 3:
    print(변수)

# 155
# 리스트에서 대문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
# A
# D
for 변수 in 리스트:
  if 변수.isupper():
    print(변수)

# 156
# 리스트에서 소문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
# b
# c
for 변수 in 리스트:
  # 논리 연산자 not 말고도 비교 연산자를 사용할 수 있음
  # isupper() == False: or isupper() != True:
  if not 변수.isupper():
    print(변수)
  
# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.
리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
for 변수 in 리스트:
  print(변수[0].upper() + 변수[1:])

# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
for 변수 in 리스트:
  split = 변수.split(".")
  print(split[0])  

# 159
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
for 변수 in 리스트:
  split = 변수.split(".")
  if split[1] == "h":
    print(변수)

# 160
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)