import cgi
import psycopg2
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


conn = psycopg2.connect("dbname=attendance user=postgres password=password")
cur = conn.cursor()

form = cgi.FieldStorage()
name = form.getvalue(str('name'),'')
day = form.getvalue('day','')
day2 = form.getvalue('day2','')
day3 = form.getvalue('day3','')
days = day + '-'+ day2+ '-'+day3



message = "イベントリスト"

print("Content-Type: text/html; charset=utf-8")
print("")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title> イベントリスト </title>
<link rel="stylesheet" href="../css/simple.css" />
</head>
<body>

<h1>{message}</h1>
<form action="/cgi-bin/eventlist.py" method="post">
<p>
<label for="items">イベントの追加 </label>
<br>
名前
<input type="text" name="name" id="name" size="20" maxlength="15" value="{name}"/>
<br>
西暦年
<input type="text" name="day" id="day" size="4" maxlength="4" value="{day}"/>
<br>
<input type="text" name="day2" id="day2" size="2" maxlength="2" value="{day2}"/>
月

<input type="text" name="day3" id="day3" size="2" maxlength="2" value="{day3}"/>
日
<br>
<p>
<input type="submit" value="送信" />
</p>
</form>
<p>
<button type="button"onclick="location.href='toppage.py'">トップに戻る</button>
</p>
</form>
<center>
<iframe src="eventtop.py">
このページでは、インラインフレームを使用しています。
対応しているブラウザで表示願います。
</iframe>
</center>
</body>
</html>
""".format(message=message, name=name,day=day,day2=day2,day3=day3,))

if name != '':

    sql = "insert into event(name,day) values(%s,%s)"
    cur.execute(sql,[name,days])

conn.commit()

cur.close()
conn.close()
