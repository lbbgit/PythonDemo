import cx_Oracle
import os
#建立和数据库系统的连接
conn = cx_Oracle.connect('tdm8032/sa@orcl')
#获取操作游标
cursor = conn.cursor()


cursor.execute("""select * from dps_user""")
one = cursor.fetchone()
print (one)
# print ('1: id:%s,username:%s,password:%s' % one)

# 获取3条记录!!!注意游标已经到了第二条
two = cursor.fetchmany(3)
print ('2 and 3:', two[0], two[1])
print (two[2])

# time.sleep(2)
# raw_input( )
# subprocess.call("pause",shell=True)

os.system("pause")

# 获取其余记录!!!注意游标已经到了第四条
three = cursor.fetchall();
for row in three:
    print (row)  # 打印所有结果

cursor.close();
conn.close();

os.system("pause")
print ('after p')
