from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.font import Font
from PIL import Image

#window size 
Accountsys = Tk()
Accountsys.rowconfigure(0,weight=1)
Accountsys.columnconfigure(0,weight=1)

width= 640
height =480
x= (Accountsys.winfo_screenwidth()//2) -(width//2)
y =(Accountsys.winfo_screenheight()//4) -(height//4)
Accountsys.geometry('{}x{}+{}+{}'.format(width,height,x,y))

Accountsys.title('Account')

#Navigating Through window
sign_in =Frame(Accountsys)
MainMenu =Frame(Accountsys)
sign_up =Frame(Accountsys)

for frame in (sign_in,MainMenu,sign_up):
    frame.grid(row =0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(MainMenu)

#================================================
#=========== Main menu PAGE =======================

 #Background Image 
MainMenu.bg =PhotoImage(file = "bg2.png")
MainMenu.bg_image = Label(MainMenu, image=MainMenu.bg).place(x=0,y=0)
        
MainMenu.logo =PhotoImage(file = "resizepro.png")
MainMenu.bg_logo = Label(MainMenu, image=MainMenu.logo).place(x=210,y=60)
       
          
#Resize 
imageresize = Image.open( 'project.png')
size = (250,250)
out = imageresize.resize(size)
out.save('resizepro.png')  
        
#Logo
imageresize = Label(MainMenu.bg_logo  ,border=0 ,bg="White",fg="Black").place(x=20,y=50)

 #Button
Login = Button(
MainMenu.bg_image,
text = "Sign in ",
bd =10 ,
font=("Press Start 2P",14,),
bg="Black",
fg="White",
command = lambda: show_frame(sign_in) 
)

Login.place(x=100 , y=350, width=200,height=60)

Regist = Button(
MainMenu.bg_image,
text = "Sign up",
bd =10 ,
font=("Press Start 2P",14,),
bg="Black",
fg="White",
command = lambda: show_frame(sign_up)
)

Regist.place(x=350 , y=350, width=200,height=60)


#================================================
#=========== SIGN UP PAGE =======================

#sign up Text variable
userName = StringVar()
email = StringVar()
password = StringVar()
confirmPassword = StringVar()

#Background Image 
sign_up.bg =PhotoImage(file = "bg2.png")
Label(sign_up, image=sign_up.bg).place(x=0,y=0)

#Frame
sign_up.frame = Frame(sign_up,width=550,height=400,background='White').place(x=55,y=38)
#Title & subtitle 
header =Label(sign_up, text="Create new account", font=("Press Start 2P",20),fg="#000000", background= "White").place(x=100 , y=60 )

#User
user_text = Label(sign_up,text="Username", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=120 , y=120 )
user_entry = Entry(
    frame,
    width=20,
    fg='white',
    border=10,
    bg='grey', 
    font=("Press Start 2P",11),
    textvariable=userName
    ).place(x=120 , y=150)



sign_up.user_icon = PhotoImage(file = 'name_icon.png')
Label(sign_up , image =sign_up.user_icon, bg="#3D404B").place(x=405,y=160)


#Mail
Mail_text = Label(sign_up,text="Email", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=120 , y=210 )
Mail_entry = Entry(
    frame,
    width=20,
    fg='white',
    border=10,
    bg='grey', 
    font=("Press Start 2P",11),
    textvariable= email
    ).place(x=120 , y=240)


sign_up.Mail_icon = PhotoImage(file = 'email-icon.png')
Label(sign_up , image =sign_up.Mail_icon, bg="#3D404B").place(x=405,y=250)

#Password
Password_text = Label(sign_up,text="Password", font=("Press Start 2P",10),fg="Black", background= "White").place(x=120 , y=300 )
Password_entry = Entry(
    frame,
    width=10,
    fg='white',
    border=10,
    bg='grey', 
    font=("Press Start 2P",11),
    textvariable=password
    ).place(x=120 , y=320)

sign_up.Password_icon = PhotoImage(file = 'pass-icon.png')
Label(sign_up , image =sign_up.Password_icon, bg="#3D404B").place(x=255,y=330)

#confirmPassword
confirm_text = Label(sign_up,text="Confirm Password", font=("Press Start 2P",10),fg="Black", background= "White").place(x=335 , y=300 )
confirm_entry = Entry(
    frame,
    width=10,
    fg='white',
    border=10,
    bg='grey', 
    font=("Press Start 2P",11),
    textvariable=confirmPassword

    ).place(x=340 , y=320)

confirm_icon = PhotoImage(file = 'pass-icon.png')
Label(sign_up , image =confirm_icon, bg="#3D404B").place(x=475,y=330)

#submit button

submit_buttonImage = PhotoImage(
    file="button.png")
submit_button =Button(
        sign_up, 
        text=" Sign Up ",
        font=("Press Start 2P",15) ,
        borderwidth=10,
        fg="White",
        bg="Black",
        highlightthickness=0,
        cursor="hand2",
        command=lambda: signup()

        ).place(x=210,y=380,width=200,height=50)

#Clear sign up fields
def clear():
   userName.set("")
   email.set("")
   password.set("")
   confirmPassword.set("")

#Database Connection for sign up 

def signup():
    
    if user_entry.get( ) == ""  or Mail_entry.get( ) == "" or Password_entry.get( ) == "" or confirm_entry.\
            get( ) == "" :  
    
       messagebox.showerror("Error","All Fields are Required")

    elif Password_entry.get() != confirm_entry.get():
         messagebox.showerror("Error","Password And Confirm Password Didn't Match")

    else:
        
        try:

            connection = sqlite3.connect("Accountsys.db")
            cur = connection.cursor()
          

            cur.execute("INSERT INTO AccountDB(UserName,EMAIL,Password)VALUES(?,?,?)",
                (user_entry.get(),Mail_entry.get(),Password_entry.get()))
            
            
            connection.commit()
          
            connection.close()
            clear()
            
    
            messagebox.showinfo('Sucess','New Account Created Successful')

        except Exception as es:
            messagebox.showerror("Error",'Something went wrong try again')
         

  
#================================================
#=========== SIGN IN PAGE =======================

email = StringVar()
password = StringVar()

#Background Image 
sign_in.bg =PhotoImage(file = "bg2.png")
Label(sign_in, image=sign_in.bg).place(x=0,y=0)

#Frame
sign_in.frame = Frame(sign_in,width=550,height=400,bg='White').place(x=55,y=38)
#Title & subtitle 
headerLogin =Label(sign_in, text="Login to continouns", font=("Press Start 2P",18),fg="#000000", background= "White").place(x=110 , y=70 )

#Mail
Mail_text = Label(sign_in,text="Email", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=145 , y=135 )
Mail_Login_entry = Entry(
        sign_in,
        width=20,
        fg='white',
        border=10,
        bg='grey', 
        font=("Press Start 2P",11),
        textvariable=email

        ).place(x=145 , y=170)

Mail_icon = PhotoImage(file = 'email-icon.png')
Label(sign_in , image =Mail_icon, bg="#3D404B").place(x=430,y=180)

#Password
Password_text = Label(sign_in,text="Password", font=("Press Start 2P",10),fg="#000000", background= "White").place(x=145 , y=250 )
Password_Login_entry = Entry(
        sign_in,
        width=20,
        fg='white',
        border=10,
        bg='grey', 
        font=("Press Start 2P",11),
        textvariable= password,
        
        ).place(x=145 , y=280)

Password_icon = PhotoImage(file = 'pass-icon.png')
Label(sign_in, image =Password_icon, bg="#3D404B").place(x=429,y=290)

#submit button
signin = Button(
        sign_in,
        text = " Sign in "
        ,bd =10 ,
        font=("Press Start 2P",10,),
        bg="Black",fg="White",
        command= lambda: login()
        
        ).place(x=230 , y=370, width=160,height=50)

#Clear Login

def clear_login():
    email.set("")
    password.set("")

#Database connection

def login():
    conn =sqlite3.connect("Accountsys.db")
    cursor =conn.cursor()
    find_user = 'SELECT * FROM AccountDB WHERE EMAIL = ? and Password = ? '
    cursor.execute(find_user,[(Password_Login_entry.get()),(Mail_Login_entry.get())])

    result = cursor.fetchall()

    if result:
        clear_login()
        messagebox.showinfo("Success",'Loggin in Successfully')
    else:
        messagebox.showerror("Falied","Sorry can't login, please try again")
    

 






#ForgetPassword
forget_text = Button(sign_in,text=" Forget Password", font=("Press Start 2P",9),fg="#000000", background= "White",activebackground="#272A37",activeforeground="#ffffff",cursor="hand2",command= lambda:forgot_password(),).place(x=210 , y=335)

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
    bg1 =PhotoImage(file = "bg3.png")
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









Accountsys.resizable(False,False)
Accountsys.mainloop()