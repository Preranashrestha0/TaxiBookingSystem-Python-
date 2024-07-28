from middleware import database

class Admin_middleware:
    def __init__(self):
        self.__drive_id = ''
        self.__user_id = ''
        self.__booking_id = ''
        self.__pickuploc = ''
        self.__pickupdate = ''
        self.__pickuptime = ''
        self.__dropuploc = ''
        self.__dropupdate = ''
        self.__dropuptime = ''
        self.__fname = ''
        self.__lname = ''
        self.__address = ''
        self.__gender = ''
        self.__email = ''
        self.__phone_num = ''
        self.__payment_method = ''
        self.__dfirstname = ''
        self.__dlastname = ''
        self.__daddress = ''
        self.__demail = ''
        self.__dcontact_num = ''
        self.__dlicense_plate = ''


    ##### Getter and Setter
    #Getter
    @property
    def get_driver_id(self):
        return self.__drive_id

    @property
    def get_booking_id(self):
        return self.__booking_id

    @property
    def get_user_id(self):
        return self.__user_id

    @property
    def get_pickuploc(self):
        return self.__pickuploc

    @property
    def get_pickupdate(self):
        return self.__pickupdate

    @property
    def get_pickuptime(self):
        return self.__pickuptime

    @property
    def get_dropuploc(self):
        return self.__dropuploc

    @property
    def get_dropupdate(self):
        return self.__dropupdate

    @property
    def get_dropuptime(self):
        return self.__dropuptime

    @property
    def firstname(self):
        return self.__fname

    @property
    def lastname(self):
        return self.__lname

    @property
    def address(self):
        return self.__address

    @property
    def gender(self):
        return self.__gender

    @property
    def email(self):
        return self.__email

    @property
    def phone_num(self):
        return self.__phone_num

    @property
    def get_dfname(self):
        return self.__dfirstname

    @property
    def get_dlname(self):
        return self.__dlastname

    @property
    def get_daddress(self):
        return self.__daddress

    @property
    def get_demail(self):
        return self.__demail

    @property
    def get_dcontact_num(self):
        return self.__dcontact_num

    @property
    def get_dlicense(self):
        return self.__dlicense_plate


    @firstname.setter
    def set_firstname(self, firstname):
        self.__fname = firstname

    @lastname.setter
    def set_lastname(self, lastname):
        self.__lname = lastname

    @address.setter
    def set_address(self, address):
        self.__address = address

    @gender.setter
    def set_gender(self, gender):
        self.__gender = gender

    @email.setter
    def set_email(self, email):
        self.__email = email

    @phone_num.setter
    def set_phonenum(self, phonenum):
        self.__phone_num = phonenum

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

    @get_pickuploc.setter
    def set_pickuploc(self, pickuploc):
        self.__pickuploc = pickuploc

    @get_pickupdate.setter
    def set_pickupdate(self, pickupdate):
        self.__pickupdate = pickupdate

    @get_pickuptime.setter
    def set_pickuptime(self, pickuptime):
        self.__pickuptime = pickuptime

    @get_dropuploc.setter
    def set_dropuploc(self, dropuploc):
        self.__dropuploc = dropuploc

    @get_dropupdate.setter
    def set_dropupdate(self, dropupdate):
        self.__dropupdate = dropupdate

    @get_dropuptime.setter
    def set_dropuptime(self, dropuptime):
        self.__dropuptime = dropuptime


    @get_dfname.setter
    def set_dfirstname(self, dfirstname):
        self.__dfirstname = dfirstname


    @get_dlname.setter
    def set_dlastname(self, dlastname):
        self.__dlastname = dlastname


    @get_daddress.setter
    def set_daddress(self, daddress):
        self.__daddress = daddress


    @get_demail.setter
    def set_demail(self, demail):
        self.__demail = demail


    @get_dcontact_num.setter
    def set_dcontact_num(self, dcontact_num):
        self.__dcontact_num = dcontact_num


    @get_dlicense.setter
    def set_dlicense(self, dlicense):
        self.__dlicense_plate = dlicense

    def __str__(self):
        return self.get_booking_id + ' ' + self.get_pickuploc + ' ' + self.get_pickupdate + ' ' + self.get_pickuptime + ' ' + self.get_dropuploc + ' ' + self.get_dropupdate + ' ' + self.get_dropuptime + ' ' + self.get_driver_id


    def display_driverid(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'select * from driver where status=%s'
            values = ('Active', )
            item = mydb.get_data(sql, connection, mycursor, values)
            return item

    def assign_driverid(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'update booking set Booking_Status=%s, driver_id=%s where Booking_id=%s'
            values = ('Booked', self.get_driver_id, self.get_booking_id)
            sql2 = 'update Driver set status=%s where driver_id=%s'
            values2 = ('Booked', self.get_driver_id)
            result = mydb.insert_or_update_table(sql, connection, mycursor, values)
            result2 = mydb.insert_or_update_table(sql2, connection, mycursor, values2)
            if result and result2:
                return True

    def admin_update_booking(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            try:
                if int(self.get_driver_id) > 0:
                    sql = 'update booking set PickUp_location=%s, PickUp_Time=%s, PickUp_date=%s, DropOff_location=%s, ' \
                          'DropOff_Time=%s, DropOff_Date=%s, Booking_Status=%s, driver_id=%s where Booking_id=%s'
                    values = (self.get_pickuploc, self.get_pickuptime, self.get_pickupdate, self.get_dropuploc,
                             self.get_dropuptime, self.get_dropupdate, 'Pending', None, self.get_booking_id)
                    sql2 = 'update Driver set status=%s where driver_id=%s'
                    values2 = ('Active', self.get_driver_id)
                    result = mydb.insert_or_update_table(sql, connection, mycursor, values)
                    result2 = mydb.insert_or_update_table(sql2, connection, mycursor, values2)
                    if result and result2:
                        return True
            except ValueError:
                sql = 'update booking set PickUp_location=%s, PickUp_Time=%s, PickUp_date=%s, DropOff_location=%s, ' \
                      'DropOff_Time=%s, DropOff_Date=%s, Booking_Status=%s, driver_id=%s where Booking_id=%s'
                values = (self.get_pickuploc, self.get_pickuptime, self.get_pickupdate, self.get_dropuploc,
                          self.get_dropuptime, self.get_dropupdate, 'Pending', None, self.get_booking_id)
                result = mydb.insert_or_update_table(sql, connection, mycursor, values)
                return result

    def cancel_booking(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            sql = 'update booking set Booking_Status=%s, driver_id=%s where Booking_id=%s'
            values = ('Cancelled', self.get_driver_id, self.get_booking_id)
            sql2 = 'update Driver set status=%s where driver_id=%s'
            values2 = ('Active', self.get_driver_id)
            result = mydb.insert_or_update_table(sql, connection, mycursor, values)
            result2 = mydb.insert_or_update_table(sql2, connection, mycursor, values2)
            if result and result2:
                return True

    def admin_update_customer(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            try:
                sql = 'update customer set first_name=%s, last_name=%s, address=%s, gender=%s, ' \
                      'email=%s, phone_num=%s where customer_id=%s'
                values = (self.firstname, self.lastname, self.address, self.gender,
                         self.email, self.phone_num, self.get_user_id)
                result = mydb.insert_or_update_table(sql, connection, mycursor, values)
                if result :
                    return True
            except ValueError:
                pass

    def admin_update_driver(self):
        mydb = database.Database()
        connection = mydb.create_conn_obj()
        if connection:
            mycursor = connection.cursor()
            try:
                sql = 'update driver set First_Name=%s, last_name=%s, Address=%s, Phone_num=%s, ' \
                      'email=%s, License_plate=%s where driver_id=%s'
                values = (self.get_dfname, self.get_dlname, self.get_daddress, self.get_dcontact_num,
                         self.get_demail, self.get_dlicense, self.get_driver_id)
                result = mydb.insert_or_update_table(sql, connection, mycursor, values)
                if result :
                    return True
            except ValueError:
                pass


if __name__ == '__main__':
    obj = Admin_middleware()
    obj.display_driverid()