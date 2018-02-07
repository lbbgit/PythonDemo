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



#region

#create Table,Insert One ,Insert Many
cursor.execute("""create table tb_user(id number, name varchar2(50),password varchar(50),primary key(id))""")

cursor.execute("""insert into tb_user values(1,'admin','password')""");
param = {'id': 2, 'n': 'admin', 'p': 'password'}
cursor.execute('insert into tb_user values(:id,:n,:p)', param);

# 一次插入多条数据
param = [{'id': 3, 'n': 'sanma', 'p': 'password3'}, {'id': 4, 'n': 'sihu', 'p': 'pass4ord4'},
         {'id': 5, 'n': 'Wulon', 'p': 'password5'},
         {'id': 6, 'n': 'Liuda', 'p': 'password6'}];
cursor.executemany('insert into tb_user values(:id,:n,:p)', param);

# 再一次插入多条数据
param = [];
for i in range(7, 11):  # [7,8,9,10]
    param.append((i, 'user' + str(i), 'password' + str(i)))
cursor.executemany('insert into tb_user values(:1,:2,:3)', param);

print('条件查询')
cursor.prepare("""select * from tb_user where id <= :id""")
cursor.execute(None, {'id': 5})
for row in cursor:  # 相当于fetchall()
    print(row)
# endregion

cursor.close();
conn.commit(); #不提交可是很好玩哦！
conn.close();

os.system("pause")
print ('after p')
