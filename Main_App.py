from tkinter import *
import tkinter as tk
import random
from tkinter.constants import CENTER
from PIL import ImageTk,Image
from tkinter import Entry, Frame, ttk
from time import strftime
from typing import Container
x=random.randint(1,100)


# Creating th main class for the app
class SentinelApp(tk.Tk):
    def __init__ (self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Welcome to Sentinel")
        self.geometry("720x300")

        # Create a container to control the frames  
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # To switch between frames
        self.frames={}
        for F in (WelcomePage , ID , PageTwo):
         page_name=F.__name__
         frame=F(parent=container , controller=self)   
         self.frames[page_name] = frame
         frame.grid(row=0, column=0, sticky="nsew")
         frame.config(background="#00A7E6")
        self.show_frame("WelcomePage")

    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()

class WelcomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        fr1 = Frame(self,width=110,height=275,bg="#148F77").place(x=0,y=0)
        fr2 = Frame(self,width=110,height=275,bg="#148F77").place(x=610,y=0)
        self.controller = controller
        button1=tk.Button(self,text="Go To The ID Page",command=lambda: controller.show_frame("ID"),font=("Comic Sans",25,"bold"),foreground="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,compound=RIGHT,height=1,width=15).place(x=205,y=180)
        label=ttk.Label(self,text=" Welcome To Sentinel ",font=("Comic Sans",34,"bold"),foreground='white',background="#081448")
        label.pack(pady=50)
        time_frame = Frame(self, width=720, height=25, bg="#080A1E")
        time_frame.place(x=0,y=275)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=270,y=1)
        my_time()



class ID (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        fr1 = Frame(self,width=110,height=275,bg="#148F77").place(x=0,y=0)
        fr2 = Frame(self,width=110,height=275,bg="#148F77").place(x=610,y=0)
        self.controller = controller
        self.random=tk.StringVar()
        label=ttk.Label(self,text="Your ID number is :",font=("Comic Sans",32,"bold"),foreground='white',background="#081448").place(x=170,y=50)
        label=ttk.Label(self,text=x ,font=("Comic Sans",32,"bold"),foreground='white',background="#081448").place(x=345,y=120)
        button1=tk.Button(self,text="Next",font=("Comic Sans",30,"bold"),height=1,width=7,command=lambda: controller.show_frame("PageTwo"),foreground="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,compound=RIGHT).place(x=285,y=190)
        time_frame = Frame(self, width=720, height=25, bg="#080A1E")
        time_frame.place(x=0,y=275)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=270,y=1)
        my_time()



class PageTwo (tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        fr1 = Frame(self,width=110,height=275,bg="#148F77").place(x=0,y=0)
        fr2 = Frame(self,width=110,height=275,bg="#148F77").place(x=610,y=0)
        time_frame = Frame(self, width=720, height=25, bg="#080A1E")
        time_frame.place(x=0,y=275)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=270,y=1)
        my_time()

        label = Label(self,text="Hello, What do you want to do?",font=("Comic Sans",16,"bold"),fg='white',bg="#081448")
        label.place(x=206,y=1)

        global img_pneumonia
        pneumonia_img = Image.open("Pneumonia.png")
        resize_pneumonia_img = pneumonia_img.resize((45, 55))
        img_pneumonia = ImageTk.PhotoImage(resize_pneumonia_img)
        #Pneumonia button
        Pneumonia = Button(self,text="Pneumonia ",font=("Comic Sans",20,"bold"),height=65,width=225,fg="black",bg="#89A725",activebackground="#89A725",justify=CENTER,relief=GROOVE,image=img_pneumonia,compound=RIGHT)
        Pneumonia.place(x=118,y=195)

        global img_lung_cancer
        lung_cancer_img = Image.open("lungcancer.png")
        resize_lung_cancer_img = lung_cancer_img.resize((45, 60))
        img_lung_cancer = ImageTk.PhotoImage(resize_lung_cancer_img)
        #lung cancer button
        lung_cancer = Button(self,text="Lung Cancer ",font=("Comic Sans",20,"bold"),height=65,width=225,fg="black",bg="#A1FF00",activebackground="#A1FF00",justify=CENTER,relief=GROOVE,image=img_lung_cancer,compound=RIGHT)
        lung_cancer.place(x=370,y=37)

        #Covid-19
        #Covid photo design
        global img_covid
        covid_img = Image.open("covid19.png")
        resize_covid_img = covid_img.resize((50, 50))
        img_covid = ImageTk.PhotoImage(resize_covid_img)
        #Covid button
        Covid =Button(self,text="Covid-19  ",font=("Comic Sans",20,"bold"),height=65,width=225,fg="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,image=img_covid,compound=RIGHT)
        Covid.place(x=118,y=37)

        global img_video
        video_img = Image.open("videocall.png")
        resize_video_img = video_img.resize((50, 35))
        img_video = ImageTk.PhotoImage(resize_video_img)
        #video call button
        Video_call = Button(self,text="Video Call ",font=("Comic Sans",20,"bold"),height=65,width=225,fg="black",bg="gray",activebackground="gray",justify=CENTER,relief=GROOVE,image=img_video,compound=RIGHT)
        Video_call.place(x=370,y=195)

        #Vital measures
        global img_vital
        vital_img = Image.open("vital.png")
        resize_vital_img = vital_img.resize((50, 50))
        img_vital = ImageTk.PhotoImage(resize_vital_img)
        #video call button
        Vital_measures = Button(self,text="Vital Measures ",font=("Comic Sans",17,"bold"),height=65,width=230,fg="black",bg="#FF00A6",activebackground="#FF00A6",justify=CENTER,relief=GROOVE,image=img_vital,compound=RIGHT)
        Vital_measures.place(x=236,y=117)

        ##back button
        global img_back
        back_img=Image.open('back.png')
        resize_back_img = back_img.resize((30,30))
        img_back = ImageTk.PhotoImage(resize_back_img)
        back_button=tk.Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back,relief=GROOVE ,state="active", command=lambda: controller.show_frame("ID")).place(x=27,y=130)

        #Robotic photo design
        global img_robotic
        image_robotic = Image.open("robotic.png")
        resize_image_robotic = image_robotic.resize((100, 130))
        img_robotic = ImageTk.PhotoImage(resize_image_robotic)
        my_label_1=Button(image=img_robotic, relief=SUNKEN, borderwidth=0, highlightthickness=0,bg="#148F77", activebackground="#148F77")
        my_label_1.place(x=620,y=145)







root=SentinelApp()
root.mainloop()