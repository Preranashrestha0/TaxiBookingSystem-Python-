from MySql import Log_db

class LogIn_Middleware:
    def __init__(self, email,  password, user_type):
        self.__user_id = ''
        self.__email = email
        self.__password = password
        self.__user_type = user_type

    @property
    def user_id(self):
        return self.__user_id

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def user_type(self):
        return self.__user_type

    @user_id.setter
    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    @email.setter
    def set_email(self, new_email):
        self.__email = new_email

    @password.setter
    def set_password(self, new_pass):
        self.__password = new_pass

    @user_type.setter
    def set_user_type(self, new_user_type):
        self.__user_type = new_user_type

    def __str__(self):
        return self.user_id + ' ' + self.email + ' ' + self.password + ' ' + self.__user_type

    def search_user(self):
        if self.user_type == 'Customer':
            db = Log_db.Database()
            connection = db.create_conn_obj()
            if connection:
                mycursor = connection.cursor()
                sql = 'SELECT customer_id, email, user_type FROM customer where email=%s and Password=%s'
                values = (self.email, self.password)
                data = db.get_login_data(sql, connection, mycursor, values)
                return data

        elif self.user_type == 'Taxi Driver':
            db = Log_db.Database()
            connection = db.create_conn_obj()
            if connection:
                mycursor = connection.cursor()
                sql = 'SELECT driver_id, email, user_type FROM driver where email=%s and Password=%s'
                values = (self.email, self.password)
                data = db.get_login_data(sql, connection, mycursor, values)
                return data

        elif self.user_type == 'Admin':
            db = Log_db.Database()
            connection = db.create_conn_obj()
            if connection:
                mycursor = connection.cursor()
                sql = 'SELECT Admin_id, Username, user_type FROM admin where Username=%s and Password=%s'
                values = (self.email, self.password)
                data = db.get_login_data(sql, connection, mycursor, values)
                return data


# if __name__ == '__main__':
#     obj = LogIn_Middleware('ps3@gmail.com', 'prerana', 'Customer')
#     data = obj.search_user()
#     for i in data:
#         print(data)