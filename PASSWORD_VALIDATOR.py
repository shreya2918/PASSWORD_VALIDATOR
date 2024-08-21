import bcrypt
from tkinter import *

def validate(password):
    hash = b'$2b$12$HHKJUbTWCG0OsV1zNF1wHe4Wmu9K4ehOno62jq23hlzZNxI6DVu4m'
    password = bytes(password, encoding='utf-8')

    if bcrypt.checkpw(password, hash):
        print('Login Successful')
    else:
        print('Invalid PassWord')


root = Tk()

root.geometry("500x500")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="validate",
                command=lambda: validate(password_entry.get()))
button.pack()
root.mainloop()


