from tkinter import *
from time import strftime
from PIL import ImageTk,Image
from tkinter import ttk
window=Tk()
## window properties
window.geometry("720x300")
window.title("Home screen")
#color of background screen
window.config(background="#00A7E6")
## HTi logo design
image = Image.open("HTI.png")
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)
my_label=Button(image=img,relief=SUNKEN , borderwidth=0,highlightthickness=0, bg="#00A7E6", activebackground="#00A7E6")
my_label.grid(row=0,column=0,sticky=NW ,pady=2)
#create time frame
time_frame = Frame(window, width=720, height=25, bg="#080A1E")
time_frame.place(x=0,y=275)
#create time and date
def my_time():
    time_string = strftime("%H:%M:%S %p, %A, %x")
    l1.config(text=time_string)
    l1.after(1000,my_time)

l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E", cursor="clock")
l1.place(x=270,y=1)
my_time()
## labels for start window
l=Label(text="مـن فـضلك قـم باختـيار اللغة",fg="#081448",bg="#00A7E6",width=30,height=2,font=("Font Awesome ",16,"bold")).place(x=155,y=22)
l=Label(text="Please choose language",fg="#081448",bg="#00A7E6",width=30,height=2,font=("Amiri Web Font",16,"bold")).place(x=160,y=59)
## buttons for start window
b_arabic =Button(text="اللغة العربية",width=25,height=2,bg="gold",fg="black",activebackground="green",activeforeground="black",bd=4,font="bold").place(x=205,y=116)
b_english =Button(text="English ",width=25,height=2,bg="gold",fg="black",activebackground="green",activeforeground="black",bd=4,font="bold").place(x=205,y=195)


window.mainloop()
