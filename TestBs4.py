from bs4 import BeautifulSoup

myHtml='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this my title</title>
</head>
<body>
<h1>this is h1,love you</h1>
<h1>這是另外一個 h1 tag</h1>
<h2>this is h2,小一點</h2>
<p>this is Mac,i love you guys, Yes!!</p>

</body>
</html>'''

myParser = BeautifulSoup(myHtml,'html.parser')
#myH1 = myParser.find('h1')
#print(myH1)
#print(myH1.string)
#myH2 = myParser.find('h2')
#print(myH2.string)

myH1 = myParser.findAll('h1')
#print(myH1)
for i in myH1:
    #print(i)
    #print(i.string)
    if "這是" in i.string:
        print(i.string)





