from tkinter import *
from tkinter.font import ITALIC

from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Combobox
from MySql import middleware_LOG, Log_db
from subprocess import call

from assignment import cust_dashboard
from assignment import admin_dash
from assignment import driver_dash

class Login:
    def __init__(self):
        #Frame Design
        self.display = Tk()
        self.display.geometry("450x550") #size of the window
        self.display.title("Login") #title of the window
        self.display.config(bg="#fff")#background color
        self.display.resizable(False,False)#display resizeable

        head=Label(self.display,text="LOGIN",font=("Forte",24, "bold"), fg="black", bg="white")
        head.place(x=200,y=50)#LBl1 will be placed in center, n, ne, e, se, s, sw, w, nw, or center

        lbl_username=Label(self.display,text="Username",font=("",11),fg="black", bg="white")
        lbl_username.place(x=120,y=100)

        self.ent_username=Entry(self.display, font=("", 12, ), borderwidth=0, fg="#6666CD")
        self.ent_username.place(x=120,y=130)
        Frame(self.display, width=250, height=2, bg='black').place(x=120, y=155)

        lbl_usertype = Label(self.display,text="Select User",font=("",11), fg="black", bg="white")
        lbl_usertype.place(x=120,y=180)

        self.cmb_usertype = Combobox(self.display, font=("", 15), foreground="blue", width=18, state='readonly',
                                values=("Select User Type", "Admin", "Taxi Driver", "Customer"))
        self.cmb_usertype.place(x=120, y=200, width=250)
        self.cmb_usertype.current(0)
        # cmb.bind('<FocusIn>', remove_char)

        lbl_password=Label(self.display,text="Password",font=("",11),fg="black",bg="white")
        lbl_password.place(x=120,y=240)

        self.ent_password=Entry(self.display, font=("", 12), width=250, borderwidth=0, fg="#6666CD", show='*')
        self.ent_password.place(x=120,y=260)
        Frame(self.display, width=250, height=2, bg='black').place(x=120, y=288)


        ###show password eye icon###
        image = Image.open('eye.png')
        res_img = image.resize((20, 20))
        new_img = ImageTk.PhotoImage(res_img)

        image1 = Image.open('eyeclose1.png')
        res_img1 = image1.resize((20, 20))
        new_img1= ImageTk.PhotoImage(res_img1)

        temp_value = True
        def ShowPwd(event):
            # if ent_password.cget("show") == "*":
            #     password = ent_password.get()
            self.ent_password.config(show="")
            btnn_eye.configure(image=new_img1)

        def hidePwd(event):
            password = self.ent_password.get()
            self.ent_password.config(show="*")
            btnn_eye.configure(image=new_img)


        btnn_eye = Button(self.ent_password, width=20, image=new_img)
        btnn_eye.place(x=220, y=0)

        btnn_eye.bind('<Button-1>', ShowPwd)
        btnn_eye.bind('<ButtonRelease-1>', hidePwd)

        btn_forgetpw=Button(self.display, text="Forget Password?", borderwidth=0, font=("",9),fg="black", bg="white")
        btn_forgetpw.place(x=270,y=290)

        btn_login=Button(self.display, text="LOGIN", font=("",16),fg="white", bg="#9090EE", width=9, command= lambda: self.validation()) #9090EE= light blue colour
        btn_login.place(x=130,y=350)

        btn_clear=Button(self.display,text="CLEAR",font=("",16),fg="white", bg="#9090EE", width=9)
        btn_clear.place(x=270,y=350)

        lbl_newacc=Label(self.display,text="Create an account?", font=("",10),fg="black",bg="white")
        lbl_newacc.place(x=150,y=400)

        btn3=Button(self.display,text="Register", borderwidth=0,font=("",10),fg="blue", command=lambda: Open())
        btn3.place(x=269,y=398)

        def Open():
            self.display.destroy()
            call(["Python", "registration.py"])

        self.display.mainloop()

    def validation(self):
        if (self.ent_username.get() == "" or self.ent_password == ""):
            messagebox.showerror('Empty', 'Enter your username and password.')
        elif self.cmb_usertype.get() == "Select User Type":
            messagebox.showerror('Error', 'Select the user type.')
        elif self.ent_username.get() == "":
            messagebox.showerror('Empty', 'Enter your username.')
        elif self.ent_password.get() == "":
            messagebox.showerror('Empty', 'Enter your password.')
        else:
            obj = middleware_LOG.LogIn_Middleware(self.ent_username.get(), self.ent_password.get(), self.cmb_usertype.get())
            try:
                data = obj.search_user()
                obj.set_user_id = data[0]
                obj.set_email = data[1]
                obj.set_user_type = data[2]
                if obj.user_type == "Customer":
                    self.display.destroy()
                    cust_dashboard.Cust_dashboard(obj.user_id)

                elif obj.user_type == "Taxi Driver":
                    print('Hello')
                    self.display.destroy()
                    driver_dash.Driver(obj.user_id)

                elif obj.user_type == "Admin":
                    self.display.destroy()
                    admin_dash.Admin(obj.user_id)
            except TypeError:
                messagebox.showerror("ERROR", "Invalid username, password or usertype")




if __name__ == '__main__':
    Login()