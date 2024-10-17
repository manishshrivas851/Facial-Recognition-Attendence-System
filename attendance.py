
from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
##################################### TEXT VARIABLE ###############################
        self.var_atten_std_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        

    
    #image 1
        img = Image.open(r"Images\stu1.jpg")
        img = img.resize((660, 180), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=660, height=180)

        #image 2
        img1 = Image.open(r"Images\stt0.jpg")
        img1= img1.resize((670, 180), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb2= Label(self.root, image=self.photoimg1)
        f_lb2.place(x=660, y=0, width=670, height=180)

        #background image
        img3 = Image.open(r"Images\stt1.jpg")
        img3 = img3.resize((1300, 560), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=180, width=1300, height=560)

        title_lbl=Label(bg_img ,text="ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=50)

        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=57,width=1257,height=550)

        
        #left label frame
        
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("Times new roman",15,"bold"),bg="white",fg="black")
        left_frame.place(x=10,y=5,width=615,height=390)

       

        img_left1 = Image.open(r"Images\scan.jpg")
        img_left1 = img_left1.resize((608, 120), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left1)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=2, y=0, width=608, height=120)

          
        left_inside_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Times new roman",15,"bold"),bg="white",fg="black")
        left_inside_frame.place(x=10 ,y=130,width=616,height=230)

        # label entry
        Student_id_label= Label(left_inside_frame, text="StudentID:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_id_label.grid(row=0, column=0, padx=10, pady=2,sticky=W)

        StudentID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_std_id,font=("Times new roman", 12, "bold"))
        StudentID_entry.grid(row=0,column=1,padx=0,sticky=W)


        #Student name
        Student_name_label= Label(left_inside_frame, text="Student Name:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_name_label.grid(row=0, column=2, padx=10, pady=2,sticky=W)

        Student_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("Times new roman", 12, "bold"))
        Student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Roll no
        Student_Roll_label= Label(left_inside_frame, text="Roll:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Student_Roll_label.grid(row=1, column=0, padx=10, pady=2,sticky=W)

        Student_Roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("Times new roman", 12, "bold"))
        Student_Roll_entry.grid(row=1,column=1,padx=0,sticky=W)

        #Time
        time_label= Label(left_inside_frame, text="Time:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        time_label.grid(row=1, column=2, padx=10, pady=2,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("Times new roman", 12, "bold"))
        time_entry.grid(row=1,column=3,padx=0,sticky=W)

        #Date
        date_label= Label(left_inside_frame, text="Date:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        date_label.grid(row=2, column=0, padx=10, pady=2,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("Times new roman", 12, "bold"))
        date_entry.grid(row=2,column=1,padx=0,sticky=W)

        #Department
        dep_label= Label(left_inside_frame, text="Department:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        dep_label.grid(row=2, column=2, padx=10, pady=2,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("Times new roman", 12, "bold"))
        dep_entry.grid(row=2,column=3,padx=0,sticky=W)

        #Attendance status
        Attendance_label= Label(left_inside_frame, text="Attendance Status:", font=("Times new roman", 12, "bold"), bg="white", fg="black")
        Attendance_label.grid(row=3, column=0, padx=10, pady=2,sticky=W)

        self.Attendance_combo = ttk.Combobox(left_inside_frame,font=("Times new roman", 12, "bold"), state="readonly", width=18,textvariable=self.var_atten_attendance)
        self.Attendance_combo["values"] = ("Present","Absent")
        self.Attendance_combo.current(0)
        self.Attendance_combo.grid(row=3, column=1, padx=0, pady=0,sticky=W)

        #buttons frame
        
        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE ,bg="white")
        button_frame.place(x=0,y=150,width=605,height=35)

        import_button=Button(button_frame,text="Import Csv",command=self.importCsv,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        import_button.grid(row=0,column=0,padx=0)

        export_button=Button(button_frame,text="Export Csv",command=self.exportCsv,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        export_button.grid(row=0,column=1,padx=2)
        

        update_button=Button(button_frame,text="Update",command=self.update_data,width=16,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        update_button.grid(row=0,column=2,padx=1)

        reset_button=Button(button_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",11,"bold"),bg="indigo",fg="white")
        reset_button.grid(row=0,column=3,padx=1)

        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Times new roman",15,"bold"),bg="white",fg="black")
        right_frame.place(x=630,y=5,width=615,height=390)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE ,bg="white")
        table_frame.place(x=3,y=0,width=600,height=330)

        #### ++++++++++++++ Scroll bar+++++++++++++++++

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("std_id","roll","std_name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("std_id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("std_name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Deparment")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("std_id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("std_name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)


########################################=====Fetch data======================

    def fetchData(self,rows):
     self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
     for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File",".*")),parent=self.root)
       with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
             mydata.append(i)
        
          self.fetchData(mydata)
                     
# #export csv
    
       
    def exportCsv(self):
      try:
        if len(mydata) < 1:
            messagebox.showerror("No data found to export", parent=self.root)
            return  # Exit if no data

        # Open file dialog
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                           filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if fln:  # Check if filename is selected
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")  # Use comma as the delimiter
                for i in mydata:
                    exp_write.writerow(i)  # Use writerow to write each row
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")

      except Exception as e:
        messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

    def get_cursor(self,event=""):
       cursor_row=self.AttendanceReportTable.focus()
       content=self.AttendanceReportTable.item(cursor_row)
       rows=content['values']
       self.var_atten_std_id.set(rows[0])
       self.var_atten_roll.set(rows[1])
       self.var_atten_name.set(rows[2])
       self.var_atten_dep.set(rows[3])
       self.var_atten_time.set(rows[4])
       self.var_atten_date.set(rows[5])
       self.var_atten_attendance.set(rows[6])
       
#################################   Reset function###########################3

    def reset_data(self):
       self.var_atten_std_id.set("")
       self.var_atten_roll.set("")
       self.var_atten_name.set("")
       self.var_atten_dep.set("")
       self.var_atten_time.set("")
       self.var_atten_date.set("")
       self.var_atten_attendance.set("")
###################Update data#############
# Add this method to your Attendance class
    
    # Add this method to your Attendance class
    def update_data(self):
        if not self.var_atten_std_id.get():
            messagebox.showerror("Error", "Select a record to update", parent=self.root)
        return

        for index, record in enumerate(mydata):
            if record[0] == self.var_atten_std_id.get():  # Assuming std_id is in the first column
                mydata[index] = [
                self.var_atten_std_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            ]
            break
        else:
            messagebox.showerror("Error", "Record not found", parent=self.root)
        return

    # Refresh the table with updated data
        self.fetchData(mydata)

    # Optionally, reset the fields after updating
        self.reset_data()

        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)







if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()

