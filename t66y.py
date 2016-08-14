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
    response = requests.get("http://www.t66y.com/thread0806.php?fid=7&search=&page="+str(page),headers = headers)
    response.encoding = 'gb18030'
    #unzip(respone.read()).decode(encoding,'ignore')
    soup = BeautifulSoup(response.text,"html.parser")
    for x in soup.findAll('h3'):
        for y in x.findAll('a'):
            try:
                list.append(str(y.get_text())+'http://www.t66y.com/'+y['href']+'\r\n')
            except KeyError:
                pass
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
    with open('t66y.txt','wb+') as f:
        for content in list:
            f.write(content)
endtime = time.clock()
print u"总共耗时: %f s" % (endtime - starttime)