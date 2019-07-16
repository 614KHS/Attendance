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



message = "メンバーリスト"

print("Content-Type: text/html; charset=utf-8")
print("")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../css/simple.css" />
<title> メンバリスト </title>
</head>
<body>
<button type="button" id="topbtn" onclick="location.href='toppage.py'">トップに戻る</button>
<h1>{message}</h1>
<form action="/cgi-bin/memberlist.py" method="post">
<p>
    <label for="items"> メンバーの追加 </label>
    <br>
    名前
    <input type="text" name="name" id="name" size="10" maxlength="8" value="{name}"/>
</p>
<p>
    <input type="submit" id="sbbtn" value="送信" />
    </form>
</p>
</form>
<center>
<iframe src="membertop.py">
このページでは、インラインフレームを使用しています。
対応しているブラウザで表示願います。
</iframe>
</center>
</body>
</html>
""".format(message=message, name=name))


if name != '':
    sql = "insert into member(name) values(%s)"
    #sql = "delete from member  where member_id = %s"
    cur.execute(sql,[name])

conn.commit()

cur.close()
conn.close()
