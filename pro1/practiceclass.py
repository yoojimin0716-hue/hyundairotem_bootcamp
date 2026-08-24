class CoinIn: 

    def __init__(self):
        self.coin = 0
        self.change = 0

    def culc(self, cupcount):
        price = cupcount*200

        if self.coin >= price:
            self.change = self.coin - price 
            print(f'커피 {cupcount}잔과 잔돈{self.change}원')

        else:
            print('요금 부족')
        

class Machine: 
    def __init__(self):
        self.cupcount = 1
        self.coin_in = CoinIn()

    def showData(self):
        self.coin_in.coin = int(input('동전을 입력하세요 : '))
        self.cupcount = int(input('몇 잔을 원하세요? : '))
        self.coin_in.culc(self.cupcount)

        

if __name__ == '__main__':
    Machine().showData()



