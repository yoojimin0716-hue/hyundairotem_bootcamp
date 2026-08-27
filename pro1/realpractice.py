sum = 0 
count = 0
for i in range(1,101):
    if i%3 == 0 or i%4 == 0 and i%7 != 0:
        print(i, end = ' ')
        count += 1
        sum = sum + i
print()
print(f'건수 : {count}')
print(f'배수의 총합 : {sum}')

