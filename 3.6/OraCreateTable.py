import cx_Oracle
import os
#建立和数据库系统的连接
conn = cx_Oracle.connect('tdm8032/sa@orcl')
#获取操作游标
cursor = conn.cursor()


cursor.execute("""select * from tb_user""")

three = cursor.fetchall();
print (three);
print ('count',three.count);
for row in three:
    print (row)  # 打印所有结果

try:
    cursor.execute("""select * from err""")
    err = cursor.fetchall();
    print (err);
    fh = open("testfile", "w");
    fh.write("这是一个测试文件，用于测试异常!!");
except IOError:
    print ("Error: 没有找到文件或读取文件失败");
except WindowsError:
    print ("Error: windowsError");
except OSError:
    print ("Error: OSERROR");
except cx_Oracle.DatabaseError:
    print ("Error: cx_Oracle.DatabaseError");
else:
    print ("内容写入文件成功");
    fh.close();


print ('closing');
cursor.close();
conn.close();
