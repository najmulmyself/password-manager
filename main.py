from email.mime import image
from tkinter import *

window = Tk()
window.title('Password Manager')

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
# logo = logo_img.resize((50,50),Image.ANTIALIAS)
canvas.create_image(100,100,image=logo_img)
canvas.pack()


window.mainloop()