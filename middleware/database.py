import mysql.connector
from tkinter import messagebox

class Database:
    __single_instance = None

    @classmethod
    def single_instance(cls):
        if not cls.__single_instance:
            cls.__single_instance = cls()

        return cls.__single_instance

    def create_conn_obj(self):
        try:
            host = "localhost"
            user = "root"
            passwd = ""
            dbase = "taxi_booking"

            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=passwd,
                                           database=dbase)
            return conn

        except mysql.connector.errors.DatabaseError as e:
            messagebox.showerror("Error", e)

    def insert_or_update_table(self, sql, conn, crsor, value):
        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
                return False
            else:
                conn.commit()
                return True

    def get_data(self, sql, conn, crsor, values):
        if sql and crsor:
            try:
                crsor.execute(sql, values)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
                return False
            else:
                item = crsor.fetchall()
                return item
        conn.close()