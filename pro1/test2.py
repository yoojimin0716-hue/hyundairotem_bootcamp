#연산자
#치환연산자
v1 = 3
v1 = v2 =v3 = 5
print(v1, v2, v3)   

v1 =10,20,30
print('v1 : ', v1) # 출력값 v1 : (10, 20, 30) ,튜플형으로 출력됨

v1, v2 = 10, 20
print(v1, v2) # 출력값 10 20, 하나씩 가짐 

v2,v1 = v1,v2
print(v1, v2) # 출력값 20 10, 서로 바뀜, 기억장소의 값 맞 교환 

print('값 할당 packing')
#Sv1,v2 = 1,2,3,4,5
#print(v1, v2) 이러면 오류남 

v1, *v2 = 1,2,3,4,5
print(v1, v2) # 출력값 1 [2, 3, 4, 5] , v1은 1만 가져오고 나머지는 리스트로 가져옴

*v1, v2 = 1,2,3,4,5
print(v1, v2) # 출력값 [1, 2, 3,
*v1, v2, v3 = 1,2,3,4,5
print(v1, v2, v3) # 출력값 [1, 2, 3] 4 5 , v1은 1,2,3 가져오고 v2는 4 가져오고 v3는 5 가져옴

v1, *v2, v3 = 1,2,3,4,5
print(v1, v2, v3) # 출력값 1 [2, 3, 4] 5 , v1은 1 가져오고 v2는 2,3,4 가져오고 v3는 5 가져옴    

v1, v2, *v3 = 1,2,3,4,5
print(v1, v2, v3) # 출력값 1 2 [3, 4, 5] , v1은 1 가져오고 v2는 2 가져오고 v3는 3,4,5 가져옴
# *v1, v2, *v3 = 1,2,3,4,5
# print(v1, v2, v3) #이러면 오류남, *는 하나만 사용 가능

print('서식에 의한 자료 출력 %s,%d,%f'%('문자열', 100, 3.14)) # 출력값 문자열,100,3.140000
name = '마우스'; price\
    = 5000 # \는 이어지는 한줄임을 의미, ;는 한줄에 여러문장을 작성할 수 있음
print(f'이름 : {name}, 가격 : {price}') # 출력값 이름 : 마우스, 가격 : 5000

print('abc')
print('def')
print('abc', end='') # end=''는 줄바꿈을 하지 않겠다는 의미
print('def') # 출력값 abcdef, 줄바꿈 없이 출력됨

print('\n\n연산자연습 계속')

print(5 + 3, 5 - 3, 5 * 3, 5 / 3, 5 // 3, 5 % 3, 5 ** 3) # 출력값 8 2 15 1.6666666666666667 1 2 125

print(divmod(5, 3)) # 출력값 (1, 2), divmod는 몫과 나머지를 튜플형으로 반환

# 연산자 우선순위 
# () > ** > 단항 > * , / , // , % > + , - > 비교연산자 > 논리연산자(not,and,or) > 치환연산자(=)

print('관계연산자')
print(5>3, 5 == 3, 5 != 3)  # 출력값 True False True

print('논리연산자')
print(5 > 4 and 4 > 3, 5 > 4 or 4 > 3, not(5 >= 4)) # 출력값 True True False

print('문자열 더하기')
print('Hello' + 'World') # 출력값 HelloWorld    
print('boring' * 3) # 출력값 boringboringboring

print('누적')
a = 10
a = a+1
a += 1 #증감연산자
print('a는 ', a) # 출력값 a는 12
print(f'a는 {a}') # 출력값 a는 12

print('부호 변경 : ', a, a*-1, -a, --a,---a) # 출력값 부호 변경 :  12 -12 -12 12 -12

print('boolean 처리 ', bool(0), bool(1), bool(-1.5))# 출력값 boolean 처리  False True True
print('boolean 처리 ', bool(0), bool(0.0), bool(False), bool(None))# 출력값 boolean 처리  False True True
print('boolean 처리 ', bool([]), bool({}), bool(set())) # 출력값 boolean 처리  False False False

print('이스케이프 문자') #escape character 특별한 의미를 표현하기 위한 문자 
print('aa\tbb')# 출력값 aa	bb, 띄어쓰기
print(r'aa\tbb') # r은 raw string, 이스케이프 문자를 무시하고 그대로 출력
print('aa\bbb') # 출력값 aabb, \b는 백스페이스, 한칸 지움       
print('aa\nbb') # 출력값 aa
print(r'aa\nbb') # 출력값 aa\nbb, r은 raw string, 이스케이프 문자를 무시하고 그대로 출력
print('c:\a\abc.txt') # 출력값 c:\abc.txt, \a는 벨소리, \b는 백스페이스, \n은 줄바꿈
print('c:\n\abc.txt') # 출력값 c:\abc.txt, \n은 줄바꿈, \a는 벨소리, \b는 백스페이스
