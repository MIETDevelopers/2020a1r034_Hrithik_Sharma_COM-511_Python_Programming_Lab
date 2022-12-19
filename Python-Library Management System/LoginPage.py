from tkinter import *
from PIL import ImageTk #pip install pillow
from PIL import Image
from tkinter import messagebox
from main import *
class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1290x650+55+15")
        
        #====Background Image=====
        image = Image.open("Authentication.png")
        #print(image.size)
        new_image = image.resize((1290, 700))
        new_image.save('authentication.png')
        self.bg=ImageTk.PhotoImage(file="authentication.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #====Login Frame=====
        Frame_login=Frame(self.root, bg= "white")
        Frame_login.place(x=150, y=150, height=340, width=500)
        title=Label(Frame_login, text="ADMIN LOGIN" ,font=("Impact" ,35, "bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login, text="System Admins Login Area" ,font=("Goudy old style" ,15, "bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        label_username=Label(Frame_login, text="Username" ,font=("Goudy old style" ,15, "bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login, font= ("times new roman" ,15),bg= "lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        label_pwd=Label(Frame_login, text="Password" ,font=("Goudy old style" ,15, "bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pwd=Entry(Frame_login, font= ("times new roman" ,15),bg= "lightgray",show="*")
        self.txt_pwd.place(x=90, y=240, width=350, height=35)

        Login_btn=Button(Frame_login, command=self.login_function, text= "Login",fg="white",bg="#d77337",font=("times new roman",20)).place(x=90, y=280)

    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pwd.get()=="":
            messagebox. showerror("Error", "All fields are required" ,parent=self.root)
        elif self.txt_user.get()!="Diksha" or self.txt_pwd.get()!="12345678":
            messagebox. showerror ("Error", "Invalid Username/Password" ,parent=self.root)
        else:
            messagebox. showinfo("Welcome", f"Welcome {self.txt_user.get()}", parent=self.root)
            self.root.destroy()
            homepage()
root=Tk()
obj=Login(root)
root.mainloop()