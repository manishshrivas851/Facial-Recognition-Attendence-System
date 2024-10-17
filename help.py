
from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
from tkinter import messagebox
# import mysql.connector
# import cv2


class desk:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="HELP DESK", font=("time new roman", 25, "bold"), bg="white", fg="dark blue")
        title_lbl.place(x=0,y=0,width=1300,height=50)

        img_top = Image.open(r"Images\HHH.JPG")
        img_top = img_top.resize((1300, 600), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1300, height=600)

        title_lbl = Label(f_lbl, text="Email:manishshrivas851@gnmail.com", font=("time new roman", 15, "bold"), bg="white", fg="blue")
        title_lbl.place(x=450,y=150)


if __name__ == "__main__":
    root = Tk()
    app = desk(root)
    root.mainloop()
