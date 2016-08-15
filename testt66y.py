#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import time
import datetime

list = []
TIME1 = datetime.datetime.now() - datetime.timedelta(days=2)
TIME2 = datetime.datetime.now() + datetime.timedelta(days=2)
TIME1 = TIME1.strftime("%Y-%m-%d")
TIME2 = TIME2.strftime("%Y-%m-%d")
# data = {'query':'query','begin_time':TIME1, 'end_time':TIME2}
# response=requests.get("http://www.t66y.com/thread0806.php?fid=7",data, headers=headers)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
def getcontent(page):
    response = requests.get("http://www.t66y.com/thread0806.php?fid=7&search=&page="+str(page),headers = headers)
    response.encoding = 'gb18030'
    soup = BeautifulSoup(response.text,"html.parser")
    for x in soup.findAll("tr",attrs={"class":"tr3 t_one"}):
        for y in x.findAll('h3'):
            for z in y.findAll('a'):
                try:
                    list.append(str(y.get_text())+'  '+'http://www.t66y.com/'+z['href']+'\r\n')
                except KeyError:
                    pass                    
        for o in x.findAll("td",attrs={"class":"tal y-style"}):
            for p in o.findAll("a",attrs={"class":"bl"}):
                try:
                    list.append(str(p.get_text())+'\r\n')
                except KeyError:
                    pass
            for p in o.findAll("div",attrs={"class":"f10"}):
                try:
                    list.append(str(p.get_text())+'\r\n')
                except KeyError:
                    pass
    
if __name__=="__main__":
    getcontent(1)
    with open('test.txt','wb+') as f:
        for content in list:
            f.write(content)