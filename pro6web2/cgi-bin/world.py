# cgi-bin/world.py 웹용 파이썬
import sys
sys.stdout.reconfigure(encoding='utf-8')  # 한글 깨짐 방지

v1 = '자료1'
v2 = '두번째 자료'

print('''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world</title>
</head>
<body>   
    <b></b> world 페이지</b>
    <br/>
    <img src = '../images/유지민 증사.jpeg'/>
    <br/>
    자료 출력 : {0}, {1}
    <br/>
    <a href = '../index.html'>메인으로</a>


    
</body>
</html>
'''.format(v1,v2))