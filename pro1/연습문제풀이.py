
#%%
# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력

sum = 0
for i in range(1,101):
    if i % 3 == 0 and i % 2 != 0:
        print(i,end = ' ')
        sum = sum + i 

print (f'합 : {sum}')
#%%
sum = 0
i = 1 
while i <=100:
    i += 1
    if i % 3 == 0 and i % 2 != 0:
        print(i,end = ' ')
        sum = sum + i
       
print (f'합 : {sum}')

#%%
#문2) 2 ~ 5 까지의 구구단 출력

for dan in range(2,6):
    print(f'------{dan}단------')
    for num in range(1,10):
        print(f'{dan} * {num} = {dan*num}')
#%%
dan = 1 

while dan <= 4 :
    dan = dan +1 
    print(f'-------{dan}단-------')
    num = 1 # 위치 중요
    while num <=9 :
        num = num + 1 
        print(f'{dan} * {num} = {dan*num}')

# %%
#3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
sum = 0
for i in range(1,101):
    if i%2==0:
        sum = sum + i 
    elif i%2 != 0 :
        sum = sum - i

print(sum)
# %%
i = 1
sum = 0
while i <= 100: 
    if i%2==0:
        sum = sum + i 
    else :
        sum = sum - i
    i += 1 # 위치 중요

print(sum)
# %%
#4 -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
sum = 0 
sum2 = 0
for i in range(3,100,4):
    sum = sum + i 

for j in range(-97,0,4):
    sum2 = sum2 + j

print(sum + sum2)


# %%
import datetime

# ------------------------------------------------
# 입력 함수 : 직원 자료를 리스트로 반환
# ------------------------------------------------
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas


# ------------------------------------------------
# 근속연수에 따른 근속수당 계산 함수
# ------------------------------------------------
def get_allowance(years):
    if years <= 3:
        return 150000
    elif years <= 8:
        return 450000
    else:  # 9년 이상
        return 1000000


# ------------------------------------------------
# 급여액(기본급+근속수당)에 따른 공제세율 계산 함수
# ------------------------------------------------
def get_tax_rate(pay):
    if pay >= 3000000:        # 300만원 이상
        return 0.5
    elif pay >= 2000000:      # 200만원 이상 300만원 미만
        return 0.3
    else:                     # 200만원 미만
        return 0.15


# ------------------------------------------------
# 처리 함수 : datas를 받아 가공 후 출력
# ------------------------------------------------
def processfunc(datas):
    this_year = datetime.datetime.now().year   # 현재 연도(근속연수 계산용)
    count = 0                                  # 처리 건수 카운트

    # 출력 헤더
    print('사번  이름   기본급    근속연수 근속수당 공제액   수령액')
    print('-' * 60)

    for row in datas:
        sabun, name, basic_pay, join_year = row   # 리스트 원소 언패킹

        # 1) 근속연수 = 현재연도 - 입사년도
        years = this_year - join_year

        # 2) 근속수당 : 근속연수표 기준으로 계산
        allowance = get_allowance(years)

        # 3) 급여액 = 기본급 + 근속수당
        pay = basic_pay + allowance

        # 4) 공제세율 : 급여액 구간 기준으로 계산
        tax_rate = get_tax_rate(pay)

        # 5) 공제액 = 급여액 * 공제세율
        deduction = int(pay * tax_rate)

        # 6) 수령액 = 급여액 - 공제액
        net_pay = pay - deduction

        # 결과 한 줄 출력
        print(f'{sabun:<4}{name:<6}{basic_pay:<10}{years:<8}{allowance:<8} {deduction:<8} {net_pay}')

        count += 1   # 처리 건수 증가

    print(f'처리 건수 : {count} 건')


# ------------------------------------------------
# 메인 실행부
# ------------------------------------------------
datas = inputfunc()      # 직원 자료 입력받기
processfunc(datas)       # 가공 후 출력