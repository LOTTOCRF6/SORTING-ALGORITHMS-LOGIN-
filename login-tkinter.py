from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("600x500")
root.config(bg="lightblue")

label_username = Label(root, text="Username:", bg="lightblue")
label_username.place(x=60, y=20, height=50, width=120)
label_password = Label(root, text="Password:", bg="lightblue")
label_password.place(x=60, y=70, height=50, width=120)

username_entry = Entry(root)
username_entry.place(x=160, y=25, height=30, width=220)
password_entry = Entry(root, show="*")
password_entry.place(x=160, y=80, height=30, width=220)

Usernames = ["Mzwa", "Likho", "Masi"]
passwords = ["1998", "1999", "2000"]


def my_user():
    found = False
    for x in range(len(Usernames)):
        if username_entry.get() == Usernames[x] and password_entry.get() == passwords[x]:
            found = True
    if found == True:
        messagebox.showinfo(title="my_output", message="Access granted")
    else:
        messagebox.showinfo(title="my_output", message="Access denied")


def clear():
    username_entry.delete(0, END)
    password_entry.delete(0, END)


def exit_program():
    return root.destroy()


log_button = Button(root, text="Login", borderwidth="10", command=my_user, font=("Consolas 15 bold"), bg="lightblue")
log_button.place(x=80, y=150)
log_button = Button(root, text="clear", borderwidth="10", command=clear, font=("Consolas 15 bold"), bg="lightblue")
log_button.place(x=240, y=150)
log_button = Button(root, text="exit", borderwidth="10", command=exit, font=("Consolas 15 bold"), bg="lightblue")
log_button.place(x=390, y=150)


root.mainloop()
