from tkinter import *
from tkinter import ttk,filedialog
import pandas
def show_files():
    delimiter = e2.get()
    header = int(cmd1.get())
    encoding = e3.get()
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files","*.csv")])
    e1.delete(0,END)
    e1.insert(0,file_path)
    
    pd=pandas.read_csv(file_path,delimiter=delimiter,encoding=encoding,header=header)
    txt.delete("1.0",END)
    txt.insert(END,pd.to_string(index=False))
root=Tk()
root.geometry("700x700")

lb1 = Label(root,text="CSV File:")
lb1.place(x=10,y=10)
e1 =Entry(root,width=50)
e1.place(x=80,y=10)
btn1 = Button(root,text="Browse",command=show_files)
btn1.place(x=400,y=8)

lb2 = Label(root,text="Delimiter:")
lb2.place(x=10,y=40)
e2 = Entry(root)
e2.insert(0,",")
e2.place(x=80,y=40)

lb3 = Label(root,text="Heading?")
lb3.place(x=10,y=70)
set_default_val=IntVar(value=1)
cmd1 = ttk.Combobox(root,textvariable=set_default_val,values=[1,0])
cmd1.place(x=80,y=70)

lb4 = Label(root,text="Encoding:")
lb4.place(x=10,y=100)
e3 =Entry(root)
e3.insert(0,"utf-8")
e3.place(x=80,y=100)

gp1 = LabelFrame(root,text="Show CSV File Info",width=200,height=250)
gp1.place(x=10,y=130)
txt = Text(gp1)
txt.pack(padx=10,pady=10,expand=False)

def write_data():
    path = e1.get()
    delimiter = e2.get()
    header = cmd1.get()
    encoding = e3.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    get_data=txt.get("1.0",END).split("\n")
    df=pandas.DataFrame(get_data)
    df=df[0].str.split(",",expand=True)
    df.to_csv(file_path,index=False,header=False)

bt2=Button(root,text="Write",command=write_data)
bt2.place(x=10,y=570)

root.mainloop()