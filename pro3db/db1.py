# sqlite : 개인용 db, python에 기본 내장, 경량 dbms
# 서버를 운영하지않아 시스템 내에서 별도의 자원을 사용할 필요가 없다.

import sqlite3
print(sqlite3.sqlite_version)  # sqlite3 버전 확인

print()
# conn = sqlite3.connect('exam.db')  # exam.db 파일이 없으면 생성, 있으면 연결, 파일에 데이터 보관
conn = sqlite3.connect(':memory:')  # 메모리 상에서 db 생성, 프로그램 종료시 사라짐, ram에서만 작업, 휘발성 




try : 
    cur = conn.cursor()  # db 작업을 위한 커서 생성, SQL처리를 위한 객체 생성, SQL 실행 담당

    #테이블 생성
    cur.execute("CREATE TABLE IF NOT EXISTS friends (name TEXT, phone TEXT, addr text)")

    #자료 입력 
    cur.execute('INSERT INTO friends VALUES ("홍길동","010-111-1111","서초 1동")')
    cur.execute('INSERT INTO friends VALUES (?,?,?)',("이기자","010-111-2222","서초 2동"))

    inputdatas = ("신기해","010-111-1234","서초 3동")
    cur.execute('INSERT INTO friends VALUES (?,?,?)', inputdatas)

    inputdatas2 = (("신기한","010-111-3333","역삼 1동"),("신기루","010-111-4444","역삼 2동"))
    cur.executemany('INSERT INTO friends VALUES (?,?,?)', inputdatas2)

    conn.commit()  # db에 반영, commit()을 하지 않으면 db에 반영되지 않는다.

    #자료보기
    cur.execute('SELECT * FROM friends')
    # print(cur.fetchone())  # 한개의 레코드(행) 읽기 - record pointer가 있는 지점의 자료만 읽음
    print(cur.fetchall())  # 모든 레코드(행) 읽기 , 리스트 안에 튜플의 형태로 집어넣음, [('홍길동', '010-111-1111', '서초 1동') ,,,
    print()

    cur.execute('SELECT name, phone,addr FROM friends') # 입력한 칼럼의 순서대로 출력됨
    for r in cur:
        # print(r) 
        print('이름 : ', r[0], '전화 : ', r[1], '주소 : ', r[2])

except Exception as e:
    print('db 작업 실패 : ', e)
finally:
    conn.close()  # db 연결 종료

    