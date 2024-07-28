from middleware.database import Database

class Driver_Middleware:
    def __init__(self):
        self.__drive_id = ''
        self.__user_id = ''
        self.__booking_id = ''

    ##### Getter and Setter
    # Getter
    @property
    def get_driver_id(self):
        return self.__drive_id

    @property
    def get_booking_id(self):
        return self.__booking_id

    @property
    def get_user_id(self):
        return self.__user_id


    #Setter
    @get_driver_id.setter
    def set_driver_id(self, did):
        self.__drive_id = did

    @get_booking_id.setter
    def set_booking_id(self, bid):
        self.__booking_id = bid

    @get_user_id.setter
    def set_user_id(self, uid):
        self.__user_id = uid

    def __str__(self):
        return self.get_booking_id + ' ' + self.get_driver_id + ' ' + self.get_user_id


    def get_rides_details(self):
        mydb = Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'select * from booking where driver_id=%s and (Booking_Status=%s or Booking_Status=%s)'
            values = (self.get_driver_id, 'Booked', 'Confirmed')
            item = mydb.get_data(sql, connection, mycursor, values)
            return item

    def get_rides_history_details(self):
        mydb = Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'select * from booking where driver_id=%s and (Booking_Status=%s or Booking_Status=%s)'
            values = (self.get_driver_id, 'Completed', 'Cancelled')
            item = mydb.get_data(sql, connection, mycursor, values)
            return item

    def start_ride(self):
        mydb = Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'update booking set Booking_Status=%s where driver_id=%s and Booking_id=%s'
            values = ('Confirmed', self.get_driver_id, self.get_booking_id)
            result = mydb.insert_or_update_table(sql, connection, mycursor, values)
            return result

    def finish_ride(self):
        mydb = Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'update booking set Booking_Status=%s where driver_id=%s and Booking_id=%s'
            values = ('Completed', self.get_driver_id, self.get_booking_id)
            sql2 = 'update Driver set status=%s where driver_id=%s'
            values2 = ('Active', self.get_driver_id)
            result = mydb.insert_or_update_table(sql, connection, mycursor, values)
            result2 = mydb.insert_or_update_table(sql2, connection, mycursor, values2)
            if result and result2:
                return True
            connection.close()


if __name__ == '__main__':
    obj = Driver_Middleware()
    obj.set_driver_id = 1
    item = obj.get_rides_history_details()
    for i in item:
        print(i)