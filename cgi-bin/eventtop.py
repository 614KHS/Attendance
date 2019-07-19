import cgi
import psycopg2
import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


conn = psycopg2.connect("dbname=attendance user=postgres password=password")
cur = conn.cursor()


print("Content-Type: text/html; charset=utf-8")
print("")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="../css/simple.css" />
<link rel="stylesheet" href="../css/iframeCSS.css" />
<body>
<table>
""")



cur.execute("select * from event")

for row in cur:

        print("<tr> "+"<td>"+"<button type=submit>"+str(row[1]) +str(row[2])+
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
</html>
""")

conn.commit()

cur.close()
conn.close()
