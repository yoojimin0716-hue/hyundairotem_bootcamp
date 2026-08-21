# oop : 객체지향(중심)적인 프로그래밍 가능. 상속, 포함, 다형성 등의 기법 구사 가능 
# class : 멤버 변수(필드), 멤버 메소드로 구성 
# 인스턴스에 의해 새로운 이름 공간을 갖는다.

import math

a = 2 
print(a)

def func():
    print('ok')

class Testclass:   # 클래스명의 첫글자는 대문자로 
    aa = 1      # 멤버 변수 

    def __init__(self): # Method의 첫 인자는 반드시 self 
        print('생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')

    def __del__(self):
        print('소멸자 : 프로그램 종료시 자동실행. 마무리 작업')

    def showMessage(self):
        name = '한국인' # 지역변수 : showMessage
        print(name)
        print(self.aa)

test = Testclass()
print(Testclass) # 클래스 자체 출력 (object가 아니라 class 정보)
print('클래스 멤버 a : ', Testclass)

test = Testclass()
print('클래스 멤버 a : ', test.aa)
test.showMessage()   # 인스턴스로 정상 호출

# 클래스 자체를 test에 대입 (인스턴스 아님)
test = Testclass()
print('클래스 멤버 a : ', test.aa)
print()

Testclass.showMessage(test)  # test는 인스턴스가 아니라 클래스이므로
                              # 인스턴스 대신 test(=Testclass)를 self 자리에 명시적으로 넘겨줌

#1. Bound Method call
test.showMessage()

#2. UnBound Method call
Testclass.showMessage(test)

print()
print(type(1))
print(type(1.0))
print(type('ok'))
print(type(test))


print(id(test))
print(id(Testclass))
test2 = Testclass()
print(id(test))