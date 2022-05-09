from distutils.command.config import config
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class FaceDetector:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.configure(bg='#c9ada7')
        self.root.title("Face Recognition System")

        # heading
        label = Label(self.root, bg='#f2e9e4', text='FACE DETECTION', font=('Helvectica', 25))
        label.place(x=0, y=30, width=1920, height=90)

        # train data buttn
        train_data_btn = Button(self.root, text='Click here to start Face Detector', command=self.face_recognition, bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        train_data_btn.place(x=800, y=450, width=360, height=150)


    def face_recognition(self):
        def draw_box(image, classifier, scale_factor, min_neighbour, color, text, trained_classifier):
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            descriptors = classifier.detectMultiScale(gray_image, scale_factor, min_neighbour)

            coordinates = []

            for (x, y, w, h) in descriptors:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = trained_classifier.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1-predict / 300)))

                conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
                my_cursor = conn.cursor()

                my_cursor.execute('select student_name from student where student_id=' + str(id))
                student_name = my_cursor.fetchone()
                student_name = '+'.join(student_name)

                my_cursor.execute('select roll_no from student where student_id=' + str(id))
                roll_no = my_cursor.fetchone()
                roll_no = '+'.join(str(roll_no))

                my_cursor.execute('select dept from student where student_id=' + str(id))
                dept = my_cursor.fetchone()
                dept = '+'.join(dept)

                if confidence > 77:
                    cv2.putText(image, f'Roll No.: {roll_no}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(image, f'Name: {student_name}', (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(image, f'Department: {dept}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                else:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 1)
                    cv2.putText(image, 'Unknown Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)

                coordinates = [x, y, w, h]
            return coordinates


        def recognizer(image, trained_classifier, face_cascade):
            coordinates = draw_box(image, face_cascade, 1.1, 10, (255, 25, 255), 'Face', trained_classifier)
            return image
                    

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        trained_classifier = cv2.face.LBPHFaceRecognizer_create()
        trained_classifier.read('classifier.xml')

        camera = cv2.VideoCapture(0)

        while True:
            ret, image = camera.read()
            image = recognizer(image, trained_classifier, face_cascade)
            cv2.imshow('Face Detector', image)

            if cv2.waitKey(1) == 13:
                break
        camera.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = FaceDetector(root)
    root.mainloop()