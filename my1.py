import sqlite3 as sq
import tkinter as tk
from tkinter import ttk

root=tk.Tk()

def create_table():
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS p_item(id integer primary key autoincrement,
                 name text,
                 price integer,
                 category text)""")
    c.close()
    cnn.close()
create_table()



gp3=tk.LabelFrame(root,text="For Record Display",height=200,width=300)
gp3.pack(padx=30,pady=30,fill="x")
t1=ttk.Treeview(gp3,columns=("id","price","category"),show="tree headings")
t1.column("#0",width=150,anchor="center")
t1.heading("id",text="id")
t1.heading("price",text="price")
t1.heading("category",text="category")


p1=t1.insert("",tk.END,text="Home Appliances",open=True)  
p2=t1.insert("",tk.END,text="Kitchen Appliances",open=True)  
p3=t1.insert("",tk.END,text="Lighting",open=True)  
p4=t1.insert("",tk.END,text="Mobile Accessories",open=True)  

cnn=sq.connect("my.db")
c=cnn.cursor()
c.execute("SELECT *FROM p_item where category=?",("Home Appliances",))
rows1=c.fetchall()

for row in rows1:
    t1.insert(p1,tk.END,text=row[1],values=[row[0],row[2],row[3]])

c.execute("SELECT *FROM p_item where category=?",("Kitchen Appliances",))
rows2=c.fetchall()
for row in rows2:
    t1.insert(p2,tk.END,text=row[1],values=[row[0],row[2],row[3]])

c.execute("SELECT *FROM p_item where category=?",("Lighting",))
rows3=c.fetchall()
for row in rows3:
    t1.insert(p3,tk.END,text=row[1],values=[row[0],row[2],row[3]])

c.execute("SELECT *FROM p_item where category=?",("Mobile Accessories",))
rows4=c.fetchall()
for row in rows4:
    t1.insert(p4,tk.END,text=row[1],values=[row[0],row[2],row[3]])

cnn.commit()
t1.pack(padx=20,pady=20,fill="x")
c.close()
cnn.close()
root.geometry("700x700")
root.mainloop()
