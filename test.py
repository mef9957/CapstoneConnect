#!/usr/bin/python
print("Content-Type: text/html\n\n")
import pandas
input1 = "Tarek%20Abdoun"
input2 = input1.replace("%20", ' ')

html_txt = """
<!DOCTYPE HTML>
<html>
<head>
</head>
<body>
<h1>hellooo</h1>
<p>1: {}</p>
<p>2: {}</p>
</body>
</html>
""".format(input1, input2)

print(html_txt)
