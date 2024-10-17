
from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="DEVELOPER", font=("time new roman", 25, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0,y=0,width=1300,height=50)

        img_top = Image.open(r"Images\d2.png")
        img_top = img_top.resize((1300, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1300, height=600)

        #### Frame
        main_frame=Frame(f_lbl,bd=2,relief=RIDGE ,bg="white")
        main_frame.place(x=750,y=0,width=500,height=500)

        img1_top = Image.open(r"Images\ddd.jpeg")
        img1_top = img1_top.resize((319, 300), Image.LANCZOS)
        self.photoimg1_top = ImageTk.PhotoImage(img1_top)

        f_lbl = Label(main_frame, image=self.photoimg1_top)
        f_lbl.place(x=250, y=0, width=250, height=250)

        #######################  Developer info  ########################3

        title_lbl=Label(main_frame,text="Hello my name is manishs shrivas",font=("time new roman",9,"bold"),bg="white")
        title_lbl.place(x=0,y=0)

        title_lbl=Label(main_frame,text=" I am passinate about data ",font=("time new roman",10,"bold"),bg="white")
        title_lbl.place(x=0,y=40)
        title_lb2=Label(main_frame,text=" science and machine learning",font=("time new roman",10,"bold"),bg="white")
        title_lb2.place(x=0,y=63)


        img2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\stu9.jpg")
        img2 = img2.resize((510, 300), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=240, width=510, height=300)












if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()



