#2 번 
class ElectProduct: # 부모 클래스 
    volume = 0 
    def volumeControl(self):
        pass

class ElecTv(ElectProduct):
    def tv(self):
        print('ElecTv 클래스의 고유 메소드')

    def volumeControl(self): #메소드 오버라이딩 
        volume1 = input('TV의 볼륨을 설정해주세요 : ')
        print(volume1)

class ElecRadio(ElectProduct):
    def volumeControl(self):
        volume2 = input('Radio의 볼륨을 설정해주세요 : ')
        print(volume2)

a1 = ElecTv()

a1.volumeControl()

a2 = ElecRadio()
a2.volumeControl()




#3번 
class Animal: # 부모 클래스 

    def move(self):
        print('동물들이 움직이는 방법')

class Dog(Animal):
    name = '개'
    def move(self):
        print('멍멍이는 아장아장')

class Cat(Animal):
    name = '고양이'
    def move(self):
        print('고양이는 살금살금')

class Wolf(Dog,Cat):
    pass 

class Fox(Cat,Dog):
    def move(self):
        print('여우는 살랑살랑')

    def foxMethod(self):
        self.move()
        super().move()
    
        print('여우는 사람을 홀리는 발걸음')

a1 = Fox()
a2 = Wolf()
a3 = Cat()
a4 = Dog()
a5 = Animal()
print('---'*5)
a5.move()
a1.move()
a2.move()
a1.foxMethod()

#2-1번

class ElectProduct: # 부모 클래스 
    volume = 0 
    def volumeControl(self):
        self.volume = input('볼륨을 설정해주세요 : ')
        print()
        

class ElecTv(ElectProduct):
    def tv(self):
        print('ElecTv 클래스의 고유 메소드')

    def volumeControl(self): #메소드 오버라이딩
        super().volumeControl() 
        print(f'TV의 볼륨 : {self.volume}')

class ElecRadio(ElectProduct):
    def volumeControl(self):
        super().volumeControl()
        print(f'Radio의 볼륨 : {self.volume}')



a1 = ElecTv()

a1.volumeControl()

a2 = ElecRadio()
a2.volumeControl()
