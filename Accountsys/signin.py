from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.font import Font
from PIL import Image


root = Tk()

class Login:
      
        root.title("Login System")
        root.geometry("640x480")

    #Background Image 
bg =PhotoImage(file = "bg2.png")
Label(root, image=bg).place(x=0,y=0)



#Frame
frame = Frame(root,width=550,height=400,bg='White').place(x=55,y=38)
#Title & subtitle 
header =Label(root, text="Create new account", font=("Press Start 2P",20),fg="#000000", background= "White").place(x=100 , y=60 )
#User
user_text = Label(root,text="Username", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=120 , y=120 )
user_entry = Entry(frame,width=20,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=120 , y=150)
user_icon = PhotoImage(file = 'name_icon.png')
Label(root , image =user_icon, bg="#3D404B").place(x=405,y=160)

#Mail
Mail_text = Label(root,text="Email", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=120 , y=210 )
Mail_entry = Entry(frame,width=20,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=120 , y=240)
Mail_icon = PhotoImage(file = 'email-icon.png')
Label(root , image =Mail_icon, bg="#3D404B").place(x=405,y=250)

#Password
Password_text = Label(root,text="Password", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=120 , y=300 )
Password_entry = Entry(frame,width=10,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=120 , y=320)
Password_icon = PhotoImage(file = 'pass-icon.png')
Label(root , image =Password_icon, bg="#3D404B").place(x=255,y=330)

#confirmPassword
confirm_text = Label(root,text="Confirm Password", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=335 , y=300 )
confirm_entry = Entry(frame,width=10,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=340 , y=320)
confirm_icon = PhotoImage(file = 'pass-icon.png')
Label(root , image =confirm_icon, bg="#3D404B").place(x=475,y=330)

#submit button
submit_buttonImage = PhotoImage(file="button.png")
submit_button =Button(root,image=submit_buttonImage,border=10 ,bg='Black', activebackground="#272A37" ,cursor="hand2").place(x=210,y=380,width=200,height=50)







root.mainloop()