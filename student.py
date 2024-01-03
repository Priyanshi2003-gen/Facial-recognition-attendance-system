import sys
print(sys.executable)
print(sys.path)


from tkinter import*
from tkinter import ttk, Label 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 


class Student:
    def __init__(self, root):   
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System") 
        
        
        #       ______VARIABLES_________
        self.var_dep = StringVar() 
        self.var_course = StringVar() 
        self.var_year = StringVar() 
        self.var_semester = StringVar() 
        self.var_std_id = IntVar() 
        self.var_std_name = StringVar() 
        self.var_div = StringVar() 
        self.var_roll = StringVar() 
        self.var_gender = StringVar() 
        self.var_dob = StringVar() 
        self.var_email = StringVar() 
        self.var_phone = StringVar() 
        self.var_address = StringVar() 
        self.var_teacher = StringVar() 
        
        
        
        img = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        #(width,height) , antialias converts higher level img to lower level
        img = img.resize((1600 , 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        #we create a label so image can be projected onto the window
        f_lbl = Label(self.root , image = self.photoimg)
        f_lbl.place(x=0, y=0 , width = 1600, height = 130)
        
        img3 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\Light blue bg.png")
        img3 = img3.resize((1600 , 700))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=130 , width = 1600, height = 700)
        
        #Now we add title to the screen
        title_lbl = Label(bg_img , text = "Student Management System" , font=("times new roman",30,"bold"),bg = "white", fg = "dark blue")
        title_lbl.place(x=0 , y = 0, width=1600, height = 45)
        
        
        #Frames on bg image
        main_frame = Frame(bg_img, bd = 2, bg="white")
        main_frame.place(x=10, y=55, width = 1500 , height=650)
        
        
        # (we can give titles to it)
        
        #           ___________LEFT LABLE FRAME___________
        #           ______________________________________
        Left_frame = LabelFrame(main_frame, bd=5, relief=RIDGE , text = "Student Details", font= ("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)
        
        #left label image
        img_left = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        img_left = img_left.resize((700 , 120))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame , image = self.photoimg_left)
        f_lbl.place(x=5, y=0 , width = 700, height = 120) 
        
        #___Current course__
        current_course_frame = LabelFrame(Left_frame, bd=5, relief=RIDGE , text = "Current Course Information", font= ("times new roman",12,"bold"))
        current_course_frame.place(x=5, y=125, width=700, height=120) 
        
        #____Department label____
        dep_label = Label(current_course_frame, text = "Department", font= ("times new roman",12,"bold"))
        dep_label.grid(row=0 , column=0,  padx=2 )
        
        #depatment combo box (drop down)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep , font= ("times new roman",12,"bold"), width=17, state="read only")
        dep_combo["values"] = ("Select Department", "Computer Scince", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2 , pady=10, sticky=W)
        
        
        
        #________Course label_______
        course_label = Label(current_course_frame, text = "Course", font= ("times new roman",12,"bold"))
        course_label.grid(row=0 , column=2,  padx=2 )
        
        #course combo box (drop down)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font= ("times new roman",12,"bold"), width=17, state="read only")
        course_combo["values"] = ("Select Course", "B-Tech", "M-Tech", "MBA", "Masters")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2 , pady=10, sticky=W)
        
        
        #________Year label________
        course_label = Label(current_course_frame, text = "Year", font= ("times new roman",12,"bold"))
        course_label.grid(row=1 , column=0,  padx=2 )
        
        #year combo box (drop down)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font= ("times new roman",12,"bold"), width=17, state="read only")
        course_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2 , pady=10, sticky=W)
        
        
         #________Semester label________
        semester_label = Label(current_course_frame, text = "Semester",  font= ("times new roman",12,"bold"))
        semester_label.grid(row=1 , column=2,  padx=2 )
        
        #Semester combo box (drop down)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,font= ("times new roman",12,"bold"), width=17, state="read only")
        semester_combo["values"] = ("Select Semester", "Sem-1", "Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2 , pady=10, sticky=W)
        
        
        #____Class student information frame____
        class_Student_frame = LabelFrame(Left_frame, bd=5, relief=RIDGE , text = "Class Student Information", font= ("times new roman",12,"bold"))
        class_Student_frame.place(x=5, y=250, width=700, height=300) 
        
        
        #Student ID
        studentID_label = Label(class_Student_frame, text = "StudentID: ", font= ("times new roman",12,"bold"))
        studentID_label.grid(row=0 , column=0,  padx=10 , sticky = W)
        
        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id , width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        studentID_entry.grid(row=0, column=1, padx=10 , sticky = W)
        
        
        #Student Name
        studentName_label = Label(class_Student_frame, text = "Student Name: ", font= ("times new roman",12,"bold"))
        studentName_label.grid(row=0 , column=2, pady=5, padx=10 , sticky = W)
        
        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,  width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        studentName_entry.grid(row=0, column=3,  pady=5,padx=10 , sticky = W)
        
        
        #Class Division
        class_div_label = Label(class_Student_frame, text = "Class Divion", font= ("times new roman",12,"bold"))
        class_div_label.grid(row=1 , column=0, pady=5, padx=10 , sticky = W)
        
        class_div_entry = ttk.Entry(class_Student_frame,  textvariable=self.var_div, width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        class_div_entry.grid(row=1, column=1,  pady=5,padx=10 , sticky = W)
        
        
        
        #Registration Number
        roll_no_label = Label(class_Student_frame, text = "Reg. No.: ", font= ("times new roman",12,"bold"))
        roll_no_label.grid(row=1 , column=2, pady=5, padx=10 , sticky = W)
        
        roll_no_entry = ttk.Entry(class_Student_frame,  textvariable=self.var_roll, width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        roll_no_entry.grid(row=1, column=3,  pady=5,padx=10 , sticky = W)
        
        
        #Gender
        gender_label = Label(class_Student_frame, text = "Gender: ", font= ("times new roman",12,"bold"))
        gender_label.grid(row=2 , column=0, pady=5, padx=10 , sticky = W)
        
        
        #gender - Combo box
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender , font= ("times new roman",12,"bold"), width=17, state="read only")
        gender_combo["values"] = ("Select gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10 , pady=5, sticky=W)
        
        #D O B
        dob_label = Label(class_Student_frame, text = "DOB :", font= ("times new roman",12,"bold"))
        dob_label.grid(row=2 , column=2, pady=5, padx=10 , sticky = W)
        
        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        dob_entry.grid(row=2, column=3,  pady=5,padx=10 , sticky = W)
        
        
        #Email
        email_label = Label(class_Student_frame, text = "Email :", font= ("times new roman",12,"bold"))
        email_label.grid(row=3 , column=0, pady=5, padx=10 , sticky = W)
        
        email_entry = ttk.Entry(class_Student_frame,  textvariable=self.var_email, width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        email_entry.grid(row=3, column=1,  pady=5,padx=10 , sticky = W)
        
        
        #Phone No
        phone_label = Label(class_Student_frame, text = "Phone No. :", font= ("times new roman",12,"bold"))
        phone_label.grid(row=3 , column=2, pady=5, padx=10 , sticky = W)
        
        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20 ,font= ("times new roman",12,"bold"))   #text box will be formed
        phone_entry.grid(row=3, column=3,  pady=5,padx=10 , sticky = W)
       
        
        #Address
        add_label = Label(class_Student_frame, text = "Address :", font= ("times new roman",12,"bold"))
        add_label.grid(row=4 , column=0, pady=5, padx=10 , sticky = W)
        
        add_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        add_entry.grid(row=4, column=1,  pady=5,padx=10 , sticky = W)
        
        #Teacher
        teacher_label = Label(class_Student_frame, text = "Teacher :", font= ("times new roman",12,"bold"))
        teacher_label.grid(row=4 , column=2, pady=5, padx=10 , sticky = W)
        
        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher,width=20,  font= ("times new roman",12,"bold"))   #text box will be formed
        teacher_entry.grid(row=4, column=3,  pady=5,padx=10 , sticky = W)
        
        #radio button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take photo sample" , value= 'YES')
        radiobtn1.grid(row=6, column=0,pady=5,padx=10 , sticky = W)
        
    
        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No sample" , value='NO')
        radiobtn2.grid(row=6, column=1,pady=5,padx=10 , sticky = W)
        
        
        #___Button Frame___
        btn_frame = LabelFrame(class_Student_frame, bd=3, relief=RIDGE , bg = "white")
        btn_frame.place(x=3, y=200, width=680, height=70) 
        
        
        save_btn = Button(btn_frame, text="Save",command=self.add_data, font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3 )
        save_btn.grid(row=0, column=0, padx=1)
        
        update_btn = Button(btn_frame, text="Update",font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3 )
        update_btn.grid(row=0, column=1, padx=1)
        
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3)
        delete_btn.grid(row=0, column=2, padx=1)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3 )
        reset_btn.grid(row=0, column=3, padx=1)
        
        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take a Photo Sample",font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3 )
        take_photo_btn.grid(row=1, column=0, padx=1)
        
        update_photo_btn = Button(btn_frame, text="Update Photo",font= ("times new roman",12,"bold"), bg="blue", fg="white", width=17, bd=3 )
        update_photo_btn.grid(row=1, column=1, padx=1)
        
        
        
        
        

        
        #               ___________RIGHT LABET FRAME__________
        
        Right_frame = LabelFrame(main_frame, bd=5, relief=RIDGE , text = "Student Details", font= ("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        
        #Right label image
        img_right = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        img_right = img_right.resize((700 , 120))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame , image = self.photoimg_right)
        f_lbl.place(x=5, y=0 , width = 700, height = 120) 
        
        
        #__Search System__
        Search_frame = LabelFrame(Right_frame, bd=5, relief=RIDGE , text = "Search System", font= ("times new roman",12,"bold"))
        Search_frame.place(x=5, y=130, width=700, height=70)
        
        
        #search label
        search_label = Label(Search_frame, text = "Search By :", font= ("times new roman",15,"bold"))
        search_label.grid(row=0 , column=0, pady=5, padx=10 , stick = W)
        
        #serach combo box
        search_combo = ttk.Combobox(Search_frame, font= ("times new roman",12,"bold"), width=17, state="read only")
        search_combo["values"] = ("Select", "Reg No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2 , pady=10, sticky=W)
        
        search_entry = ttk.Entry(Search_frame, width=15, font= ("times new roman",12,"bold"))   #text box will be formed
        search_entry.grid(row=0, column=2,  pady=5,padx=10 , stick = W)
        
        search_btn = Button(Search_frame, text="Search",font= ("times new roman",12,"bold"), bg="blue", fg="white", width=12, bd=3 )
        search_btn.grid(row=0, column=3, padx= 1)
        
        showAll_btn = Button(Search_frame, text="Show all",font= ("times new roman",12,"bold"), bg="blue", fg="white", width=12, bd=3 )
        showAll_btn.grid(row=0, column=4, padx=1)
        
        
        
        #_____Table frame______
        table_frame = Frame(Right_frame, bd=5, relief=RIDGE )
        table_frame.place(x=5, y=210, width=700, height=330)
        
        #scroll bar - x and y axis
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame, column = ("dept","course","year","sem", "id", "name" ,"div","dob","email", "phone", "address","teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM , fill=X)
        scroll_y.pack(side=RIGHT , fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        #heading
        self.student_table.heading("dept", text = "Department")
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("sem", text = "Semester")
        self.student_table.heading("id", text = "StudentID")
        self.student_table.heading("name", text = "Name")
        self.student_table.heading("div", text = "Division")
        self.student_table.heading("dob", text = "DOB")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("phone", text = "Phone")
        self.student_table.heading("address", text = "Address")
        self.student_table.heading("teacher", text = "Teacher")
        self.student_table.heading("photo", text = "Photo Sample")
        self.student_table["show"] = "headings"
        #now we set width of columns
        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #       ___________FUNCTION DECLARATION______________
    
    
    #To add the data fields
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error" , "All fields are required",parent=self.root)
        
        #Connection with Mysql workbench. If the fields are empty then showing error  
        else:
                
            try:
                connection=mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer")
                my_cursor= connection.cursor()   
            
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get() , self.var_dob.get() , self.var_email.get() , self.var_phone.get() , self.var_address.get() , self.var_teacher.get(), self.var_radio1.get()))
            
                connection.commit()
                self.fetch_data()
                connection.close()
                
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
                
    
    #_____________FETCH DATA INTO THE RIGHT LABEL TABLE______________      
    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer") 
        my_cursor= connection.cursor()
        my_cursor.execute("select * from student")  #executing a query
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                
            connection.commit()
        connection.close()   
        
        
    #____________________GET ITEMS TO DISPLAY____________
    
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_teacher.set(data[11]),
        self.var_radio1.set(data[12])
        
        
    #Update Function
    
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error" , "All fields are required",parent=self.root)
            
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update the details ?", parent=self.root)
                
                if Update>0:
                    connection=mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer")
                    my_cursor= connection.cursor() 
                    my_cursor.execute("update student set Dept=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo Sample=%s where StudentID = %s", (
                        self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get() , self.var_dob.get() , self.var_email.get() , self.var_phone.get() , self.var_address.get() , self.var_teacher.get(), self.var_radio1.get(),self.var_std_id.get()
                    ))
                    
                else:
                    if not Update:
                        return
                    
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
                
                
    #_____Delete Function_____
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent = self.root)
            
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete this student", parent = self.root)
                
                if delete>0:
                    connection=mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer")
                    my_cursor= connection.cursor() 
                    sql = "delete from student WHERE StudentID=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                
                else:
                    if not delete:
                        return
                    
                    
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
                    
                    
    #____Reset Function_____
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select course"),
        self.var_year.set("Select year"),
        self.var_semester.set("Select semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_gender.set("Select gender"),
        self.var_roll.set(""),
        self.var_div.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
        
        
        
    #________________GENERATE DATA SET AND TAKE PHOTO SAMPLE_______________-
    
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error" , "All fields are required",parent=self.root)
            
        else:
            try:
                
                connection=mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer")
                my_cursor= connection.cursor() 
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                
                my_cursor.execute("""
    UPDATE student
    SET Dept=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, `Photo Sample`=%s
    WHERE StudentID = %s
""", (
    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_name.get(),
    self.var_div.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
    self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get() == (id + 1)  # Assuming StudentID is numeric
))
    
                #my_cursor.execute("UPDATE student SET Dept=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo Sample=%s WHERE StudentID = %s", (self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get() , self.var_dob.get() , self.var_email.get() , self.var_phone.get() , self.var_address.get() , self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()==id+1))
                    
                
                

                connection.commit()
                self.fetch_data()
                self.reset_data()
                connection.close()
                
                
                
                
                
                #________LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV__________
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                #For cropping the image
                def face_cropped(img):
                    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)    #Blue , red , green images will be converted to gray
                    
                    faces = face_classifier.detectMultiScale(gray, 1.3 , 5)   
                    #1.3 = scaling factor
                    #5 = Min neighbour
                    
                    #Now we need a rectangle
                    for (x,y,w,h) in faces:
                        face_cropped = img[y: y+h, x:x+w]
                        return face_cropped
                 
                #To open the camera and capture image   
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()   #for reading images
                    
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    
                        #now we need to store the photos in afolder
                        #This string format is the format in which the name of each images will be stored
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                    
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                    
                        #show
                        cv2.imshow("Cropped face", face)
                        
                   
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed ")
                
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)
                
                
            

 

#We make an object to run the main window       
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop() 
