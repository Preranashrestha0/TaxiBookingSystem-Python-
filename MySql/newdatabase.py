import mysql.connector
import sys

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='taxi_Booking')
        print("Connected!")
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(copy):
    sql = "INSERT INTO regdb VALUES (%s,%s, %s, %s, %s, %s, %s)"
    values = (copy.getfullname(), copy.get(), copy.getPrice())
    result = {'status':False, 'message':None}
    try:
        conn = connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result['status']=True
        result['message']="Record save successfully"
        print("Inserted!")
    except:
        result['status'] = False
        result['message'] = sys.exc_info()
        print("Error", sys.exc_info())
    finally:
        del values
        del sql
        return result

# import mysql.connector as ms
#
# conn=ms.connect(host="localhost", user="root", password="",database="Sample2")
# conn.autocommit = True
# # print(conn)
# cursor=conn.cursor()
# #cursor.execute('CREATE DATABASE Sample2;')
# #cursor.execute('CREATE TABLE ABC(id int, name  varchar(255))')
# #cursor.execute('INSERT into ABC(id, name)values(1, "Prerana"),(2, "Reena")')
# #conn.commit() #permanently saves datas
# #cursor.execute('CREATE TABLE Datas(id int primary key, fullname varchar(255), gender varchar(255), address varchar(255)) ')
# #cursor.execute('INSERT into Datas(id, fullname, gender, address) values (1, "Prerana", "female", "Ktm")')
# #cursor.execute('DROP table Datas')

