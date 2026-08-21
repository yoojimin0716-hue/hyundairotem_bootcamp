class car :
    handle = 1
    speed = 0

    def __init__(self,name,speed):
        self.name = name #현재 객체의 name에게 name(지역변수) 인자값 치환
        self.speed = speed

    def showData(self):
        km = '킬로미터'
        msg = '속도 :' + str(self.speed) + km
        return msg

    def printHandle(self):
        return self.handle

print(car.handle) #원형 클래스의 멤버 호출

car1 = car('tom',10)# 생성자 호출을 통해 객체 생성(인스턴스화)
print('car1 객체 주소 : ', car1)
print('car1 : ', car1.name,' ', car1.speed,' ', car1.handle)
car1.color = '파랑'
print('car1.color : ', car1.color)
print('---')
car2 = car('oscar',20)
print('car2 :', car2.name,' ', car2.speed,' ',car2.handle)

print(car,car1,car2)
print(id(car),id(car1),id(car2))
print()

print(car1.__dict__)
print(car2.__dict__)


print('메소드~~~~~~')
print('car1 speed : ', car1.showData())
print('car2 speed : ', car2.showData())

print()
print('car1 handle : car1.printHandle')
print('car2 handle : car2.printHandle')
car.handle2 # 원형(원본) 클래스의 멤버 변수 값 수정 
print('car1 handle : car1.printHandle')
print('car2 handle : car2.printHandle')