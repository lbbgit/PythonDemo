import pymssql
#version 3.6 to high!!!
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
server="127.0.0.1"
database="GiantSql"
user="sa"
password="sbf"
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()

# 新建、插入操作
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# 如果没有指定autocommit属性为True的话就需要调用commit()方法
conn.commit()

# 查询操作
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 也可以使用for循环来迭代查询结果
# for row in cursor:
#     print("ID=%d, Name=%s" % (row[0], row[1]))

# 关闭连接
conn.close()






c1 = conn.cursor() 
c2 = conn.cursor()  
c1.execute('SELECT ...')
c1_list = c1.fetchall()

c2.execute('SELECT ...')
c2_list = c2.fetchall()




conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cursor:
    print("ID=%d, Name=%s" % (row['id'], row['name']))
conn.close()



with pymssql.connect(server, user, password, database) as conn:
    with conn.cursor(as_dict=True) as cursor:
        # 创建存储过程
        cursor.execute("""
        CREATE PROCEDURE FindPerson
            @name VARCHAR(100)
        AS BEGIN
            SELECT * FROM persons WHERE name = @name
        END
        """)

        # 调用存储过程
        cursor.callproc('FindPerson', ('Jane Doe',))
        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))