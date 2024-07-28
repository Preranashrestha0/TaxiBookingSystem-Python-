import  mysql.connector as ms
from tkinter import messagebox

import mysql.connector.errors

class Booking_db:
    def __init__(self):
        pass
    def create_conn_obj(self):
        try:
            host = "localhost"
            user = "root"
            passwd = ""
            dbase = ""

            conn = ms.connect(host=host,
                                           user=user,
                                           password=passwd,
                                           database=dbase)
            conn.autocommit = True
            messagebox.showinfo("Connection Successfull", "Connection to the database successfully !!")
            return conn

        except mysql.connector.errors.DatabaseError as e:
            messagebox.showerror("Database Connection Error.", e.msg)
    #
    # def db(self, conn):
    #     myconn = conn
    #     mycursor = myconn.cursor()
    #     mycursor.execute("create database IF NOT EXISTS taxi_booking ")

    def create_table(self, sql, cursor):
        if sql and cursor:
            try:
                cursor.execute(sql)
            except ms.Error as e:
                if e.errno == ms.errorcode.ER_CANT_CREATE_TABLE:
                    messagebox.showerror("ERROR", str(e))
                else:
                    print(e.msg)