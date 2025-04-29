

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=50)

        # Left Image
        img_top = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\face-recognition.jpg")
        img_top = img_top.resize((650, 565), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=650, height=565)

        # Right Image
        img_top2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\scan2.jpg")
        img_top2 = img_top2.resize((650, 565), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        f_lbl2 = Label(self.root, image=self.photoimg_top2)
        f_lbl2.place(x=650, y=50, width=650, height=565)

        # Button
        b1_1 = Button(f_lbl2, text="Start Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=230, y=485, width=225, height=55)

    def mark_attendence(self, i, r, n, d, absent=False):
        filename = os.path.join(os.getcwd(), "manish.csv")
        with open(filename, "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_List = [line.split(",")[0] for line in myDatalist]

            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtstring = now.strftime("%H:%M:%S")

            if absent:
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Absent")
            else:
                if i not in name_List:
                    f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf, recognized_ids):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", user="root", password="1234567890", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT std_id, roll, std_name, dep FROM student WHERE std_id=%s", (id,))
                student = my_cursor.fetchone()
                conn.close()

                if student:
                    i, r, n, d = map(str, student)

                    if confidence > 79:
                        cv2.putText(img, f"ID: {i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        recognized_ids.add(i)
                        self.mark_attendence(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade, recognized_ids):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf, recognized_ids)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("D:/FACE RECOGNITON ATTENDENCE SYSTEM/classifier.xml")

        recognized_ids = set()
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade, recognized_ids)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter
                break

        video_cap.release()
        cv2.destroyAllWindows()

        # Mark Absent
        conn = mysql.connector.connect(host="localhost", user="root", password="1234567890", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT std_id, roll, std_name, dep FROM student")
        all_students = my_cursor.fetchall()
        conn.close()

        for student in all_students:
            student_id, student_roll, student_name, student_dep = map(str, student)
            if student_id not in recognized_ids:
                self.mark_attendence(student_id, student_roll, student_name, student_dep, absent=True)

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
