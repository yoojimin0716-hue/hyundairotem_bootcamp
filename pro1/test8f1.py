# function : 여러개의 수행문을 하나의 이름으로 묶은 실행 단원 
# 함수 고유의 공간을 갖는다. 
# 자원의 재활용이 가능 

# 내장 함수 : 일부 체험 
print(sum([1,2,3]))
print(8,bin(8))
print(eval('4+5'))
print(round(1.2), round(1.6))

import math
print(math.ceil(1.2), ' ', math.ceil(1.6)) #올림
print(math.floor(1.2), ' ',math.floor(1.6)) #내림 

b_list = [True, 1, False]
print(all(b_list))
print(any(b_list))

data = [10,20,30]
data2 = ['a','b']
for i in zip(data,data2):
    print(i) # 데이터 2묶음을 튜플로 묶어주는 내장함수 

import builtins
builtins.print('자동 로딩')
builtins.print(builtins.sum([2,5]))
#print = 7 
#print('안녕') 이미 프린트 함수를 숫자로 지정해버려서 함수의 기능을 잃어버림 

