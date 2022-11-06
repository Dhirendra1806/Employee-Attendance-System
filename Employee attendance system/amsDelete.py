import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
def amsfour():
    

    def finddata():
        
        db = pymysql.connect(host='localhost', user='root',
                                 password='root', database='company')
        cur=db.cursor()
        x=a.get()
        s="select ename from ams where empid= '%s' "%(x)
        cur.execute(s)
        data=cur.fetchone()
                       
        e2.delete(0,100)                
        e2.insert(0,data[0])
        
                    
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
    
    def atmDelete():
        if len(e2.get())==0:
               e2.config(bg='Red')
               
               messagebox.showwarning("Warning","please fill it all")
        else:
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='company')
            cur=db.cursor()
            x=a.get()
            s="delete from ams where empid='%s' "%(x)
            cur.execute(s)
            db.commit()
            messagebox.showinfo("Data Delete","Deleted..")
            a.delete(0,100)
            
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            
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
    
    l3 = Label(c, text='Employee Name :', font=('Times new roman', 20))
    l3.place(x=120, y=180)
    e2 = Entry(c, width=50)
    e2.place(x=400, y=180, height=35)
    
    
    bt22 = Button(c, text='DELETE', width=40, height=1,font=('Times new roman',15),command=atmDelete)
    bt22.place(x=400, y=450)
    bt23 = Button(c, text='FIND', width=40, height=1, font=('Times new roman',15), command = finddata)
    bt23.place(x=400, y=550)
    
    