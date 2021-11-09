# from tkinter import *
# from tkinter import ttk
# from Database import DBconnect

# dbconnect=DBconnect()


# class ListData :
#     def __init__(self): 
#         self.root=Tk()
#         self.dbconnect=DBconnect()
#         tv=ttk.Treeview(self.root) 
#         tv.pack() #fill list
#         tv.heading('#0',text='ID')
#         tv.configure(column=('#Name','#Gender','#Fever',"#Tired","#Cough","#Breathing","#RunnyNose","#sorethroat","#Nasalcongestion","#Diarrhea")) 
#         tv.heading('#Name',text="Name")
#         tv.heading('#Gender',text="Gender")
#         tv.heading('#Fever',text="Fever")
#         tv.heading('#Tired',text="Tired")
#         tv.heading('#Cough',text="Cough")
#         tv.heading('#Breathing',text="Breathing")
#         tv.heading('#RunnyNose',text="RunnyNose")
#         tv.heading('#sorethroat',text="sorethroat")
#         tv.heading('#Nasalcongestion',text="Nasalcongestion")
#         tv.heading('#Diarrhea',text="Diarrhea")
#         cursor=self.dbconnect.ListRequest()
#         for row in record :
#             tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
#             tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
#             # tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
#             # tv.set('#{}'.format(row['ID']),'#Fever',row['Fever'])
#             # tv.set('#{}'.format(row['ID']),'#Tired',row['Tired'])
#             # tv.set('#{}'.format(row['ID']),'#Cough',row['Cough'])
#             # tv.set('#{}'.format(row['ID']),'#Breathing',row['Breathing'])
#             # tv.set('#{}'.format(row['ID']),'#RunnyNose',row['RunnyNose'])
#             # tv.set('#{}'.format(row['ID']),'#sorethroat',row['sorethroat'])
#             # tv.set('#{}'.format(row['ID']),'#Nasalcongestion',row['Nasalcongestion'])
#             # tv.set('#{}'.format(row['ID']),'#Diarrhea',row['Diarrhea'])
#         self.root.mainloop()
