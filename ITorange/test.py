import mysql.connector
import pickle
data_path=open('compdb.pkl','rb')
complist=pickle.load(data_path)
passwd=input('Please input your password:')
config={'host':'127.0.0.1',
	'user':'root',
	'password':passwd,#######need to clear before upload
	'port':3306,
	'database':'ITOrange',
	'charset':'utf8',
	}
def main():
	try:
		cnn=mysql.connector.connect(**config)
	except mysql.connector.Error as e:
		print('connect failed!{}'.format(e))
	sql_insert1=r"insert into student (name, age) values ('orange', 20)"
	a=r"insert into student (name,age) values ('rose',16)"
	#sql_create_table='CREATE TABLE student \
	#(id int(10) NOT NULL AUTO_INCREMENT primary key,\
	#name varchar(10) DEFAULT NULL,\
	#age int(3) DEFAULT NULL)'

	cursor=cnn.cursor()
	cursor.execute(sql_insert1)
	cursor.execute(a)
	cnn.commit()
	cnn.close()

main()

