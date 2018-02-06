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
    reg = r'https://.[^\s]+?.jpg|https://.[^\s]+?.png'
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0
    print(imglist)
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'R:\%s.jpg' %x)
        #urllib.urlretrieve(imgurl,'R:\\'+x+'.jpg')
        x+=1
#html = getHtml("https://tieba.baidu.com/p/4379053321?see_lz=1")
#print getImg(html)

import re
text = "“JGood is a handsome boy, he is cool, clever, and so on…” "
regex = re.compile(r'\w*oo\w*')
print regex.findall(text) #查找所有包含’oo’的单词

# 1).re.I(re.IGNORECASE): 忽略大小写
# 2).re.M(MULTILINE): 多行模式，改变’^’和’$’的行为
# 3).re.S(DOTALL): 点任意匹配模式，改变’.’的行为
# 4).re.L(LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# 5).re.U(UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# 6).re.X(VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释