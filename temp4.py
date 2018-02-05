# -*- coding: utf-8 -*-
import urllib2
import codecs
def saveFile(filename, contents):
  f = codecs.open(filename, 'w', 'utf-8')
  f.write(contents)
  f.close();

f = open('baidu_image.ini')
txt = f.read()
#print txt



from bs4 import BeautifulSoup
soup = BeautifulSoup(f, 'html.parser')
items = soup.find_all('img', class_='blessing-img')
print items

soup = BeautifulSoup('baidu_image.ini','html.parser')
print(soup.select('img'))


#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urllib2.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
    reg = r'src="(.+?\.jpg)" '
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    print(imglist)
    for imgurl in imglist:
        urllib2.urlretrieve(imgurl,'R:\\%s.jpg' % x)
        x+=1
html = getHtml("https://tieba.baidu.com/p/4379053321?see_lz=1")
print(html)
print getImg(html)