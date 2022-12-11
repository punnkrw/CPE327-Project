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
frameLogin = Frame(root,width=550,height=400,bg='White').place(x=55,y=38)
#Title & subtitle 
headerLogin =Label(root, text="Login to continouns", font=("Press Start 2P",18),fg="#000000", background= "White").place(x=110 , y=70 )


#Mail
Mail_text = Label(root,text="Email", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=145 , y=135 )
Mail = Entry(frameLogin,width=20,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=145 , y=170)
Mail_icon = PhotoImage(file = "email-icon.png")
Label(root , image =Mail_icon, bg="#3D404B").place(x=430,y=180)

#Password
Password_text = Label(root,text="Password", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=145 , y=250 )
Password = Entry(frameLogin,width=20,fg='white',border=10,bg='grey', font=("Press Start 2P",11)).place(x=145 , y=280)
Password_icon = PhotoImage(file = " pass-icon.png")
Label(root , image =Password_icon, bg="#3D404B").place(x=429,y=290)

#submit button
signin = Button(frameLogin,text = " Sign in ",bd =10 ,font=("Press Start 2P",10,),bg="Black",fg="White").place(x=230 , y=370, width=160,height=50)


#ForgetPassword
forget_text = Button(frameLogin,text=" Forget Password", font=("Press Start 2P",9),fg="#000000", background= "White",activebackground="#272A37",activeforeground="#ffffff",cursor="hand2",command= lambda:forgot_password(),).place(x=210 , y=335)

#FunctionForget
def forgot_password():
    
    win = Toplevel()
    window_width = 640
    window_height =480
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title("Forget Password")

    #Background
    bg1 =PhotoImage(file = " bg3.png")
    Label(win, image=bg1).place(x=0,y=0)

    #Frame
    frameFoget = Frame(win,width=550,height=400,bg='White').place(x=55,y=38)

    #Emailforget
    email_entry3 = Entry(win, bg="#3D404B", font=("Press Start 2P", 12), highlightthickness=1,
                         bd=5)
    email_entry3.place(x=130, y=120, width=300, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="black", bg='white',
                         font=("Press Start 2P", 12, 'bold'))
    email_label3.place(x=130, y=70)

    #======= New password ==============
    new_password_entry = Entry(win, bg="#3D404B", font=("Press Start 2P", 12), show='•', highlightthickness=1,
                               bd=5)
    new_password_entry.place(x=130, y=250, width=300, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="black", bg='white',
                               font=("Press Start 2P", 11, 'bold'))
    new_password_label.place(x=130, y=200)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='black', font=("Press Start 2P", 12, "bold"),
                         cursor='hand2', relief="flat", bd=10, highlightthickness=0, activebackground="#1D90F5")
    update_pass.place(x=180, y=350, width=300, height=50)
    
    
    #Input Background
    win.configure(background=bg1)
    win.resizable(False, False)






root.mainloop()