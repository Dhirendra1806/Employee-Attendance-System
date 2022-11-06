import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import datetime
import pymysql

def amsone():
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=[]
        s="select empid from employee" 
        cur.execute(s)
        data=cur.fetchall()
        for res in data:
            x.append(res[0])
           
        return x
    def finddata():
        db = pymysql.connect(host='localhost', user='root',
                             password='root', database='company')
        cur=db.cursor()
        x=a.get()
        s="select ename from employee where empid= '%s' "%(x)
        cur.execute(s)
        data=cur.fetchone()
       
        
        e2.insert(0,data[0])
        e2.configure(state=DISABLED)
        

    def atmInsert():
        
        if len(e2.get())==0:
               e2.config(bg='Red')
               e3.config(bg='Red')
               cbox.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(e3.get())==0:
               
               e3.config(bg='Red')
               cbox.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        elif len(cbox.get())==0:
               cbox.config(bg='Red')
               messagebox.showwarning("Warning","please fill it all")
        else:
            
            db = pymysql.connect(host='localhost', user='root',
                                password='root', database='company')
            cur = db.cursor()
            x= a.get()
            b = e2.get()
            c = e3.get()
            d = cbox.get()
            s = "insert into ams values('%s','%s','%s','%s')" % (x,
                 b, c, d)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Data saved", "Saved")
           
            e2.delete(0, 100)
            e3.delete(0, 100)
            cbox.delete(0, 100)
            db.close()
    c=Canvas(width=1000,height=700,bg='grey')
    c.place(x=500,y=50)
    
    l1 = Label(c, text='ATTENDANCE MASTER DATA', fg='grey', bg='light yellow',
            font=('Arial', 20), width=40, height=1)
    l1.place(x=300, y=50)
    l2 = Label(c, text='Employee Id :', font=('Times new roman', 20))
    l2.place(x=120, y=120)
    a=ttk.Combobox(c, width=50)
    a.place(x=400,y=120, height=30)
    data=filldata()
    a['values']=data
   
    l3 = Label(c, text='Employee Name :',  font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=400, y=180, height=35)
    
    l4 = Label(c, text='Date Of Mark :', font=('Times new roman', 20))
    l4.place(x=120, y=240)
    e3 = Entry(c, width=50)
    e3.place(x=400, y=240, height=35)
    d = datetime.datetime.now()
    e3.insert(END, d.strftime('%Y-%m-%d  %A %H:%M:%S'))
    e3.configure(state=DISABLED)
   
    l4 = Label(c, text='Status :', font=('Times new roman', 20))
    l4.place(x=120, y=300)
    cbox = ttk.Combobox(c,width=50, values=['Present', 'Absent'], state='readonly')
    cbox.place(x=400,y=300,height=35)
   
    bt21 = Button(c, text='SAVE', width=40, height=1,font=('Times new roman',15),command=atmInsert)
    bt21.place(x=400, y=450)
    bt3 = Button(c, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
    bt3.place(x=500, y=620)
  

    