### python 54번 문제 1
# 문1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

 

# 직원번호 입력 : _______

# 직원명 입력 : _______

# 직원번호 직원명 부서명 부서전화 직급 성별

#    1         홍길동 총무부 111-1111 이사 남           <== 홍길동으로 로그인한 경우
import MySQLdb

from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),
    'charset':os.getenv('DB_CHARSET')

}

def LoginFunc():
    conn = None
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jikwon_no = input("직원번호:")
        jikwon_name = input("직원이름:")
        if jikwon_no == "" or jikwon_name =="":
            print("로그인 정보를 입력하세요")
            return
    
        sql = """
                select 
                j.jikwonno as 직원번호, j.jikwonname as 직원명,
                b.busername as 부서명, b.busertel as 부서전화, j.jikwonjik as 직급, j.jikwongen as 성별
                from jikwon j 
                left outer join buser b on j.busernum = b.buserno
                where jikwonno = %s and jikwonname = %s  
        """

        # sql 실행
        cursor.execute(sql,(jikwon_no, jikwon_name))

        # 로그인 성공 직원 정보 출력
        data = cursor.fetchone()

        if data:
            print("로그인 성공")
            print("직원번호 : ", data[0])
            print("직원명 : ", data[1])
            print("부서명 : ", data[2])
            print("부서전화 : ", data[3])
            print("직급 : ", data[4])   
            print("성별 : ", data[5])

        else:
            print("로그인 실패 : 입력자료 확인하세요")

    except Exception as e:
        print("에러:",e)
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    LoginFunc()

### 문제 1-1 
# 문1-1) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력

# 해당 직원이 근무하는 부서 내의 직원 전부를 직급별 오름차순우로 출력. 
# 직급이 같으면 이름별 오름차순한다.

# 직원번호 입력 : _______

# 직원명 입력 : _______

# 직원번호 직원명 부서명 부서전화 직급 성별

# 1 홍길동 총무부 111-1111 이사 남

'''

직원 수 :

 

이어서 로그인한 해당 직원이 관리하는 고객 자료도 출력한다.

고객번호 고객명 고객전화 나이

1 사오정 555-5555 34

관리 고객 수 :
'''
import MySQLdb  

from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),
    'charset':os.getenv('DB_CHARSET')

}

def LoginFunc():
    conn = None
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jikwon_no = input("직원번호:")
        jikwon_name = input("직원이름:")
        if jikwon_no == "" or jikwon_name =="":
            print("로그인 정보를 입력하세요")
            return
    
        sql = """
                select 
                j.jikwonno as 직원번호, j.jikwonname as 직원명,
                b.busername as 부서명, b.busertel as 부서전화, 
                j.jikwonjik as 직급, j.jikwongen as 성별
                from jikwon j 
                left outer join buser b on j.busernum = b.buserno
                where jikwonno = %s and jikwonname = %s  
        """

        # sql 실행
        cursor.execute(sql,(jikwon_no, jikwon_name))

        # 로그인 성공 직원 정보 출력
        data = cursor.fetchone()

        if data:
            print("로그인 성공")
            print("직원번호 : ", data[0])
            print("직원명 : ", data[1])
            print("부서명 : ", data[2])
            print("부서전화 : ", data[3])
            print("직급 : ", data[4])   
            print("성별 : ", data[5])

        else:
            print("로그인 실패 : 입력자료 확인하세요")

    except Exception as e:
        print("에러:",e)
    finally:
        if conn: conn.close()

if __name__ == "__main__":
    LoginFunc()
 



