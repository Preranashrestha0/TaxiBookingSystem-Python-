from tkinter import Tk, Label, Canvas, BOTH, Entry, Button, END, DISABLED, IntVar
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkinter import messagebox
from subprocess import call

welcome = Tk()
welcome.title("Welcome Page")
welcome.geometry('1540x850')
welcome.configure(bg="#fff")
welcome.resizable(False, False)

#heading
head = Label(welcome, width=70, text="Online Taxi Booking System", font=("Harlow Solid Italic", 30), fg="black", bg="#eee000")
head.place(x=0, y=0)

#for bg picture
lbl_pic= Label(welcome, width=218, height=52)
lbl_pic.place(x=0, y=50)

#for image
canvas = Canvas(lbl_pic, width=1540, height=800)#img place
canvas.pack(fill=BOTH, expand=False)

global image, resized, image2
image = Image.open(r"welcome.png").resize((1540, 800))#img size and image
image2 = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=image2, anchor='nw')
canvas.create_text(700,720,text="We provide more, You pay less",fill="white",font=("Forte", 40, "bold"))#Bauhaus 93
#label
lbl0 = Label(lbl_pic, bg="black", width=218, height=3)
lbl0.place(x=0, y=0)

lbl1 = Label(lbl0, text="Home", bg="black", fg="white", font=("Harlow Solid Italic", 18))
lbl1.place(x=0, y=8)

# lbl2 = Label(lbl_pic, text="We provide more, You pay less", fg="white", bg="black", font=("Aerial", 35))
# lbl2.place(x=500, y=600)

#button
btn1 = Button(lbl0, text="Contact",  bg="black", fg="white", font=("Harlow Solid Italic", 18), command=lambda : nextOpen())
btn1.place(x=100, y=0)

btn2 = Button(lbl0, text="Facilities", bg="black", fg="white", font=("Harlow Solid Italic", 18))
btn2.place(x=250, y=0)

btn3 = Button(lbl0, text="About Us", bg="black", fg="white", font=("Harlow Solid Italic", 18))
btn3.place(x=400, y=0)

btn_login = Button(lbl0, text="Log in", bg="black", fg="white", font=("Harlow Solid Italic", 18),command=lambda: Open())
btn_login.place(x=1190, y=0)

btn_register = Button(lbl0, text="Become a partner", bg="black", fg="white", font=("Harlow Solid Italic", 18), command=lambda: newOpen())
btn_register.place(x=1320, y=0)
def Open():
    call(["Python", "new_log.py"])

def newOpen():
    call(["Python", "driver_reg.py"])

def nextOpen():
    call(["Python", "Contact.py"])


welcome.mainloop()