import sqlite3 as sq
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv;

t1 = "";
def create_table():
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS product_item(id integer primary key autoincrement,
                 name text,
                 price integer)""")
    c.close()
    cnn.close()
create_table()

root=tk.Tk()
gp1=tk.LabelFrame(root,text="For Record Insert",height=180,width=300)
gp1.pack(padx=30,pady=30,fill="x")

lb1 = tk.Label(gp1, text="Name")
lb1.place(x=30, y=30)
txt1 = tk.Entry(gp1)
txt1.place(x=90, y=30)
lb2 = tk.Label(gp1, text="Price")
lb2.place(x=30, y=70)
txt2 = tk.Entry(gp1)
txt2.place(x=90, y=70)

def insert_data():
    a=txt1.get()
    b=txt2.get()
    if(a=="" and b==""):
        messagebox.showinfo("Error","Please The Name And Price")
    else:
        cnn=sq.connect("my.db")
        c=cnn.cursor()
        c.execute("INSERT INTO product_item(name,price)values(?,?)",(a,b))
        cnn.commit()
        c.close()
        cnn.close()
        messagebox.showinfo("Inserted","Sucssesfully Inserted")
        t1.insert("",tk.END,values=(c.lastrowid,a,b))
        txt1.delete(0, tk.END)
        txt2.delete(0, tk.END)
        display()
        


        
bt1=tk.Button(gp1,text="Insert",command=insert_data)
bt1.place(x=50,y=110)

gp2=tk.LabelFrame(root,text="For Record Search",height=130,width=200)
gp2.pack(padx=30,pady=30,fill="x")

lb3=tk.Label(gp2,text="Name")
lb3.place(x=30,y=30)
txt3=tk.Entry(gp2)
txt3.place(x=90,y=30)

gp3=tk.LabelFrame(root,text="For Record Display",height=200,width=300)
gp3.pack(padx=30,pady=0,fill="x")

def display():
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("SELECT *FROM product_item")
    rows=c.fetchall()

    t1=ttk.Treeview(gp3,columns=("id","name","price"),show="headings")
    t1.heading("id",text="id")
    t1.heading("name",text="name")
    t1.heading("price",text="price")
    t1.column(column=0,width=50,anchor="center")
    t1.column(column=1,width=50,anchor="center")
    t1.column(column=2,width=50,anchor="center")

    for row in rows:
        t1.insert("",tk.END,values=row)
    #print(row)
    t1.pack(padx=20,pady=20,fill="x")
    c.close()
    cnn.close()
display()

def search_record():
    for wid in gp3.winfo_children():
        wid.destroy();
    t1=ttk.Treeview(gp3,columns=("id","name","price"),show="headings")
    t1.heading("id",text="id")
    t1.heading("name",text="name")
    t1.heading("price",text="price")
    t1.column(column=0,width=50,anchor="center")
    t1.column(column=1,width=50,anchor="center")
    t1.column(column=2,width=50,anchor="center")
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("SELECT * FROM product_item where name LIKE ? ",(f"%{txt3.get()}%",))
    rows=c.fetchall()
    for row in rows:
        t1.insert("",tk.END,values=row)
    t1.pack(fill="x")
    c.close()
    cnn.close()

bt2=tk.Button(gp2,text="Search",command=search_record)
bt2.place(x=250,y=28)




f1=tk.Frame(root,height=100,width=300)
f1.pack()
def edit_data():
    global t1;
    d = t1.selection();
    a= len(d)
    if(a>0):
        d1 = t1.item(d[0])["values"]
        top=tk.Toplevel(root)
        gp4=tk.LabelFrame(top,text="Update Record",height=180,width=300)
        gp4.pack(padx=10,pady=20,fill="x")

        lb6=tk.Label(gp4,text="name")
        lb6.place(x=30,y=30)
        txt4=tk.Entry(gp4)
        txt4.place(x=70,y=30)
        txt4.insert(0,d1[1])
        lb7=tk.Label(gp4,text="price")
        lb7.place(x=30,y=60)
        txt5=tk.Entry(gp4)
        txt5.place(x=70,y=60)
        txt5.insert(0,d1[2])
        
        def update_record():
            cnn=sq.connect("my.db")
            c=cnn.cursor()
            c.execute("update product_item set name=?,price=? where id=? ",(txt4.get(),txt5.get(),d1[0]))
            cnn.commit()
            if c.rowcount>0:
                messagebox.showinfo("Information","Recorde Update Sucessfully")
            else:
                messagebox.showerror("Information","Recorde Not Updated")
            c.close()
            cnn.close()

            for wid in gp3.winfo_children():
                wid.destroy();
            display()
 
        bt6=tk.Button(gp4,text="Update",command=update_record)
        bt6.place(x=50,y=110)
        top.geometry("500x500")
        top.mainloop()
    else:
        messagebox.showinfo("Info","Please Select Data !")
bt3=tk.Button(f1,text="Edit",command=edit_data)
bt3.place(x=10,y=12)

def delete_data():
    msg = messagebox.askyesno("Question","Do You Want To Delete This Record ?")
    if(msg==True):
        global t1;
        d = t1.selection();
        d1 = t1.item(d[0])["values"]
        cnn=sq.connect("my.db")
        c=cnn.cursor()
        c.execute("delete from product_item where id=?",(d1[0],))
        cnn.commit()
        c.close()
        cnn.close()

    for wid in gp3.winfo_children():
            wid.destroy();
    display()


bt4=tk.Button(f1,text="Delete",command=delete_data)
bt4.place(x=60,y=12)

def export_data():
    cnn = sq.connect("my.db");
    cursor = cnn.cursor();
    cursor.execute("select * from product_item"); 
    t1 = cursor.fetchall();
    f = open("my_data.csv","w",newline="")
    writer = csv.writer(f)
    a=["id","name","price"]
    writer.writerow(a)
    writer.writerows(t1)
    cursor.close()
    cnn.close()


bt5=tk.Button(f1,text="Export",command=export_data)
bt5.place(x=120,y=12)

root.geometry("1000x750+10+10")
root.mainloop()