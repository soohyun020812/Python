# 251 클래스, 객체, 인스턴스
# 클래스와 객체에 대해 설명해봅시다.
# 클래스는 일종의 설계도, 객체가 가지는 속성(필드)와 동작(메서드)으로 이루어져 있음
# 객체는 자신의 속성을 가지고 있고, 다른 것과 식별 가능한 것 (물리적으로 존재하거나 추상적으로 생각할 수 있는 것 중)

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
class Human:
    pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
class Human:
    pass
areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요. 
# areum = Human()
# 응애응애
class Human:
    def __init__(self):
        print("응애응애")
areum = Human()

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# areum = Human("아름", 25, "여자")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")
print(areum.name)

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예
# areum.age
# 25
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")
print(areum.age)

# 257 클래스 메소드-1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
# areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
areum = Human("아름", 25, "여자")
areum.who()
# Human.who(areum)

# 258 클래스 메소드-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# areum = Human("모름", 0, "모름")
# areum.setInfo("아름", 25, "여자")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("불명", "미상", "모름")
areum.who()
# Human.who(areum)
areum.setInfo("아름", 25, "여자")
areum.who()
# Human.who(areum)

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# areum = Human("아름", 25, "여자")
# del areum
# 나의 죽음을 알리지 말라
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print("나의 죽음을 알리지마라")
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")
del(areum)

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
'''
class OMG : 
    def print() :
        print("Oh my god")
        myStock = OMG()
    myStock.print()
TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()
TypeError: print() takes 0 positional arguments but 1 was given
'''
# OMG클래스의 print메서드가 정의될 때 인자를 받지 않도록 정의되었지만
# 객체를 통해 호출할 때 하나의 인자(자기 자신을 나타내는 self라 불리는 인자)가 전달되었기 때문에 발생
# 파이썬에서 클래스의 메서드는 항상 첫 번째 매개변수로 self를 가져야 함
'''
# 수정한 코드
class OMG:
    def print(self):
        print("Oh my god")
# 객체 생성
myStock = OMG()
# 메서드 호출
myStock.print()
'''