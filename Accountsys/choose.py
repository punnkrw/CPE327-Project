
from tkinter import *
from tkinter.font import Font
from PIL import Image


root = Tk()
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("640x480")
       
       

        #Background Image 
        self.bg =PhotoImage(file = "bg2.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0)
        
        self.logo =PhotoImage(file = "resizepro.png")
        self.bg_logo = Label(self.root, image=self.logo).place(x=210,y=60)
       
          
        #Resize 
        imageresize = Image.open('project.png')
        size = (250,250)
        out = imageresize.resize(size)
        out.save('resizepro.png')  
        
        #Logo
        imageresize = Label(self.bg_logo  ,border=0 ,bg="White",fg="Black").place(x=20,y=50)

        #Button
        Login = Button(self.bg_image,text = "Sign in ",bd =10 ,font=("Press Start 2P",14,),bg="Black",fg="White").place(x=100 , y=350, width=200,height=60)
        Regist = Button(self.bg_image,text = "Sign up",bd =10 ,font=("Press Start 2P",14,),bg="Black",fg="White").place(x=350 , y=350, width=200,height=60)
        
       



obj = Login(root)
root.mainloop()