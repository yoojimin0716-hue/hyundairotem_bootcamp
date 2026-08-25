# 상속 

class Person:  # 용도 : 부모 클래스로 사용 
    say = '난 사람이야' # 접근 권한 : public , +는 퍼블릭이라는 뜻 
    nai = '20' # 전역변수 
    __msg = 'good : private 멤버 - 현재 클래스에서만 유효하다' #파이썬에서 - 는 프라이빗 변수

    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai  #self.nai는 객체 변수, nai는 def 안에 있는 지역변수 

    def printInfo(self): # 접근 권한 : public
        print(f'나이 : {self.nai}, 이야기 : {self.say}')

    def hellomethod(self):
        print('안녕')
        print('hello : ', self.say, self.nai,self.__msg)
      

print(Person.say, Person.nai) # 원형 클래스로 멤버 호출 (비권장)
#Person.printInfo() #- 에러남 person클래스를 실행을 하면 자동으로 init이 실행이 되는데 이 생성자 함수는 
# nai를 별도로 매개변수로 가지기 때문에 Person('25') 이런식으로 값을 줘야함 
# 반대로 printInfo는 (self)만 가지고 있기때문에 따로 값을 안넣어도 실행 가능 
# 저 방식으로 하고싶다면 Person('30').printInfo() 라고 작성 

per = Person('25')
per.printInfo()
per.hellomethod()

print('-----' * 5)
class Employee(Person):
    subject = '근로자'
    def __init__(self):
        print('Employee 생성자')

    def printInfo(self):
        print('Employee 클래스의 printInfo() 호출됨') # < -- 부모가 가지고있는 메서드를 자식도 가지고 있는경우 
        # 메소드 오버라이딩이라고 함 

    def ePrintInfo(self): 
        print(self.subject,self.say, self.nai)
        #print(self.__msg) #부모 클래스의 private 멤버 호출 = error 프라이빗 멤버니까 emloyee 클래스 안에서는 오류
        self.hellomethod()
        self.printInfo() # 현재 클래스에 없으면 부모 메소드에서 호출 
        super().printInfo() # 애초부터 부모 메소드의 것을 호출하고 싶을때 super 사용 
        print(self.say, super().say)

emp = Employee()
print(emp.subject,emp.nai, emp.subject)
emp.printInfo()
emp.ePrintInfo()


print('---' *5)
class Worker(Person):
    def __init__(self,nai):
        print('worker 생성자')
        super().__init__(nai)  # 부모 클래스 생성자 호출 

    def wPrintInfo(self):
        print('Worker - wPrintInfo() 처리')
        self.printInfo()
        super().printInfo()

wor = Worker('30')
print(wor.say,wor.nai)


print('----'*5)
class Programmer(Worker):
    def __init__(self,nai):
        print('programmer 생성자')
        # super().__init__(nai)   # bound method call 
        Worker.__init__(self, nai) #Un bound method call  - 이 두개는 같은말 super로 부모생성자 부르거나 직접 부모생성자 부르기 

    def pPrintInfo(self):
            print('Programmer - pPrintInfo() 처리함')

    def wPrintInfo(self):
            print('Programmer 클래스에서 오버라이딩')



pro = Programmer('35')
print(pro.say,pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()

print('\n클래스 타입 확인 ---------')
a = 3; print(type(a)) # <class 'int'> : Maker가 만든 기본 타입 
print(type(pro)) #<class '__main__.Programmer'>
print(type(wor)) #<class '__main__.Worker'>

print(Person.__bases__) #(<class 'object'>,) 부모 클래스를 알려주는? 그런느낌 
print(Employee.__bases__)
print(Worker.__bases__)
print(Programmer.__bases__)