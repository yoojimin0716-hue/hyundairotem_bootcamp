# 배열 연산 
# 기본 수학 함수는 배열에 요소별로 적용되고, 
# +, -, *,/ 나 또는 add, subtract, multifly,divide
# 벡터화 연산을 하므로 for 문을 사용하지 않고 바로 배열에 대한 연산 가능 


import numpy as np 

# x = np.array([[1,2],[3,4]], dtype=np.float32) 실수 처리하는법 아니면 아래처럼 실수를 줘버리면 됨 
x = np.array([[1,2],[3,4]])
print(x,' ',x.dtype) 

# y = np.arange(5,9)  # [5 6 7 8]   int64 1차원 배열 생성
y = np.arange(5,9).reshape(2,2)  # 구조 변경 (1차원 -> 2차원)
y = y.astype(np.float32) #type 변경 
print(y,' ',y.dtype) # [[5. 6.] [7. 8.]]   float32

print(x.ndim,' ',y.ndim) # 2 2 

print()
print(x + y)
print(np.add(x,y))

print()
print(x - y)
print(np.subtract(x,y))

print()
print(x * y)
print(np.multiply(x,y))

print()
print(x / y)
print(np.divide(x,y))

print()
print(np.sqrt(x),' ',np.exp(x),' ',np.log(x),' ',np.cos(x))

print('\ndot()은 numpy 모듈의 인스턴스 메소드로 내적 연산이 가능')
v = np.array([9,10])   
w = np.array([11,12])

print(v*w)  # 요소별 곱셈 [ 99 120 ] <= 9*11, 10*12

# 벡터의 내적 (행렬곱)
print(v.dot(w))
print(np.dot(v,w))

print()

# 배열 계산 함수 
print(x)
print(np.mean(x),' ',np.var(x))
print(np.max(x),' ',np.min(x))
print(np.argmax(x),' ',np.argmin(x))
print(np.cumsum(x))
print(np.cumprod(x))

names1 = np.array(['tom','james','tom','oscar'])
names2 = np.array(['tom','page','john'])

print(np.unique(names1))
print(np.intersect1d(names1,names2)) # 교집합 ( 중복 x )

print(np.intersect1d(names1,names2,assume_unique=True)) # 교집합 (중복 0)
print(np.union1d(names1,names2)) # 합집합 

print("\n 전치(Transpose)- 2차원 배열에서 행과 열의 위치를 바꿈")
print(x)
print(x,T)
print(x.transpose())
print(x.swapaxes(0,1))

print('\nBroadcasting :  크기가 다른 배열 간의 연산 - 작은 배열을 여러번 반복해 큰 배열과 연산 ')
x = np.arange(1,10).reshape(3,3)
y = np.array([1,0,1])
print(x)
print(y)
print(x+y)

# 배열자료 파일로 저장
np.savetxt("numpy2.txt", x)         # file i/o
imsi = np.loadtxt("numpy2.txt")
print(imsi)