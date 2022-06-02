from email.mime import image
from re import L
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
# logo = logo_img.resize((50,50),Image.ANTIALIAS)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#function

def get_entry():
    websiteName= website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # print(websiteName)
    # print(password)
    with open("entry.txt","a") as f:
        f.write(f"{websiteName} | {email} | {password} \n")
        website_entry.delete(0,END)
        password_entry.delete(0,END)


#Label

website_label = Label(text='Website')
website_label.grid(row=1,column=0)

email_label = Label(text='Email')
email_label.grid(row=2,column=0)

password_label = Label(text='Password')
password_label.grid(row=3,column=0)


#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'najmulmyself@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Button

generate_password_btn = Button(text='Generate Password')
generate_password_btn.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=get_entry)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()