print('hello world!')
'''
이건 주석이야 실행과는 상관없대 

'''
#한줄 주석 
print('작업계속')
var1 = '안녕 파이썬' #따옴표는 ' 또는 " 둘다 가능
print(var1)
a=3
b=5
print(a is b, a==b) #이건 오류가 나겠지
c = b
print(a,b,c)
print(id(a), id(b), id(c)) #id는 메모리 주소를 알려주는 함수
print(a is c, a==c) #a와 c는 같은 메모리 주소를 가리키고 있지 않기 때문에 False, is 는 주소비교 , ==값 비교
print(a is b, a==b) #a와 b는 같은 메모리 주소를 가리키고 있지 않기 때문에 False
print(b is c, b==c) #b와 c는 같은 메모리 주소를 가리키고 있기 때문에 True
aa=[100]
bb=[100]
print(aa is bb, aa==bb) #리스트는 같은 값을 가지고 있어도 다른 메모리 주소를 가리키고 있기 때문에 False
aa=100
bb=100
print(aa is bb, aa==bb) #정수는 같은 값을 가지고 있으면 같은 메모리 주소를 가리키고 있기 때문에 True

# 변수 : 기억 장소의 이름 - 동적 (객체값 자체가 아니라 객체의 주소를 기억)
# 상수 : 기억 장소의 이름 - 정적 

print()
import keyword # 외부 모듈 읽기 - 보조 기억 장치에 저장된 모듈을 주 기억 장치로 
print('키워드(예약어)목록:', keyword.kwlist) #파이썬 예약어 출력
# 주의 : 예약어는 사용자 이름으로 사용하면 안됨

# print() 한줄 띄우라는 의미
print('\ntype(자료형)확인') #\n 이것도 한줄 띄우기(line skip)
print(5, type(5)) #정수형
print(3.14, type(3.14)) #실수형
print(3+4j, type(3+4j)) #복소수형
print(True, type(True)) #논리형
print('kbs', type('kbs')) #문자열형
print((1,), type((1,))) #튜플형
print([1], type([1])) #리스트형
print({1}, type({1})) #집합형
print({'a':1}, type({'a':1})) #딕셔너리형
# ctrl + / : 한줄 주석 처리
# ctrl + s : 저장