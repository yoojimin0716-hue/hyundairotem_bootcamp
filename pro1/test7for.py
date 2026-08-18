#반복문 for
#for target in object:

#for i in [1,2,3,4,5]:
#for i in (1,2,3,4,5):
#for i in {1,2,3,4,5}:, 집합형 데이터를 꺼내옴, 중복은 배제
for i in {1,2,3,4,5,5,5,5,5,5}:
    pass
    print(i, end = ' ') #결과는 1,2,3,4,5

print('분산/표준편차---')
numbers = [1,3,5,7,9]

tot = 0 
for a in numbers:
    tot += a

print(f'합은 {tot}, 평균은 {tot/len(numbers)}') # 합은 25 평균은 5.0

numbers = [-3,4,5,7,12]

avg = tot/len(numbers)
#편차 제곱의 합
hap = 0 
for i in numbers:
    hap += (i - avg) ** 2
print(f'편차 제곱의 합은 {hap}, 분산은 {hap/len(numbers)}, 표준편차는 {(hap/len(numbers))**0.5}')

colors = ["red", "green", "blue"]
for v in colors:
    print(v, end = ' ')

print()
print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')
iterator = iter(colors)
for v in iterator:
    print(v, end = ' ')

print()
for idx, d in enumerate(colors): #enumerate() : 반복 가능한 객체를 인덱스와 함께 반환 (colors, start = 1)로 시작 인덱스 지정 가능
    print(idx, d, end = ' ')

print('\n사전형 ---')
datas = {'python' : '만능언어', 'java' : '웹용언어', 'mariadb' : 'rdbms'}
print(datas.items())
for i in datas. items():
    print(i[0], '~~', i[1])

for k in datas.keys(): 
    print(k,end = ' ')

print()
for v in datas.values():
    print(v,end = ' ')

print('\n 다중 for----------')

for n in [2,3]:
        print(f'{n}단 ~~~')
        for su in [1,2,3,4,5,6,7,8,9]:
            print(f'{n}*{su} = {n*su}')

print('\nfor : continue, break -----')
nums = [1,2,3,4,5]
for i in nums:
    if i ==2 :
        continue #한줄로 처리 가능 if i ==2: continue
    if i ==4 : # 얘를 주석처리하면 1,3,4,5 정상종료
        break
    print(i,end =' , ')
else :
    print('정상종료')

print('\n\n정규표현식 + for 연습 ---')
message =''' (MHN 김예나 기자) 방송인 김숙이 털어놓은 과거 연예인 관련 일화가 뜻밖의 실명 추측과 마녀사냥으로 번지고 있다. 수십 년간 방송 현장을 누빈 베테랑으로서 자신의 한마디가 얼마나 큰 파장을 일으킬 수 있는지 누구보다 잘 알 만한 김숙인 만큼 특정인을 향한 추측의 여지를 남긴 이번 발언을 두고 아쉽다는 목소리도 커지고 있다.

지난 1일 김숙은 유튜브 채널 ‘비보티비’에서 정신건강의학과 전문의 이광민과 통화하던 중 과거 겪었던 한 유명 연예인의 태도를 언급했다.(MHN 김예나 기자) 방송인 김숙이 털어놓은 과거 연예인 관련 일화가 뜻밖의 실명 추측과 마녀사냥으로 번지고 있다. 수십 년간 방송 현장을 누빈 베테랑으로서 자신의 한마디가 얼마나 큰 파장을 일으킬 수 있는지 누구보다 잘 알 만한 김숙인 만큼 특정인을 향한 추측의 여지를 남긴 이번 발언을 두고 아쉽다는 목소리도 커지고 있다.

지난 1일 김숙은 유튜브 채널 ‘비보티비’에서 정신건강의학과 전문의 이광민과 통화하던 중 과거 겪었던 한 유명 연예인의 태도를 언급했다.addf#@$$# '''

import re 
result = re.sub(r'[^가-힣\s]','',message) #정규표현식에선 항상 소문자 r, ^[]는 시작이라는 뜻, [^]는 부정이라는 뜻, 한글 전체를 제외한것을 공백으로 취급한다는 뜻 
print(result)

import re
message2 = re.sub(r'[^가-힣\s]','',message)
print(message2)
message3 = message2.split(' ')
print(message3, ' ', len(message3))
# 단어별 빈도수 출력 : dict 사용 
cou = {}
for i in message3:
    if i in cou:
        cou[i] += 1 # 같은 단어가 있으면 누적 
    else:
        cou[i] = 1 

print(cou)

print('정규표현식 좀더 ---')
for imsi in ['111-1234','일이삼 - 일이삼사', '222-1234','333@3432']:
    if re.match(r'^\d{3}-\d{4}$', imsi): #숫자 3자리 - 숫자4자리 / $는 끝이라는 뜻 
        print(imsi,'전화번호 맞네')
    else:
        print(imsi,'전화번호 아니야')

print('\ncomprehension : 반복문 + 조건문 + 값 생성을 한줄로 표현')
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i%2==0:
        li.append(i)
print(li) #[2,4,6,8,10]출력

print(list(i for i in a if i%2==0)) #[2,4,6,8,10]

print()
datas = [1,2,'a',True,3.0]
li2 = [i for i in datas if type(i) == int] 
print(li2)

print()
id_name = { 1:'tom', 2: 'james'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)

print()
aa = [(1,2),(3,4),(5,6)]
for a,b in aa:
    print(a + b)

print([a+b for a,b in aa]) #[3,7,11]
print(*[1,2,3]) #리스트에서 벗어남

print(*[a+b for a,b in aa], sep='\n')

print('\n 수열 생성 : range(start,stop,step)')
print(list(range(1,6))) #print(list(range(6))) 초기치와 간격치를 설정을 안하면 0부터시작 간격은 1 [0,1,2,3,4,5,6]
#print(list(range(1,6,2))) 1은 start 6은 stop 2는 step(1부터6까지2간격으로) 
print(tuple(range(1,6,2)))
print(list(range(-10,-100,-20)))
print()
for i in range(6):
    print(i,end = ',')

for _ in range(6): # 변수를 쓸생각이 없으면 -로 써도 무관함 
    print('반복') 

print('1~10까지 정수 합')
tot = 0 
for i in range(1,11):
    tot += i

print('tot : ', tot, ' ', sum(range(1,11))) #sum () 내장함수 

for i in range(1,10):
    print(f'2 * {i} = {2 * i}')

print('2~9 구구단 출력 (단은 행단위 출력)')
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} * {j} = {j * i}')
    print()

print('주사위를 두번 던져 나온 숫자들의 합이 4의 배수가 되는 경우만 출력')

for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2 
        if n%4 ==0:
            print(n1,n2)

print()
for i in range(1,7,1):
    for j in range(1,7):
        hap = i + j 
        if hap%4==0:
            print(i,j)
