from tkinter import *
import mysql.connector

root=Tk()
root.configure(background='aqua')
root.geometry('1600x800+0+0')
root.title("MY FIRST SOFTWARE")

def login():
     conn = mysql.connector.connect(host= "localhost",user="root",password="",db="first_project")
     cursor=conn.cursor()
     cursor.execute("select * from reg where email='"+e1.get()+"' and pwd = '"+PWD.get()+"'")
     if(cursor.fetchone()):
         import FIRST_PAGE

def registeration1():
    import registration


top = Frame(root,width=1600,height=80,bg='black',relief = SUNKEN, bd=12)
top.pack(side=TOP)

center = Frame(root,width=800,height=400,bg='black',relief = SUNKEN,bd=12)
center.place(x=460,y=200)


lt = Label(top,text = "LOGIN PAGE",font = ('Arial',50,'bold'),bg = 'black',fg='pink')
lt.pack(side=TOP)

l1 = Label(center,text = "USER ID",font=('Arial',28,'bold'),bg='black',fg='pink')
l1.grid(row=0,column=0)

l2 = Label(center,text = "PASSWORD",font=('Arial',28,'bold'),bg='black',fg='pink')
l2.grid(row=1,column=0)

l3 = Label(center,text = "NEW USER ?",font=('Arial',28,'bold'),bg='black',fg='pink')
l3.grid(row=3,column=0)

Button(center,text = "LOGIN",font = ('Arial',18,'bold'),bg='black',fg='pink',width = 12,command = login).grid(row=2,column=1)
Button(center,text = "SIGN UP",font = ('Arial',18,'bold'),bg='black',fg='pink',width = 12,command = registeration1).grid(row=3,column=1)


e1 = Entry(center,width=24)
e1.grid(row=0,column=1)

PWD= Entry(center,show='*',width=24)
PWD.grid(row=1,column=1)

root.mainloop()
