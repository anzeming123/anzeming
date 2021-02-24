import requests
import re
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',}
a = []
b = []
c='1613906145310'
d='0'
for i in range(0,1200):
    url = 'https://coral.qq.com/article/5963339045/comment/v2?callback=_article5963339045commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+d+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+c
    data = requests.get(url, headers=headers).content.decode()
    con='content":"(.*?),"'
    a= re.findall(con,data,re.S)
    b.append(a)
    d=re.findall('"last":"(.*?)"',data,re.S)[0].replace("\n","").replace("","")
    c=str(int(c)+1)
    print(i)
with open('comments.json','a',encoding='utf-8') as file:
    file.write(str(b)+'\n')

