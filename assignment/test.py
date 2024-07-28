# myconn = conn
# mycursor = myconn.cursor()
# mycursor.execute("create table IF NOT EXISTS regdb(id int(10) primary key auto_increment, fullname text, gender text, address text, email text, contact_no text, user_type text, password text)")


#     if myconn:
#         mycursor = myconn.cursor()
#         myconn.autocommit=True
#         mycursor.execute("create database IF NOT EXISTS taxi_Booking ")
#         mycursor.execute("use taxi_Booking")
#         mycursor.execute("create table IF NOT EXISTS logindb(username varchar(50), user_type varchar(50), password varchar(50))")
#         # mycursor.execute("insert into logindb (username, user_type, password) values('Prerana', 'ADMIN', 'prerana111')")
#         ####registration####
#         mycursor.execute("create table IF NOT EXISTS regdb(id int(10) primary key auto_increment, fullname text, gender text, address text, email text, contact_no text, user_type text, password text )")
#         # mycursor.execute("insert into regdb(fullname, gender, address, email, contact_no, user_type, password)values ('Prerana', 'Female', 'Bkt','preranas111@gmail.com', '9800778891', 'ADMIN', 'prerana111')")
#         mycursor.execute("select * from regdb")
#         result = mycursor.fetchall()
#         for i in result:
#             print("id =",i[0], end=" ")
#             print("fullname = ", i[1], end="\t")
#             print("gender = ", i[2], end="\t")
#             print("address = ", i[3], end="\t")
#             print("email = ", i[4], end="\t")
#             print("contact_no = ", i[5], end="\t")
#             print("user_type = ", i[6], end="\t")
#             print("password = ", i[7], end="\t")

#def insert_or_update(self, sql, conn, cursor):
    #     if sql or cursor:
    #         try:
    #             cursor.execute(sql)
    #         except ms.Error as e:
    #             messagebox.showerror("ERROR", e.msg)
    #         else:
    #             conn.commit()
    #             messagebox.showinfo("INFO", "Data Inserted Successfully")

def register(self):
    pass

#
#     if not validation():
#         return
# register_credentials = mid_REG.GetSetReg(fullname=self.ent_fullname.get(),
#                                 address=self.ent_address.get(),
#                                gender= "male" if self.rb_val.get() == 0 else "female" if self.rb_val.get() == 1 else "others",
#                                email=self.ent_email.get(),
#                                phone_num=self.ent_contact.get(),
#                                select_user = self.cmb_usertype.get(),
#                                password = self.ent_password.get()
#                                )
# # exit(ent7.get())




