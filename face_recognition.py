import sys
print(sys.executable)
print(sys.path)


from tkinter import*
from tkinter import ttk, Label 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 
from time import strftime
from datetime import datetime
import os #to import a file or a folder
import numpy as np


class Face_Recognition:
    def __init__(self, root):   
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")
        
        
        title_lbl = Label(self.root , text = "FACE RECOGNITION" , font=("times new roman",30,"bold"),bg = "white", fg = "dark blue")
        title_lbl.place(x=0 , y = 0, width=1600, height = 45)
        
        #Bg image
        img_bg = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\recognition bg.png")
        img_bg = img_bg.resize((1530 , 700))
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        f_lbl = Label(self.root , image = self.photoimg_bg)
        f_lbl.place(x=0, y=55 , width = 1530, height = 700) 
        
        # button
        b1_1 = Button(f_lbl , text="Face Recognition" , cursor="hand2", command=self.face_recog, font=("times new roman",20,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 630, y=550, width=250, height=60)
        
    
    #__________ATTENDANCE_____________
    
    def mark_attendance(self,r, n ,d):
        with open("priyanshi.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList :
                entry = line.split((","))
                name_list.append(entry[0])
            
            #this checks if attendance is already taken of te student, his name doesnt come again in the excel    
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
                
                now=datetime.now()
                d1 = now.strftime("%d/%m/%Y")   #Date
                dtString = now.strftime("%H:%M:%S")   #Time
                f.writelines(f"\n{r},{n},{d},{dtString}, {d1} , Preset")
            
    
      
        
    #________FACE RECOGNITION FUNC_________
    
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            
            coord = []
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
                id,predict = clf.predict(gray_image[y:y+h , x:x+w])
                confidence = int((100*(1-predict/300)))
                
                connection=mysql.connector.connect(host="localhost", username="root", password="W@2915djkq#", database="face_recognizer")
                my_cursor= connection.cursor() 
                
                #For writing name in the image recognition screen
                #Student ID
                my_cursor.execute("select StudentID from student where StudentID=" + str(id) )
                r = my_cursor.fetchone()
                r = "+".join(map(str,r))
                
                
                #Name
                my_cursor.execute("select Name from student where StudentID=" + str(id) )
                n = my_cursor.fetchone()
                n = "+".join(map(str,n))
                
                
                #Dept
                my_cursor.execute("select Dept from student where StudentID=" + str(id) )
                d = my_cursor.fetchone()
                d = "+".join(map(str,d))
                
                
                if confidence > 77:
                    cv2.putText(img, f"ID:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"IName:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Dept:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(r,n,d)
                    
                else:
                    cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                
                coord = [x,y,w,h]
                
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face recognization", img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()       
        
        
        
        
        
#We make an object to run the main window       
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()