import sys
print(sys.executable)
print(sys.path)


from tkinter import*
from tkinter import ttk, Label 
from PIL import Image, ImageTk  
from tkinter import messagebox
import mysql.connector
import cv2 
import os #to import a file or a folder
import numpy as np


class Train:
    def __init__(self, root):   
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System") 
        
        
        #_________TItLE_________
        title_lbl = Label(self.root , text = "Train Dataset" , font=("times new roman",30,"bold"),bg = "white", fg = "dark blue")
        title_lbl.place(x=0 , y = 0, width=1600, height = 45)
        
        
        
        #_________IMAGES_________
        
        #Top img
        img_top = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\train_top.png")
        img_top = img_top.resize((1530 , 325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root , image = self.photoimg_top)
        f_lbl.place(x=0, y=55 , width = 1530, height = 325) 
        
        
        #middle button
        b1_1 = Button(self.root , text="TRAIN DATA" , command=self.train_classifier , cursor="hand2",  font=("times new roman",20,"bold"),bg = "grey", fg = "white")
        b1_1.place(x = 0, y=380, width=1530, height=60)
        
        
        #Bottom img
        img_bottom = Image.open(r"C:\Users\pnsha\Facial regognition attendance sysytem\images\train_bottom.png")
        img_bottom = img_bottom.resize((1530 , 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root , image = self.photoimg_bottom)
        f_lbl.place(x=0, y=440 , width = 1530, height = 325) 
        
    
    #uses LBPH algorithm to train the images    
    def train_classifier(self):
        data_dir = ("data") 
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]   #data of data_dir is taken in "path" varible

        faces = []
        ids = []
        
        #images will be converted into gray scale that are present in path    
        for image in path:
            img = Image.open(image).convert('L') #To convert in gray scale img
            #____NUMPY____ used to make grid system in image
            imageNp = np.array(img, 'uint8') #unit8 = datatype
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        
        ids = np.array(ids)


	        
        #_______TRAIN CLASSIFIER_______
        
        classifier_folder = "classifier"
        os.makedirs(classifier_folder, exist_ok = True)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed !!")
        
        
    
        

        
        
        
            
        
        
        
        
        
        
        
        
        
        
#We make an object to run the main window       
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 
