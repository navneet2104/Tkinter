from tkinter import *
import mysql.connector

def view():
    root.destroy()
    import viewinfo

def homepage2():
    root.destroy()
    import FIRST_PAGE

def logoutthis():
    root.destroy()


def adveh():
    a = str(e1.get())
    b = str(e2.get())
    c = str(e3.get())
    d = str(e4.get())
    e = str(e5.get())
    f = str(e6.get())
    g = str(e7.get())
    h = str(e8.get())
    i = str(e9.get())
    j = str(e10.get())
    k = str(e11.get())

    conn = mysql.connector.connect(host = "localhost",user = "root",password="",db="vehicle")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO veinfo(vtype,vbrand,vname,vnumber,oname,phone,address,dob,city,pincode,state) values('"+a.upper()+"','"+b.upper()+"','"+c.upper()+"','"+d.upper()+"','"+e.upper()+"','"+f+"','"+g.upper()+"','"+h.upper()+"','"+i.upper()+"','"+j.upper()+"','"+k.upper()+"')")
    conn.commit()



root = Tk()
root.config(background = "aqua")
root.title("ADD VEHICLE")
root.geometry("1600x800+0+0")



menubar1= Menu(root)
infomenu1 = Menu(menubar1,tearoff=0)
menubar1.add_cascade(label ="VEHICLE INFO",menu=infomenu1)
infomenu1.add_command(label = "View Info",command=view)

homemenu=Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="GO TO",menu=homemenu)
homemenu.add_command(label = "Home Page",command=homepage2)

logout3 = Menu(menubar1,tearoff=0)
menubar1.add_cascade(label="LOGOUT",menu=logout3)
logout3.add_command(label = "logout",command = logoutthis)

root.config(menu=menubar1)

Label(root,text = "ADD VEHICLE INFORMATION",bg='aqua',fg='black',font=('algerian',28,'bold','underline')).place(x=400,y=50)

center = Frame(root,width=1600,height=550,bg='black',relief = SUNKEN,bd=12)
center.place(x=410,y=120)

Label(center,text="Vehicle Type",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=0,column=0)
e1=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e1.grid(row=0,column=1)

Label(center,text="Vehicle Brand",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=1,column=0)
e2=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e2.grid(row=1,column=1)

Label(center,text="Vehicle Name",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=2,column=0)
e3=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e3.grid(row=2,column=1)

Label(center,text="Vehicle Number",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=3,column=0)
e4=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e4.grid(row=3,column=1)

Label(center,text="Owner Name",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=4,column=0)
e5=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e5.grid(row=4,column=1)

Label(center,text="Phone",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=5,column=0)
e6=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e6.grid(row=5,column=1)

Label(center,text="Address",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=6,column=0)
e7=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e7.grid(row=6,column=1)

Label(center,text="Date of Birth",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=7,column=0)
e8=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e8.grid(row=7,column=1)

Label(center,text="City",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=8,column=0)
e9=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e9.grid(row=8,column=1)

Label(center,text="Pincode",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=9,column=0)
e10=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e10.grid(row=9,column=1)

Label(center,text="State",bg="black",fg="yellow",font=("comic sans MS",20)).grid(row=10,column=0)
e11=Entry(center,font=("comic sans MS",15),bd=2,fg="white",bg="grey")
e11.grid(row=10,column=1)

Button(center,text="SUBMIT",font=('algerian',18,'bold'),bg='grey',fg='black',padx=4,pady=4,command=adveh).grid(row=11,column=1)

root.mainloop()
