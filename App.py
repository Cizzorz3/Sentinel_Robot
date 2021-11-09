from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Database import DBconnect
import tkinter.font as TkFont
# from ListRequest import ListData
from PIL import ImageTk,Image

#connecting the database
dbconnect=DBconnect()


##creating the root
root=Tk()




#size of Root
root.geometry('720x300')

##Favicon
root.iconbitmap('HTI_Logo.ico')
root.title("Corona Virus Diagnosis")
root.config(background="#FFFFFF")

#create A Main Frame
# main_frame=Frame(root)
# main_frame.grid_columnconfigure(2, weight=5)
# main_frame.grid_rowconfigure(2, weight=5)


#Create a canvas
my_canvas=Canvas(root,height=300,width=700,background= "white")
my_canvas.grid(row=0, column=0)


#Adding scroll bar
my_scrollbar=ttk.Scrollbar(root,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.grid(row=0, column=2, sticky='ns')

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.config(scrollregion=my_canvas.bbox("all"))

#create another frame inside the canvas
second_frame=Frame(my_canvas,background="white",width=300,height=200)
#Adding new frame
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

#font
#helv36 = tkFont.Font(family='Helvetica',
     #   size=36, weight='bold')

#style
style=ttk.Style()
style.theme_use("clam")
style.configure("TLabel",background="#FFFFFF",borderwidth=0)
style.configure("TButton",background="#FFFFFF" , borderwidth=0)
style.configure("TRadiobutton",background="#FFFFFF")



## HTi logo 
image = Image.open("HTI_Logo.jpg")
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
my_label=Button(image=img,relief=SUNKEN , borderwidth=0,highlightthickness=0 )
my_label.grid(row=0,column=0,sticky=NW ,pady=2)


#submit button image
submit_btn=PhotoImage(file='1428.png')
img_label=ttk.Label(image=submit_btn)
#img_label.grid(pady=20)




# ##Name
# ttk.Label(root,text="Full name: ",font=('Arial',16)).grid(row=0,column=0,padx=2,pady=2)
# EntryFullName=ttk.Entry(root,width=20,font=('Arial',16))
# EntryFullName.grid(row=0,column=1,pady=5,sticky=W)


##gender
ttk.Label(second_frame,text="Gender: ",font=('Arial',16)).grid(row=0,column=0)
SpanGender=StringVar()
ttk.Radiobutton(second_frame,text="Male",variable=SpanGender,value="Male").grid(row=0,column=1)
ttk.Radiobutton(second_frame,text="Female",variable=SpanGender,value="Female").grid(row=0,column=2)

#Fever
ttk.Label(second_frame,text="Do you have Fever ? " ,font=('Arial',16)).grid(row=5,column=0,pady=20)
Spanfever=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spanfever,value="Yes").grid(row=5,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spanfever,value="No").grid(row=5,column=2)

#Tired 
ttk.Label(second_frame,text="Do you feel Tired ? " ,font=('Arial',16)).grid(row=6,column=0,pady=20)
Spantired=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spantired,value="Yes").grid(row=6,column=1,)
ttk.Radiobutton(second_frame,text="No",variable=Spantired,value="No").grid(row=6,column=2)

#Dry cough
ttk.Label(second_frame,text="Is your cough dry ? " ,font=('Arial',16)).grid(row=8,column=0,pady=20)
Spancough=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spancough,value="Yes").grid(row=8,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spancough,value="No").grid(row=8,column=2)

#Difficulty-in-Breathing
ttk.Label(second_frame,text="Do you have difficulty-in-Breathing ? " ,font=('Arial',16)).grid(row=10,column=0,pady=20)
Spanbreathing=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spanbreathing,value="Yes").grid(row=10,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spanbreathing,value="No").grid(row=10,column=2)

#contact
ttk.Label(second_frame,text="Have you contaced anyone outside your house? " ,font=('Arial',16)).grid(row=12,column=0,pady=20)
Spancontact=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spancontact,value="Yes").grid(row=12,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spancontact,value="No").grid(row=12, column=2)

#Runny-Nose
ttk.Label(second_frame,text="Do you have runny nose? " ,font=('Arial',16)).grid(row=14,column=0,pady=20)
Spanrunnynose=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spanrunnynose,value="Yes").grid(row=14,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spanrunnynose,value="No").grid(row=14, column=2)

#sore throat
ttk.Label(second_frame,text="Do you have sore throat? " ,font=('Arial',16)).grid(row=16,column=0,pady=20)
Spanthroat=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spanthroat,value="Yes").grid(row=16,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spanthroat,value="No").grid(row=16, column=2)

#Nasal-Congestion
ttk.Label(second_frame,text="Do you have Nasal-Congestion? " ,font=('Arial',16)).grid(row=18 , column=0,pady=20)
Spannasal=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spannasal,value="Yes").grid(row=18,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spannasal,value="No").grid(row=18, column=2)

#Diarrhea
ttk.Label(second_frame,text="Do you have Diarrhea? " ,font=('Arial',16)).grid(row=20 , column=0,pady=20)
Spandiarrhea=StringVar()
ttk.Radiobutton(second_frame,text="Yes",variable=Spandiarrhea,value="Yes" ).grid(row=20,column=1)
ttk.Radiobutton(second_frame,text="No",variable=Spandiarrhea,value="No").grid(row=20, column=2)

#buttons
submit_button=ttk.Style()
submit_button=ttk.Button(second_frame,width=10,image=submit_btn)
submit_button.grid(row=21,column=2)

# History_button=ttk.Button(root,text="History")
# History_button.grid(row=10,column=2)


####Submitting the Data to The Database

def save_data():
    # print("Fullname: {}".format(EntryFullName.get()))
    # print("Gender: {}".format(SpanGender.get()))
    # print("Fever : {}" .format(Spanfever.get()))
    # print("Tired : {}".format(Spantired.get()))
    # print("Cough : {}".format(Spancough.get()))
    # print("Diffculty in breating : {}".format(Spanbreathing.get()))
    msg=dbconnect.Add(SpanGender.get(),Spanfever.get(),
    Spantired.get(),Spancough.get(),Spanbreathing.get(),
    Spanrunnynose.get(),Spanthroat.get(),Spannasal.get(),Spandiarrhea.get())
    messagebox.showinfo(title="Add info",message=msg)
    #EntryFullName.delete(0,'end')

    
# def Bulistdata():
#     ListRequest=ListData()

submit_button.config(command=save_data)
# History_button.config(command=Bulistdata)
root.mainloop()


