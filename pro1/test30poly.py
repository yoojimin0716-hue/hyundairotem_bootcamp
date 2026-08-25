# 메소드 오버라이딩을 통한 polymorphism(다형성) 구현
# 카드결제, 현금결제, 포인트 결제를 각 클래스에서 결제 메소드를 오버라이딩 하기 

class Payment : #부모 클래스 : 결제라는 공통기능 pay를 정의 
    def pay(self,amount):
        print(f'{amount}원 결제를 진행') 
        # pass - 내용 없이 만들수도 있음  

    
# 이하 자식 클래스 
class CardPayment(Payment): #카드 결제 클래스 : 카드수수료 2%를 계산하여 결제 

    def abc():
        print('Cardpayment 고유 메소드')

    def pay(self,amount): # <-- 메소드 오버라이드 - 강요는 아님, 선택적 
        fee = amount*0.02
        total = amount + fee 
        print(f'[카드결제]')
        print(f'상품 금액 : {amount}, 수수료 : {fee}원, 최종 결제 금액 : {total}원')

class Cash(Payment): # 현금 결제 클래스 : 현금 할인 5프로를 적용하여 결제 
    def pay(self,amount):
        discount = amount *0.05
        total = amount - discount
        print(f'[현금결제]')
        print(f'상품 금액 : {amount}, 할인금액 : {discount}원, 최종 결제 금액 : {total}원')

class Point(Payment):
    def pay(self,amount): # 포인트 결제 클래스 : 금액 만큼 포인트를 사용 
        print('[포인트 결제]')
        print(f'{amount}포인트를 사용함')

# 클래스 공통 처리 함수 : 전달 받은 객체의 pay()를 호출한다.
def process_payment(paymentAddr : Payment,amount : int)-> None:
    paymentAddr.pay(amount)

if __name__ == '__main__': # < -- 다른 코드에서 이 test30poly.py의 로직을 쓰고싶어서 이 파일을 불러올때 실행시키 않기위해서 쓰는 코드
    # 근데 지금 이 코드에서는 이 코드가 main이니까 써도 실행이 되는것임 
    p1 = CardPayment()
    p2 = Cash()
    p3 = Point()

process_payment(p1,10000)
print()
process_payment(p2,10000)
print()
process_payment(Point(),10000)
print()



