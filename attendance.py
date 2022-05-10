from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv

data = []

class Attendance:
    def __init__ (self, root):
        self.root = root
        self.root.geometry("1920x1090+0+0")
        self.root.configure(bg='#c9ada7')
        self.root.title("Attendance")

        # variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_section = StringVar()
        self.var_roll_no = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_attendance = StringVar()



        # heading
        label = Label(self.root, bg='#f2e9e4', text='ATTENDANCE DETAILS', font=('Helvectica', 25))
        label.place(x=0, y=30, width=1920, height=90)

        # attendance details frame
        main_frame = Frame(self.root, bd=2, bg='#c9ada7')
        main_frame.place(x=10, y=140, width=1890, height=870)

        # left frame
        left_frame = Frame(main_frame, bg='#f2e9e4')
        left_frame.place(x=20, y=20, width=700, height=900)


        # left frame label
        left_frame_label = Label(left_frame, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 15, 'bold'))
        left_frame_label.place(x=0, y=20, width=700, height=90)

        
        # class student information frame       
        class_student_frame = LabelFrame(left_frame, bd=2, text='Student Information', font=('Helvectica', 15))
        class_student_frame.place(x=20, y=120, width=650, height=750)


        # enter student id
        student_id_label = Label(class_student_frame, text='Student ID:', font=('Helvectica', 12))
        student_id_label.grid(row=0, column=0, padx=5, pady=20, sticky=W)

        student_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_id, font=('Helvectica', 12), width=17)
        student_id_entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        

        # enter student name
        student_name_label = Label(class_student_frame, text='Student Name:', font=('Helvectica', 12))
        student_name_label.grid(row=0, column=2, padx=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_student_name, font=('Helvectica', 12), width=17)
        student_name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        

        # select class section
        section_label = Label(class_student_frame, text='Section:', font=('Helvectica', 12))
        section_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        section_label_combo = ttk.Combobox(class_student_frame, textvariable=self.var_section, font=('Helvectica', 12), width=17, state="readonly")
        section_label_combo['values'] = ('Select Section', 'CSE-1', 'CSE-2', 'IT-1', 'IT-2')
        section_label_combo.current(0)
        section_label_combo.grid(row=1, column=1, padx=2, pady=20, sticky=W)
        

        # enter roll number
        roll_no_label = Label(class_student_frame, text='Roll Number:', font=('Helvectica', 12))
        roll_no_label.grid(row=1, column=2, padx=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no, font=('Helvectica', 12), width=17)
        roll_no_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # enter semester
        semester_label = Label(class_student_frame, text='Semester:', font=('Helvectica', 12))
        semester_label.grid(row=2, column=0, padx=5, pady=20, sticky=W)

        semester_combo = ttk.Combobox(class_student_frame, textvariable=self.var_semester, font=('Helvectica', 12), width=20, state="readonly")
        semester_combo['values'] = ('Select Semester', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII')
        semester_combo.current(0)
        semester_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)


        # select department
        dept_label = Label(class_student_frame, text='Department:', font=('Helvectica', 12))
        dept_label.grid(row=2, column=2, padx=5, sticky=W)

        dept_combo = ttk.Combobox(class_student_frame, textvariable=self.var_dept, font=('Helvectica', 12), width=20, state="readonly")
        dept_combo['values'] = ('Select Department', 'CSE', 'IT')
        dept_combo.current(0)
        dept_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)


        # select year
        year_label = Label(class_student_frame, text='Year:', font=('Helvectica', 12))
        year_label.grid(row=3, column=0, padx=5, pady=20, sticky=W)

        year_combo = ttk.Combobox(class_student_frame, textvariable=self.var_year, font=('Helvectica', 12), width=20, state="readonly")
        year_combo['values'] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
        year_combo.current(0)
        year_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)


        # select course
        course_label = Label(class_student_frame, text='Course:', font=('Helvectica', 12))
        course_label.grid(row=3, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(class_student_frame, textvariable=self.var_course, font=('Helvectica', 12), width=20, state="readonly")
        course_combo['values'] = ('Select Course', 'BE', 'FE', 'TE')
        course_combo.current(0)
        course_combo.grid(row=3, column=3, padx=2, pady=10, sticky=W)


        # enter time
        time_label = Label(class_student_frame, text='Time:', font=('Helvectica', 12))
        time_label.grid(row=4, column=0, padx=5, pady=20, sticky=W)

        time_entry = ttk.Entry(class_student_frame, textvariable=self.var_time, font=('Helvectica', 12), width=17)
        time_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)


        # enter date
        date_label = Label(class_student_frame, text='Date:', font=('Helvectica', 12))
        date_label.grid(row=4, column=2, padx=5, sticky=W)

        date_entry = ttk.Entry(class_student_frame, textvariable=self.var_date, font=('Helvectica', 12), width=17)
        date_entry.grid(row=4, column=3, padx=2, pady=10, sticky=W)


        # attendance status
        attendance_label = Label(class_student_frame, text='Attendance:', font=('Helvectica', 12))
        attendance_label.grid(row=5, column=0, padx=5, pady=20, sticky=W)

        attendance_combo = ttk.Combobox(class_student_frame, textvariable=self.var_attendance, font=('Helvectica', 12), width=20, state="readonly")
        attendance_combo['values'] = ('Status', 'Present', 'Absent')
        attendance_combo.current(0)
        attendance_combo.grid(row=5, column=1, padx=2, pady=10, sticky=W)
       

        # buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=10, y=400, width=620, height=210)

        # import csv
        import_btn = Button(btn_frame, text='IMPORT CSV', command=self.import_csv,font=('Helvectica', 12), bg='#c9ada7', width=32)
        import_btn.place(x=160, y=10)

        # export csv
        export_btn = Button(btn_frame, text='EXPORT CSV', command=self.export_csv, font=('Helvectica', 12), bg='#c9ada7', width=32)
        export_btn.place(x=160, y=60)


        # update button
        update_btn = Button(btn_frame, text='UPDATE', command=self.update_data, font=('Helvectica', 12), bg='#c9ada7', width=32)
        update_btn.place(x=160, y=110)


        # reset button
        reset_btn = Button(btn_frame, text='RESET', command=self.reset_data, font=('Helvectica', 12), bg='#c9ada7', width=32)
        reset_btn.place(x=160, y=160)


        # right frame
        right_frame = Frame(main_frame, bg='#f2e9e4')
        right_frame.place(x=750, y=20, width=1100, height=870)

        # right frame label
        right_frame_label = Label(right_frame, bg='#f2e9e4', text='STUDENT DETAILS', font=('Helvectica', 15, 'bold'))
        right_frame_label.place(x=0, y=20, width=1100, height=90)
   

        # table frame
        table_frame = LabelFrame(right_frame, bd=2, text='Search Student Information', font=('Helvectica', 15), width=12)
        table_frame.place(x=20, y=120, width=1050, height=700)

        horizontal_scroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        vertical_scroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        column_names = ('date', 'id', 'name', 'roll', 'div', 'dept', 'sem', 'year', 'course', 'time', 'attendance')
        self.attendance_table = ttk.Treeview(table_frame, columns=column_names, xscrollcommand=horizontal_scroll.set, yscrollcommand=vertical_scroll.set)

        horizontal_scroll.pack(side=BOTTOM, fill=X)
        vertical_scroll.pack(side=RIGHT, fill=Y)
        horizontal_scroll.config(command=self.attendance_table.xview)
        vertical_scroll.config(command=self.attendance_table.yview)

        self.attendance_table.heading('date', text='Date')
        self.attendance_table.heading('id', text='Student ID')
        self.attendance_table.heading('name', text='Name')
        self.attendance_table.heading('roll', text='Roll Number')
        self.attendance_table.heading('div', text='Section')
        self.attendance_table.heading('dept', text='Department')
        self.attendance_table.heading('sem', text='Semester')
        self.attendance_table.heading('year', text='Year')
        self.attendance_table.heading('course', text='Course')
        self.attendance_table.heading('time', text='Time')
        self.attendance_table.heading('attendance', text='Attendance')

        self.attendance_table['show'] = 'headings'

        self.attendance_table.column('date', width=150)
        self.attendance_table.column('id', width=150)
        self.attendance_table.column('name', width=150)
        self.attendance_table.column('roll', width=150)
        self.attendance_table.column('div', width=150)
        self.attendance_table.column('dept', width=150)
        self.attendance_table.column('sem', width=150)
        self.attendance_table.column('year', width=150)
        self.attendance_table.column('course', width=150)
        self.attendance_table.column('time', width=150)
        self.attendance_table.column('attendance', width=150)

        self.attendance_table.pack(fill=BOTH, expand=1)

        self.attendance_table.bind('<ButtonRelease>', self.get_cursor)


    def fetch_data(self, rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for row in rows:
            self.attendance_table.insert("", END, values=row)


    def import_csv(self):
        global data
        data.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File', '*.csv'), ('All File', '*.*')), parent=self.root)
        with open(file_name) as file:
            read_csv = csv.reader(file, delimiter=',')
            for content in read_csv:
                data.append(content)
            self.fetch_data(data)


    def export_csv(self):
        try:
            if len(data) < 1:
                messagebox.showerror('Error', 'No Data Found to Export', parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File', '*.csv'), ('All File', '*.*')), parent=self.root)
            with open(file_name, mode='w', newline='') as file:
                write_in_file = csv.writer(file, delimiter=',')
                for content in data:
                    write_in_file.writerow(content)
                messagebox.showinfo('Result', 'Data Exported Successfully!')
        except Exception as err:
            messagebox.showerror('Error', f'Due To : {str(err)}', parent=self.root)


    def get_cursor(self):
        focus_cursor = self.attendance_table.focus()
        contents = self.attendance_table.item(focus_cursor)
        data = contents['values']

        self.var_date.set(data[0])
        self.var_student_id.set(data[1])
        self.var_student_name.set(data[2])
        self.var_roll_no.set(data[3])
        self.var_section.set(data[4])
        self.var_dept.set(data[5])
        self.var_semester.set(data[6])
        self.var_year.set(data[7])
        self.var_course.set(data[8])
        self.var_time.set(data[9])
        self.var_attendance(data[10])



    def reset_data(self):
        self.var_date.set('')
        self.var_student_id.set('')
        self.var_student_name.set('')
        self.var_roll_no.set('')
        self.var_section.set('')
        self.var_dept.set('')
        self.var_semester.set('')
        self.var_year.set('')
        self.var_course.set('')
        self.var_time.set('')
        self.var_attendance('')

    def update_data():
        pass
    def generate_dataset():
        pass



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()