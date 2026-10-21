# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.
# 
# Django 또는 Flask 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.
# 
#  
# 
#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
# 
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
# 
#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
# 
#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.
# 
#    4) 성별, 직급별 빈도표를 출력하시오.
# 
#    5) 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력 
#        출력 항목: 부서명, 직원명, 연봉
#    6) 부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율(%) 
#        비율 계산 (%)은 dept_ratio = (dept_count / total * 100).round(2)
#       결과를 DataFrame으로 출력
#       예: 총 인원: 30명
#            영업부 20%
#            총무부 30%
#            전산부 5%
#            ...

#%%
from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')          # 서버(창 없는 환경)에서 그래프 그리기
import matplotlib.pyplot as plt
import koreanize_matplotlib    # 한글 폰트
import io, base64
from markupsafe import escape

app = Flask(__name__)

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

def get_connection():
    return pymysql.connect(**config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow", methods=['GET','POST'])
def dbshow():
    # 1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수 (join) / 부서번호, 직원명 오름차순
    sql = """
        select j.jikwonno as 사번, j.jikwonname as 직원명,
        b.busername as 부서명, j.jikwonjik as 직급,
        j.jikwonpay as 연봉,
        timestampdiff(year, j.jikwonibsail, now()) as 근무년수,
        j.jikwongen as 성별
        from jikwon j inner join buser b
        on j.busernum = b.buserno
        order by b.buserno asc, j.jikwonname asc
    """

    # SQL 실행
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]

    df = pd.DataFrame(rows, columns=cols)

    if df.empty:
        msg = "직원 정보가 없어요"
        return render_template("dbshow.html",
                               jikwondata=msg, busertstats=msg, jikstats=msg,
                               chartdata="", crossdata=msg, topdata=msg,
                               ratiodata=msg, total=0)

    # 1) 직원 목록
    jikwondata = df[["사번","직원명","부서명","직급","연봉","근무년수"]].to_html(index=False)

    # 2) 부서명별 / 직급별 연봉합, 연봉평균
    buser_stats = (
        df.groupby("부서명")["연봉"]
        .agg(연봉합="sum", 연봉평균="mean")
        .round(2)
        .reset_index()
    )
    busertstats = buser_stats.to_html(index=False)

    jik_stats = (
        df.groupby("직급")["연봉"]
        .agg(연봉합="sum", 연봉평균="mean")
        .round(2)
        .reset_index()
    )
    jikstats = jik_stats.to_html(index=False)

    # 3) 부서명별 연봉합, 평균 세로막대 그래프
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    ax1.bar(buser_stats["부서명"], buser_stats["연봉합"], color='steelblue')
    ax1.set(title='부서별 연봉합', xlabel='부서명', ylabel='연봉합')
    ax2.bar(buser_stats["부서명"], buser_stats["연봉평균"], color='orange')
    ax2.set(title='부서별 연봉평균', xlabel='부서명', ylabel='연봉평균')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    chartdata = base64.b64encode(buf.getvalue()).decode('utf-8')

    # 4) 성별, 직급별 빈도표
    crosst = pd.crosstab(
        index=df['성별'], columns=df['직급'], margins=True, margins_name='합계'
    )
    crossdata = crosst.to_html()

    # 5) 부서별 최고 연봉자
    top_df = df.loc[df.groupby("부서명")["연봉"].idxmax(), ["부서명","직원명","연봉"]]
    topdata = top_df.to_html(index=False)

    # 6) 부서별 직원 비율(%)
    total = len(df)
    dept_count = df["부서명"].value_counts()
    dept_ratio = (dept_count / total * 100).round(2)
    ratio_df = pd.DataFrame({
        "부서명": dept_count.index,
        "인원수": dept_count.values,
        "비율(%)": dept_ratio.values
    })
    ratiodata = ratio_df.to_html(index=False)

    return render_template("dbshow.html",
                           jikwondata=jikwondata,
                           busertstats=busertstats,
                           jikstats=jikstats,
                           chartdata=chartdata,
                           crossdata=crossdata,
                           topdata=topdata,
                           ratiodata=ratiodata,
                           total=total)

if __name__ == '__main__':
    app.run(debug=True)