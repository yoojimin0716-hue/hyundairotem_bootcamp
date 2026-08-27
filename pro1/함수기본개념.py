#class 정의 : 객체를 찍어내기 위한 틀

class CoinIn:
    ...

# 객체/인스턴스 : 틀로 찍어낸 실물, CoinIn()이라는틀로 실제로 찍어낸 것 

c1 = CoinIn()

# 생성자 : 객체를 만드는 그 순간, 자동으로 딱 한번 실행되는 메서드 

__init__ 

# 메서드 : 클래스 안에 정의된 함수 

def culc(self,cupcount):

# 속성/객체 변수/인스턴스 변수 : self.가 붙은 변수 (객체가 개인적으로 가지고있는 데이터)
self.coin = 0

# 지역 변수 : 메서드/ 함수 안에서만 잠깐 있는 변수 (def 안에서는 self가 안붙어있음)
def culc(self,cupcount):
    price = cupcount*200 # <-- price는 지역변수 

# 매개변수 : 함수/메서드가 호출될때 받는 입력값 
def culc(self,cupcount): #<-- cupcount 가 매개변수, 만약에 self.coin_in.culc(6)이라고 하면 cupcount 자리에 6이 들어감 


# 전역변수 : 클래스/함수밖에 파일 최상단에 있는 변수 ,프로그램 어디서든 접근 가능 
PRICE_PER_CUP = 200   # 전역변수 (파일 어디서나 접근 가능)

class CoinIn:
    def culc(self, cupcount):
        price = cupcount * PRICE_PER_CUP   # 함수 안에서도 그냥 읽을 수 있음

# 함수에 self만 필요한 경우 : 메서드가 이미 인스턴스로만 동작할수있을때
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):  # self만 있으면 충분
        print(f"{self.name}가 짖습니다!")

    def get_age(self):  # 저장된 값만 리턴
        return self.age

# 매개변수가 추가로 필요한 경우 : 메서드를 호출할때마다 새로운 정보를 넘겨줘야 할때(외부에서 받는값)
    def celebrate_birthday(self, years=1):  # 몇 살 늘릴지는 그때그때 다름
        self.age += years

    def rename(self, new_name):  # 새 이름은 외부에서 줘야 알 수 있음
        self.name = new_name