from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
from MySql.driver_middleware import Driver_Middleware

class Driver:

    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.driver = Tk()
        self.driver.geometry('1540x840')
        self.driver.title('driver dashboard')
        self.driver.resizable(False, False)
        self.driver.wm_state('zoomed')
        ###Labels####
        head = Label(self.driver, text="Online Taxi Booking System", bg="#eee000",
                     font=("Harlow Solid Italic", 30, "bold"), fg="black", width=60)
        head.place(x=0, y=0)

        self.lbl_left = Frame(self.driver,  bg="#D3D3D3")
        self.lbl_left.place(x=0, y=58,width=290, height=790)

        self.lbl_right = Frame(self.driver, bg="grey")
        self.lbl_right.place(x=285, y=58,width=1250, height=790)

        ####labels in label left
        lbl_driver = Label(self.lbl_left, text="Driver", bg="#eee000", fg="black",
                          font=("Harlow Solid Italic", 20, "bold"), width=14)
        lbl_driver.place(x=5, y=10, height=50)

        btn_viewnewtrips = Button(self.lbl_left, text="View New Trips", bg="#eee000", fg="black",
                                  font=("Harlow Solid Italic", 18, "bold"), width=15, command=self.open_newtrips)
        btn_viewnewtrips.place(x=5, y=100)

        btn_viewbookinghistory = Button(self.lbl_left, text="Booking History",bg="#eee000", fg="black",
                                  font=("Harlow Solid Italic", 18, "bold"), width=15,command=self.openhistory )
        btn_viewbookinghistory.place(x=5, y=180)

        btn_logout = Button(self.lbl_left, text="Log Out", bg="#eee000", fg="black",
                            font=("Harlow Solid Italic", 18, "bold"), width=15, command= self.opennewpage)
        btn_logout.place(x=5, y=700)

        self.driver.mainloop()

    def opennewpage(self):
        call(["Python", "welcomepage.py"])
        self.driver.destroy()

    def open_newtrips(self):
        for item in self.lbl_right.winfo_children():
            item.destroy()
        self.frame_newtrips = Frame(self.lbl_right, bg="grey")
        self.frame_newtrips.place(x=10, y=10, width=1228, height=765)

        ###adding new label in label right
        self.lb_inside = Label(self.frame_newtrips, bg="#D3D3D3")
        self.lb_inside.place(x=8, y=8,  width=1280,height=260)

        lb_head = Label(self.lb_inside, text="Upcoming Trips",bg="#D3D3D3",font=("Harlow Solid Italic", 25))
        lb_head.place(x=480, y=10, height=30, width=300)

        lb_customerid = Label(self.lb_inside, text="Customer Id :", bg="#D3D3D3",font=("Forte", 18))
        lb_customerid.place(x=2, y=75)

        self.ent_custid = Entry(self.lb_inside, width=25)
        self.ent_custid.place(x=170, y=80, height=25)

        lb_bookingid = Label(self.lb_inside, text="Booking Id :", bg="#D3D3D3",font=("Forte", 18))
        lb_bookingid.place(x=400, y=75)

        self.ent_bookingid = Entry(self.lb_inside, width=25)
        self.ent_bookingid.place(x=560, y=80, height=25)

        lb_pickup = Label(self.lb_inside, text="Pickup Location", bg="#D3D3D3",font=("Forte", 18))
        lb_pickup.place(x=2, y=120)

        self.ent_pickup = Entry(self.lb_inside, width=29)
        self.ent_pickup.place(x=10, y=155, height=25)

        lb_pictime = Label(self.lb_inside, text="Pickup Time", bg="#D3D3D3", font=("Forte", 18))
        lb_pictime.place(x=242, y=120)

        self.ent_pickuptime = Entry(self.lb_inside, width=29)
        self.ent_pickuptime.place(x=250, y=155, height=25)

        lb_picdate = Label(self.lb_inside, text="Pickup Date", bg="#D3D3D3", font=("Forte", 18))
        lb_picdate.place(x=482, y=120)

        self.ent_picdate = Entry(self.lb_inside, width=29)
        self.ent_picdate.place(x=490, y=155, height=25)

        lb_bookstatus = Label(self.lb_inside, text="Booking Status", bg="#D3D3D3", font=("Forte", 18))
        lb_bookstatus.place(x=720, y=120)

        self.ent_bookstatus = Entry(self.lb_inside, width=29)
        self.ent_bookstatus.place(x=720, y=155, height=25)

        lb_dropofflocation = Label(self.lb_inside, text="DropOff Location", bg="#D3D3D3", font=("Forte", 18))
        lb_dropofflocation.place(x=2, y=180)

        self.ent_dropofflocation = Entry(self.lb_inside, width=29)
        self.ent_dropofflocation.place(x=10, y=215, height=25)

        lb_droptime = Label(self.lb_inside, text="DropOff Time", bg="#D3D3D3", font=("Forte", 18))
        lb_droptime.place(x=242, y=180)

        self.ent_droptime = Entry(self.lb_inside, width=29)
        self.ent_droptime.place(x=250, y=215, height=25)

        lb_dropdate = Label(self.lb_inside, text="DropOff Date", bg="#D3D3D3", font=("Forte", 18))
        lb_dropdate.place(x=482, y=180)

        self.ent_dropdate = Entry(self.lb_inside, width=29)
        self.ent_dropdate.place(x=490, y=215, height=25)

        btn_start = Button(self.lb_inside, text="Start Ride", font=("Forte", 18), bg="#eee000", command=self.start_ride)
        btn_start.place(x=1000, y=30)

        btn_finish = Button(self.lb_inside, text="Finish Ride", font=("Forte", 18), bg="#eee000", command=self.finish_ride)
        btn_finish.place(x=1000, y=100)

        ###tabel in label right
        ###constructing a table
        column = ('booking_id', 'picdate', 'pictime', 'Pickup Location', 'DropOff Location', 'dropdate', 'droptime', 'custid', 'status')
        self.tree = ttk.Treeview(self.frame_newtrips, columns=column, show='headings')

        ##defining heading
        self.tree.heading('booking_id', text='Booking Id')
        self.tree.heading('picdate', text='Pickup Date')
        self.tree.heading('pictime', text='Pickup Time')
        self.tree.heading('dropdate', text='DropOff Date')
        self.tree.heading('droptime', text='DropOf Time')
        self.tree.heading('Pickup Location', text='Pickup Location')
        self.tree.heading('DropOff Location', text='Destination')
        self.tree.heading('custid', text='Customer Id')
        self.tree.heading('status', text='Booking Status')

        ##adding styles in table
        style = ttk.Style()

        ##configure color of tree view
        style.configure("Treeview",
                        background="grey",
                        foreground="black",
                        rowheight=45)

        ### sizing the heading in the columns
        self.tree.column("booking_id", anchor=CENTER, stretch=NO, width=80)
        self.tree.column("picdate", anchor=CENTER, stretch=NO, width=160)  # , ne, e, se, s, sw, w, nw,
        self.tree.column("pictime", anchor=CENTER, stretch=NO, width=160)
        self.tree.column("dropdate", anchor=CENTER, stretch=NO, width=160)  # , ne, e, se, s, sw, w, nw,
        self.tree.column("droptime", anchor=CENTER, stretch=NO, width=150)
        self.tree.column("Pickup Location", anchor=CENTER, stretch=NO, width=200)
        self.tree.column("DropOff Location", anchor=CENTER, stretch=NO, width=200)
        self.tree.column("custid", anchor=CENTER,stretch=NO, width=90)
        self.tree.column("status", anchor=CENTER,stretch=NO, width=150)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.frame_newtrips, orient="vertical", command=self.tree.yview)
        scrlbarx = ttk.Scrollbar(self.frame_newtrips, orient="horizontal", command=self.tree.xview)
        ##placing scrollbar by using place()
        self.tree.place(x=8, y=270, width=1220, height=490)
        scrlbar.place(x=1208, y=270, height=490)
        scrlbarx.place(x=8, y=740, width=1200)
        self.tree.configure(yscrollcommand=scrlbar.set)
        self.tree.configure(xscrollcommand=scrlbarx.set)
        self.get_table_datas()
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

    def get_table_datas(self):
        driver_mw = Driver_Middleware()
        driver_mw.set_driver_id = self.driver_id
        data = driver_mw.get_rides_details()
        count = 0
        for items in self.tree.get_children():
            self.tree.delete(items)

        try:
            for i in data:
                self.tree.insert('', count, text="", values=(i[0], i[4], i[3], i[1], i[2], i[6], i[5], i[9], i[7]))
        except TypeError:
            pass

    def item_selected(self, event):
        # Iteration to get data of selected data of table
        for select_item in self.tree.selection():
            item = self.tree.item(select_item)
            data = item['values']

            # Delete all the data available in the table
            self.ent_bookingid.delete(0, END)
            self.ent_picdate.delete(0, END)
            self.ent_pickuptime.delete(0, END)
            self.ent_pickup.delete(0, END)
            self.ent_dropofflocation.delete(0, END)
            self.ent_dropdate.delete(0, END)
            self.ent_droptime.delete(0, END)
            self.ent_custid.delete(0, END)
            self.ent_bookstatus.delete(0, END)

            # Inserting the selected data from table to its respected fields
            self.ent_bookingid.insert(0, data[0])
            self.ent_picdate.insert(0, data[1])
            self.ent_pickuptime.insert(0, data[2])
            self.ent_pickup.insert(0, data[3])
            self.ent_dropofflocation.insert(0, data[4])
            self.ent_dropdate.insert(0, data[5])
            self.ent_droptime.insert(0, data[6])
            self.ent_custid.insert(0, data[7])
            self.ent_bookstatus.insert(0, data[8])


    def openhistory(self):
        for item in self.lbl_right.winfo_children():
            item.destroy()
        self.frame_previoustrips = Frame(self.lbl_right, bg="aquamarine")
        self.frame_previoustrips.place(x=10, y=10, width=1228, height=765)

        ###constructing a table
        column = ('booking_id', 'picdate', 'pictime', 'Pickup Location', 'DropOff Location', 'dropdate', 'droptime', 'custid', 'status')
        self.tree = ttk.Treeview(self.frame_previoustrips, columns=column, show='headings')

        ##defining heading
        self.tree.heading('booking_id', text='Booking Id')
        self.tree.heading('picdate', text='Pickup Date')
        self.tree.heading('pictime', text='Pickup Time')
        self.tree.heading('dropdate', text='DropOff Date')
        self.tree.heading('droptime', text='DropOf Time')
        self.tree.heading('Pickup Location', text='Pickup Location')
        self.tree.heading('DropOff Location', text='Destination')
        self.tree.heading('custid', text='Customer Id')
        self.tree.heading('status', text='Booking Status')

        ##adding styles in table
        style = ttk.Style()

        ##configure color of tree view
        style.configure("Treeview",
                        background="grey",
                        foreground="black",
                        rowheight=45)

        ### sizing the heading in the columns
        self.tree.column("booking_id", anchor=CENTER, stretch=NO, width=80)
        self.tree.column("picdate", anchor=CENTER, stretch=NO, width=160)  # , ne, e, se, s, sw, w, nw,
        self.tree.column("pictime", anchor=CENTER, stretch=NO, width=160)
        self.tree.column("dropdate", anchor=CENTER, stretch=NO, width=160)  # , ne, e, se, s, sw, w, nw,
        self.tree.column("droptime", anchor=CENTER, stretch=NO, width=150)
        self.tree.column("Pickup Location", anchor=CENTER, stretch=NO, width=200)
        self.tree.column("DropOff Location", anchor=CENTER, stretch=NO, width=200)
        self.tree.column("custid", anchor=CENTER, stretch=NO, width=80)
        self.tree.column("status", anchor=CENTER, stretch=NO, width=150)

        ###scroll barr
        # constructing vertical scrollbar
        scrlbar = ttk.Scrollbar(self.frame_previoustrips, orient="vertical", command=self.tree.yview)
        # constructing horizontal scrollbar
        scrlbarx = ttk.Scrollbar(self.frame_previoustrips, orient="horizontal", command=self.tree.xview)
        ##placing scrollbar by using place()
        self.tree.place(x=8, y=20, width=1200, height=730)
        scrlbar.place(x=1198, y=20, height=730)
        scrlbarx.place(x=8, y=730, width=1200)
        self.tree.configure(yscrollcommand=scrlbar.set)
        self.tree.configure(xscrollcommand=scrlbarx.set)
        self.get_table_history_datas()

    def get_table_history_datas(self):
        driver_mw = Driver_Middleware()
        driver_mw.set_driver_id = self.driver_id
        data = driver_mw.get_rides_history_details()
        count = 0
        for items in self.tree.get_children():
            self.tree.delete(items)

        try:
            for i in data:
                self.tree.insert('', count, text="", values=(i[0], i[4], i[3], i[1], i[2], i[6], i[5], i[9], i[7]))
        except TypeError:
            pass

    def start_ride(self):
        check = self.ent_bookstatus.get()
        if check == "Booked":
            confirm = messagebox.askyesno('Confirm', 'Do you want to start your ride ?')
            if confirm:
                driver_mw = Driver_Middleware()
                driver_mw.set_driver_id = self.driver_id
                driver_mw.set_booking_id = self.ent_bookingid.get()
                result = driver_mw.start_ride()
                if result:
                    self.get_table_datas()
                    self.clear_all_fields()
                    messagebox.showinfo('Success', 'Your ride has been started.\nHave a nice trip.')

        else:
            messagebox.showerror('Error', 'Please finish your previous ride.')

    def finish_ride(self):
        check = self.ent_bookstatus.get()
        if check == "Confirmed":
            confirm = messagebox.askyesno('Confirm', 'Do you want to finish your ride ?')
            if confirm:
                driver_mw = Driver_Middleware()
                driver_mw.set_driver_id = self.driver_id
                driver_mw.set_booking_id = self.ent_bookingid.get()
                result = driver_mw.finish_ride()
                if result:
                    self.get_table_datas()
                    self.clear_all_fields()
                    messagebox.showinfo('Success', 'Your ride has been completed.')
        else:
            messagebox.showerror('Error', 'First start your ride.')

    def clear_all_fields(self):
        self.ent_bookingid.delete(0, END)
        self.ent_picdate.delete(0, END)
        self.ent_pickuptime.delete(0, END)
        self.ent_pickup.delete(0, END)
        self.ent_dropofflocation.delete(0, END)
        self.ent_dropdate.delete(0, END)
        self.ent_droptime.delete(0, END)
        self.ent_custid.delete(0, END)
        self.ent_bookstatus.delete(0, END)


if __name__ == '__main__':
    Driver(1)