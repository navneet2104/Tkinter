from tkinter import *

root=Tk()
root.configure(background='blue')
root.geometry('1600x800+0+0')
root.title("VEHICLE MANAGEMENT")

def addv():
    root.destroy()
    import addvehicle

def viewv():
    root.destroy()
    import viewinfo

def logout1():
    root.destroy()
    import login_page


center = Frame(root,width=800,height=400,bg='black',relief = SUNKEN,bd=12)
center.place(x=280,y=250)


lt = Label(center,text = "     WELCOME OWNER    ",font = ('ALGERIAN',50,'bold','underline'),bg = 'pink',fg='black',bd=12)
lt.pack(side=TOP)

menubar = Menu(root)
fmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="ADD VEHICLE",menu=fmenu)
fmenu.add_command(label  = "Add info",command=addv)


infomenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label ="VEHICLE INFO",menu=infomenu)
infomenu.add_command(label = "View Info",command=viewv)


logout = Menu(menubar,tearoff=0)
menubar.add_cascade(label="LOGOUT",menu = logout)
logout.add_command(label="Logout",command=logout1)

root.config(menu=menubar)



root.mainloop()
