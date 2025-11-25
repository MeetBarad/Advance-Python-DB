
import sqlite3 as sq
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

gp3=tk.LabelFrame(root,text="For Record Display",height=200,width=300)
gp3.pack(padx=30,pady=30,fill="x")
t1=ttk.Treeview(gp3,columns=("id","name","price"),show="tree headings")

t1.heading("id",text="id")
t1.heading("name",text="name")
t1.heading("price",text="price")
t1.column("#0",width=150,anchor="center")

p1=t1.insert("",tk.END,text="Home Appliances",open=True)  

t1.insert(p1,"end",text="",values=(1,"ad","hshs"))
t1.insert(p1,"end",text="",values=(2,"abc","bori"))

t1.pack();


root.geometry("700x700")
root.mainloop()
