#4 추상 클래스를 이용한 상속문제 

from abc import ABC,abstractclassmethod

class Employee(ABC):
    def __init__(self,irum,nai):
        self.irum = irum
        self.nai = nai

    @abstractclassmethod
    def pay(self):
        pass

    @abstractclassmethod
    def data_print(self):
        pass 

    def irumnai_print(self):
        print('이름 : ',self.irum, end = ' ')
        print('나이 : ',self.nai,'살',end = ' ')

class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):
        super().__init__(irum,nai)
        self.ilsu = ilsu
        self.ildang = ildang 

    def pay(self):
        return self.ilsu * self.ildang 

    def data_print(self):
        super().irumnai_print()
        print('월급 : ',self.pay(),'원' )

class Regular(Employee):
    def __init__(self,irum,nai,salary):
        super().__init__(irum,nai)
        self.salary = salary 

    def pay(self):
        return self.salary

    def data_print(self):
        super().irumnai_print()
        print('급여 : ',self.pay(),'원')

class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):
        super().__init__(irum,nai,salary)
        self.sales = sales
        self.commission = commission

    def pay(self):
        return self.sales * self.commission

    def data_print(self):
        super().irumnai_print()
        print('수령액 : ',self.pay() + self.salary,'원' )

t = Temporary('홍길동',25,20,15000)
r = Regular('한국인',27,3500000)
s = Salesman('손오공',29,1200000,5000000,0.25)

t.data_print()
r.data_print()
s.data_print()