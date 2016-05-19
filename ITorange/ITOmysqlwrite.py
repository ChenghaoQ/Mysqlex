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
	cursor=cnn.cursor()
	for company in complist:
		try:
			data_insert="insert company (company,groups,location,time,status,description) values (%s,%s,%s,%s,%s,%s)"
			data=(company[0],company[2],company[3],company[4],company[5],company[1])
			cursor.execute(data_insert,data)
			print("%s has been insert in table company!"%company[0])
			
		except mysql.connector.Error as e:
			print('insert data error!{}'.format(e))
	cnn.commit()
	cursor.close()
	cnn.close()

main()




