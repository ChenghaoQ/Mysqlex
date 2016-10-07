import mysql.connector                                                                                                                   
import pickle

passwd= input("please input your password:")
config={'host':'127.0.0.1',
        'user':'root',
        'password':passwd,
        'port':3306,
        'database':'ITO',
        'charset':'utf8',
        }

def get_stats():
        company_stats=[]
        try:
                cnn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
                print('connnect failed!{}'.format(e))
        cursor = cnn.cursor()


    
        sql = ["select * from comloca",
                "select * from comstatus",
                "select * from comtype",
                "select * from comyear"]

        for each in sql:
                count = cursor.execute(each)
                result = cursor.fetchall()
                #company_stats.append(result)
                item=[]
                stats_content=[]
                for each in result:
                        item.append(each[0])
                        stats_content.append(each[1])
                company_stats.append((item,stats_content))
        cursor.close()
        cnn.close()  

        return company_stats
