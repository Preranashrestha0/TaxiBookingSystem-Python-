from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from MySql import  cust_middleware, Log_db
from tkinter import messagebox
from middleware.booking_middleware import Booking_middleware

class Customer:
    def __init__(self, customer_Id = 1):
        self.customer_Id = customer_Id
        self.dashboard = Tk()
        self.dashboard.title("Dashboard")
        self.dashboard.geometry('1140x850')
        self.dashboard.configure(bg="#fff")
        self.dashboard.resizable(False,False)

        #Labels

        self.label_left = Label(self.dashboard, width=162, height=22, bg="#e2e5de")
        self.label_left.place(x=0, y=0)

        self.label_right = Label(self.dashboard, width=162, height = 30, bg="gray")
        self.label_right.place(x=0, y=330)

        head = Label(self.dashboard,text="Online Taxi Booking System", bg="#eee000", font=("Harlow Solid Italic", 30, "bold"), fg="black", width=45)
        head.place(x=0,y=0)

        ##label in left side
        booking_head = Label(self.label_left, text="Taxi Booking Details", fg="black", bg="#e2e5de", font=("Harlow Solid Italic", 19), width=54)
        booking_head.place(x=90, y=60)

        pick_up = Label(self.label_left, text="From City : ", fg="black", bg="#e2e5de",font=("", 15))
        pick_up.place(x=20, y=100)

        self.ent_pickup=Entry(self.label_left, font=("", 15), width=20)
        self.ent_pickup.place(x=20, y=130)

        drop_off = Label(self.label_left, text="To : ", fg="black",bg="#e2e5de", font=("", 15))
        drop_off.place(x=300, y=100)

        self.ent_dropoff=Entry(self.label_left, font=("", 15), width=20)
        self.ent_dropoff.place(x=300, y=130)

        ptime = Label(self.label_left, text="PickUp Time : ", fg="black",bg="#e2e5de", font=("", 15))#, bg="#aaaddd"
        ptime.place(x=20, y=160)

        self.ent_ptime=Entry(self.label_left, font=("", 15),width=20)
        self.ent_ptime.place(x=20, y=195)

        pdate = Label(self.label_left, text="PickUp Date : ", fg="black", bg="#e2e5de", font=("", 15))
        pdate.place(x=20, y=225)

        self.ent_pdate = DateEntry(self.label_left, selectmode="day", year=2022, month=12, date=1, width=18,font=("", 15))
        self.ent_pdate.place(x=20, y=255)

        self.ent_dropoff = Entry(self.label_left, font=("", 15), width=20)
        self.ent_dropoff.place(x=300, y=130)

        dtime = Label(self.label_left, text="DropOff Time : ", fg="black", bg="#e2e5de", font=("", 15))  # , bg="#aaaddd"
        dtime.place(x=300, y=160)

        self.ent_dtime = Entry(self.label_left, font=("", 15), width=20)
        self.ent_dtime.place(x=300, y=195)

        ddate = Label(self.label_left, text="DropOff Date : ", fg="black", bg="#e2e5de", font=("", 15))
        ddate.place(x=300, y=225)

        self.ent_ddate = DateEntry(self.label_left, selectmode="day", year=2022, month=12, date=1, width=18,
                                  font=("", 15))
        self.ent_ddate.place(x=300, y=255)

        self.ent_booking_id = Entry(self.label_left)
        self.ent_driver_id = Entry(self.label_left)
        self.ent_booking_status = Entry(self.label_left)

        # self.ent_booking_id.place(x=20, y=290)
        # self.ent_driver_id.place(x=380, y=290)
        # self.ent_booking_status.place(x=520, y=290)
        # #
        ##button
        btn_booking = Button(self.label_left, font=("", 15), text="Book", fg="black", bg="#eee000", width=8,
                             command=self.booking_mw)
        btn_booking.place(x=800, y=100)

        btn_update = Button(self.label_left, font=("", 15), text="Update", fg="black", bg="#eee000", width=8,
                            command=self.update_booking)
        btn_update.place(x=800, y=150)

        btn_delete = Button(self.label_left, font=("", 15), text="Cancel", fg="black", bg="#eee000", width=8,
                            command=self.cancel_booking)
        btn_delete.place(x=800, y=200)

        btn_clear = Button(self.label_left, font=("", 15), text="Clear", fg="black", bg="#eee000", width=8,
                            command=self.clear_entry)
        btn_clear.place(x=800, y=250)

        ##Table
        ##constructing table
        column = ('booking_id', 'Pickup_location', 'DropOff_location', 'picdate', 'pictime','dropdate','droptime', 'booking_status', 'driver_id', 'cust_id')
        self.table = ttk.Treeview(self.label_right, columns=column, show='headings')

        ##defining heading
        self.table.heading('booking_id', text='Id')
        self.table.heading('Pickup_location', text='PickUp')
        self.table.heading('DropOff_location', text='Destination')
        self.table.heading('picdate', text='Pick Up Date')
        self.table.heading('pictime', text='Pick Up Time')
        self.table.heading('dropdate', text='DropOff Date')
        self.table.heading('droptime', text='DropOff Time')
        self.table.heading('booking_status', text='Booking Status')
        self.table.heading('driver_id', text='Drivers Id')
        self.table.heading('cust_id', text='Customer id')
        ##Add some style
        style = ttk.Style()
        ##configure our treeview color
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=45,
                        font = ("", 13))

        ### sizing the heading in the columns
        self.table.column("booking_id", anchor=CENTER, stretch=NO, width=87, minwidth=67)
        self.table.column("Pickup_location", anchor=CENTER, stretch=NO, width=120)
        self.table.column("DropOff_location", anchor=CENTER, stretch=NO, width=120)
        self.table.column("picdate", anchor=CENTER, stretch=NO, width=120)
        self.table.column("pictime", anchor=CENTER, stretch=NO, width=100)
        self.table.column("dropdate", anchor=CENTER, stretch=NO, width=120)
        self.table.column("droptime", anchor=CENTER, stretch=NO, width=100)
        self.table.column("booking_status", anchor=CENTER, stretch=NO, width=120)
        self.table.column("driver_id", anchor=CENTER, stretch=NO, width=100)
        self.table.column("cust_id", anchor=CENTER, stretch=NO, width=100)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.label_right, orient="vertical", command=self.table.yview)
        ##placing scrollbar by using place()
        self.table.place(x=0, y=0, height=450, width=1130)
        scrlbar.place(x=1120, y=0, height=450)
        self.table.configure(yscrollcommand=scrlbar.set)
        self.get_table_data()
        self.table.bind('<<TreeviewSelect>>', self.item_selected)

        self.dashboard.mainloop()

    def get_table_data(self):
        db = Log_db.Database()
        data = db.get_booking_table_data()
        count = 0
        for delete_data in self.table.get_children():
            self.table.delete(delete_data)

        try:
            for i in data:
                self.table.insert('', count, text="", values=(i[0], i[1], i[2], i[4], i[3],i[6],i[5],i[7],  i[8], i[9]))
        except TypeError:
            pass


    def item_selected(self, event):
        for selected_item in self.table.selection():
            item = self.table.item(selected_item)
            record = item['values']

            # Delete data from entry
            self.ent_pickup.delete(0, END)
            self.ent_dropoff.delete(0, END)
            self.ent_ptime.delete(0, END)
            self.ent_dtime.delete(0, END)
            self.ent_booking_id.delete(0, END)
            self.ent_driver_id.delete(0, END)
            self.ent_booking_status.delete(0, END)

            # Set data into entry
            self.ent_booking_id.insert(0, record[0])
            self.ent_pickup.insert(0, record[1])
            self.ent_dropoff.insert(0, record[2])
            pdate = datetime.strptime(record[3], '%Y-%m-%d').date()
            self.ent_pdate.set_date(pdate)
            self.ent_ptime.insert(0, record[4])
            ddate = datetime.strptime(record[5], '%Y-%m-%d').date()
            self.ent_ddate.set_date(ddate)
            self.ent_dtime.insert(0, record[6])
            self.ent_booking_status.insert(0, record[8])
            self.ent_driver_id.insert(0, record[7])

    def booking_mw(self):
        pdate = self.ent_pdate.get_date()
        set_pdate = pdate.strftime('%Y-%m-%d')
        ddate = self.ent_ddate.get_date()
        set_ddate = ddate.strftime('%Y-%m-%d')
        booking_credentials = cust_middleware.Customer_bookingdata(self.ent_pickup.get(), self.ent_dropoff.get(),
                                                                   self.ent_ptime.get(), set_pdate, self.ent_dtime.get(),set_ddate,
                                                                    self.customer_Id)

        try:
            db = Log_db.Database()
            db.user_booking(booking_credentials)
            self.clear_entry()
            self.get_table_data()
        except AttributeError:
            messagebox.showerror('Error', 'Could not established connection to mysql database !!')
            self.clear_entry()

    def update_booking(self):
        pdate = self.ent_pdate.get_date()
        set_pdate = pdate.strftime('%Y-%m-%d')
        ddate = self.ent_ddate.get_date()
        set_ddate = ddate.strftime('%Y-%m-%d')
        booking_md = Booking_middleware(self.ent_pickup.get(), self.ent_dropoff.get(), self.ent_ptime.get(),
                                        set_pdate, self.ent_dtime.get(),set_ddate, self.ent_booking_id.get(), self.customer_Id)
        booking_md.set_booking_status = self.ent_booking_status.get()
        check = messagebox.showwarning('Update', 'Do you really want to update your booking?')
        if check == 'ok':
            if booking_md.get_status == 'Pending':
                result = booking_md.update_booking()
                if result:
                    messagebox.showinfo('Success', 'Your booking has been updated successfully')
                    self.clear_entry()
                    self.get_table_data()
                else:
                    messagebox.showerror('Error', 'Failed to update your booking.')
                    self.clear_entry()

    def cancel_booking(self):
        pdate = self.ent_pdate.get_date()
        set_pdate = pdate.strftime('%Y-%m-%d')
        ddate = self.ent_ddate.get_date()
        set_ddate = ddate.strftime('%Y-%m-%d')
        booking_md = Booking_middleware(self.ent_pickup.get(), self.ent_dropoff.get(), self.ent_ptime.get(),
                                        set_pdate,self.ent_dtime.get(), set_ddate, self.ent_booking_id.get(), self.customer_Id)
        booking_md.set_booking_status = self.ent_booking_status.get()
        check = messagebox.askyesno('Update', 'Do you really want to cancel your booking?')
        if check == 'yes':
            if booking_md.get_status == 'Pending':
                result = booking_md.cancel_booking()
                if result:
                    messagebox.showinfo('Success', 'Your booking has been cancelled successfully')
                    self.clear_entry()
                    self.get_table_data()
                else:
                    messagebox.showerror('Error', 'Failed to update your booking.')
                    self.clear_entry()

    def clear_entry(self):
        self.ent_pickup.delete(0, END)
        self.ent_dropoff.delete(0, END)
        self.ent_ptime.delete(0, END)
        self.ent_dtime.delete(0, END)
        self.ent_driver_id.delete(0, END)
        self.ent_booking_id.delete(0, END)
        self.ent_booking_status.delete(0, END)


if __name__ == '__main__':
    Customer()