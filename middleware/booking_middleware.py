from middleware import database

class Book_middleware:
    def __init__(self, pickup, drop, ptime, pdate, dtime, ddate, booking_id, customer_id, driver_id=None, booking_status=None):
        self.__pickup = pickup
        self.__drop = drop
        self.__ptime = ptime
        self.__pdate = pdate
        self.__dtime = dtime
        self.__ddate = ddate
        self.__booking_id = booking_id
        self.__booking_status = booking_status
        self.__customer_id = customer_id
        self.__driver_id = driver_id

    @property
    def get_pickup(self):
        return self.__pickup

    @get_pickup.setter
    def set_pickup(self, pickup):
        self.__pickup = pickup

    @property
    def get_drop(self):
        return self.__drop

    @get_drop.setter
    def set_drop(self, drop):
        self.__drop = drop

    @property
    def get_ptime(self):
        return self.__ptime

    @get_ptime.setter
    def set_ptime(self, ptime):
        self.__ptime = str(ptime)

    @property
    def get_pdate(self):
        return self.__pdate

    @get_pdate.setter
    def set_pdate(self, pdate):
        self.__pdate = str(pdate)

    @property
    def get_dtime(self):
        return self.__dtime

    @get_dtime.setter
    def set_dtime(self, dtime):
        self.__dtime = str(dtime)

    @property
    def get_ddate(self):
        return self.__ddate

    @get_ddate.setter
    def set_ddate(self, ddate):
        self.__ddate = str(ddate)

    @property
    def get_booking_id(self):
        return self.__booking_id

    @get_booking_id.setter
    def set_booking_id(self, book_id):
        self.__booking_id = str(book_id)

    @property
    def get_customer_id(self):
        return self.__customer_id

    @get_customer_id.setter
    def set_customer_id(self, cust_id):
        self.__customer_id = cust_id

    @property
    def get_driver_id(self):
        return self.__driver_id

    @get_driver_id.setter
    def set_driver_id(self, driver_id):
        self.__driver_id = driver_id

    @property
    def get_status(self):
        return self.__booking_status

    @get_status.setter
    def set_booking_status(self, book_stat):
        self.__booking_status = book_stat

    def __str__(self):
        return self.get_pickup + ' ' + self.get_drop + ' ' + self.get_ptime + ' ' + self.get_pdate + ' ' +self.get_dtime+' '+self.get_ddate+ ' '+ \
               self.get_booking_id + ' ' + self.get_customer_id + ' ' + self.get_driver_id + ' ' + self.get_status

    def update_booking(self):
        db = database.Database()
        connection = db.create_conn_obj()
        if connection:
            cursor = connection.cursor()
            sql = 'update Booking set PickUp_location=%s, DropOff_location=%s, PickUp_Time=%s, PickUp_date=%s, DropOff_Time=%s, DropOff_Date=%s,Booking_Status=%s ' \
                  'where Booking_id=%s and customer_id=%s'
            values = (
                self.get_pickup,
                self.get_drop,
                self.get_ptime,
                self.get_pdate,
                self.get_dtime,
                self.get_ddate,
                'Pending',
                self.get_booking_id,
                self.get_customer_id
            )
            result = db.insert_or_update_table(sql, connection, cursor, values)
            print(result)
            return result

    def cancel_booking(self):
        db = database.Database()
        connection = db.create_conn_obj()
        if connection:
            cursor = connection.cursor()
            sql = 'update Booking set Booking_Status=%s where Booking_id=%s and customer_id=%s'
            values = (
                'Cancelled',
                self.get_booking_id,
                self.get_customer_id
            )
            result = db.insert_or_update_table(sql, connection, cursor, values)
            print(result)
            return result