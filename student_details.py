from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.configure(bg='#c9ada7')
        self.root.title("Face Recognition System")


        # variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_section = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_mobile_no = StringVar()
        self.var_teacher = StringVar()
        self.take_sample_radio = StringVar()


        # heading
        label = Label(self.root, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 25))
        label.place(x=0, y=30, width=1920, height=90)
        # label.configure(anchor='center')


        # student details frame
        main_frame = Frame(self.root, bd=2, bg='#c9ada7')
        main_frame.place(x=10, y=140, width=1890, height=870)


        # left frame
        left_frame = Frame(main_frame, bg='#f2e9e4')
        left_frame.place(x=20, y=20, width=700, height=870)


        # left frame label
        left_frame_label = Label(left_frame, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 15, 'bold'))
        left_frame_label.place(x=0, y=20, width=700, height=90)
        # left_frame_label.configure(anchor='center')


        # current course details frame
        current_course_frame = LabelFrame(left_frame, bd=2, text='Current Course Information', font=('Helvectica', 15))
        current_course_frame.place(x=20, y=120, width=650, height=150)


        # select department
        dept_label = Label(current_course_frame, text='Department:', font=('Helvectica', 12))
        dept_label.grid(row=0, column=0, padx=5, sticky=W)

        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=('Helvectica', 12), width=20, state="readonly")
        dept_combo['values'] = ('Select Department', 'CSE', 'IT')
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        # select course
        course_label = Label(current_course_frame, text='Course:', font=('Helvectica', 12))
        course_label.grid(row=0, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=('Helvectica', 12), width=20, state="readonly")
        course_combo['values'] = ('Select Course', 'BE', 'FE', 'TE')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        # select year
        year_label = Label(current_course_frame, text='Year:', font=('Helvectica', 12))
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=('Helvectica', 12), width=20, state="readonly")
        year_combo['values'] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        

        # select semester
        semester_label = Label(current_course_frame, text='Semester:', font=('Helvectica', 12))
        semester_label.grid(row=1, column=2, padx=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=('Helvectica', 12), width=20, state="readonly")
        semester_combo['values'] = ('Select Semester', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # class student information frame
        class_student_frame = LabelFrame(left_frame, bd=2, text='Student Information', font=('Helvectica', 15))
        class_student_frame.place(x=20, y=300, width=650, height=540)


        # enter student id
        student_id_label = Label(class_student_frame, text='Student ID:', font=('Helvectica', 12))
        student_id_label.grid(row=0, column=0, padx=5, sticky=W)

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_id, font=('Helvectica', 12), width=17)
        student_id_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        

        # enter student name
        student_name_label = Label(class_student_frame, text='Student Name:', font=('Helvectica', 12))
        student_name_label.grid(row=0, column=2, padx=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_name, font=('Helvectica', 12), width=17)
        student_name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        

        # select class section
        section_label = Label(class_student_frame, text='Section:', font=('Helvectica', 12))
        section_label.grid(row=1, column=0, padx=5, sticky=W)

        section_label_combo = ttk.Combobox(class_student_frame, textvariable=self.var_section, font=('Helvectica', 12), width=17, state="readonly")
        section_label_combo['values'] = ('Select Section', 'CSE-1', 'CSE-2', 'IT-1', 'IT-2')
        section_label_combo.current(0)
        section_label_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        

        # enter roll number
        roll_no_label = Label(class_student_frame, text='Roll Number:', font=('Helvectica', 12))
        roll_no_label.grid(row=1, column=2, padx=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no, font=('Helvectica', 12), width=17)
        roll_no_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # select gender
        gender_label = Label(class_student_frame, text='Gender:', font=('Helvectica', 12))
        gender_label.grid(row=2, column=0, padx=5, sticky=W)

        gender_label_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=('Helvectica', 12), width=17, state="readonly")
        gender_label_combo['values'] = ('Select Gender', 'Male', 'Female', 'Other', 'Prefer not to say')
        gender_label_combo.current(0)
        gender_label_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)


        # enter email address
        email_label = Label(class_student_frame, text='E-mail Address:', font=('Helvectica', 12))
        email_label.grid(row=2, column=2, padx=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=('Helvectica', 12), width=17)
        email_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)


        # enter mobile number
        mobile_no_label = Label(class_student_frame, text='Mobile Number:', font=('Helvectica', 12))
        mobile_no_label.grid(row=3, column=0, padx=5, sticky=W)

        mobile_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_mobile_no, font=('Helvectica', 12), width=17)
        mobile_no_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)
        
        
        # enter teacher name
        teacher_name_label = Label(class_student_frame, text='Teacher Name:', font=('Helvectica', 12))
        teacher_name_label.grid(row=3, column=2, padx=5, sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, font=('Helvectica', 12), width=17)
        teacher_name_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)

        
        # take sample photos radio button
        take_sample_frame = Frame(class_student_frame, bd=0, relief=RIDGE)
        take_sample_frame.place(x=10, y=190, width=620, height=30)

        take_sample_btn = ttk.Radiobutton(take_sample_frame, variable=self.take_sample_radio, text='Take Sample Photo', value='Yes')
        take_sample_btn.grid(row=4, column=0)


        # no sample photos radio button
        no_sample_frame = Frame(class_student_frame, bd=0, relief=RIDGE)
        no_sample_frame.place(x=10, y=220, width=620, height=30)
        
        no_sample_btn = ttk.Radiobutton(no_sample_frame, variable=self.take_sample_radio, text='No Sample Photo', value='No')
        no_sample_btn.grid(row=5, column=0)


        # buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=270, width=620, height=170)

        # save
        save_btn = Button(btn_frame, text='Save', command=self.add_data,font=('Helvectica', 12), bg='#c9ada7', width=32)
        save_btn.grid(row=0, column=0, padx=5, pady=10)

        # update
        update_btn = Button(btn_frame, text='Update', command=self.update_data, font=('Helvectica', 12), bg='#c9ada7', width=32)
        update_btn.grid(row=0, column=1, padx=5, pady=10)


        # delete
        delete_btn = Button(btn_frame, text='Delete', command=self.delete_data, font=('Helvectica', 12), bg='#c9ada7', width=32)
        delete_btn.grid(row=1, column=0, padx=5, pady=10)


        # reset
        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data, font=('Helvectica', 12), bg='#c9ada7', width=32)
        reset_btn.grid(row=1, column=1, padx=5, pady=10)


        # take photo sample button
        take_sample_btn = Button(btn_frame, text='Take Sample Photo', command=self.generate_dataset, font=('Helvectica', 12), bg='#c9ada7', width=32)
        take_sample_btn.grid(row=2, column=0, padx=5, pady=10)


        # update photo sample
        update_sample_btn = Button(btn_frame, text='Update Sample Photo', font=('Helvectica', 12), bg='#c9ada7', width=32)
        update_sample_btn.grid(row=2, column=1, padx=5, pady=10)


        # right frame
        right_frame = Frame(main_frame, bg='#f2e9e4')
        right_frame.place(x=750, y=20, width=1100, height=870)

        # right frame label
        right_frame_label = Label(right_frame, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 15, 'bold'))
        right_frame_label.place(x=0, y=20, width=1100, height=90)
        # right_frame_label = Label(right_frame, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 15))
        # right_frame_label.place(x=750, y=20, width=1100, height=90)
        # right_frame_label.configure(anchor='center')

        # search frame
        search_frame = LabelFrame(right_frame, bd=2, text='Search Student', font=('Helvectica', 15), width=12)
        search_frame.place(x=20, y=120, width=1050, height=100)


        # search box
        search_label = Label(search_frame, text='Search By:', font=('Helvectica', 12), width=15)
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=('Helvectica', 12), width=20, state="readonly")
        search_combo['values'] = ('Select', 'Roll Number', 'Phone Number')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, font=('Helvectica', 12), width=25)
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)


        # search button
        search_btn = Button(search_frame, text='Search', font=('Helvectica', 12), bg='#c9ada7', width=15)
        search_btn.grid(row=0, column=3, padx=10, pady=10)


        # show all button
        show_all_btn = Button(search_frame, text='Show All', font=('Helvectica', 12), bg='#c9ada7', width=15)
        show_all_btn.grid(row=0, column=4, padx=10, pady=10)


        # table frame
        table_frame = LabelFrame(right_frame, bd=2, text='Search Student Information', font=('Helvectica', 15), width=12)
        table_frame.place(x=20, y=240, width=1050, height=600)

        horizontal_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        vertical_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        column_names = ('dept', 'course', 'year', 'sem', 'id', 'name', 'div', 'roll', 'gender', 'phone', 'email', 'teacher', 'photo')
        self.student_table = ttk.Treeview(table_frame, columns=column_names, xscrollcommand=horizontal_scroll.set, yscrollcommand=vertical_scroll.set)

        horizontal_scroll.pack(side=BOTTOM, fill=X)
        vertical_scroll.pack(side=RIGHT, fill=Y)
        horizontal_scroll.config(command=self.student_table.xview)
        vertical_scroll.config(command=self.student_table.yview)

        self.student_table.heading('dept', text='Department')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('div', text='Section')
        self.student_table.heading('roll', text='Roll Number')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('phone', text='Phone')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('teacher', text='Teacher')
        self.student_table.heading('photo', text='Photo Sample Status')

        self.student_table['show'] = 'headings'

        self.student_table.column('dept', width=150)
        self.student_table.column('course', width=150)
        self.student_table.column('year', width=150)
        self.student_table.column('sem', width=150)
        self.student_table.column('id', width=150)
        self.student_table.column('name', width=150)
        self.student_table.column('div', width=150)
        self.student_table.column('roll', width=150)
        self.student_table.column('gender', width=150)
        self.student_table.column('phone', width=150)
        self.student_table.column('email', width=150)
        self.student_table.column('teacher', width=150)
        self.student_table.column('photo', width=150)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()

    
    # function
    def add_data(self):
        if self.var_dept.get() == 'Select Department' or self.var_student_name.get() == '' or self.var_student_id.get() == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                                    (
                                        self.var_dept.get(),
                                        self.var_course.get(),
                                        self.var_year.get(), 
                                        self.var_semester.get(),
                                        self.var_student_id.get(),
                                        self.var_student_name.get(),
                                        self.var_section.get(),
                                        self.var_roll_no.get(),
                                        self.var_gender.get(),
                                        self.var_mobile_no.get(),
                                        self.var_email.get(),
                                        self.var_teacher.get(),
                                        self.take_sample_radio.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Student Details Added Successfully!', parent=self.root)
            except Exception as err:
                messagebox.showerror('Error', f'Due to: {str(err)}', parent=self.root)



    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=''):
        focus_cursor = self.student_table.focus()
        contents = self.student_table.item(focus_cursor)
        data = contents['values']

        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_student_name.set(data[5])
        self.var_section.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_mobile_no.set(data[9])
        self.var_email.set(data[10])
        self.var_teacher.set(data[11])
        self.take_sample_radio.set(data[12])


    def update_data(self):
        if self.var_dept.get() == 'Select Department' or self.var_student_name.get() == '' or self.var_student_id.get() == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                ask_for_update = messagebox.askyesno('Update', 'Do you want to update the details?', parent = self.root)
                if ask_for_update > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute ("update student set dept=%s, course=%s, year=%s, semester=%s, student_name=%s, section=%s, roll_no=%s, gender=%s, mobile_no=%s, email=%s, teacher=%s, photo_sample=%s where student_id=%s", 
                                        (
                                            self.var_dept.get(),
                                            self.var_course.get(),
                                            self.var_year.get(), 
                                            self.var_semester.get(),
                                            self.var_student_name.get(),
                                            self.var_section.get(),
                                            self.var_roll_no.get(),
                                            self.var_gender.get(),
                                            self.var_mobile_no.get(),
                                            self.var_email.get(),
                                            self.var_teacher.get(),
                                            self.take_sample_radio.get(),
                                            self.var_student_id.get()
                                        ))
                else:
                    if not ask_for_update:
                        return
                messagebox.showinfo('Success', 'Student Details Updated Successfully!', parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as err:
                messagebox.showerror('Error', f'Due To: {str(err)}', parent = self.root)
    
    
    
    def delete_data(self):
        if self.var_student_id.get() == '':
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                ask_for_delete = messagebox.askyesno('Delete', 'Do you want to delete the details?', parent = self.root)
                if ask_for_delete > 0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
                    my_cursor = conn.cursor()
                    query = 'delete from student where student_id=%s'
                    value = (self.var_student_id.get(),)
                    my_cursor.execute(query, value), 
                else:
                    if not ask_for_delete:
                        return      
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Student Details Deleted Successfully!', parent = self.root)
            except Exception as err:
                messagebox.showerror('Error', f'Due To: {str(err)}', parent = self.root)
    
    
    
    def reset_data(self):
        self.var_dept.set('Select Department')  
        self.var_course.set('Select Course')  
        self.var_year.set('Select Year')  
        self.var_semester.set('Select Semester')  
        self.var_student_id.set('')  
        self.var_student_name.set('')  
        self.var_section.set('Select Section')  
        self.var_roll_no.set('')  
        self.var_gender.set('Select Gender')  
        self.var_mobile_no.set('')  
        self.var_email.set('')  
        self.var_teacher.set('')  
        self.take_sample_radio.set('')   



    def generate_dataset(self):
        if self.var_dept.get() == 'Select Department' or self.var_student_name.get() == '' or self.var_student_id.get() == '':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='sneha1203', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                result = my_cursor.fetchall()
                id = 0
                for res in result:
                    id += 1
                    my_cursor.execute ("update student set dept=%s, course=%s, year=%s, semester=%s, student_name=%s, section=%s, roll_no=%s, gender=%s, mobile_no=%s, email=%s, teacher=%s, photo_sample=%s where student_id=%s", 
                                        (
                                            self.var_dept.get(),
                                            self.var_course.get(),
                                            self.var_year.get(), 
                                            self.var_semester.get(),
                                            self.var_student_name.get(),
                                            self.var_section.get(),
                                            self.var_roll_no.get(),
                                            self.var_gender.get(),
                                            self.var_mobile_no.get(),
                                            self.var_email.get(),
                                            self.var_teacher.get(),
                                            self.take_sample_radio.get(),
                                            self.var_student_id.get()
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()   

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # neighbour = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped


                camera = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = camera.read()
                    
                    if face_cropped (my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = 'data/user.' + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
                        cv2.imshow('Cropped Face', face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                camera.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Data Sets Generated Successfully!', parent=self.root)

            except Exception as err:
                messagebox.showerror('Error', f'Due To: {str(err)}', parent = self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()