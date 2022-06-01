from email.mime import image
from tkinter import *

window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
# logo = logo_img.resize((50,50),Image.ANTIALIAS)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


website_label = Label(text='Website')
website_label.grid(row=1,column=0)

email_label = Label(text='Email/Username')
email_label.grid(row=2,column=0)

password_label = Label(text='Password')
password_label.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

button = Entry(width=14)
button = Button(text='generate')
button.grid(row=3,column=2)


window.mainloop()