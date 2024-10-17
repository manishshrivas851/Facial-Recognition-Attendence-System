
from tkinter import *
from tkinter import ttk
import tkinter.messagebox  
from PIL import Image, ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import desk


class Face_Recognition_System:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        #image 1
        img = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\r.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=100)

        #image 2
        img1 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\img2.jpg")
        img1= img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2= Label(self.root, image=self.photoimg1)
        f_lb2.place(x=400, y=0, width=450, height=100)

        #image 3
        img2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\face1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=850, y=0, width=450, height=100)


        #background image
        img3 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\bg2.jpg")
        img3 = img3.resize((1300, 560), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1300, height=560)

        title_lbl=Label(bg_img ,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("time new roman",25,"bold"),bg="white",fg="dark red")
        title_lbl.place(x=0,y=0,width=1300,height=50)


        #student image
        img4 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\student.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.STUDENT,cursor="hand2")
        b1.place(x=130,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.STUDENT,cursor="hand2",font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=130,y=250,width=200,height=35)

        #Detect face button 
        
        img5 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\detect.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detect",cursor="hand2",command=self.face_data,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=400,y=250,width=200,height=35)

        #attendence button 
    
        img6 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\aatendence2.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=670,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=670,y=250,width=200,height=35)

        #help buuton 
    
        img7 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\help.png")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.desk_data,cursor="hand2")
        b1.place(x=950,y=65,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.desk_data,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=950,y=250,width=200,height=35)

        #Training data button
        
        img8 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\traing.png")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=130,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Traing Data",command=self.train_data,cursor="hand2",font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=130,y=490,width=200,height=35)


        #photo button
    
        img9 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\photo.jpg")
        img9 = img9.resize((200, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=400,y=490,width=200,height=35)

        
    
        #Developer
        img10 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\developer.jpg")
        img10 = img10.resize((200, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=670,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=670,y=490,width=200,height=35)

        #Exit button 

        img11 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\exit.jpg")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=950,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",18,"bold"),bg="indigo",fg="white")
        b1_1.place(x=950,y=490,width=200,height=35)


    def open_img(self):
        os.startfile("data")


########################################   Exit Button ##################################


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition ","Are you sure exit this project ",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



#___________________Function button____________________________


    def STUDENT(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


      
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def desk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=desk(self.new_window)







if __name__ == "__main__":  # Corrected indentation for main block
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()



