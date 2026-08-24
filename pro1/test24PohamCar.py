#여러개의 부품 객체를 조립해 완성차 생성 
# 클래스의 포함 관계 사용 ( 자원의 재활용 )
# 포함 관계 : 다른 클래스(객체)를 마치 자신의 멤버처럼 선언하고 사용 
from test24PohamHandle import PohamHandle 

class PohamCar:
    turnShowMessage = '정지'   # 철자 통일

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle()

    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'

if __name__ == '__main__':   # 언더스코어 2개
    tom = PohamCar('미스터 톰')   # 대소문자 수정
    tom.turnHandle(0)
    print(tom.ownerName + '의 회전량은' + tom.turnShowMessage + ' ' + str(tom.handle.quantity))

    print()
    john = PohamCar('미스터 존')   # 대소문자 수정
    john.turnHandle(10)
    print(john.ownerName + '의 회전량은' + john.turnShowMessage + ' ' + str(john.handle.quantity))

    jimin = PohamCar('유지민')   # 대소문자 수정
    jimin.turnHandle(-10)
    print(jimin.ownerName + '의 회전량은' + jimin.turnShowMessage + ' ' + str(jimin.handle.quantity))