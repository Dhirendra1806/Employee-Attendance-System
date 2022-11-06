import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
import datetime

def amstwo():
    
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
    
    def atmUpdate():
        
        if len(e2.get())==0:
               e2.config(bg='Red')
               e3.config(bg='Red')
               
               messagebox.showwarning("Warning","please fill it all")
        elif len(e3.get())==0:
               
               e3.config(bg='Red')
               
               messagebox.showwarning("Warning","please fill it all")
        
        else:
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='company')
            cur=db.cursor()
            b=e2.get()
            c=e3.get()
            d=cbox.get()
            
            x=a.get()
                
            s="update ams set ename='%s',date ='%s',status='%s' where empid='%s'"%(b,c,d,x)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Update","Updated..")
            a.delete(0,100)
            db.close()
            
    def cl():
        e2.configure(state=NORMAL)        
        e2.delete(0,100)
        
        e3.configure(state=NORMAL)        
        e3.delete(0,100)
            
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
    #e1 = Entry(t, width=50)
    #e1.place(x=400, y=120, height=35)
    
    l3 = Label(c, text='Employee Name :', font=('Times new roman', 20))
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
   
    
    bt22 = Button(c, text='UPDATE', width=40, height=1,font=('Times new roman',15),command=atmUpdate)
    bt22.place(x=400, y=450)
    bt23 = Button(c, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
    bt23.place(x=400, y=550)
    bt24 = Button(c, text='clear', width=40, height=1, font=('Times new roman',15), command = cl)
    bt24.place(x=400, y=650)
    
    