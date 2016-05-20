import mysql.connector
import pickle
data_path=open('3dlot.pkl','rb')
lotlot=pickle.load(data_path)
passwd=input('Please input your password:')
config={'host':'127.0.0.1',
	'user':'root',
	'password':passwd,#######need to clear before upload
	'port':3306,
	'database':'Lottery',
	'charset':'utf8',
	}
def main():
	try:
		cnn=mysql.connector.connect(**config)
	except mysql.connector.Error as e:
		print('connect failed!{}'.format(e))
	cursor=cnn.cursor()
	for lot in lotlot:
		try:
			data_insert="insert 3dlot (issue_num,date,win_number,test_number,Sales,issurance,win_price) values (%s,%s,%s,%s,%s,%s,%s)"
			data=(lot[0],lot[1],lot[2],lot[3],lot[4],lot[5],lot[6])
			cursor.execute(data_insert,data)
			print("%s has been insert in table 3dlot!"%lot[0])
			
		except mysql.connector.Error as e:
			print('insert data error!{}'.format(e))
	cnn.commit()
	cursor.close()
	cnn.close()

main()




