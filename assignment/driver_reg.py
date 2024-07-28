from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from subprocess import call
from MySql import driverreg_middleware, Log_db


class driver_Reg:
    def __init__(self):
        self.dregister = Tk()
        self.dregister.title("Driver Registration")
        self.dregister.geometry('350x600')
        self.dregister.configure(bg='#D3D3D3')
        self.dregister.resizable(False, False)

        ###Labels####
        lbl_head = Label(self.dregister, text="Driver Registration", font=("Harlow Solid Italic", 20), width=14, height=1, bg="#D3D3D3")
        lbl_head.place(x=70, y=10)

        lbl_fname = Label(self.dregister, text="First Name", font=("Magneto", 15), bg="#D3D3D3")
        lbl_fname.place(x=20, y=50)

        self.ent_fname = Entry(self.dregister, width=39)
        self.ent_fname.place(x=30, y=78, height=23)

        lbl_lname = Label(self.dregister, text="Last Name", font=("Magneto", 15), bg="#D3D3D3")
        lbl_lname.place(x=20, y=105)

        self.ent_lname = Entry(self.dregister, width=39)
        self.ent_lname.place(x=30, y=132, height=23)

        lbl_address = Label(self.dregister, text="Address", font=("Magneto", 15), bg="#D3D3D3")
        lbl_address.place(x=20, y=160, height=23)

        self.ent_address = Entry(self.dregister, width=39)
        self.ent_address.place(x=30, y=185, height=23)

        lbl_contact = Label(self.dregister, text="Phone Number", font=("Magneto", 15), bg="#D3D3D3")
        lbl_contact.place(x=20, y=210,height=23)

        self.ent_contact = Entry(self.dregister, width=39)
        self.ent_contact.place(x=30, y=238,height=23)

        lbl_email = Label(self.dregister, text="E-Mail", font=("Magneto", 15), bg="#D3D3D3")
        lbl_email.place(x=20, y=270)

        self.ent_email = Entry(self.dregister, width=39)
        self.ent_email.place(x=30, y=298, height=23)

        lbl_license = Label(self.dregister, text="License plate", font=("Magneto", 15), bg="#D3D3D3")
        lbl_license.place(x=20, y=330, height=23)

        self.ent_license = Entry(self.dregister, width=39)
        self.ent_license.place(x=30, y=358, height=23)

        lbl_password = Label(self.dregister, text="Password",font=("Magneto", 15), bg="#D3D3D3")
        lbl_password.place(x=20, y=390, height=23)

        self.ent_password =Entry(self.dregister, width=39)
        self.ent_password.place(x=30, y=418, height=23)


        ###show password eye icon###
        self.image = Image.open('eye.png')
        self.res_img = self.image.resize((20, 20))
        self.new_img = ImageTk.PhotoImage(self.res_img)

        self.image1 = Image.open('eyeclose1.png')
        self.res_img1 = self.image1.resize((20, 20))
        self.new_img1= ImageTk.PhotoImage(self.res_img1)

        temp_value = True

        self.btnn = Button(self.ent_password, width=30, image=self.new_img1)
        self.btnn.place(x=200, y=0)

        self.btnn.bind('<Button-1>', self.ShowPwd)
        self.btnn.bind('<ButtonRelease-1>', self.hidePwd)


        ######Button###########
        ###function to open login page
        def newOpen():
            call(['Python', 'new_log.py'])

        btn_submit = Button(self.dregister, text="Submit", font=("Bradley Hand ITC", 15, "bold"), bg="black", fg="white", width=7, height=1,
                            command= self.dregisteration)
        btn_submit.place(x=70, y=450)

        btn_back= Button(self.dregister, text="Back", font=("Bradley Hand ITC", 15, "bold"), bg="black", fg="white",
                            width=7, height=1)
        btn_back.place(x=190, y=450)



        self.dregister.mainloop()
    def ShowPwd(self, event):
        self.ent_password.config(show="")
        self.btnn.configure(image=self.new_img)

    def hidePwd(self, event):
        self.ent_password.config(show="*")
        self.btnn.configure(image=self.new_img1)

    def validation(self):
        driver_mw = driverreg_middleware.Driver_mid(self.ent_fname.get(), self.ent_lname.get(), self.ent_address.get(), self.ent_email.get(), self.ent_contact.get(), self.ent_license.get(), self.ent_password.get())
        if not all((self.ent_fname.get(), self.ent_lname.get(), self.ent_address.get(), self.ent_contact.get(), self.ent_email.get(), self.ent_license.get(), self.ent_password.get())):
            messagebox.showwarning('Empty Field', 'Please insert all the fields')
            return False
        elif not(driver_mw.is_valid_fname(driver_mw.firstname)):
            pass
        elif not(driver_mw.is_valid_lname(driver_mw.lastname)):
            pass
        elif not(driver_mw.is_valid_address(driver_mw.address)):
            pass
        elif not(driver_mw.is_valid_number(driver_mw.phone_num)):
            pass
        elif not(driver_mw.is_valid_email(driver_mw.email)):
            pass
        elif not(driver_mw.is_valid_licence(driver_mw.license)):
            pass
        elif not(driver_mw.is_valid_password(driver_mw.password)):
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
        self.ent_license.delete(0, END)
        self.ent_password.delete(0, END)

        # def Register():

    def dregisteration(self):
        if not self.validation():
            pass
        else:
            dregister_credentials = driverreg_middleware.Driver_mid(self.ent_fname.get(), self.ent_lname.get(), self.ent_address.get(),
                                                                    self.ent_email.get(),self.ent_contact.get(),
                                                                     self.ent_license.get(), self.ent_password.get(), 'Driver')
            # print(register_credentials.__str__())
            db = Log_db.Database()
            db.dregister_user(dregister_credentials)
            messagebox.showinfo("Successful", "Registration Successful")
            self.dregister.destroy()
            call(["Python", "new_log.py"])


if __name__ =='__main__':
    driver_Reg()