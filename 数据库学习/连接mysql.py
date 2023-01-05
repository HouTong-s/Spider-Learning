import MySQLdb
db_connect = MySQLdb.connect(db="pachong", host="localhost", user="root",password="houzipashu.123", charset="utf8")

db_cursor = db_connect.cursor()
#新增数据
sql='insert into hot(name, author, type, form)values("道君", "未知", "仙侠", "连载")'
db_cursor.execute(sql)


#修改数据
sql='update hot set author = "跃千愁" where name="道君"'
db_cursor.execute(sql)


#查询表hot中type为仙侠的数据
sql='select * from hot where type="仙侠"'
db_cursor.execute(sql)


#删除表中type为仙侠的数据
#sql='delete from hot where type="仙侠"'
#db_cursor.execute(sql)

#必须调用commit()以实现最终修改数据库
db_connect.commit()

db_cursor.close()
db_connect.close()