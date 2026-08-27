# 직원 급여 계산 예제 
# 직원이라는 개념은 있지만 실제 급여 계산은 정규직과 아르바이트가 있다 

from abc import ABC,abstractclassmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name 

    @ abstractclassmethod
    def get_salary(self):
        pass

    def show_salary(self):
        print('이름 : ',self.name)
        print('급여 : ',self.get_salary(),'원')

# 정규직 
class FullTimeEmployee(Employee):
    def __init__(self, name,month_salary):
        super().__init__(name)
        self.monthly_salary = month_salary

    def get_salary(self):
        return self.monthly_salary

    def showMe(self):
        print('나는 정규직이야')

# 알바 
class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hours_pay):
        super().__init__(name)
        self.hours = hours
        self.hours_pay = hours_pay
        
    def get_salary(self):
        return self.hours * self.hours_pay

emp1 = FullTimeEmployee('홍길동',3500000)
emp2 = PartTimeEmployee('유지민',80,10500)

emp1.show_salary()
emp2.show_salary()
# 추상 클래스를 사용하는 이유는 여러 자식 클래스가 반드시 가져야할 공통 규칙을 정하고 구현을 강제하기 위함 
