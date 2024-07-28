from  tkinter import *

contact = Tk()
contact.title("Contact")
contact.geometry('400x200')
contact.configure(bg="#fff")
contact.resizable(False, False)

lbl1 = Label(contact, text="Email us at:",  font=("", 15, "bold"), width=10 , bg="white", fg="#8470FF")
lbl1.place(x=130, y=0)

lbl2 = Label(contact, text="preranas767@gmail.com", font=("", 12, "bold"), width=30 , bg="white", fg="blue")
lbl2.place(x=50, y=40)

lbl3 =Label(contact, text="Call us at:", font=("", 15, "bold"), width=10, bg="white", fg="#8470FF")
lbl3.place(x=120, y=80)

lbl4 = Label(contact, text="+977 9803190091", font=("", 12, "bold"), width=20 , bg="white", fg="blue")
lbl4.place(x=80, y=120)
contact.mainloop()