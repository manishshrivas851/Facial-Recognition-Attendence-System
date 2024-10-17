from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=50)



    
    
        img_top = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\training.png")
        img_top = img_top.resize((1300, 250), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1300, height=260)


        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",25,"bold"),bg="indigo",fg="white")
        b1_1.place(x=0,y=305,width=1300,height=55)

        img_top2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\photo.jpg")
        img_top2 = img_top2.resize((1300, 250), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl = Label(self.root, image=self.photoimg_top2)
        f_lbl.place(x=0, y=360, width=1300, height=260)

     
    def train_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

            faces=[]
            ids=[]


            for image in path:
                img = Image.open(image).convert('L')  # gray scale
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
                


            ########################## Train classifier ###########################
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result ","Training   datasets completed!!")





if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()



# from tkinter import *
# from tkinter import ttk  
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import cv2
# import os
# import numpy as np

# class Train:
#     def __init__(self, root):  
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")
        
#         # Title Label
#         title_lbl = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 25, "bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=1300, height=50)

#         # Top Image
#         img_top = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\training.png")
#         img_top = img_top.resize((1300, 250), Image.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl = Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=50, width=1300, height=260)

#         # Train Data Button
#         b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("time new roman", 25, "bold"), bg="indigo", fg="white")
#         b1_1.place(x=0, y=305, width=1300, height=55)

#         # Bottom Image
#         img_top2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\photo.jpg")
#         img_top2 = img_top2.resize((1300, 250), Image.LANCZOS)
#         self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
#         f_lbl = Label(self.root, image=self.photoimg_top2)
#         f_lbl.place(x=0, y=360, width=1300, height=260)
     
#     def train_classifier(self):
#         data_dir = "data"
#         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('jpg', 'png', 'jpeg'))]

#         faces = []
#         ids = []

#         if not path:
#             messagebox.showerror("Error", "No images found in the data directory.")
#             return

#         for image in path:
#             img = Image.open(image).convert('L')  # Convert to grayscale
#             imageNp = np.array(img, 'uint8')

#             # Extract ID from filename
#             filename = os.path.split(image)[1]
#             parts = filename.split('.')
            
#             if len(parts) < 2:
#                 print(f"Skipping file {filename}: Does not have an expected format.")
#                 continue
            
#             id_str = parts[1]  # Assuming ID is in the second part of the filename
            
#             try:
#                 id = int(id_str)
#             except ValueError:
#                 print(f"Skipping file {filename}: ID '{id_str}' is not a valid integer.")
#                 continue
            
#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training", imageNp)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
#                 break

#         if len(faces) == 0 or len(ids) == 0:
#             messagebox.showerror("Error", "No faces or IDs found.")
#             cv2.destroyAllWindows()
#             return

#         ids = np.array(ids, dtype=np.int32)  # Convert ids to integers

#         # Train classifier
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces, ids)
#         clf.write("classifier.xml")
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result", "Training datasets completed!!")

# if __name__ == "__main__":
#     root = Tk()
#     app = Train(root)
#     root.mainloop()

# from tkinter import *
# from tkinter import ttk  
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import cv2
# import os
# import numpy as np

# class Train:
#     def __init__(self, root):  
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")
        
#         # Title Label
#         title_lbl = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 25, "bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=1300, height=50)

#         # Top Image
#         img_top = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\training.png")
#         img_top = img_top.resize((1300, 250), Image.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl = Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=50, width=1300, height=260)

#         # Train Data Button
#         b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("time new roman", 25, "bold"), bg="indigo", fg="white")
#         b1_1.place(x=0, y=305, width=1300, height=55)

#         # Bottom Image
#         img_top2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\photo.jpg")
#         img_top2 = img_top2.resize((1300, 250), Image.LANCZOS)
#         self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
#         f_lbl = Label(self.root, image=self.photoimg_top2)
#         f_lbl.place(x=0, y=360, width=1300, height=260)
     
#     def train_classifier(self):
#         data_dir = "data"
#         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('jpg', 'png', 'jpeg'))]

#         faces = []
#         ids = []

#         if not path:
#             messagebox.showerror("Error", "No images found in the data directory.")
#             return

#         for image in path:
#             img = Image.open(image).convert('L')  # Convert to grayscale
#             imageNp = np.array(img, 'uint8')

#             # Extract ID from filename
#             filename = os.path.split(image)[1]
#             parts = filename.split('.')
            
#             if len(parts) < 2:
#                 print(f"Skipping file {filename}: Does not have an expected format.")
#                 continue
            
#             id_str = parts[1]  # Assuming ID is in the second part of the filename
            
#             try:
#                 id = int(id_str)
#             except ValueError:
#                 print(f"Skipping file {filename}: ID '{id_str}' is not a valid integer.")
#                 continue
            
#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training", imageNp)
#             if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
#                 break

#         if len(faces) == 0 or len(ids) == 0:
#             messagebox.showerror("Error", "No faces or IDs found.")
#             cv2.destroyAllWindows()
#             return

#         ids = np.array(ids, dtype=np.int32)  # Convert ids to integers

#         # Train classifier
#         try:
#             clf = cv2.face.LBPHFaceRecognizer_create()
#             clf.train(faces, ids)
#             clf.write("classifier.xml")
#             messagebox.showinfo("Result", "Training datasets completed!!")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {str(e)}")
#         finally:
#             cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     app = Train(root)
#     root.mainloop()
