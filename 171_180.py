# 171
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
for i in range(len(price_list)):
    print(price_list[i])

# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
for i, data in enumerate(price_list):
    # enumerate : 순서가 있는 자료형을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴함
    print(i, data)

# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

# 175
# my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
for i in range( 1, len(my_list) ) :
  print(my_list[i-1], my_list[i])

# 176
# 리스트를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마 
for i in range( 2, len(my_list) ):
    print(my_list[i-2], my_list[i-1], my_list[i])

# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 178
# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
# 100
# 200
# 400
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

# 179
# 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
my_list = [100, 200, 400, 800, 1000, 1300]
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])