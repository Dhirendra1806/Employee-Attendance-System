import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkinter import *
from empinsert import *
from empinsert import *
from empinsert import *
from empUpdate import *
from empFind import *
from empDelete import *
from amsInsert import*
from amsUpdate import*
from amsFind import*
from amsDelete import*
from depInsert import *
from depUpdate import *
from depFind import *
from depDelete import *
from holidayInsert import *
from holidayUpdate import *
from holidayFind import *
from holidayDelete import *
from ToShowalldata import *
from toshowams import *
from toshowdept import *
from toshowholiday import *
from toshowworkplan import *




from PIL import ImageTk,Image
import datetime
def fronttwouser():

    t = tkinter.Tk()
    t.geometry('1550x900')
    t.config(bg='light blue')


    
    def Okuser():
        
        
            x=e1.get()
            
            ps=e2.get() 
            
            db=pymysql.connect(host='localhost',user='root',password='root',database='company')
            cur=db.cursor()
            x=e1.get()
            ps=e2.get()
            
            s="select ename from employee where empid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            #ps=StringVar()
            #y=e2.get()
            if ps=="" and x=="":
                messagebox.showinfo("error","fill id or password..")
            elif ps=="":
                messagebox.showinfo("error","fill required password..")
            elif x=="":
                messagebox.showinfo("error","fill required id..")
            elif ps==data[0]:
                db = pymysql.connect(host='localhost', user='root',
                                    password='root', database='company')
                cur = db.cursor()
                a = e1.get()
                b = e2.get()
                c = e3.get()
                d = cbox.get()
                s = "insert into ams values('%s','%s','%s','%s')" % (
                    a, b, c,d)
                cur.execute(s)
                db.commit()
                
                e1.delete(0, 100)
                e2.delete(0, 100)
                e3.delete(0, 100)
                
                db.close()
                
                messagebox.showinfo("info","Your attend has been marked")
            
            else:
                messagebox.showerror("Info","Invalid Username or password")            
        
    l1 = Label(t, text='USER LOGIN PAGE', font=('Times new Roman', 20),
               fg='grey', bg='light yellow', width=50, height=1)
    l1.place(x=350, y=50)
    l2 = Label(t, text='Employee ID :', font=('Times new roman', 20))
    l2.place(x=450, y=220)
    e1 = Entry(t, width=50)
    e1.place(x=650, y=220, height=35)
    l3 = Label(t, text='Password :', font=('Times New Roman', 20))
    l3.place(x=450, y=315)
    e2 = Entry(t, width=50, show='*')
    e2.place(x=650, y=315, height=35)
    
    d = datetime.datetime.now()

    
    e3 = Entry(t, width=50,font=('Times new roman',20))
    e3.place(x=1, y=1, height=35)
    e3.insert(END, d.strftime('%Y-%m-%d  %A %H:%M:%S'))
    l4 = Label(t, text='Status :', font=('Times New Roman', 20))
    l4.place(x=450, y=400)
    
    cbox = ttk.Combobox(t,width=47, values=['Present', 'Absent'], state='readonly')
    cbox.place(x=650,y=400,height=35)
    
    
    bt1 = Button(t, text='OK', font=('Times New Roman', 15),command=Okuser)
    bt1.place(x=580, y=460)
    bt2 = Button(t, text='CANCEL', font=('Times New Roman', 15),command=t.destroy) 
    bt2.place(x=690, y=460) 
    bh=Button(t,width=20,text='View Holidays',font=('Times new roman',15),command=viewholiday)
    bh.place(x=1300,y=1)
   
    '''bt4 = Button(t, text='FORGOT PASSWORD', font=('Times New Roman', 15),command=forg) 
    bt4.place(x=750, y=540) '''
    t.mainloop()



def frontone():

    t = tkinter.Tk()
    t.geometry('1550x900')
    t.config(bg='light blue')
    
    def Okadmin():
        
            
        
        x=e1.get()
        ps=e2.get()
        
        
            
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        x=e1.get()
        ps=e2.get()
        
        s="select pass from adlogin where user='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        #ps=StringVar()
        #y=e2.get()
        if ps=="" and x=="":
            messagebox.showinfo("Info","fill id or password..")
        elif ps=="":
            messagebox.showinfo("Info","fill required password..")
        elif x=="":
            messagebox.showinfo("Info","fill required id..")
        elif ps==data[0]:
             
        
            c=Canvas(width=1550,height=900,bg='grey')
            c.place(x=0,y=0)
                        
                        
            l1=Label(c,text='Employee',font=('Times new roman',15))
            l1.place(x=50,y=20)
            b1=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=Empone)
            b1.place(x=30,y=50)
            b2=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=Emptwo)
            b2.place(x=30,y=80)
            b3=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=Empthree)
            b3.place(x=30,y=110)
            b4=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=Empfour)
            b4.place(x=30,y=140)
                        
            
            l2=Label(c,text='Department',font=('Times new roman',15))
            l2.place(x=50,y=180)
            b5=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=deptone)
            b5.place(x=30,y=210)
            b6=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=depttwo)
            b6.place(x=30,y=240)
            b7=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=deptthree)
            b7.place(x=30,y=270)
            b8=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=deptfour)
            b8.place(x=30,y=300)
                
                        
            l4=Label(c,text='Holiday Master',font=('Times new roman',15))
            l4.place(x=40,y=340)
            b13=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=holione)
            b13.place(x=30,y=370)
            b14=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=holitwo)
            b14.place(x=30,y=400)
            b15=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=holithree)
            b15.place(x=30,y=430)
            b16=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=holifour)
            b16.place(x=30,y=460)
                        
            l5=Label(c,text='Attendance Master',font=('Times new roman',15))
            l5.place(x=30,y=500)
            b17=Button(c,width=20,height=1,text='Insert',font=('Times new roman',11),command=amsone)
            b17.place(x=30,y=530)
            b18=Button(c,width=20,height=1,text='Update',font=('Times new roman',11),command=amstwo)
            b18.place(x=30,y=560)
            b19=Button(c,width=20,height=1,text='find',font=('Times new roman',11),command=amsthree)
            b19.place(x=30,y=590)
            b20=Button(c,width=20,height=1,text='Delete',font=('Times new roman',11),command=amsfour)
            b20.place(x=30,y=610)
            
            l6=Label(c,text='View Records',font=('Times new roman',15))
            l6.place(x=210,y=20)
            b21=Button(c,width=20,height=1,text='View Holidays',font=('Times new roman',11),command=viewholiday)
            b21.place(x=210,y=50)
            b22=Button(c,width=20,height=1,text='View Emloyee',font=('Times new roman',11),command=viewone)
            b22.place(x=210,y=80)
            b23=Button(c,width=20,height=1,text='View Department',font=('Times new roman',11),command=viewdept)
            b23.place(x=210,y=110)
            b25=Button(c,width=20,height=1,text='View Attendance',font=('Times new roman',11),command=viewams)
            b25.place(x=210,y=140)
            
            messagebox.showinfo("info","Login Successfull")
                    
                    
            
            
            
          
            
    
        
              
    
                    
                        
                        
                
      
    l1 = Label(t, text='ADMIN LOGIN PAGE', font=('Times new Roman', 20),
                               fg='grey', bg='light yellow', width=50, height=1)
    l1.place(x=350, y=50)
    l2 = Label(t, text='Admin Id :', font=('Times new roman', 20))
    l2.place(x=450, y=220)
    e1 = Entry(t, width=40, font=('Times new roman', 15))
    e1.place(x=650, y=220, height=35)
    l3 = Label(t, text='Password :', font=('Times New Roman', 20))
    l3.place(x=450, y=330)
    e2 = Entry(t, width=40, show='*', font=('Times new roman', 15))
    e2.place(x=650, y=330, height=35)
    bt1 = Button(t, text='LOGIN', font=('Times New Roman', 15),command=Okadmin)
    bt1.place(x=670, y=440)
    bt2 = Button(t, text='CANCEL', font=('Times New Roman', 15),command=t.destroy)
    bt2.place(x=900, y=440)
   
    '''
    bt3 = Button(t, text='FORGET PASSWORD', font=('Times New Roman', 15))
    bt3.place(x=670, y=440)
    bt5 = Button(t, text='REGISTER', font=('Times New Roman', 15))
    bt5.place(x=900, y=440)
    '''
    t.mainloop() 

t = tkinter.Tk()
t.geometry('1550x900')
t.config(bg='light blue')


c2=Canvas(t,width=130,height=130)
c2.place(x=450,y=350)
img=ImageTk.PhotoImage(Image.open("Adminicon.png"))
c2.create_image(70,70,anchor='center',image=img)
c1=Canvas(t,width=130,height=130)
c1.place(x=800,y=350)
img1=ImageTk.PhotoImage(Image.open("user3.png"))
c1.create_image(70,70,anchor='center',image=img1)
 

l3 = Label(t, text='Select the type of login you would like to use',
           font=('Verdana', 20), fg='Black', bg='White', width=40, height=2)
l3.place(x=350, y=200)


l1 = Label(t, text='EMPLOYEE ATTENDANCE MANAGEMENT SYSTEM', font=('Lucida Handwriring', 30),
           fg='grey', bg='light yellow', width=50, height=2)
l1.place(x=150, y=50)

bt1 = Button(t, text='Admin', width=20, height=1, font=('Times new roman',15),command=frontone)
bt1.place(x=400, y=500)
bt2 = Button(t, text='User', width=20, height=1, font=('Times new roman',15),command=fronttwouser)
bt2.place(x=750, y=500)






t.mainloop()