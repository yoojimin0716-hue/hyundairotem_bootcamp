# 예외 처리 : 파일, 네트워크 , DB 작업, 실행 오류 등의 에러에 대처 
# try ~ except는 프로그램 실행 중 발생 할 수 있는 오류(Exeption)을 처리해서 프로그램이 갑자기 종료되지 않도록 하는 문법

# try 에는 오류가 발생할 가능성이 있는 코드를 작성하고,
# except에는 해당 오류가 발생했을떄 어떻게 처리할지를 작성한다 

# try :
# 실행할 코드 
# ,,,
# except 예외종류 :
# 오류 처리 코드 
# finally :
# 오류 유무와 상관없이 처리할구문 (반드시 실행할 코드) 

def divideFunc(a,b):
    return a/b

print('이런 저런 작업을 하다가 ,,,')
# c = divideFunc(5,2)
# print(c)

try :
    # 실행문 처리블럭(오류 가능 영역)
    c = divideFunc(5,2), #()안에 원래는 동적인 것이 들어감
    # c = divideFunc(5,0) # <-- 얘가 오류가 나기때문에 '계속' 이 출력이 안되고 , '두번째 값은 0을 주면 안돼여'가 출력이 된다.
    print(c)
    print('계속') 
    aa = [1,2]
    # print(aa[0])
    # print(aa[3])  # <--  오류가 나지만 except ZeroDivisionError:   는 오직 0으로 나누는 에러에서만 출력되기 때문에 그냥 터미널에서 오류가 남

    # 파일 읽기
    open('c:/work/ok.txt') # <-- 얘도 얘에 해당하는 오류 처리 클래스를 불러와야지만 터미널에서 오류가 안나고 except가 활동을 함 
except ZeroDivisionError:   
    #에러 발생시에만 처리하는 영역
    print('두번쨰 값은 0을 주면 안돼여')

except IndexError as err:
    print('참조 범위 오류 : ',err)

except Exception as e: # <-- 얘는 여러 오류를 다 한번에 받아서 활동하는 애이기 때문에 따로 처리하고싶은 오류가 있으면 얘보다 위에 위치해야함
    print('에러 : ',e)

finally :    # < -- try, except은 무조건 붙어다니지만 finally는 없어도됨
    print('에러 유무에 상관없이 반드시 수행됨')


print('프로그램 종료')