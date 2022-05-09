from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_details import Student
import os
from train_data import TrainData
from face_detector import FaceDetector

class FaceRecognitionSystem:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.configure(bg='#c9ada7')
        self.root.title("Face Recognition System")

        # heading
        label = Label(self.root, bg='#f2e9e4', text='ATTENDANCE TRACKING SYSTEM USING FACE RECOGNITION', font=('Helvectica', 25))
        label.place(x=0, y=50, width=1920, height=90)

        # student details button
        student_btn = Button(self.root, text='Student Details', command=self.student_details, bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        student_btn.place(x=208, y=270, width=220, height=200)

        # face detector button
        face_detector_btn = Button(self.root, text='Face Detector', command=self.detect_face, bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        face_detector_btn.place(x=636, y=270, width=220, height=200)

        # attendance button
        attendance_btn = Button(self.root, text='Attendance', bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        attendance_btn.place(x=1064, y=270, width=220, height=200)

        # help desk button
        help_desk_btn = Button(self.root, text='Help Desk', bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        help_desk_btn.place(x=1492, y=270, width=220, height=200)

        # train data button
        train_data_btn = Button(self.root, text='Train Data', command=self.train_data,bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        train_data_btn.place(x=208, y=600, width=220, height=200)

        # photos button
        photos_btn = Button(self.root, text='Photos', command=self.open_images, bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        photos_btn.place(x=636, y=600, width=220, height=200)

        # developer button
        developer_btn = Button(self.root, text='Developer', bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        developer_btn.place(x=1064, y=600, width=220, height=200)

        # exit button
        exit_btn = Button(self.root, text='Exit', bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        exit_btn.place(x=1492, y=600, width=220, height=200)


    # function
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def open_images(self):
        os.startfile('data')


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = TrainData(self.new_window)


    def detect_face(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceDetector(self.new_window)
        


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()





#c9ada7 -- dusty pink
#f2e9e4 -- cream
