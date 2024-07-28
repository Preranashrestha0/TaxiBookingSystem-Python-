from tkinter import *
from tkinter import messagebox
from subprocess import call
from tkinter import ttk
from tkinter.ttk import Combobox

from MySql import Log_db
from MySql.mid_REG import GetSetReg
from middleware.admin_middleware import Admin_middleware

class Admin:

    def __init__(self, user_id):
        self._user_id = user_id
        self.admin = Tk()
        self.admin.geometry('1550x840')
        self.admin.title('admin dashboard')
        self.admin.resizable(False,False)
        self.admin.wm_state('zoomed')

        ####heading######
        head = Label(self.admin, text="Online Taxi Booking System", bg="#eee000",
                     font=("Harlow Solid Italic", 30, "bold"), fg="black", width=60)
        head.place(x=0, y=0)

        self.lbl_left = Label(self.admin, width=40, bg="#D3D3D3", height=60)
        self.lbl_left.place(x=0, y=58)

        self.lbl_right = Label(self.admin, width=185, bg="grey", height=60)
        self.lbl_right.place(x=285, y=58)

        ###labels in right side
        btn_mngcustomer = Button (self.lbl_left, text="Manage Customer", bg="#eee000", fg="black", width=20, font=("Forte",17), command=self.opencustomer)
        btn_mngcustomer.place(x=4, y=10)

        btn_mngdriver = Button(self.lbl_left, text="Manage Driver", bg="#eee000", fg="black", width=20, font=("Forte",17), command=self.open_mngdriver)
        btn_mngdriver.place(x=4, y=70)

        btn_assigndriver = Button(self.lbl_left, text="Booking Request", bg="#eee000", fg="black", width=20, font=("Forte",17), command=self.open_bookreq)
        btn_assigndriver.place(x=4, y=130)

        btn_viewbooking = Button(self.lbl_left, text="Booking History", bg="#eee000", fg="black", width=20, font=("Forte",17), command=self.open_bookhist)
        btn_viewbooking.place(x=4, y=190)

        btn_logOut = Button(self.lbl_left, text="Log Out" , bg="#eee000", fg="black", width=20, font=("Forte",17))
        btn_logOut.place(x=4, y=700)

        self.admin.mainloop()
    def opencustomer(self):
        self.frame_opencust = Frame(self.lbl_right, bg="aquamarine1")
        self.frame_opencust.place(x=10, y=10, width=1230, height=760)

        ####Labels####
        head = Label(self.frame_opencust, text="Customers Data", bg="#eee000", fg="black", font=("Forte", 25))
        head.place(x=0, y=0,width=1230)

        self.lv_left = Label(self.frame_opencust, bg="#D3D3D3")
        self.lv_left.place(x=0, y=42, width=370, height=725)

        self.lv_right = Label(self.frame_opencust, bg="grey")
        self.lv_right.place(x=356, y=42, width=890, height=725)

        ##form
        cust_id = Label(self.lv_left, text="Customer Id", font=("Forte", 17), bg="#D3D3D3")
        cust_id.place(x=2, y=10)

        self.ent_cust_id = Entry(self.lv_left, width=28)
        self.ent_cust_id.place(x=102, y=14, height=25)

        fname = Label(self.lv_left, text="First Name", font=("Forte", 17), bg="#D3D3D3")
        fname.place(x=2, y=64)

        self.ent_fname = Entry(self.lv_left, width=38)
        self.ent_fname.place(x=42, y=94, height=25)

        lname = Label(self.lv_left, text="Last Name", font=("Forte", 17), bg="#D3D3D3")
        lname.place(x=2, y=123)

        self.ent_lname = Entry(self.lv_left, width=38)
        self.ent_lname.place(x=42, y=150, height=25)

        address = Label(self.lv_left, text="Address", font=("Forte", 17), bg="#D3D3D3")
        address.place(x=2, y=180)

        self.ent_address = Entry(self.lv_left, width=38)
        self.ent_address.place(x=42, y=210, height=25)

        gender = Label(self.lv_left, text="Gender", font=("Forte", 17), bg="#D3D3D3")
        gender.place(x=2, y=240)

        self.ent_gender = Entry(self.lv_left, width=38)
        self.ent_gender.place(x=42, y=278, height=25)

        email = Label(self.lv_left, text="E-Mail", font=("Forte", 17), bg="#D3D3D3")
        email.place(x=2, y=310)

        self.ent_email = Entry(self.lv_left, width=38)
        self.ent_email.place(x=42, y=340, height=25)

        ph_number = Label(self.lv_left, text="Contact No.", font=("Forte", 17), bg="#D3D3D3")
        ph_number.place(x=2, y=370)

        self.ent_phnumber = Entry(self.lv_left, width=38)
        self.ent_phnumber.place(x=42, y=408, height=25)


        ###Buttons
        self.btn_update = Button(self.lv_left, text="UPDATE", font=("Forte", 17), bg="#A3A3A3", fg="black", command=self.update_customerdata)
        self.btn_update.place(x=40, y=520)

        self.btn_clear = Button(self.lv_left, text="CLEAR", font=("Forte", 17), bg="#A3A3A3", fg="black", command=self.clear_all)
        self.btn_clear.place(x=160, y=520)

        ###table
        ##constructing table
        column = ('customer_id', 'fname','lname','Address', 'gender', 'email', 'ph_number')
        self.ttree = ttk.Treeview(self.lv_right, columns=column, show='headings')

        ##defining heading
        self.ttree.heading('customer_id', text='Id')
        self.ttree.heading('fname', text='First Name')
        self.ttree.heading('lname', text='Last Name')
        self.ttree.heading('Address', text='Address')
        self.ttree.heading('gender', text='Gender')
        self.ttree.heading('email', text='Email')
        self.ttree.heading('ph_number', text='Contact No')
        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=45,
                        font=("", 13))

        ### sizing the heading in the columns
        self.ttree.column("customer_id", anchor=CENTER, stretch=NO, width=87, minwidth=57)  # , ne, e, se, s, sw, w, nw,
        self.ttree.column("fname", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("lname",anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("Address", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("gender", anchor=CENTER, stretch=NO, width=110)
        self.ttree.column("email", anchor=CENTER, stretch=NO, width=140)
        self.ttree.column("ph_number", anchor=CENTER, stretch=NO, width=130)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.lv_right, orient="vertical", command=self.ttree.yview)
        ##placing scrollbar by using place()
        self.ttree.place(x=0, y=0, height=710, width=868)
        scrlbar.place(x=855, y=0, height=710)
        self.ttree.configure(yscrollcommand=scrlbar.set)
        self.get_table_data()
        self.ttree.bind('<<TreeviewSelect>>', self.item_selected)

    def get_table_data(self):
        db = Log_db.Database()
        data = db.get_cust_data()
        count = 0
        for delete_data in self.ttree.get_children():
            self.ttree.delete(delete_data)

        try:
            for i in data:
                self.ttree.insert('', count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        except TypeError:
            pass

    def item_selected(self, event):
        for selected_item in self.ttree.selection():
            item = self.ttree.item(selected_item)
            record = item['values']

            # Delete data from entry
            self.ent_cust_id.delete(0, END)
            self.ent_fname.delete(0, END)
            self.ent_lname.delete(0, END)
            self.ent_gender.delete(0, END)
            self.ent_address.delete(0, END)
            self.ent_phnumber.delete(0, END)
            self.ent_email.delete(0, END)

            # Set data into entry
            self.ent_cust_id.insert(0, record[0])
            self.ent_fname.insert(0, record[1])
            self.ent_lname.insert(0, record[2])
            self.ent_address.insert(0, record[3])
            self.ent_gender.insert(0, record[4])
            self.ent_email.insert(0, record[5])
            self.ent_phnumber.insert(0, record[6])

    def clear_all(self):
        self.ent_cust_id.delete(0, END)
        self.ent_fname.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_gender.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_phnumber.delete(0, END)

    def update_customerdata(self):
        obj = Admin_middleware()
        obj.set_user_id = self.ent_cust_id.get()
        obj.set_firstname = self.ent_fname.get()
        obj.set_lastname = self.ent_lname.get()
        obj.set_address = self.ent_address.get()
        obj.set_gender = self.ent_gender.get()
        obj.set_email = self.ent_email.get()
        obj.set_phonenum = self.ent_phnumber.get()
        res = obj.admin_update_customer()
        if res :
            # self.clear_all_entry()
            self.get_table_data()
            messagebox.showinfo("Successful", 'Updated Successfully')

    def open_mngdriver(self):
        for item in self.lbl_right.winfo_children():
            item.destroy()
        self.frame_driver = Frame(self.lbl_right, bg="aquamarine1")
        self.frame_driver.place(x=10, y=10, width=1230, height=760)

        ####Labels####
        head = Label(self.frame_driver, text="Drivers Data", bg="#eee000", fg="black", font=("Forte", 25), width=70)
        head.place(x=0, y=0)

        self.lv_left = Label(self.frame_driver, bg="#D3D3D3")
        self.lv_left.place(x=0, y=42,width=360, height=725)

        self.lv_right = Label(self.frame_driver, bg="grey")
        self.lv_right.place(x=356, y=42, width=900, height=725)

        ##form
        driver_id = Label(self.lv_left, text="Driver Id", font=("Forte", 17), bg="#D3D3D3")
        driver_id.place(x=2, y=10)

        self.ent_driver_id = Entry(self.lv_left, width=28)
        self.ent_driver_id.place(x=102, y=14, height=25)

        fname = Label(self.lv_left, text="First Name", font=("Forte", 17), bg="#D3D3D3")
        fname.place(x=2, y=64)

        self.ent_fullname = Entry(self.lv_left, width=38)
        self.ent_fullname.place(x=42, y=94, height=25)

        lastname = Label(self.lv_left, text="Last Name", font=("Forte", 17), bg="#D3D3D3")
        lastname.place(x=2, y=123)

        self.ent_lastname = Entry(self.lv_left, width=38)
        self.ent_lastname.place(x=42, y=150, height=25)

        lb_address = Label(self.lv_left, text="Address", font=("Forte", 17), bg="#D3D3D3")
        lb_address.place(x=2, y=180)

        self.entaddress = Entry(self.lv_left, width=38)
        self.entaddress.place(x=42, y=210, height=25)

        lb_email = Label(self.lv_left, text="E-Mail", font=("Forte", 17), bg="#D3D3D3")
        lb_email.place(x=2, y=240)

        self.entemail = Entry(self.lv_left, width=38)
        self.entemail.place(x=42, y=278, height=25)

        lb_contact = Label(self.lv_left, text="Contact No.", font=("Forte", 17), bg="#D3D3D3")
        lb_contact.place(x=2, y=310)

        self.entcontact = Entry(self.lv_left, width=38)
        self.entcontact.place(x=42, y=340, height=25)

        license_plate = Label(self.lv_left, text="License Plate", font=("Forte", 17), bg="#D3D3D3")
        license_plate.place(x=2, y=370)

        self.license_plate = Entry(self.lv_left, width=38)
        self.license_plate.place(x=42, y=408, height=25)

        ###Buttons
        self.btnupdate = Button(self.lv_left, text="UPDATE", font=("Forte", 17), bg="#A3A3A3", fg="black", command=self.update_driver)
        self.btnupdate.place(x=40, y=520)

        self.btnclear = Button(self.lv_left, text="CLEAR", font=("Forte", 17), bg="#A3A3A3", fg="black", command=self.clearall)
        self.btnclear.place(x=160, y=520)

        ###table
        ##constructing table
        column = ('driver_id', 'fname', 'lname', 'Address', 'email', 'ph_number', 'license_plate')
        self.ttree = ttk.Treeview(self.lv_right, columns=column, show='headings')

        ##defining heading
        self.ttree.heading('driver_id', text='Id')
        self.ttree.heading('fname', text='First Name')
        self.ttree.heading('lname', text='Last Name')
        self.ttree.heading('Address', text='Address')
        self.ttree.heading('email', text='Email')
        self.ttree.heading('ph_number', text='Contact No')
        self.ttree.heading('license_plate', text='License Plate')
        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=45,
                        font=("", 13))

        ### sizing the heading in the columns
        self.ttree.column("driver_id", anchor=CENTER, stretch=NO, width=87, minwidth=47)  # , ne, e, se, s, sw, w, nw,
        self.ttree.column("fname", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("lname", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("Address", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("email", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("ph_number", anchor=CENTER, stretch=NO, width=130)
        self.ttree.column("license_plate", anchor=CENTER, stretch=NO, width=130)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.lv_right, orient="vertical", command=self.ttree.yview)
        ##placing scrollbar by using place()
        self.ttree.place(x=0, y=0, height=720, width=868)
        scrlbar.place(x=855, y=0, height=720)
        self.ttree.configure(yscrollcommand=scrlbar.set)
        self.ttree.bind('<<TreeviewSelect>>', self.item_selects)
        self.get_tableinfo()

    def get_tableinfo(self):
        db = Log_db.Database()
        data = db.get_driver_data()
        count = 0
        for delete_data in self.ttree.get_children():
            self.ttree.delete(delete_data)

        try:
            for i in data:
                self.ttree.insert('', count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        except TypeError:
            pass

    def item_selects(self, event):
        for select_items in self.ttree.selection():
            item = self.ttree.item(select_items)
            record = item['values']

            # Delete data from entry
            self.ent_driver_id.delete(0, END)
            self.ent_fullname.delete(0, END)
            self.ent_lastname.delete(0, END)
            self.entemail.delete(0, END)
            self.entaddress.delete(0, END)
            self.entcontact.delete(0, END)
            self.license_plate.delete(0, END)

            # Set data into entry
            self.ent_driver_id.insert(0, record[0])
            self.ent_fullname.insert(0, record[1])
            self.ent_lastname.insert(0, record[2])
            self.entaddress.insert(0, record[3])
            self.entcontact.insert(0, record[4])
            self.entemail.insert(0, record[5])
            self.license_plate.insert(0, record[6])
    def clearall(self):
        self.ent_driver_id.delete(0, END)
        self.ent_fullname.delete(0, END)
        self.ent_lastname.delete(0, END)
        self.entaddress.delete(0, END)
        self.entcontact.delete(0, END)
        self.entemail.delete(0, END)
        self.license_plate.delete(0, END)

    def update_driver(self):
        obj = Admin_middleware()
        obj.set_driver_id = self.ent_driver_id.get()
        obj.set_dfirstname = self.ent_fullname.get()
        obj.set_dlastname = self.ent_lastname.get()
        obj.set_daddress = self.entaddress.get()
        obj.set_dcontact_num = self.entcontact.get()
        obj.set_demail = self.entemail.get()
        obj.set_dlicense = self.license_plate.get()
        res = obj.admin_update_driver()
        if res :
            # self.clear_all_entry()
            self.get_tableinfo()
            messagebox.showinfo("Successful", 'Updated Successfully')



    def open_bookreq(self):
        for item in self.lbl_right.winfo_children():
            item.destroy()
        self.frm_bookingreq = Frame(self.lbl_right, bg="aquamarine1")
        self.frm_bookingreq.place(x=10, y=10, width=1230, height=760)

        self.labelleft = Label(self.frm_bookingreq, bg="#D3D3D3")
        self.labelleft.place(x=0, y=0, width=400, height=760)

        self.labelright = Label(self.frm_bookingreq, bg="black")
        self.labelright.place(x=400, y=0, width=830, height=760)

        ###label in label right
        lbl_head = Label(self.labelleft, text="Booking Details", bg="#D3D3D3", font=("Forte", 18))
        lbl_head.place(x=90, y=10, width=250)

        lbl_bookingid = Label(self.labelleft,text="Booking Id", bg="#D3D3D3", font=("Forte", 18))
        lbl_bookingid.place(x=0,y=40)

        self.ent_bookingid = Entry(self.labelleft)
        self.ent_bookingid.place(x=140, y=40, width=170, height=20)

        lbl_pickup_loc = Label(self.labelleft, text="Pick Up Location", bg="#D3D3D3", font=("Forte", 18))
        lbl_pickup_loc.place(x=0, y=70)

        self.entpicloc = Entry(self.labelleft)
        self.entpicloc.place(x=50, y=100, width=200, height=20)

        lbl_picdate = Label(self.labelleft, text="Pick Up Date", bg="#D3D3D3", font=("Forte", 18))
        lbl_picdate.place(x=0, y=130)

        self.entpicdate = Entry(self.labelleft)
        self.entpicdate.place(x=50, y=160, width=200, height=20)

        lbl_pictime = Label(self.labelleft, text="Pick Up Time", bg="#D3D3D3", font=("Forte", 18))
        lbl_pictime.place(x=0, y=190)

        self.entpictime = Entry(self.labelleft)
        self.entpictime.place(x=50, y=220, width=200, height=20)

        lbl_drop_loc = Label(self.labelleft, text="Drop Off Location", bg="#D3D3D3", font=("Forte", 18))
        lbl_drop_loc.place(x=0, y=250)

        self.entdroploc = Entry(self.labelleft)
        self.entdroploc.place(x=50, y=280, width=200, height=20)

        lbl_drop_time = Label(self.labelleft, text="Drop Off Time", bg="#D3D3D3", font=("Forte", 18))
        lbl_drop_time.place(x=0, y=310)

        self.entdroptime = Entry(self.labelleft)
        self.entdroptime.place(x=50, y=340, width=200, height=20)

        lbl_drop_date = Label(self.labelleft, text="Drop Off Date", bg="#D3D3D3", font=("Forte", 18))
        lbl_drop_date.place(x=0, y=370)

        self.entdropdate = Entry(self.labelleft)
        self.entdropdate.place(x=50, y=400, width=200, height=20)

        booking_stat = Label(self.labelleft, text="Booking Status", bg="#D3D3D3", font=("Forte", 18))
        booking_stat.place(x=0, y=430)

        self.ent_bookingstat = Entry(self.labelleft)
        self.ent_bookingstat.place(x=50, y=460, width=200, height=20)

        cust_id = Label(self.labelleft, text="Customer Id", bg="#D3D3D3", font=("Forte", 18))
        cust_id.place(x=0, y=490)

        self.ent_custid = Entry(self.labelleft)
        self.ent_custid.place(x=50, y=520, width=200, height=20)

        driver_id = Label(self.labelleft, text="Driver ID", bg="#D3D3D3", font=("Forte", 18))
        driver_id.place(x=0, y=550)

        self.ent_driverid = Entry(self.labelleft)
        # self.ent_driverid.place(x=50, y=580, width=200, height=20)
        self.cmb_driver_id = Combobox(self.labelleft, values=[], state='readonly')
        self.display_driver_id()
        self.cmb_driver_id.place(x=50, y=580, width=200, height=20)

        btn_confirm = Button(self.labelleft, text="CONFIRM", bg="#eee000", font=("Forte", 18), command=self.confirm_driver)
        btn_confirm.place(x=20, y=630)

        btn_update = Button(self.labelleft, text="UPDATE", bg="#eee000", font=("Forte", 18), command=self.update_booking)
        btn_update.place(x=200, y=630)

        btn_cancel = Button(self.labelleft, text="CANCEL", bg="#eee000", font=("Forte", 18), command=self.cancel_booking)
        btn_cancel.place(x=120, y=690)

        ##table in right
        ##constructing table
        column = ('booking_id', 'Pickup_location', 'DropOff_location', 'picdate', 'pictime', 'dropdate', 'droptime',
                  'booking_status', 'driver_id', 'cust_id')
        self.treet = ttk.Treeview(self.labelright, columns=column, show='headings')

        ##defining heading
        self.treet.heading('booking_id', text='bookingId')
        self.treet.heading('Pickup_location', text='PickUp')
        self.treet.heading('DropOff_location', text='Destination')
        self.treet.heading('picdate', text='PickUp Date')
        self.treet.heading('pictime', text='PickUp Time')
        self.treet.heading('dropdate', text='DropOff Date')
        self.treet.heading('droptime', text='DropOff Time')
        self.treet.heading('booking_status', text='Booking Status')
        self.treet.heading('driver_id', text='Driverid')
        self.treet.heading('cust_id', text='Customerid')
        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=45,
                        font=("", 13))

        ### sizing the heading in the columns
        self.treet.column("booking_id", anchor=CENTER, stretch=NO, width=67)
        self.treet.column("Pickup_location", anchor=CENTER, stretch=NO, width=120)
        self.treet.column("DropOff_location", anchor=CENTER, stretch=NO, width=120)
        self.treet.column("picdate", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("pictime", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("dropdate", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("droptime", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("booking_status", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("driver_id", anchor=CENTER, stretch=NO, width=100)
        self.treet.column("cust_id", anchor=CENTER, stretch=NO, width=100)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.labelright, orient="vertical", command=self.treet.yview)
        scolbar = ttk.Scrollbar(self.labelright, orient="horizontal", command=self.treet.xview)
        ##placing scrollbar by using place()
        self.treet.place(x=0, y=0, height=750, width=830)
        scrlbar.place(x=810, y=0, height=750)
        scolbar.place(x=0, y=730, width=830)
        self.treet.configure(yscrollcommand=scrlbar.set, xscrollcommand=scolbar.set)
        self.get_table_datas()
        self.treet.bind('<<TreeviewSelect>>', self.item_select)
    def get_table_datas(self):
        db = Log_db.Database()
        data = db.get_booking_table_data(self._user_id)
        count = 0
        for items in self.treet.get_children():
            self.treet.delete(items)

        try:
            for i in data:
                self.treet.insert('', count, text="",
                                  values=(i[0], i[1], i[2], i[4], i[3], i[5], i[6], i[7], i[8], i[9]))
        except TypeError:
            pass

    def item_select(self, event):
        for select_item in self.treet.selection():
            item = self.treet.item(select_item)
            record = item['values']

            # Delete data from entry
            self.ent_bookingid.delete(0, END)
            self.entpicloc.delete(0, END)
            self.entdroploc.delete(0, END)
            self.entpictime.delete(0, END)
            self.entpicdate.delete(0, END)
            self.entdropdate.delete(0, END)
            self.entdroptime.delete(0, END)
            self.ent_driverid.delete(0, END)
            self.ent_custid.delete(0, END)
            self.ent_bookingstat.delete(0, END)

            # Set data into entry
            self.ent_bookingid.insert(0, record[0])
            self.entpicloc.insert(0, record[1])
            self.entdroploc.insert(0, record[2])
            self.entpicdate.insert(0, record[3])
            self.entpictime.insert(0, record[4])
            self.entdropdate.insert(0, record[6])
            self.entdroptime.insert(0, record[5])
            self.ent_bookingstat.insert(0, record[7])
            self.ent_custid.insert(0, record[9])
            self.ent_driverid.insert(0, record[8])

    def display_driver_id(self):
        admin_mw = Admin_middleware()
        items = admin_mw.display_driverid()
        values=['Select Driver Id',]
        try:
            for i in items:
                values.append(i[0])
        except TypeError:
            pass
        self.cmb_driver_id['values']=values
        self.cmb_driver_id.current(0)

    def confirm_driver(self):
        admin_mw = Admin_middleware()
        admin_mw.set_booking_id = self.ent_bookingid.get()
        admin_mw.set_driver_id = self.cmb_driver_id.get()
        if self.ent_bookingstat.get() == 'Pending':
            if not(self.cmb_driver_id.get() == 'Select Driver Id'):
                result = admin_mw.assign_driverid()
                if result:
                    self.display_driver_id()
                    self.clear_all_entry()
                    self.get_table_datas()
                    messagebox.showinfo('Success', 'Successfully booked the booking.')
            else:
                messagebox.showerror('Error', 'Please select driver Id before conformation.')
        else:
            messagebox.showerror('Error', 'Cannot assign the driver to Driver status booked.')

    def update_booking(self):
        admin_mw = Admin_middleware()
        admin_mw.set_booking_id = self.ent_bookingid.get()
        admin_mw.set_pickuploc = self.entpicloc.get()
        admin_mw.set_pickupdate = self.entpicdate.get()
        admin_mw.set_pickuptime = self.entpictime.get()
        admin_mw.set_dropuploc = self.entdroploc.get()
        admin_mw.set_dropuptime = self.entdroptime.get()
        admin_mw.set_dropupdate = self.entdropdate.get()
        admin_mw.set_driver_id = self.ent_driverid.get()
        confirm = messagebox.showinfo('Update', 'Do you really want to update this booking?')
        if confirm:
            result = admin_mw.admin_update_booking()
            if result:
                self.display_driver_id()
                self.clear_all_entry()
                self.get_table_datas()
                messagebox.showinfo('Success', 'Successfully update the booking.')

    def cancel_booking(self):
        admin_mw = Admin_middleware()
        admin_mw.set_booking_id = self.ent_bookingid.get()
        admin_mw.set_driver_id = self.ent_driverid.get()
        result = admin_mw.cancel_booking()
        if result:
            self.display_driver_id()
            self.clear_all_entry()
            self.get_table_datas()
            messagebox.showinfo('Success', 'Successfully cancel the booking.')

    def open_bookhist(self):
        for item in self.lbl_right.winfo_children():
            item.destroy()
        self.frm_bookinghist = Frame(self.lbl_right, bg="aquamarine1")
        self.frm_bookinghist.place(x=10, y=10, width=1230, height=760)

        ##table in right
        ##constructing table
        column = ('booking_id', 'Pickup_location', 'DropOff_location', 'picdate', 'pictime', 'dropdate', 'droptime',
                  'booking_status', 'driver_id', 'cust_id')
        self.table = ttk.Treeview(self.frm_bookinghist, columns=column, show='headings')

        ##defining heading
        self.table.heading('booking_id', text='bookingId')
        self.table.heading('Pickup_location', text='PickUp')
        self.table.heading('DropOff_location', text='Destination')
        self.table.heading('picdate', text='PickUp Date')
        self.table.heading('pictime', text='PickUp Time')
        self.table.heading('dropdate', text='DropOff Date')
        self.table.heading('droptime', text='DropOff Time')
        self.table.heading('booking_status', text='Booking Status')
        self.table.heading('driver_id', text='Driverid')
        self.table.heading('cust_id', text='Customerid')
        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=45,
                        font=("", 13))

        ### sizing the heading in the columns
        self.table.column("booking_id", anchor=CENTER, stretch=NO, width=67)
        self.table.column("Pickup_location", anchor=CENTER, stretch=NO, width=120)
        self.table.column("DropOff_location", anchor=CENTER, stretch=NO, width=120)
        self.table.column("picdate", anchor=CENTER, stretch=NO, width=150)
        self.table.column("pictime", anchor=CENTER, stretch=NO, width=150)
        self.table.column("dropdate", anchor=CENTER, stretch=NO, width=150)
        self.table.column("droptime", anchor=CENTER, stretch=NO, width=150)
        self.table.column("booking_status", anchor=CENTER, stretch=NO, width=150)
        self.table.column("driver_id", anchor=CENTER, stretch=NO, width=150)
        self.table.column("cust_id", anchor=CENTER, stretch=NO, width=150)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.frm_bookinghist, orient="vertical", command=self.table.yview)
        scolbar = ttk.Scrollbar(self.frm_bookinghist, orient="horizontal", command=self.table.xview)
        ##placing scrollbar by using place()
        self.table.place(x=0, y=0, height=760, width=1230)
        scrlbar.place(x=1210, y=0, height=760)
        scolbar.place(x=0, y=740, width=1230)
        self.table.configure(yscrollcommand=scrlbar.set, xscrollcommand=scolbar.set)
        self.get_tabledatas()
        # self.table.bind('<<TreeviewSelect>>', self.item_select)

    def get_tabledatas(self):
        db = Log_db.Database()
        data = db.show_all_bookdata()
        count = 0
        for delete_data in self.table.get_children():
            self.table.delete(delete_data)

        try:
            for i in data:
                self.table.insert('', count, text="",
                                  values=(i[0], i[1], i[2], i[4], i[3], i[5], i[6], i[7], i[8], i[9]))
        except TypeError:
            pass

    def clear_all_entry(self):
        self.ent_bookingid.delete(0, END)
        self.entpicloc.delete(0, END)
        self.entpicdate.delete(0, END)
        self.entpictime.delete(0, END)
        self.entdroploc.delete(0, END)
        self.entdroptime.delete(0, END)
        self.entdropdate.delete(0, END)
        self.ent_bookingstat.delete(0, END)
        self.ent_custid.delete(0, END)
        self.ent_driverid.delete(0, END)
        self.cmb_driver_id.current(0)

if __name__ =='__main__':
    Admin(1)