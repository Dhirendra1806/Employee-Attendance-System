# -- coding: utf-8 --
"""
Created on Fri Jul 29 12:56:48 2022

@author: HP
"""

from tkinter import ttk
from tkinter import *
import tkinter as tk
import pymysql


#def connect():

#    db = pymysql.connect(host='localhost', user='root', password='root', database='company')

#    cur=db.cursor()

  #  db.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

 #   db.commit()

 #   db.close()

def viewone():    
    def View():
    
        db=pymysql.connect(host='localhost',user='root',password='root',database='company')
        cur=db.cursor()
        
        s="select * from employee" 
        cur.execute(s)
        
        data=cur.fetchall()
        
        for row in data:
            
            
    
            tree.insert("", tk.END, values=row)        
    
        db.close()
    
    
    # connect to the database
    
    #connect() 
    
    root = tk.Tk()
    root.geometry('1550x900')
    root.config(bg='light blue')

    
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
    
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Employee ID")
    
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Employee name")
    
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Address")
    
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="phone")
    
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Email")
    
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="department ID")
    
    
    
    tree.pack()
    
    bt1 = Button(root, text='display data', width=20, height=1, font=('Times new roman',15),command=View)
    bt1.place(x=600, y=300)

    root.mainloop()
    
   