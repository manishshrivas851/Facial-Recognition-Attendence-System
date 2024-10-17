
from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        ########-----VAriables_______####

      
        self.var_dep = StringVar()         # Department
        self.var_std_id = StringVar()      # StudentID
        self.var_std_name = StringVar()    # Name
        self.var_address = StringVar()     # Address
        self.var_email = StringVar()       # Email
        self.var_gender = StringVar()      # Gender
        self.var_dob = StringVar()         # DOB
        self.var_year = StringVar()        # Year
        self.var_teacher = StringVar()     # Teacher
        self.var_roll = StringVar()        # Roll
        self.var_semester = StringVar()    # Semester
        self.var_mobile = StringVar()      # Mobile
        self.var_course = StringVar()      # Course
        self.var_Photosample = StringVar()
        self.var_div=StringVar() # PhotoSampleStatus


    #image 1
        img = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\stu1.jpg")
        img = img.resize((450, 100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=100)

        #image 2
        img1 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\stu7.jpg")
        img1= img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2= Label(self.root, image=self.photoimg1)
        f_lb2.place(x=400, y=0, width=450, height=100)

        #image 3
        img2 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\stu9.jpg")
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

        title_lbl=Label(bg_img ,text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=50)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=57,width=1257,height=550)

        #left label frame
        
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times new roman",15,"bold"),bg="white",fg="black")
        left_frame.place(x=10,y=5,width=615,height=465)

# 
        img_left1 = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\st2.jpg")
        img_left1 = img_left1.resize((608, 80), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left1)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=2, y=0, width=608, height=80)


        #current course leve frame
        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course",font=("Times new roman",15,"bold"),bg="white",fg="black")
        current_course_frame.place(x=2,y=80,width=608,height=110)

        #department
        dep_level = Label(current_course_frame, text="Department", font=("Times new roman", 14, "bold"), bg="white", fg="black")
        dep_level.grid(row=0, column=0 ,padx=10,pady=5,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("Times new roman", 12, "bold"), state="readonly", width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=5,pady=5,sticky=W)


       #semester: 
       
        sem_level = Label(current_course_frame, text="Sem", font=("Times new roman", 14, "bold"), bg="white", fg="black")
        sem_level.grid(row=0, column=3 ,padx=10,pady=5,sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("Times new roman", 12, "bold"), state="readonly", width=17)
        sem_combo["values"] = ("Select Semester", "Sem 1", "Sem 2", "Sem 3", "Sem 4")
        sem_combo.current(0)
        sem_combo.grid(row=0, column=4, padx=5, pady=5,sticky=W)

        #course
        course_label = Label(current_course_frame, text="Course", font=("Times new roman", 14, "bold"), bg="white", fg="black")
        course_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("Times new roman", 12, "bold"), state="readonly", width=17)
        course_combo["values"] = ("Select Course", "Course 1", "Course 2", "Course 3", "Course 4")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=5, pady=5,sticky=W)

        #year
        year_label = Label(current_course_frame, text="Year", font=("Times new roman", 14, "bold"), bg="white", fg="black")
        year_label.grid(row=1, column=3, padx=10, pady=5,sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("Times new roman", 12, "bold"), state="readonly", width=17)
        year_combo["values"] = ("Select Year", "Year 1", "Year 2", "Year 3", "Year 4")
        year_combo.current(0)
        year_combo.grid(row=1, column=4, padx=5, pady=5,sticky=W)


       #class student information
        class_Student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information ",font=("Times new roman",15,"bold"),bg="white",fg="black")
        class_Student_frame.place(x=2,y=180,width=608,height=275)

        Student_id_label= Label(class_Student_frame, text="StudentID:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_id_label.grid(row=0, column=0, padx=10, pady=2,sticky=W)

        StudentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("Times new roman", 12, "bold"))
        StudentID_entry.grid(row=0,column=1,padx=0,sticky=W)


        #Student name
        Student_name_label= Label(class_Student_frame, text="Student Name:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_name_label.grid(row=0, column=2, padx=10, pady=2,sticky=W)

        Student_name_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("Times new roman", 12, "bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Roll no
        Student_Roll_label= Label(class_Student_frame, text="Roll:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_Roll_label.grid(row=1, column=0, padx=10, pady=2,sticky=W)

        Student_Roll_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("Times new roman", 12, "bold"))
        Student_Roll_entry.grid(row=1,column=1,padx=0,sticky=W)

        #class div
        class_div_label= Label(class_Student_frame, text="Class Division:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        class_div_label.grid(row=1, column=2, padx=10, pady=2,sticky=W)

        # class_div_label_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_Div,font=("Times new roman", 12, "bold"))
        # class_div_label_entry.grid(row=1,column=3,padx=10,sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div,font=("Times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1, column=3, padx=10, pady=10,sticky=W)


        #Gender
        gender_label= Label(class_Student_frame, text="Gender:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        gender_label.grid(row=2, column=0, padx=10, pady=2,sticky=W)

        # gender_label_entry=ttk.Entry(class_Student_frame,textvariable=self.var_Gender,width=20,font=("Times new roman", 12, "bold"))
        # gender_label_entry.grid(row=2,column=1,padx=0,sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,font=("Times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=0, pady=0,sticky=W)


        #DoB
        DoB_label= Label(class_Student_frame, text="DOB:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        DoB_label.grid(row=2, column=2, padx=10, pady=2,sticky=W)

        DoB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("Times new roman", 12, "bold"))
        DoB_entry.grid(row=2,column=3,padx=10,sticky=W)

        #Email
        Email_label= Label(class_Student_frame, text="Email:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Email_label.grid(row=3, column=0, padx=10, pady=2,sticky=W)

        
        Email_label_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("Times new roman", 12, "bold"))
        Email_label_entry.grid(row=3,column=1,padx=0,sticky=W)

        #Mobile no
        mobile_label= Label(class_Student_frame, text="Mobile NO:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        mobile_label.grid(row=3, column=2, padx=10, pady=2,sticky=W)

        mobile_entry=ttk.Entry(class_Student_frame,textvariable=self.var_mobile,width=20,font=("Times new roman", 12, "bold"))
        mobile_entry.grid(row=3,column=3,padx=10,sticky=W)

        #Address
        address_label= Label(class_Student_frame, text="Address:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        address_label.grid(row=4, column=0, padx=10, pady=2,sticky=W)

        address_label_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("Times new roman", 12, "bold"))
        address_label_entry.grid(row=4,column=1,padx=0,sticky=W)

        #Teacher name
        teacher_label= Label(class_Student_frame, text="Teacher Name:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        teacher_label.grid(row=4, column=2, padx=0, pady=2,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("Times new roman", 12, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)


        #Radio buttons
        self.var_Photosample=StringVar()
        radio_btn=ttk.Radiobutton(class_Student_frame,variable=self.var_Photosample,text="Take Photo Sample",value="Yes")
        radio_btn.grid(row=6,column=0)


        #Radio buttons
        # self.var_radio2=StringVar()
        radio_btn2=ttk.Radiobutton(class_Student_frame,variable=self.var_Photosample,text="No Photo Sample",value="No")
        radio_btn2.grid(row=6,column=1)

        #buttons frame
        
        button_frame=Frame(class_Student_frame,bd=2,relief=RIDGE ,bg="white")
        button_frame.place(x=0,y=180,width=605,height=30)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        save_button.grid(row=0,column=0,padx=0)

        update_button=Button(button_frame,text="Update",command=self.update_data,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        update_button.grid(row=0,column=1,padx=2)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        delete_button.grid(row=0,column=2,padx=1)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        reset_button.grid(row=0,column=3,padx=1)

        
        
        button_frame2=Frame(class_Student_frame,bd=2,relief=RIDGE ,bg="white")
        button_frame2.place(x=0,y=210,width=605,height=55)


        
       
        takephoto_sample_button=Button(button_frame2, command=self.generate_dataset,text="Take Photo",width=30,font=("times new roman",13,"bold"),bg="indigo",fg="white")
        takephoto_sample_button.grid(row=0,column=1,padx=0)

        update_photo_button=Button(button_frame2,text="Update Photo",width=30,font=("times new roman",13,"bold"),bg="indigo",fg="white")
        update_photo_button.grid(row=0,column=2,padx=2)







        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times new roman",15,"bold"),bg="white",fg="black")
        right_frame.place(x=630,y=5,width=615,height=465)

        # img_right = Image.open(r"D://FACE RECOGNITON ATTENDENCE SYSTEM//Images//stu9.jpg")
        img_right = Image.open(r"D:\FACE RECOGNITON ATTENDENCE SYSTEM\Images\stu9.jpg")

        img_right = img_right.resize((608, 80), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=2, y=0, width=608, height=80)


        #seacrh frame
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text=" Search System",font=("Times new roman",15,"bold"),bg="white",fg="black")
        search_frame.place(x=2,y=80,width=608,height=70)

        search_label= Label(search_frame, text="Search By:", font=("Times new roman", 12, "bold"), bg="red", fg="black",foreground="white")
        search_label.grid(row=0, column=0, padx=10, pady=2,sticky=W)

        combo_combo = ttk.Combobox(search_frame, font=("Times new roman", 12, "bold"), state="readonly", width=14)
        combo_combo["values"] = ("Select search", "Roll No", "Mobile No")
        combo_combo.current(0)
        combo_combo.grid(row=0, column=1, padx=2, pady=5,sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("Times new roman", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_button=Button(search_frame,text="Serach",width=10,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        search_button.grid(row=0,column=3)

        showall_button=Button(search_frame,text="Show All",width=10,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        showall_button.grid(row=0,column=4,padx=3)


        #table frame
        table_frame=LabelFrame(right_frame,bd=1,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=150,width=608,height=270)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "id", "name", "address", "email", "gender", "dob", "year", "teacher", "roll", "sem","mobile","course","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

            
        

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("mobile", text="Mobile")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"]= "headings"
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # # #########----------------------Function declaration------------------######


    def add_data(self):
        # Check if required fields are filled
        if (self.var_dep.get() == "Select Department" or
            self.var_std_name.get() == "" or
            self.var_std_id.get() == ""): 
            
    
          
            
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567890",
                database="face_recognizer" )
                my_cursor = conn.cursor()
                my_cursor.execute(
                """
                INSERT INTO student (
                    dep,std_id,std_name,address,email,gender,dob,year,teacher,roll,semester,mobile,course,Photosample
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                (
                    self.var_dep.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
            
                    self.var_address.get(),
                
                
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_year.get(),
                    self.var_teacher.get(),
                    self.var_roll.get(),
                    self.var_semester.get(),
                    self.var_mobile.get(),
                    self.var_course.get(),
                    
                    # self.var_div.get(),
                    self.var_Photosample.get()
                )
            )

                

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            
            

            

        # ============================= Fetch Data================================
    def fetch_data(self):
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234567890",
        database="face_recognizer"
        )
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# # +++++++++++++++++=========== Get cursor for  update ++++++++++++-=============

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

    

        self.var_dep.set(data[0])
        self.var_std_id.set(data[1])
        self.var_std_name.set(data[2])
        self.var_address.set(data[3])
        self.var_email.set(data[4])
        self.var_gender.set(data[5])
        self.var_dob.set(data[6])
        self.var_year.set(data[7])
        self.var_teacher.set(data[8])
        self.var_roll.set(data[9])
        self.var_semester.set(data[10])
        self.var_mobile.set(data[11])
        self.var_course.set(data[12])
        self.var_Photosample.set(data[13])


#++++++++++++++================ Update function++++++++++ ============
    


    def update_data(self):
        # Check if required fields are filled
        if (self.var_dep.get() == "Select Department" or
            self.var_std_name.get() == "" or
            self.var_std_id.get() == ""): 
                        
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update ","Do you want to update this student details",parent=self.root)
                if Update:
                
                    conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234567890",
                    database="face_recognizer" )
                    my_cursor = conn.cursor()
                    my_cursor.execute (
                    """
                        UPDATE student SET 
                                    dep=%s, 
                                    std_name=%s, 
                                    address=%s, 
                                    email=%s, 
                                    gender=%s, 
                                    dob=%s, 
                                    year=%s, 
                                    teacher=%s, 
                                    roll=%s, 
                                    semester=%s, 
                                    mobile=%s, 
                                    course=%s, 
                                    Photosample=%s 
                                    WHERE std_id=%s""",

                     (
                                    self.var_dep.get(),
                                    self.var_std_name.get(),
                                    self.var_address.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_year.get(),
                                    self.var_teacher.get(),
                                    self.var_roll.get(),
                                    self.var_semester.get(),
                                    self.var_mobile.get(),
                                    self.var_course.get(),
                                    self.var_Photosample.get(),
                                    self.var_std_id.get()   
                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details  succesfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
           
############################  delete function ####################
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must required",parent=self.root)
        else:
            try:
              delete=messagebox.askyesno("Student Delete Page ","Do you want to delete this student",parent=self.root)    
              if delete >0:
                  conn=mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="1234567890",
                  database="face_recognizer" )
                  my_cursor = conn.cursor()
                  sql="delete from student where std_id=%s"
                  val=(self.var_std_id.get(),)
                  my_cursor.execute(sql,val)
              else:
                  if not delete:
                       return
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Delete ","Successfully deleted students details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
             
                
##############################################  RESET FUNCTION  #######################################


    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mobile.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_Photosample.set("")


################################# Generate data set  or take photo sample  ##########################
    
    def generate_dataset(self):
        if (self.var_dep.get() == "Select Department" or
            self.var_std_name.get() == "" or
            self.var_std_id.get() == ""): 
                        
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                
                
                conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567890",
                database="face_recognizer" )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute (
                    """
                        UPDATE student SET 
                                    dep=%s, 
                                    std_name=%s, 
                                    address=%s, 
                                    email=%s, 
                                    gender=%s, 
                                    dob=%s, 
                                    year=%s, 
                                    teacher=%s, 
                                    roll=%s, 
                                    semester=%s, 
                                    mobile=%s, 
                                    course=%s, 
                                    Photosample=%s 
                                    WHERE std_id=%s""",

                     (
                                    self.var_dep.get(),
                                    self.var_std_name.get(),
                                    self.var_address.get(),
                                    self.var_email.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_year.get(),
                                    self.var_teacher.get(),
                                    self.var_roll.get(),
                                    self.var_semester.get(),
                                    self.var_mobile.get(),
                                    self.var_course.get(),
                                    self.var_Photosample.get(),
                                    self.var_std_id.get()==id+1  
                            ))
                    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
############################ load predifined data on face frontals from opencv ++++++++++++++
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(430,430))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        
                        
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed !!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    

                            

                




if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()



