import sqlite3 #self contains
#import pysqlite3
#import sqlite3database
import os

# 定义函数 触发异常
def mye(level):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行


try:
    mye(0)  # 触发异常
except "Invalid level!":
    print('except')
else:
    print('else')

try:
    mye(1) #触发异常
except "Invalid level!":
    print ('except')
else:
    print ('else')


os.system("cmd")
os.system("pause")


cx = sqlite3.connect("D:/db/PySqlite3Test.db")
cu = cx.cursor()

# commit()–事务提交
# rollback()–事务回滚
# close()–关闭一个数据库连接
# cursor()–创建一个游标
# execute()–执行sql语句
# executemany–执行多条sql语句
# close()–关闭游标
# fetchone()–从结果中取一条记录，并将游标指向下一条记录
# fetchmany()–从结果中取多条记录
# scroll()–游标滚动

#region createTable Try
try:
    cu.execute('drop table catalog')
    cx.commit();
except sqlite3.OperationalError :
    print ("Catch drop eroor: sqlite3.OperationalError");
else:
    print ("drop table成功");

try:
    cu.execute('create table if not exists catalog(id integer primary key,pid integer,name varchar(10) UNIQUE）')
    #cu.execute('create table catalog(id integer primary key,pid integer,name varchar(10) UNIQUE）')
except sqlite3.OperationalError:
    print ("Catch Error: sqlite3.OperationalError");
else:
    print ("create table成功");
#endregion


cu.execute("insert into catalog values(0, 0, 'name1')")
cu.execute("insert into catalog values(1, 0, 'hello')")
# cx.commit()

cu.execute("select * from catalog") #要提取查询到的数据,使用游标的fetch***函数,如:
print (cu.fetchall()) # [(0, 0, u'name1'), (1, 0, u'hello')]

cu.execute("update catalog set name='name2' where id = 0")

cx.commit()

cu.execute("delete from catalog where id = 1")

cx.commit()
cx.close();


#conn.execute("create table if not exists t1(id integer primary key autoincrement, name varchar(128), info varchar(128))")
