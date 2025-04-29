# Facial Recognition Attendance System

This project is a Python-based facial recognition attendance system that detects and records students' attendance using real-time image capture and a database backend.

## 🐍 Python Version
- Python 3.8.5

## 🎯 Features
- Face detection and recognition using OpenCV.
- Stores student details in a MySQL database.
- Automatically starts student IDs from 1 and increments.
- Stores photo samples for training recognition.
- Clean and structured GUI for data entry and attendance tracking.

## 🗃️ Database Schema

**Table: `student`**

| Column Name | Type        | Null | Key | Default | Description              |
|-------------|-------------|------|-----|---------|--------------------------|
| dep         | varchar(45) | YES  |     | NULL    | Department               |
| std_id      | varchar(45) | NO   | PRI | NULL    | Student ID (starts from 1) |
| std_name    | varchar(45) | YES  |     | NULL    | Full Name                |
| address     | varchar(45) | YES  |     | NULL    | Address                  |
| email       | varchar(45) | YES  |     | NULL    | Email Address            |
| gender      | varchar(45) | YES  |     | NULL    | Gender                   |
| dob         | varchar(45) | YES  |     | NULL    | Date of Birth            |
| year        | varchar(45) | YES  |     | NULL    | Academic Year            |
| teacher     | varchar(45) | YES  |     | NULL    | Class Teacher Name       |
| roll        | varchar(45) | YES  |     | NULL    | Roll Number              |
| semester    | varchar(45) | YES  |     | NULL    | Semester                 |
| mobile      | varchar(45) | YES  |     | NULL    | Mobile Number            |
| course      | varchar(45) | YES  |     | NULL    | Enrolled Course          |
| Photosample | varchar(45) | YES  |     | NULL    | Image Sample Reference   |

## 💾 Requirements
- OpenCV
- MySQL Connector
- Tkinter
- PIL (Pillow)

## 🔧 How to Run
1. Clone this repository.
2. Install dependencies.
3. Run `main.py`.
4. Enter student data and capture face samples.
5. Train model and take attendance.

---

Let me know if you’d like to include a screenshot, project goal, or instructions for training the model or integrating with MySQL.
