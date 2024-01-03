import sys
print(sys.executable)
print(sys.path)


from tkinter import* # Used for crating GUI, develop desktop applications
from tkinter import ttk #This library has even more stylish designs
from PIL import Image, ImageTk  #Use to crop image 
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os


class Face_Recognition_System:
    def __init__(self, root):   #we use root for this vscode window, the home window
        self.root = root
        #we set the geometry of the screen
        self.root.geometry("1530x790+0+0")  #width x ht + x-axis + y-axis
        self.root.title("Face Recognition System")  #We set the title of the window

        #we are adding images to our window so we copy the path of the image and open it
        img = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\header.png")
        #(width,height) , antialias converts higher level img to lower level
        img = img.resize((1600 , 130))
        self.photoimg = ImageTk.PhotoImage(img)
        
        #we create a label so image can be projected onto the window
        f_lbl = Label(self.root , image = self.photoimg)
        f_lbl.place(x=0, y=0 , width = 1600, height = 130)
        
        
        #bg image
        img3 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\Light blue bg.png")
        img3 = img3.resize((1600 , 700))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        #sinve we need the backgroud below the header, the y axis will start from that coordinate where it ended the header which id the height of the header=130
        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=130 , width = 1600, height = 700)
        
        
        #Now we add title to the screen
        title_lbl = Label(bg_img , text = "Face Recognition Attendance System" , font=("times new roman",31,"bold"),bg = "white", fg = "dark blue")
        title_lbl.place(x=0 , y = 0, width=1600, height = 45)
        
        
        #Now we make buttons for different functions
        
        #1st button (Student details)
        img4 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\student.png")
        img4 = img4.resize((220 , 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        #this will act like a button
        b1 = Button(bg_img , image = self.photoimg4 ,command = self.student_details, cursor="hand2")
        b1.place(x = 200, y=100, width=220, height=220)
        #Now we want a text inside the button
        b1_1 = Button(bg_img , text="Student Details" ,command = self.student_details, cursor="hand2", font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 200, y=300, width=220, height=40)  #command is used so that when we click on the button a different page is opened
        
        
        #2nd button (Detect Face)
        img5 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\face detection.png")
        img5 = img5.resize((220 , 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img , image = self.photoimg5 , cursor="hand2",command = self.face_data)
        b1.place(x = 500, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Face Detector" , cursor="hand2",command = self.face_data , font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 500, y=300, width=220, height=40)
        
        
        #3rd button (Attendance)
        img6 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\attendance.png")
        img6 = img6.resize((220 , 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img , image = self.photoimg6 , cursor="hand2")
        b1.place(x = 800, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Attendace" , cursor="hand2", font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 800, y=300, width=220, height=40)
        
        
        #4th button (Help Desk)
        img7 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\help desk.png")
        img7 = img7.resize((220 , 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img , image = self.photoimg7 , cursor="hand2")
        b1.place(x = 1100, y=100, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Help Desk" , cursor="hand2", font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 1100, y=300, width=220, height=40)
        
        
        #5th button (Train face dataset)
        img8 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\train.png")
        img8 = img8.resize((220 , 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img , image = self.photoimg8 , cursor="hand2",command=self.train_data)
        b1.place(x = 200, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Train Dataset" , cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 200, y=600, width=220, height=40)
        
        
        #6th button (Photos )
        img9 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\photos.png")
        img9 = img9.resize((220 , 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img , image = self.photoimg9 , cursor="hand2", command=self.open_img)
        b1.place(x = 500, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Photos" , cursor="hand2", command=self.open_img, font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 500, y=600, width=220, height=40)
        
        
        #7th button (Developer info))
        img10 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\developer.png")
        img10 = img10.resize((220 , 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img , image = self.photoimg10 , cursor="hand2")
        b1.place(x = 800, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Developer" , cursor="hand2", font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 800, y=600, width=220, height=40)
        
        
        #8th button (Exit)
        img11 = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\exit.png")
        img11 = img11.resize((220 , 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img , image = self.photoimg11 , cursor="hand2")
        b1.place(x = 1100, y=400, width=220, height=220)
        
        b1_1 = Button(bg_img , text="Exit" , cursor="hand2", font=("times new roman",15,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 1100, y=600, width=220, height=40)
        
    
    #_______FUNCTION TO OPEN DATA FOLDER TO VIEW PHOTOS_________
    
    def open_img(self):
        os.startfile("data")   #since the code is working on current directory so its okay if you dont mention the whole file name and just the folder that you want to open in that directory
    
    
        
    #_______________FUNCTION BUTTONS_____________
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
        
        
        
   

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()  #A python window will be opened where we have do do all the things