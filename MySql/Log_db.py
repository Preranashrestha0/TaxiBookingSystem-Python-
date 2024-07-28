import mysql.connector as ms
from tkinter import messagebox

import mysql.connector.errors


# import os
# import configparser

class Database:
    def __init__(self):
        pass

    def create_conn_obj(self):
        try:
            host = "localhost"
            user = "root"
            passwd = ""
            dbase = "taxi_booking"

            conn = ms.connect(host=host,
                                           user=user,
                                           password=passwd,
                                           database=dbase)
            conn.autocommit = True
            # messagebox.showinfo("Connection Successfull", "Connection to the database successfully !!")
            return conn

        except mysql.connector.errors.DatabaseError as e:
            messagebox.showerror("Database Connection Error.", e.msg)

    def get_login_data(self, sql, conn, crsor, value):
        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                print(e.msg)
                messagebox.showerror("Error", e.msg)
            else:
                info = crsor.fetchone()
                return info
            conn.close()


    def db(self, conn):
        myconn = conn
        mycursor = myconn.cursor()
        mycursor.execute("create database IF NOT EXISTS taxi_booking ")
        mycursor.execute("CREATE TABLE IF NOT EXISTS bookingdb(id int(10) primary key auto_increment, pickUp text, DropOff text, time text, date text)")

    def create_table(self, sql, cursor):
        if sql and cursor:
            try:
                cursor.execute(sql)
            except ms.Error as e:
                if e.errno == ms.errorcode.ER_CANT_CREATE_TABLE:
                    messagebox.showerror("ERROR", str(e))
                else:
                    print(e.msg)

    def register_user(self, user):
        sql = "insert into customer(first_name,last_name, address, gender, email, phone_num, user_type, payment_method, Password) values(?,?,?,?,?,?,?,?,?)"

        values = (
                user.firstname,
                user.lastname,
                user.address,
                user.gender,
                user.email,
                user.phone_num,
                'Customer',
                user.payment_method,
                user.password,
        )
        connection = self.create_conn_obj()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, values)
        connection.close()

    def dregister_user(self, user):
        sql = "insert into driver(First_Name,last_name, address, email, phone_num, License_plate,Password, user_type, status) values(?,?,?,?,?,?,?,?,?)"

        values = (
                user.firstname,
                user.lastname,
                user.address,
                user.email,
                user.phone_num,
                user.license,
                user.password,
                user.usertype,
                'Active'
        )
        print(values)
        connection = self.create_conn_obj()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, values)
        connection.close()

    def user_booking(self, booking_data):
        sql = "insert into Booking(PickUp_location, DropOff_location, PickUp_Time, PickUp_date,DropOff_Time,DropOff_Date, Booking_Status, customer_id) values(?,?,?,?,?,?,?,?)"

        values = (
            booking_data.get_pickup,
            booking_data.get_dropOff,
            booking_data.get_ptime,
            booking_data.get_pdate,
            booking_data.get_dtime,
            booking_data.get_ddate,
            'Pending',
            booking_data.get_customer_id
        )
        connection = self.create_conn_obj()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, values)
        connection.close()

    def user_booking_update(self, booking_data):
        sql = 'update Booking set PickUp_location=?, DropOff_location=?, PickUp_Time=?, PickUp_date=?, DropOff_Time=?, DropOff_Date=?,Booking_Status=? ' \
              'where Booking_id=? and customer_id=?'
        values = (
            booking_data.get_pickup,
            booking_data.get_dropOff,
            booking_data.get_ptime,
            booking_data.get_pdate,
            booking_data.get_dtime,
            booking_data.get_ddate,
            'Pending',
            1,
            1
        )
        connection = self.create_conn_obj()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, values)
        connection.close()

    def user_update(self, user_data):
        sql = 'update customer set first_name=?, last_name=?, address=?, gender=?, email=?, phone_num=?,Password=? ' \
              'customer_id=?'
        values = (
            user_data.firstname,
            user_data.lastname,
            user_data.address,
            user_data.gender,
            user_data.email,
            user_data.phone_num,
            user_data.password,
        )
        connection = self.create_conn_obj()
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, values)
        connection.close()

    def insert_or_update_data(self, sql, conn, crsor, value):
        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
                return False
            else:
                conn.commit()
                conn.close()
                return True

    #
    def check_login(self, email, password):
        sql = "select * from customer where email=? and Password=?"
        conn = self.create_conn_obj()
        cursor = conn.cursor(prepared=True)

        # execute sql
        cursor.execute(sql, [
            email,
            password
        ])
        detail = cursor.fetchall()
        if not detail:
            return False
        conn.close()
        return detail

    def get_booking_table_data(self, customer_id=''):
        sql = 'select * from Booking where (Booking_Status="Pending" or Booking_Status="Booked" or Booking_Status="Confirmed") and customer_id =?'
        values = (customer_id,)
        conn= self.create_conn_obj()
        try:
            cursor = conn.cursor(prepared=True)
            cursor.execute(sql, values)
            data = cursor.fetchall()
            if not data:
                return False
            conn.close()
            return data
        except AttributeError:
            pass

    def get_cust_data(self):
        sql = 'Select * from customer'
        conn = self.create_conn_obj()
        try:
            cursor = conn.cursor(prepared=True)
            cursor.execute(sql)
            cust_data = cursor.fetchall()

            if not cust_data:
                return False
            conn.close()
            return cust_data
        except AttributeError:
            pass

    def get_driver_data(self):
        sql = 'Select * from Driver'
        conn = self.create_conn_obj()
        try:
            cursor = conn.cursor(prepared=True)
            cursor.execute(sql)
            cust_data = cursor.fetchall()

            if not cust_data:
                return False
            conn.close()
            return cust_data
        except AttributeError:
            pass

    def show_all_bookdata(self):
        sql = 'select * from Booking where Booking_Status="Cancelled" or Booking_Status="Completed"'
        conn = self.create_conn_obj()
        try:
            cursor = conn.cursor(prepared=True)
            cursor.execute(sql)
            data = cursor.fetchall()
            if not data:
                return False
            conn.close()
            return data
        except AttributeError:
            pass

    def show_booking(self, customer_id=''):
        sql = 'select * from Booking where customer_id =? and (Booking_Status=? or Booking_Status=?)'
        values = (customer_id, 'Cancelled', 'Completed')
        conn = self.create_conn_obj()
        cursor = conn.cursor(prepared=True)
        cursor.execute(sql, values)
        data = cursor.fetchall()
        if not data:
            return False
        conn.close()
        return data