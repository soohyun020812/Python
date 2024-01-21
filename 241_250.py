# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
import datetime
now = datetime.datetime.now()
print(now)

# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
import datetime
now = datetime.datetime.now()
print(now, type(now))

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
import datetime
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01 
import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
import datetime
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
import time
import datetime
while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# import os     # os.rename()
# from os import rename     # rename()
# from os import *      # getcwd(), rename()
# import os as myos     # myos.getcwd()

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
import os
ret = os.getcwd()
print(ret, type(ret))

# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250 numpy
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)