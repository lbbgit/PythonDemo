# -*- coding: utf-8 -*-
import urllib2
import codecs
def saveFile(filename, contents):
  f = codecs.open(filename, 'w', 'utf-8')
  f.write(contents)
  f.close();
url = "http://www.baidu.com"
url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%91%84%E5%BD%B1%E4%BD%9C%E5%93%81&oq=%E6%91%84%E5%BD%B1&rsp=1"
data = urllib2.urlopen(url).read()
data = data.decode('UTF-8')
saveFile("baidu_image.ini", data)
#print "------------"
#print(data)


#f = open('/path/to/the/file.txt')
f = open('baidu_image.ini')
txt = f.read()
