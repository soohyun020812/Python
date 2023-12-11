# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위    영화
#  1    닥터 스트레인지
#  2	스플릿
#  3	럭키
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# 리스트 숫자    :     0            1        2        3
# 따라서 닥터 스트레인지와 스플릿 사이에 들어가게 될 경우 기존 스플릿(1)번 자리에 슈퍼맨을 추가하고 스플릿이 2번으로 넘어가게 됨
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# 0, 1, 2, 3 순서로 스플릿(2), 배트맨(3)번임
# 허나 스플릿(2)을 지우게 될 시 배트맨이 (2)번이 됨, 따라서 각자의 순서를 고려하여 삭제해야 함
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# 실행 예 : >> langs = ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
langs = lang1 + lang2
print(langs)

#057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예 : max : 7, min : 1
print("max : ", max(nums)) # 최대값
print("min : ", min(nums)) # 최솟값

# 058
# 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
# 실행 예 : 15
print(sum(nums))

# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
# 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
# 평균 : 리스트 총합 / 리스트 개수
average = sum(nums) / len(nums)
print(average)