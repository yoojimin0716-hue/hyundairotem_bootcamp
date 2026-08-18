#사용자 정의 함수 
'''
def 함수명(가인수)    #dummy argument, 매개변수
    #,,,
    return 반환값     #1개만 반환, return이 없으면 return None

함수명(실인수,,,)     #함수 호출   #actual arguement
'''

import builtins
builtins.print('자동 로딩')
builtins.print(builtins.sum([2,5]))
#print = 7 
#print('안녕') 이미 프린트 함수를 숫자로 지정해버려서 함수의 기능을 잃어버림 

print('뭔가를 실행...')
# 함수 선언 
def doFunc1():
    print('doFunc1 수행')
    return None #생략 가능

# 함수 호출 
doFunc1()
print('어떤 작업 처리')
doFunc1()
print('함수 주소는', doFunc1)
imsi = doFunc1 #doFunc1의 주소를 imsi에게 임명
imsi() #함수 실행 가능 
imsi2 = doFunc1() #함수 실행 결과를 기억 
print(imsi) # 실행 결과를 출력 
print(doFunc1())
print('작업 종료') 

def doFunc2(name) : 
    print('name : ', name)

print('--------')
# doFunc2() #Argument 가 안맞아서 오류 ()안에 숫자라도 집어 넣어야함 
doFunc2('홍길동')

def doFunc3(arg1, arg2):
    res = arg1 + arg2
    return res 

doFunc3('대한','민국') #이렇게 수행하면 아무것도 안찍힘 
print(doFunc3('대한','민국'))


def doFunc3(arg1, arg2):
    res = arg1 + arg2
    return res #return이 없으면 항상 출력값이 none 


doFunc3('대한','민국') #이렇게 수행하면 아무것도 안찍힘 
print(doFunc3('대한','민국'))
# print(doFunc3('대한','4')) - 이건 불가능

result = doFunc3('3','4')
print('result : ',result)

def doFunc4(a1,a2):
    imsi = a1 + a2
    if imsi %2 == 1:
        return
    else :
        return imsi

    #kbs = 9 이런거 쓰면 그냥 안먹힘 죽은 문장임 

print(doFunc4(3,5))

print('**' * 30)
def triArea(a,b):
    c = a*b/2
    triAreaPrint(c) #함수 내에서 다른 함수 호출 c 가 하나니까 arg처럼 하나의 변수로 수를 맞춰줘야함 

def triAreaPrint(arg):
    print('삼각형의 면적은 ', arg)

triArea(20,30)

print()
def passResult(kor,eng):
    ss = kor +eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20,50):
    print('합격')
else:
    print('불합격')

print()
def swapFunc(a,b):
    return b,a

a =10; b = 20
print(a, ' ',b)
print(swapFunc(a,b))

print()

def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부함수 funcInner 실행')

    funcInner()

funcTest()

print()
#if 조건식 안에 함수 적용 
def isOdd(para):
    return para % 2 == 1 # 홀수 이면 True 반환

mydict = {x:x for x in range(11) if isOdd(x)}
print(mydict)

print('\n 변수의생존 범위 (scope rule)')

# 변수가 저장되는 이름공간은 변수가 어디에서 선언 되었는가에 따라 생존 시간이 다다르다 
# 전역, 지역 변수 
# 변수가 영향을 미치는 범위  Local> Enclosing function> Global> Built in 
player = '전국 대표' #전역변수 (현재 파일(모듈) 어디서든 호출 가능)
name = '신기해'

def funcsoccer():
    name = '이기자' #지역변수 (현재 함수 내에서만 유효)
    city = '서울'
    print(f'이름은 {name} 수준은 {player}')
    print(f'지역은 {city}')


print()
a = 10; b = 20; c = 30 
(f'foo 수행 전 a : {a}, b : {b}, c: {c}')
def foo(): 
    def bar():
        a = 3 # a 는 bar에 속해있으므로 이거는 3으로 출력 근데  global a라고 하면 bar의 멤버가 아니라 모듈의 멤버가 된다(전역)
        print(f'Bar 수행 중 a : {a}, b : {b}, c: {c}')
    bar()
    print(f'Bar 수행 후 a : {a}, b : {b}, c: {c}')

foo()
print(f'foo 수행 후 a : {a}, b : {b}, c: {c}')
funcsoccer()

print()
a = 10; b = 20; c = 30 

def foo(): 
    a = 7 # 지역 변수 
    b = 100

    def bar():
        global c # bar의 멤버가 아니라 모듈의 멤버가 됨 (전역)
        nonlocal b  #이걸 사용함으로써 bar가 아니라 foo의 멤버로 들어감 
        b = 8 # 지역 변수 
        print(f'Bar 수행 중 a : {a}, b : {b}, c: {c}')
        c = 9
        b = 200
    bar()
    print(f'Bar 수행 후 a : {a}, b : {b}, c: {c}')

foo()
print(f'foo 수행 후 a : {a}, b : {b}, c: {c}')

print()
g = 1 
print('g: ',g) #1
def func():
    global g
    a = g
    g = 2
    return a 

print(func())
print('g: ',g) #2








print('작업 종료')