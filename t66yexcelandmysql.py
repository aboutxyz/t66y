#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import time
import datetime
import threading
import xlwt
import MySQLdb
from time import sleep
from fake_useragent import UserAgent
ua = UserAgent()

starttime = time.clock()

TIME1 = datetime.datetime.now() - datetime.timedelta(days=2)
TIME2 = datetime.datetime.now() + datetime.timedelta(days=2)
TIME1 = TIME1.strftime("%Y-%m-%d")
TIME2 = TIME2.strftime("%Y-%m-%d")
# data = {'query':'query','begin_time':TIME1, 'end_time':TIME2}
# response=requests.get("http://www.t66y.com/thread0806.php?fid=7",data, headers=headers)
headers = {
    'Host': 'www.t66y.com',
    'User-Agent': ua.random,
    'Accept-Encoding': '',
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
    # proxies = {'http':'http://123.56.74.13:8080'}
    # response = requests.get("http://www.t66y.com/thread0806.php?fid=7&search=&page="+str(page),headers = headers,proxies=proxies)
    response = requests.get("http://www.t66y.com/thread0806.php?fid=7&search=&page="+str(page),headers = headers)
    response.encoding = 'gb18030'
    #unzip(respone.read()).decode(encoding,'ignore')
    soup = BeautifulSoup(response.text,"html.parser")
    for x in soup.findAll("tr",attrs={"class":"tr3 t_one"}):
        for y in x.findAll('h3'):
            for z in y.findAll('a'):
                try:
                    templist.append(str(z.get_text()))
                    templist.append('http://www.t66y.com/'+z['href'])
                except KeyError:
                    pass                
        for o in x.findAll("td",attrs={"class":"tal y-style"}):
            for p in o.findAll("a",attrs={"class":"bl"}):
                try:
                    templist.append(str(p.get_text()))
                except KeyError:
                    pass
            for q in o.findAll("div",attrs={"class":"f10"}):
                try:
                    templist.append(str(q.get_text()))
                except KeyError:
                    pass
    list.extend(templist)
page = 1
list = []
def Mutipleth():
    threads = []
    count = 0
    for url in range(2,81):
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
    db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='900502',db='t66y',port=3306,charset='utf8')
    cursor=db.cursor()
    try:
        for i in range((len(list)-1)/4):
            actsql = "INSERT INTO t66y(TITLE,LINK,AUTHOR,TIME) VALUES (%s,%s,%s,%s)"
            cursor.execute(actsql,(str(list[4*i]),str(list[4*i+1]),str(list[4*i+2]),str(list[4*i+3])))
            db.commit()
    except:
        db.rollback()
    db.close()
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1',cell_overwrite_ok=True)
    table.write(0,0,'title')
    table.write(0,1,'link')
    table.write(0,2,'author')
    table.write(0,3,'time')
    for i in range((len(list)-1)/4):
        row = i+1
        for j in range(4):
            table.write(row, j, str(list[4*i+j]).decode('utf-8'))
    file.save('democ.xls')
endtime = time.clock()
print u"总共耗时: %f s" % (endtime - starttime)