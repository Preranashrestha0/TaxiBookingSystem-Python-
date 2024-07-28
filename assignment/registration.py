import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
from MySql import mid_REG, Log_db


class Registration:
    def __init__(self):
        self.Page = Tk()
        self.Page.title("Registration form")
        self.Page.geometry('1200x750')
        self.Page.configure(bg="#fff")
        self.Page.resizable(False,False)

         #Labels
        label_pic = Label(self.Page, width=150, height=70)
        label_pic.place(x=0, y=0)

        self.label_info = Label(self.Page, bg="white", borderwidth=0,width=90, height=70, relief="solid")#"flat", "raised", "sunken", "ridge", "solid", and "groove"
        self.label_info.place(x=700, y=0)

        #for image
        canvas = Canvas(label_pic, width=800, height=880)
        canvas.pack(fill=BOTH, expand=False)

        global image, resized, image2
        image = Image.open(r"taxi_img.png").resize((800, 750))
        image2 = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image = image2, anchor='nw')

        # head=Label(self.Page, text="Taxi Booking System", font=("Harlow Solid Italic",30, "bold"), fg="black", bg="#eee000", width=50)
        # head.place(x=0, y=0)

        head2=Label(self.Page, text="Get Your Comfortable Journey For Outstations!", font=("Harlow Solid Italic",30, "bold"), fg="white", bg="black", width=48)
        head2.place(x=0, y=700)

        title=Label(self.label_info,text="Registration Form",font=("Harlow Solid Italic",25, "bold"), fg="black", bg="white")
        title.place(x=200,y=60)#LBl1 will be placed in center, n, ne, e, se, s, sw, w, nw, or center

        lbl_fname=Label(self.label_info,text="First name:",font=("",15, "bold"),fg="black", bg="white")
        lbl_fname.place(x=100,y=140)

        self.ent_fname=Entry(self.label_info, font=("", 15))
        self.ent_fname.place(x=250,y=140)

        lbl_lname = Label(self.label_info, text="Last name:", font=("", 15, "bold"), fg="black", bg="white")
        lbl_lname.place(x=100, y=190)

        self.ent_lname = Entry(self.label_info, font=("", 15))
        self.ent_lname.place(x=250, y=190)

        Address=Label(self.label_info,text=" Address :",font=("",15, "bold"),fg="black", bg="white")
        Address.place(x=92,y=245)

        self.ent_address=Entry(self.label_info, font=("", 15))
        self.ent_address.place(x=250,y=245)

        lbl_gender=Label(self.label_info,text="Gender:",font=("",15, "bold"),fg="black", bg="white")
        lbl_gender.place(x=95,y=300)

        # ent3=Entry(label_info, font=("", 15))
        # ent3.place(x=250,y=300)

        lbl0 = Label(self.label_info,width=50, height=2, bg="white")
        lbl0.place(x=250, y=300)

        self.rb_val = IntVar()
        # rb_val.set(0)
        self.rb = Radiobutton(lbl0, width=5, bg="white", font=("", 12), text="Male",variable=self.rb_val, value=0)
        self.rb.grid(row=0, column=1)

        self.rb1 = Radiobutton(lbl0, width=5,bg="white", font=("", 12), text="Female",variable=self.rb_val, value=1)
        self.rb1.grid(row=0, column=2)

        self.rb2 = Radiobutton(lbl0, width=5,bg="white",font=("", 12), text="Others",variable=self.rb_val, value=2)
        self.rb2.grid(row=0, column=3)

        lbl_email=Label(self.label_info,text="Email:",font=("",15, "bold"),fg="black", bg="white")
        lbl_email.place(x=100,y=355)

        self.ent_email=Entry(self.label_info, font=("", 15))
        self.ent_email.place(x=250,y=355)

        lbl_contact=Label(self.label_info,text="Contact No. :",font=("",15, "bold"),fg="black", bg="white")
        lbl_contact.place(x=100,y=410)

        self.ent_contact=Entry(self.label_info, font=("", 15))
        self.ent_contact.place(x=250,y=410)

        lbl_payment_method=Label(self.label_info,text="Payment Method :",font=("",15, "bold"),fg="black")
        lbl_payment_method.place(x=100,y=465)

        self.cmb_paymentmethod = Combobox(self.label_info, font=("", 15), width=16, values=( "Khalti","Esewa", "ImePay"))
        self.cmb_paymentmethod.place(x=280, y=465)

        # ent6=Entry(label_info, font=("", 15))
        # ent6.place(x=250,y=465)

        lbl_password=Label(self.label_info,text="Password :",font=("",15, "bold"),fg="black")
        lbl_password.place(x=100,y=520)

        # def remove_char(event):
        #     ent7.delete(0, END)
        #     ent7.config(show="*")

        self.ent_password=Entry(self.label_info, show="*",font=("", 16), width=18, justify="left")
        # ent7.insert(0, "password")
        self.ent_password.place(x=250,y=520)
        # ent7.bind('<FocusIn>', remove_char)


        ###show password eye icon###
        self.image = Image.open('eye.png')
        self.res_img = self.image.resize((20, 20))
        self.new_img = ImageTk.PhotoImage(self.res_img)

        self.image1 = Image.open('eyeclose1.png')
        self.res_img1 = self.image1.resize((20, 20))
        self.new_img1= ImageTk.PhotoImage(self.res_img1)

        temp_value = True

        self.btnn = Button(self.ent_password, width=30, image=self.new_img1)
        self.btnn.place(x=180, y=0)

        self.btnn.bind('<Button-1>', self.ShowPwd)
        self.btnn.bind('<ButtonRelease-1>', self.hidePwd)

        btn_register = Button(self.label_info, text="REGISTER", font=("Forte", 17), bg="black", fg="white",
                              command=lambda: self.register())
        btn_register.place(x=200, y=600)

        btn_clear = Button(self.label_info, text="CLEAR ALL", font=("Forte", 17), bg="black", fg="white",
                           command=lambda: self.clear_entry_box())
        btn_clear.place(x=340, y=600)

        btn_back = Button(self.label_info, text="BACK", font=("Forte", 17), bg="black", fg="white", command=lambda: self.Open_homepage())
        btn_back.place(x=300, y=650)

        # exit(ent7.get())
        obj = Log_db.Database()
        # # obj.register_user(self.register_credentials)

        self.Page.mainloop()

    def ShowPwd(self, event):
        # if ent7.cget("show") == "*":
        #     password = ent7.get()
        self.ent_password.config(show="")
        self.btnn.configure(image=self.new_img)
        # else:
        #     ent7.config(show="*")
        #     btnn.configure(image=new_img)
        #
    def hidePwd(self, event):
        # password = ent7.get()
        self.ent_password.config(show="*")
        self.btnn.configure(image=self.new_img1)

    #ent7 = maskpass.advpass()

    def Open_homepage(self):
        call(["Python", "welcomepage.py"])
        self.Page.destroy()

        ####Validation###
    def validation(self):
        reg_mw = mid_REG.GetSetReg(self.ent_fname.get(), self.ent_lname.get(), self.ent_address.get(), self.rb_val.get(), self.ent_email.get(), self.ent_contact.get(), self.cmb_paymentmethod.get(), self.ent_password.get())
        if not all((self.ent_fname.get(), self.ent_lname.get(),self.ent_address.get(), self.cmb_paymentmethod.get(), self.ent_contact.get(), self.ent_email.get(), self.ent_password.get())):
            messagebox.showwarning('Empty Field', 'Please insert all the fields')
            return False
        elif not(reg_mw.is_valid_fname(reg_mw.firstname)):
            pass
        elif not(reg_mw.is_valid_lname(reg_mw.lastname)):
            pass
        elif not(reg_mw.is_valid_address(reg_mw.address)):
            pass
        elif not(reg_mw.is_valid_email(reg_mw.email)):
            pass
        elif not(reg_mw.is_valid_number(reg_mw.phone_num)):
            pass
        elif not(reg_mw.is_valid_password(reg_mw.password)):
            pass
        else:
            return True

        # messagebox.showinfo('Successful', 'Validation Successfully !!')
        # return True

    def clear_entry_box(self):
        self.ent_fname.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_contact.delete(0, END)
        self.cmb_paymentmethod.delete(0, END)
        self.ent_password.delete(0, END)




    # def Register():

    def register(self):
        if not self.validation():
            print('Hello')
        else:
            if self.rb_val.get() == 0:
                self.gender = 'Male'
            elif self.rb_val.get() == 1:
                self.gender = 'Female'
            else:
                self.gender = 'Others'
            register_credentials = mid_REG.GetSetReg(self.ent_fname.get(),self.ent_lname.get(), self.ent_address.get(), self.gender,
                                                     self.ent_email.get(), self.ent_contact.get(),self.cmb_paymentmethod.get(),
                                                     self.ent_password.get())
            # print(register_credentials.__str__())
            db = Log_db.Database()
            db.register_user(register_credentials)
            messagebox.showinfo("Successful", "Registration Successful")
            self.Page.destroy()
            call(["Python", "new_log.py"])



if __name__=='__main__':
    Registration()