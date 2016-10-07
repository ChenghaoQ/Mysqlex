import mysql.connector
import pickle
data = open('ITOdata.pkl','rb')
complist = pickle.load(data)
passwd= input("please input your password:")

config={'host':'127.0.0.1',
        'user':'root',
        'password':passwd,
        'port':3306,
        'database':'ITO',
        'charset':'utf8',
        }

def main():
        try:
                cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
                print('connnect failed!{}'.format(e))
        cursor = cnn.cursor()
        
        company_table_create = "create table IF NOT EXISTS company( id int primary key auto_increment, company varchar(30), groups varchar(20), location varchar(20), year varchar(10),month varchar(10), status varchar(20));"
        cursor.execute(company_table_create)
        
        for company in complist:
                try:
                        date = company[3].split('.') 
                        data_insert ="insert company (company,groups,location,year,month,status) values (%s,%s,%s,%s,%s,%s)"
                        comp = (company[0],company[1],company[2],date[0],date[1],company[4])
                        cursor.execute(data_insert,comp)
                        
                        print("%s has been innsert in table!"%company[0])
                except mysql.connector.Error as e:
                        print("Inserting data error!{}".format(e))
        company_stats_table=["create table IF NOT EXISTS comloca(select location,count(location) from company group by location ORDER BY count(location) DESC);",
                                "create table IF NOT EXISTS comstatus(select status,count(status) from company group by status ORDER BY count(status) DESC);",
                                "create table IF NOT EXISTS comtype(select groups,count(groups) from company group by groups ORDER BY count(groups) DESC);",
                                "create table IF NOT EXISTS comyear(select year,count(year) from company group by year ORDER BY count(year) DESC);"]


        for each in company_stats_table:
                cursor.execute(each)

        cnn.commit()
        cursor.close()
        cnn.close()

main()
