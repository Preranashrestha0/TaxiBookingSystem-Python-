from tkinter import messagebox

import mysql

from MySql.Log_db import Database

class Customer_bookingdata:
    def __init__(self, pickUp_location, DropOff_location, PTime, PDate, DTime, DDate, cust_id, book_id=2, driver_id=None, booking_stat=None):
        self.__pickUp_location = str(pickUp_location)
        self.__dropOff_location = str(DropOff_location)
        self.__ptime = str(PTime)
        self.__pdate = str(PDate)
        self.__dtime = str(DTime)
        self.__ddate = str(DDate)
        self.__customer_id = str(cust_id)
        self.__booking_id = book_id
        self.__driver_id = driver_id
        self.__booking_status = booking_stat

    @property
    def get_customer_id(self):
        return self.__customer_id

    @property
    def get_pickup(self):
        return self.__pickUp_location
    @property
    def get_dropOff(self):
        return self.__dropOff_location
    @property
    def get_ptime(self):
        return self.__ptime
    @property
    def get_pdate(self):
        return self.__pdate

    @property
    def get_dtime(self):
        return self.__dtime

    @property
    def get_ddate(self):
        return self.__ddate

    @property
    def get_booking_id(self):
        return self.__booking_id

    @property
    def get_driver_id(self):
        return self.__driver_id

    @property
    def get_booking_status(self):
        return self.__booking_status

    @get_booking_id.setter
    def set_booking_id(self, book_id):
        self.__booking_id = book_id

    @get_customer_id.setter
    def set_custid(self, custid):
        self.__customer_id = custid

    @get_pickup.setter
    def set_pickuplocation(self, pickuplocation):
        self.__pickUp_location = pickuplocation
    @get_dropOff.setter
    def set_dropOfflocation(self, dropOfflocation):
        self.__dropOff_location = dropOfflocation

    @get_ptime.setter
    def set_ptime(self, ptime):
        self.__ptime = ptime

    @get_pdate.setter
    def set_pdate(self, pdate):
        self.__pdate = pdate

    @get_dtime.setter
    def set_dtime(self, dtime):
        self.__dtime = dtime

    @get_ddate.setter
    def set_ddate(self, ddate):
        self.__ddate = ddate

    @get_booking_status.setter
    def set_booking_status(self, book_status):
        self.__booking_status = book_status

    @get_driver_id.setter
    def set_driver_id(self, driver_id):
        self.__driver_id = driver_id

    def __str__(self):
        return self.get_pickup + ' ' + self.get_dropOff + ' ' + self.get_pdate + ' ' + self.get_ptime + ' ' +self.get_dtime + ' ' + self.get_ddate +' '+ \
               self.get_customer_id + ' ' + self.get_booking_id + ' ' + self.get_driver_id + ' ' + self.get_booking_status


    def user_booking_update(self):
        print(self.__str__())
        sql = 'update Booking set PickUp_location=?, DropOff_location=?, PickUp_Time=?, PickUp_date=?,DropOff_Time=?,DropOff_Date=? Booking_Status=? ' \
              'where Booking_id=? and customer_id=?'
        values = (
            self.get_pickup,
            self.get_dropOff,
            self.get_ptime,
            self.get_pdate,
            self.get_dtime,
            self.get_ddate,
            'Pending',
            2,
            1
        )
        print('Hello')
        # connection = Database.create_conn_obj()
        # cursor = connection.cursor(prepared=True)
        # cursor.execute(sql, values)
        # connection.connect()
        # connection.close()