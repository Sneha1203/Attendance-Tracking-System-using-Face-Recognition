from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class TrainData:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.configure(bg='#c9ada7')
        self.root.title("Face Recognition System")

        # heading
        label = Label(self.root, bg='#f2e9e4', text='TRAIN DATASET', font=('Helvectica', 25))
        label.place(x=0, y=30, width=1920, height=90)

        # train data buttn
        train_data_btn = Button(self.root, text='Click here to Train Data', command=self.train_images, bg='#f2e9e4', activebackground='#c9ada7', bd=0, cursor='hand2', font=('Helvectica', 15))
        train_data_btn.place(x=800, y=450, width=330, height=150)


    def train_images(self):
        data_dir = ('data')
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')    # conversion to grayscale image
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow('Training', image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Results', 'Data Sets Trained Successfully!', parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = TrainData(root)
    root.mainloop()