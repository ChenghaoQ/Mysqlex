import mysql.connector
import pickle
data_path=open('EngineGrad.pkl','rb')
colllist=pickle.load(data_path)
passwd=input('Please input your password:')
config={'host':'127.0.0.1',
	'user':'root',
	'password':passwd,#######need to clear before upload
	'port':3306,
	'database':'USCollege',
	'charset':'utf8',
	}
def main():
	try:
		cnn=mysql.connector.connect(**config)
	except mysql.connector.Error as e:
		print('connect failed!{}'.format(e))
	cursor=cnn.cursor()
	for school in colllist:
		try:
			data_insert="insert engineGrads (Rank,School_name,Tuition,Enrollment,Location) values (%s,%s,%s,%s,%s)"
			data=(school[0],school[1],school[2],school[3],school[4])
			cursor.execute(data_insert,data)
			print("%s has been insert in table engineGrad!"%school[1])
			
		except mysql.connector.Error as e:
			print('insert data error!{}'.format(e))
	cnn.commit()
	cursor.close()
	cnn.close()

main()




