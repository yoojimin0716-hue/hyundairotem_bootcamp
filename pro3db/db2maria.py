#%%
#  원격 데이터베이스와 연동 프로그래밍
# MariaDB : 
# 준비1) IP(네트워크에서 컴퓨터나 장치를 구분 규약)) 주소 필요.
# 준비2) 연결용 Driver file(모듈) 필요

# pip install mysqlclinet

import MySQLdb
# 연결 정보 매핑 방법 1
"""conn = MySQLdb.connect(         # 연결 정보 dict를 원함 ,DB 연결 담당 

    host = '127.0.0.1', # 192.168.0.15, localhost
    user = 'root',
    password = '123',
    database='test',
    port=3306           # MariaDB/MySQL 서버가 기본적으로 사용하는 포트 번호

)        
"""
# 연결 정보 매핑 방법 2
config_data = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,  
    'charset' : 'utf8'
}

# 연결 정보 매핑 방법 3
import json

with open('dbconnect.json', mode = 'r', encoding='utf-8') as f:
    config_data = json.load(f)  # json 파일을 읽어 dict로 변환

def myFunc():
    try:
        # 방법 2,3
        conn = MySQLdb.connect(**config_data)
        # conn.autocommit(True)  # 자동 commit 모드, commit()을 하지 않아도 db에 반영됨
        # conn.autocommit(False) # 수동 commit 모드, commit()을 해야 db에 반영됨
        cursor = conn.cursor()


        # 자료추가
        # isql = "insert into sangdata(code, sang, su, dan) values(5,'마스크',5,'3000')"
        #cusror.execute(isql)
        #conn.commit()  # db에 반영, commit()을 하지 않으면 db에 반영되지 않는다.
        '''
        isql = "insert into sangdata values(%s,%s,%s,%s)"
        # INS_DATA = (6, '커피', 10, 5000) # tuple type 
        ins_data = 6, '커피', 10, 5000

        cursor.execute(isql, ins_data)
        conn.commit()  # db에 반영, commit()을 하지 않으면 db에 반영되지 않는다.
        '''

        # 자료 수정 
        '''
        usql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s"
        up_data = '물티슈',3,1000,5 # ('물티슈', 3, 1000, 5) 이거랑 동일함 
        cursor.execute(usql, up_data)
        conn.commit()  # db에 반영, commit()을 하지 않으면 db에 반영되지 않는다.
        '''

        '''usql = "update sangdata set sang = %s, su = %s, dan = %s where code = %s"
        up_data ='콜라',11,1000,6 # ('물티슈', 3, 1000, 5) 이거랑 동일함
        # insert, update, delete는 성공하면 성공갯수, 실패하면 0을 반환
        cou = cursor.execute(usql, up_data)
        print('수정된 레코드 수 :', cou)
        conn.commit()  # db에 반영, commit()을 하지 않으면 db에 반영되지 않는다.
        '''

        # 자료 삭제 
        code = '6';
        # dsql = "delete from sangdata where code = " + code
        # print(dsql)
        # 참고 : secure coding 가이드라인에 맞게 프로그래밍 해야한다.
        # 해킹 위험 : sql 인젝션은 사용자의 입력값을 검증하지 않는 웹 애플리케이션 


        # dsql = "delete from sangdata where code = '{0}'".format(code) # 추천 1
       
        dsql = "delete from sangdata where code = %s" # 추천 2 - 권장
        cursor.execute(dsql, code) # 튜플로 전달해야함, 튜플은 쉼표를 붙여야함

        cou = cursor.execute(dsql,code) # 삭제후 반환값 얻기
        if cou != 0:
            print('삭제 성공 :', cou)
              

        else:
            print('삭제 실패 :', cou)
        conn.commit()







        #자료읽기
        #sql = "select * from sangdata;"
        sql = "select code, sang,su,dan from sangdata"
        cursor.execute(sql)
        for data in cursor.fetchall():
            # print(data)
            print('%s %s %s %s'%data)

        print()
        cursor.execute(sql)
        for data in cursor:
            print(data[0], data[1], data[2], data[3])

        print()
        cursor.execute(sql)
        for code, sang, su, dan in cursor:
            print(code, sang, su, dan)

        print()
        cursor.execute(sql)
        for a, b, 수량, 단가 in cursor:
            print(a, b, 수량, 단가 * 1000)
        
        

    except Exception as e:
        print('처리 오류 :',e)
    finally:
        conn.close()


if __name__ == '__main__':          # 응용프로그램의 시작을 알리는 부분
    myFunc()