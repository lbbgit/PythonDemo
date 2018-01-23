#!/usr/bin/python
# -*- coding: cp936 -*-

import sqlite3
import HTMLParser
import codecs
import time

f=codecs.open('note.txt','a',"utf-8") #以追加方式打开一个文件

conn = sqlite3.connect('note.db') #打开sqlite数据库

print "Opened database successfully";

#执行查询语句，返回一个cursor
cursor = conn.execute("select created,weather,address,latitude,longitude,content from tb_notescontents,tb_notes where tb_notescontents.note_guid=tb_notes.guid")

#遍历每一行
for row in cursor:

    #取出改行的每一列
    created= row[0]
    weather= row[1]
    address= row[2]
    latitude= row[3]
    longitude= row[4]
    content= row[5]

    html_parser = HTMLParser.HTMLParser()

    d = time.localtime(created/1000)
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',d)

    #因为原理的内容是经过html转义了，所以要转回来，形如：&#20170;&#22825;&#65292;
    weather = html_parser.unescape(weather) 
    address = html_parser.unescape(address) 
    content = html_parser.unescape(content) 


    f.write(currentTime) #写入文件
    f.write('              ')
    f.write(weather)
    f.write('              ')
    f.write(address)
    f.write('              ')
    f.write(content)

    f.write('\n')
    f.write('\n')
    f.write('\n')

conn.close() ## 关闭数据库
f.close() #关闭文件
print "Operation done successfully";
