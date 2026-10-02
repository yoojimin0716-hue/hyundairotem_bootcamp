from flask import Flask, render_template,request, redirect, url_for,flash,session
import pymysql
import os



app = Flask(__name__)
app.secret_key = "abcd1234"

#MariaDB 연결 정보 
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3305"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")
DB_NAME = os.getenv("DB_NAME", "test")

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4", #오타 수정: urf8mb4 -> utf8mb4 (전 세계 문자(한글 포함) + 이모지까지 처리 가능)
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )

@app.get("/")
def index():
    return redirect(url_for("login_form"))

@app.get("/login")
def login_form():
    return render_template("login.html")

@app.post("/login")
def login_post():
    jikwonno_raw = (request.form.get("jikwonno") or "").strip()
    jikwonname = (request.form.get("jikwonname") or "").strip()

    if not jikwonno_raw.isdigit() or not jikwonname:
        flash("직원 번호는 숫자여야 합니다.")
        return redirect(url_for("login_form"))

    jikwonno = int(jikwonno_raw)

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT jikwonno,jikwonname FROM jikwon WHERE jikwonno = %s AND jikwonname = %s""", (jikwonno, jikwonname))
            me = cur.fetchone()
            if not me:
                flash("로그인 실패 !: 직원 번호와 이름이 일치하지 않습니다.")
                return redirect(url_for("login_form"))
            # 로그인 성공
            cur.execute("""SELECT jikwonno,jikwonname,busername,jikwonjik,jikwonpay,
                year(jikwonibsail) as jikwonibsail_year
                from jikwon inner join buser
                on busernum=buserno order by jikwonno""")
            rows = cur.fetchall()

        #세션 생성 : 직원번호와 이름이 일치하면 세션에 저장
        session["jikwonno"] = me["jikwonno"]
        session["jikwonname"] = me["jikwonname"]
        return render_template("jikwonlist.html", rows=rows, login_user=me)
            
            
    finally:
        conn.close()

@app.get("/gogek/<int:jikwonno>")
def gogek_list(jikwonno:int):
    if "jikwonno" not in session:
        flash("로그인 후 이용 가능합니다.")
        return redirect(url_for("login_form"))

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            #gogekdamsano(담당직원번호)로 고객검색
            cur.execute("""SELECT gogekno,gogekname,gogektel
                from gogek where gogekdamsano=%s order by gogekno""", (jikwonno,))
            rows = cur.fetchall()

            #직원 이름도 같이 표시하기
            cur.execute("SELECT jikwonname from jikwon where jikwonno=%s", (jikwonno,))
            emp = cur.fetchone()

        return render_template("gogek_list.html", rows=rows, empno=jikwonno, empname=(emp["jikwonname"] if emp else ""))
                
    finally:
        conn.close()

@app.get("/jikwon")
def jikwon_list():
    if "jikwonno" not in session:
        flash("로그인 후 이용 가능합니다.")
        return redirect(url_for("login_form"))

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT jikwonno,jikwonname,busername,jikwonjik,jikwonpay,
                year(jikwonibsail) as jikwonibsail_year
                from jikwon inner join buser
                on busernum=buserno order by jikwonno""")
            rows = cur.fetchall()

        login_user={
            "jikwonno": session.get("jikwonno"),
            "jikwonname": session.get("jikwonname")

        }

        return render_template("jikwonlist.html", rows=rows, login_user=login_user)
                
    finally:
        conn.close()

@app.post("/logout")
def log_out():
    session.clear()
    return redirect(url_for("login_form"))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#로그인 후 직원이 담당하는 고객을 보는 창으로 가고, 그 웹의 주소를 복사한뒤, 처음 페이지로 돌아가서 그 주소를 
#복사한뒤, 주소창에 붙여넣기하면, 세션이남아있으므로 다시 로그인하지않고 바로 고객리스트가 보인다.

#하지만, 로그아웃을 하고나서, 그 주소를 붙여넣기하면, 세션이 없으므로 로그인창으로 이동한다.