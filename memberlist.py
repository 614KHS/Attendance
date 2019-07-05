import cgi
import psycopg2
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


conn = psycopg2.connect("dbname=attendance user=postgres password=password")
cur = conn.cursor()

form = cgi.FieldStorage()
name = form.getvalue('name','')



message = "メンバーリスト"

print("Content-Type: text/html; charset=utf-8")
print("")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title> メンバリスト </title>
</head>
<body>

<h1>{message}</h1>
<form action="/cgi-bin/memberlist.py" method="post">
<p>
<label for="items"> メンバーの追加 </label>
<br>
名前
<input type="text" name="name" id="name" size="10" maxlength="8" value="{name}"/>
</p>
<p>
</form>
<form name="send" action="/cgi-bin/memberlist.py" method="get">
<input type="submit" value="送信" />
</form>
</p>
<p>
</p>
<table>
""".format(message=message, name=name))


cur.execute("select * from member")

for row in cur:

        print("<tr> "+"<td>"+"<button type=submit>"+str(row[1]) +
              "</button>"+"</td>"+"<td><a id='"+str(row[1])+"'>出</a></td>"+"</tr>"+
              "<script type='text/javascript'>" +
              "document.getElementById('" + str(row[1]) + "').onclick = function() {" +
              "if(this.innerHTML == '欠'){"+
                     "this.innerHTML = '出';"+
                     "}else{"+
                    "this.innerHTML = '欠';"+
                    "};"
                    "};"+
              "</script>"
              )

print("""
</table>
</form>

</body>
""")


print("""
</html>
""")


#なぜかいかない
#sql = "insert into member(name) values(%s)"
# #cur.execute(sql,[name])

conn.commit()

cur.close()
conn.close()
