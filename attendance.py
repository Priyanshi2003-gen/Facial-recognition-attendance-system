import sys
print(sys.executable)
print(sys.path)


from tkinter import*
from tkinter import ttk, Label 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 


class Attendance:
    def __init__(self, root):   
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System") 
        
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
        title_lbl = Label(bg_img , text = "ATTENDANCE" , font=("times new roman",30,"bold"),bg = "white", fg = "dark blue")
        title_lbl.place(x=0 , y = 0, width=1600, height = 45)
        
        
        #Frames on bg image
        main_frame = Frame(bg_img, bd = 2, bg="white")
        main_frame.place(x=10, y=55, width = 1500 , height=650)
        
        
        # (we can give titles to it)
        
        #           ___________LEFT LABLE FRAME___________
        
        Left_frame = LabelFrame(main_frame, bd=5, relief=RIDGE , text = "Student Details", font= ("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)
        
        #left label image
        img_left = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        img_left = img_left.resize((700 , 120))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame , image = self.photoimg_left)
        f_lbl.place(x=5, y=0 , width = 700, height = 120) 
        
        
        left_inside_frame = Frame(Left_frame, bd=5, relief=RIDGE )
        left_inside_frame.place(x=0, y=135, width=700, height=300)
        
       
        #Labels and Entries
        
         #Attendance ID
        studentID_label = Label(left_inside_frame, text = "Attendance ID: ", font= ("times new roman",12,"bold"))
        studentID_label.grid(row=0 , column=0,  padx=10 , sticky = W)
        
        studentID_entry = ttk.Entry(left_inside_frame , width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        studentID_entry.grid(row=0, column=1, padx=10 , sticky = W)
        
        
        #Student Name
        studentName_label = Label(left_inside_frame, text = "Student Name: ", font= ("times new roman",12,"bold"))
        studentName_label.grid(row=0 , column=2, pady=5, padx=10 , sticky = W)
        
        studentName_entry = ttk.Entry(left_inside_frame,  width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        studentName_entry.grid(row=0, column=3,  pady=5,padx=10 , sticky = W)
        
        
        #Date
        date_label = Label(left_inside_frame, text = "Date: ", font= ("times new roman",12,"bold"))
        date_label.grid(row=1 , column=0, pady=5, padx=10 , sticky = W)
        
        date_entry = ttk.Entry(left_inside_frame,  width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        date_entry.grid(row=1, column=1,  pady=5,padx=10 , sticky = W)
        
        #Time
        time_label = Label(left_inside_frame, text = "Time: ", font= ("times new roman",12,"bold"))
        time_label.grid(row=1 , column=2, pady=5, padx=10 , sticky = W)
        
        time_entry = ttk.Entry(left_inside_frame,  width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        time_entry.grid(row=1, column=3,  pady=5,padx=10 , sticky = W)
        
        
        #Dept
        att_dept_label = Label(left_inside_frame, text = "Department: ", font= ("times new roman",12,"bold"))
        att_dept_label.grid(row=2 , column=0, pady=5, padx=10 , sticky = W)
        
        att_dept_entry = ttk.Entry(left_inside_frame,  width=20, font= ("times new roman",12,"bold"))   #text box will be formed
        att_dept_entry.grid(row=2, column=1,  pady=5,padx=10 , sticky = W)
        
        
         #Gender
        gender_label = Label(left_inside_frame, text = "Gender: ", font= ("times new roman",12,"bold"))
        gender_label.grid(row=2 , column=0, pady=5, padx=10 , sticky = W)
        
        
        
        
        
        
        
         #               ___________RIGHT LABET FRAME__________
        
        Right_frame = LabelFrame(main_frame, bd=5, relief=RIDGE , text = "Attendance Details", font= ("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        
        #Right label image
        img_right = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        img_right = img_right.resize((700 , 120))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame , image = self.photoimg_right)
        f_lbl.place(x=5, y=0 , width = 700, height = 120) 
        
        
#We make an object to run the main window       
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop() 