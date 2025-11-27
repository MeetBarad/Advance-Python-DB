from tkinter import *
import sqlite3 as sq

root=Tk()
def init():
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("create table if not exists test(username text,password text)")
    cnn.commit()
    c.close()
    cnn.close()
init()

lbl1=Label(root,text="Userame")
lbl1.place(x=10,y=10)
e1=Entry(root)
e1.place(x=70,y=10)

lbl2=Label(root,text="Password")
lbl2.place(x=10,y=40)
e2=Entry(root)
e2.place(x=70,y=40)


lb1=Listbox(root,width=30)
lb1.place(x=10,y=100)
def add_data():
    nm=e1.get()
    psw=e2.get()
    if nm!="" and psw!="":
        cnn=sq.connect("my.db")
        c=cnn.cursor()
        c.execute("insert into test(username,password)values(?,?)",(nm,psw))
        cnn.commit()
        c.close()
        cnn.close()
        e1.delete(0,END)
        e2.delete(0,END)

def display():
    lb1.delete(0,END)
    cnn=sq.connect("my.db")
    c=cnn.cursor()
    c.execute("select *from test")
    rows=c.fetchall()
    for i in rows:
        data=f"{i[0]} | {i[1]}"
        lb1.insert(END,data)
    cnn.commit()
    c.close()
    cnn.close()

bt1=Button(root,text="Add",command=add_data)
bt1.place(x=30,y=70)
bt2=Button(root,text="Display",command=display)
bt2.place(x=70,y=70)

root.geometry("500x500")
root.mainloop()