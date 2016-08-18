#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import time
import datetime
import threading

starttime = time.clock()

TIME1 = datetime.datetime.now() - datetime.timedelta(days=2)
TIME2 = datetime.datetime.now() + datetime.timedelta(days=2)
TIME1 = TIME1.strftime("%Y-%m-%d")
TIME2 = TIME2.strftime("%Y-%m-%d")
# data = {'query':'query','begin_time':TIME1, 'end_time':TIME2}
# response=requests.get("http://www.t66y.com/thread0806.php?fid=7",data, headers=headers)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
# def unzip(data):
    # import gzip
    # import StringIO
    # data = StringIO.StringIO(data)
    # gz = gzip.GzipFile(fileobj=data)
    # data = gz.read()
    # gz.close()
    # return data
def getcontent(page):
    templist = []
    response = requests.get("http://www.t66y.com/thread0806.php?fid=7&search=&page="+str(page),headers = headers)
    response.encoding = 'gb18030'
    #unzip(respone.read()).decode(encoding,'ignore')
    soup = BeautifulSoup(response.text,"html.parser")
    for x in soup.findAll("tr",attrs={"class":"tr3 t_one"}):
        for y in x.findAll('h3'):
            for z in y.findAll('a'):
                try:
                    templist.append(str(z.get_text())+'  '+'http://www.t66y.com/'+z['href']+'\r\n')
                except KeyError:
                    pass                    
        for o in x.findAll("td",attrs={"class":"tal y-style"}):
            for p in o.findAll("a",attrs={"class":"bl"}):
                try:
                    templist.append(str(p.get_text())+'\r\n')
                except KeyError:
                    pass
            for q in o.findAll("div",attrs={"class":"f10"}):
                try:
                    templist.append(str(q.get_text())+'\r\n')
                except KeyError:
                    pass
        list.extend(templist)
page = 1
list = []
def Mutipleth():
    threads = []
    count = 0
    for url in range(1,95):
        t = threading.Thread(target=getcontent,args=(url,))
        count = count+1
        print u"正在抓取"+str(count)+u"张网页"
        threads.append(t)
    for task in threads:
        task.start()
    for task in threads:
        task.join()


if __name__ == "__main__":
    Mutipleth()
    with open('t66yupdate.txt','wb+') as f:
        for content in list:
            f.write(content)
endtime = time.clock()
print u"总共耗时: %f s" % (endtime - starttime)