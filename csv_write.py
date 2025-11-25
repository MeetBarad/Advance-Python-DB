from tkinter import *
from tkinter import ttk
import csv

root=Tk()
root.geometry("500x500")

tree=ttk.Treeview(root,columns=("id","name","city"),show="headings")
tree.heading("id",text="ID")
tree.heading("name",text="Name")
tree.heading("city",text="City")
tree.column(column=0,width=20,anchor="center")
tree.column(column=1,width=100,anchor="center")
tree.column(column=2,width=100,anchor="center")
tree.pack(padx=20,pady=200,fill="both",expand=False)
with open("data.txt","r",newline="") as f:
        row=csv.reader(f)
        #rows=(["1","rohit","ksd"],["2","kunal","ksd"])
        #row1=([id,nm,ct])
        for i in row:
            tree.insert("",END,values=i)
        #row.writerows(tree)

lb1=Label(root,text="Id")
lb1.place(x=20,y=20)
tx1=Entry(root)
tx1.place(x=70,y=20)

lb2=Label(root,text="Name")
lb2.place(x=20,y=60)
tx2=Entry(root)
tx2.place(x=70,y=60)

lb3=Label(root,text="City")
lb3.place(x=20,y=100)
tx3=Entry(root)
tx3.place(x=70,y=100)

def save_record():
    id=tx1.get()
    nm=tx2.get()
    ct=tx3.get()
    tree.insert("",END,values=(id,nm,ct))
    with open("data.txt","a",newline="") as f:
        row=csv.writer(f)
        #rows=(["1","rohit","ksd"],["2","kunal","ksd"])
        row1=([id,nm,ct])
        row.writerow(row1)
    tx1.delete(0,END)
    tx2.delete(0,END)
    tx3.delete(0,END)
    
    

bt1=Button(root,text="Save",command=save_record)
bt1.place(x=45,y=140)



root.mainloop()