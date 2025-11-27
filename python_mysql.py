from tkinter import *
import mysql.connector as sq
from tkinter import ttk
from tkinter import messagebox
root=Tk();
def inite():
    cnn=sq.connect(host="localhost",user="root",password="",database="test")
    cursor=cnn.cursor()
    cursor.execute("create table IF NOT EXISTS data(id int primary key auto_increment,name varchar(20),price int)")
    cnn.commit()
    cursor.close()
    cnn.close()
inite()

def insert_recorde():
    nm=txt1.get()
    pr=txt2.get()
    if(nm=="" or pr==""):
        messagebox.showwarning("Warning","Please Fill The Data!")
    else:
        cnn=sq.connect(host="localhost",user="root",password="",database="test")
        cursor=cnn.cursor()
        cursor.exeocute("insert into data(name,price)values(%s,%s)",(nm,pr))
        messagebox.showinfo("Sucess","Record Inserted!")
        t1.insert("",END,values=(cursor.lastrowid,nm,pr))
        cnn.commit()
        cursor.close()
        cnn.close()
        txt1.delete(0,END)
        txt2.delete(0,END)
gp1=LabelFrame(root,text="Insert Record",height="200",width="400")
gp1.pack(padx=10,pady=10,fill="both",expand=False)

lb1=Label(gp1,text="Name")
lb1.place(x=20,y=30)
txt1=Entry(gp1)
txt1.place(x=70,y=30)

lb2=Label(gp1,text="Price")
lb2.place(x=20,y=70)
txt2=Entry(gp1)
txt2.place(x=70,y=70)

bt1=Button(gp1,text="Insert",command=insert_recorde)
bt1.place(x=40,y=110)

gp2=LabelFrame(root,text="Search Record",height="100",width="200")
gp2.pack(padx=10,pady=10,fill="both",expand=False)

def search_record():
    for i in t1.get_children():
        t1.delete(i)
    cnn=sq.connect(host="localhost",user="root",password="",database="test")
    cursor=cnn.cursor()
    cursor.execute("SELECT * FROM data where name LIKE %s ",(f"%{txt3.get()}%",))
    rows=cursor.fetchall()
    for row in rows:
        t1.insert("",END,values=row)
    cursor.close()
    cnn.close()
lb3=Label(gp2,text="Name")
lb3.place(x=20,y=10)
txt3=Entry(gp2)
txt3.place(x=70,y=10)

bt2=Button(gp2,text="Search",command=search_record)
bt2.place(x=40,y=40)

gp3=LabelFrame(root,text="Record Display",height="200",width="300")
gp3.pack(padx=10,pady=10,fill="both",expand=False)

gp4=LabelFrame(root,text="Operations",height="100",width="150")
gp4.pack(padx=10,pady=10,fill="both",expand=False)

def delete_record():
    get_id=t1.item(t1.focus())
    if(get_id["values"]==""):
        messagebox.showerror("Error","Please Select The Data!")
    else:
        mes=messagebox.askyesno("Warning","Do You Want Delete This Record ?")
        if(mes==True):
            id=get_id["values"][0]
            cnn=sq.connect(host="localhost",user="root",password="",database="test")
            cursor=cnn.cursor()
            cursor.execute("delete from data where id=%s",(id,))
            cnn.commit()
            cursor.close()
            cnn.close()
            t1.delete(t1.focus())
    
    
bt3=Button(gp4,text="Delete",command=delete_record)
bt3.place(x=30,y=20)

def Edit_record():
    get_id=t1.item(t1.focus())
    if(get_id["values"]==""):
        messagebox.showerror("Error","Please Select The Data!")
    else:
        top=Toplevel(root)
        gp5=LabelFrame(top,text="Record Update",height="200",width="400")
        gp5.pack(padx=10,pady=10,fill="both",expand=False)

        row_id=get_id["values"][0]
        nm=get_id["values"][1]
        pr=get_id["values"][2]

        lb4=Label(gp5,text="Name")
        lb4.place(x=20,y=30)
        txt4=Entry(gp5)
        txt4.place(x=70,y=30)

        lb5=Label(gp5,text="Price")
        lb5.place(x=20,y=70)
        txt5=Entry(gp5)
        txt5.place(x=70,y=70)

        txt4.insert(0,nm)
        txt5.insert(0,pr)
        def update_record():
            nm1=txt4.get()
            pr1=txt5.get()
        
            cnn=sq.connect(host="localhost",user="root",password="",database="test")
            cursor=cnn.cursor()
            cursor.execute("update data set name=%s,price=%s where id=%s",(nm1,pr1,row_id))
            if(cursor.rowcount>0):
                messagebox.showinfo("Information","Record Update Sucessfully!")
            else:
                messagebox.showinfo("Information","Record Not Update Sucessfully!")
            cnn.commit()
            cursor.close()
            cnn.close()
            t1.item(t1.focus(),values=(row_id,nm1,pr1))
    bt5=Button(gp5,text="Update",command=update_record)
    bt5.place(x=40,y=110)
    top.geometry("400x400")
    top.mainloop()

bt4=Button(gp4,text="Edit",command=Edit_record)
bt4.place(x=90,y=20)
t1=ttk.Treeview(gp3,columns=("id","name","price"),show="headings")
def display():
    cnn=sq.connect(host="localhost",user="root",password="",database="test")
    c=cnn.cursor()
    c.execute("SELECT *FROM data")
    rows=c.fetchall()
    t1.heading("id",text="id")
    t1.heading("name",text="name")
    t1.heading("price",text="price")
    t1.column(column=0,width=50,anchor="center")
    t1.column(column=1,width=50,anchor="center")
    t1.column(column=2,width=50,anchor="center")

    for row in rows:
        t1.insert("",END,values=row)
    t1.pack(padx=20,pady=20,fill="x")
    c.close()
    cnn.close()
display()

root.geometry("700x700")
root.mainloop()