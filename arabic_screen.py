#importing libraries
from tkinter import *
from PIL import ImageTk,Image
from time import strftime

window = Tk()
window.geometry("720x300")
window.title("Home screen")
window.resizable(FALSE,FALSE)
window.lift()
#window.iconify() #--> to make minimize



    
#color of background screen
window.config(background="#00A7E6")
fr1 = Frame(window,width=110,height=275,bg="#148F77").place(x=0,y=0)
fr2 = Frame(window,width=110,height=275,bg="#148F77").place(x=610,y=0)

#create time frame
time_frame = Frame(window, width=720, height=25, bg="#080A1E")
time_frame.place(x=0,y=275)
#create time and date
def my_time():
    time_string = strftime("%H:%M:%S %p, %A, %x")
    l1.config(text=time_string)
    l1.after(1000,my_time)

l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
l1.place(x=270,y=1)
my_time()

#welcome screen
label = Label(window,text="أهـلا من فضلك قم باختيار نوع الفحـص",font=("Comic Sans",16,"bold"),fg='#080A1E',bg="#00A7E6")
label.place(x=206,y=10)

#Covid-19
#Covid photo design
covid_img = Image.open("covid19.png")
resize_covid_img = covid_img.resize((50, 50))
img_covid = ImageTk.PhotoImage(resize_covid_img)
#Covid button
Covid = Button(window,text=" فيروس كورنا ",font=("Comic Sans",20,"bold"),height=80,width=225,fg="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=SOLID,image=img_covid,compound=LEFT)
Covid.place(x=120,y=60)

#lung cancer
#lung cancer photo design
lung_cancer_img = Image.open("lungcancer.png")
resize_lung_cancer_img = lung_cancer_img.resize((45, 60))
img_lung_cancer = ImageTk.PhotoImage(resize_lung_cancer_img)
#lung cancer button
lung_cancer = Button(window,text=" سرطان الرئة ",font=("Comic Sans",20,"bold"),height=80,width=225,fg="black",bg="#A1FF00",activebackground="#A1FF00",justify=CENTER,relief=GROOVE,image=img_lung_cancer,compound=LEFT)
lung_cancer.place(x=370,y=60)

##Pneumonia
#Pneumonia photo design
pneumonia_img = Image.open("Pneumonia.png")
resize_pneumonia_img = pneumonia_img.resize((45, 55))
img_pneumonia = ImageTk.PhotoImage(resize_pneumonia_img)
#Pneumonia button
Pneumonia = Button(window,text=" التهاب رئوي",font=("Comic Sans",20,"bold"),height=80,width=225,fg="black",bg="#89A725",activebackground="#89A725",justify=CENTER,relief=GROOVE,image=img_pneumonia,compound=LEFT)
Pneumonia.place(x=120,y=170)

##Video call
#Covid photo design
video_img = Image.open("videocall.png")
resize_video_img = video_img.resize((50, 35))
img_video = ImageTk.PhotoImage(resize_video_img)
#video call button
Video_call = Button(window,text=" مكالمة فيديو ",font=("Comic Sans",20,"bold"),height=80,width=225,fg="black",bg="gray",activebackground="gray",justify=CENTER,relief=SOLID,image=img_video,compound=LEFT)
Video_call.place(x=370,y=170)

## HTi logo design
image = Image.open("HTI.png")
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
my_label=Button(image=img,relief=SUNKEN , borderwidth=0,highlightthickness=0, bg="#148F77", activebackground="#148F77")
my_label.place(x=615,y=0)

#Robotic photo design
image_robotic = Image.open("robotic.png")
resize_image_robotic = image_robotic.resize((100, 130))
img_robotic = ImageTk.PhotoImage(resize_image_robotic)
my_label_1=Button(image=img_robotic, relief=SUNKEN, borderwidth=0, highlightthickness=0, bg="#148F77", activebackground="#148F77")
my_label_1.place(x=0,y=145)
# back button 
back_img=Image.open('back.png')
resize_back_img = back_img.resize((30,30))
img_back = ImageTk.PhotoImage(resize_back_img)
back=Button(text=" العودة",height=40,width=80,fg="black",bg="#9FE2BF",activebackground="#6495ED",activeforeground="black",bd=4,font="bold",image=img_back,compound=LEFT).place(x=10,y=60)

############################################
window.mainloop()