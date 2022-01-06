from tkinter import *
from tkinter import messagebox
import mysql.connector as sqltr

def listtostring(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s))

def create_window():
    window1=Tk()
    
    def storevalue():
        global value0
        value0=entry0.get()
        value01=entry10.get()
        print(value0)
        print(value01)
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST0="insert into medicines values('{}','{}')".format(value0,value01)
        cursor.execute(ST0)
        cursor1=mycon.cursor()
        St0="select * from medicines where medicine='{}'".format(value0)
        cursor1.execute(St0)
        data=cursor1.fetchall()
        print(data)
        mycon.close()
    def removevalue():
        value02=entry11.get()
        print(value02)
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST01="delete from medicines where medicine='{}'".format(value02)
        cursor.execute(ST01)
        mycon.close()
    window1.title("Database")
    window1.geometry("600x600")
    lbl0=Label(window1,text="ADD OR REMOVE MEDICINES FROM HERE",font="bold",bg="white",anchor="n")
    lbl0.grid(column=1,row=0)
    btn0=Button(window1,text="ADD NEW MEDICINE",bg="white",command=storevalue)
    btn0.grid(column=1,row=4)
    btn01=Button(window1,text="REMOVE MEDICINE",bg="white",command=removevalue)
    btn01.grid(column=1,row=10)
    lbl01=Label(window1,text="MEDICINE NAME",font="bold",bg="white",anchor="n")
    lbl01.grid(column=3,row=4)
    lbl02=Label(window1,text="MEDICINE DETAILS",font="bold",bg="white",anchor="n")
    lbl02.grid(column=3,row=7)
    entry0=Entry(window1,bd=5)
    entry0.grid(column=5,row=4)
    entry10=Entry(window1,bd=5)
    entry10.grid(column=5,row=7)
    lbl03=Label(window1,text="MEDICINE NAME",font="bold",bg="white",anchor="n")
    lbl03.grid(column=3,row=12)
    entry11=Entry(window1,bd=5)
    entry11.grid(column=5,row=12)
    window1.mainloop()


def getmedicinesname():
    global value
    value=entry.get()
    print(value)
    global value1
    value1=entry1.get()
    global value2
    value2=entry2.get()
    global value3
    value3=entry3.get()
    global value4
    value4=entry4.get()
    print(value1)
    print(value2)
    print(value3)
    print(value4)
    if value=="PARACETAMOL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST02="select details from medicines where medicine='{}'".format("PARACETAMOL")
        cursor.execute(ST02)
        data=cursor.fetchall()
        print(data)
        cursor01=mycon.cursor()
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)
    
    elif value=="RABEPREZOL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("RABEPREZOL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        cursor01=mycon.cursor()
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif  value=="ABATACEPT":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ABATACEPT")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ARPIPRAZOLE":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ARPIPRAZOLE")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ABCAVIR-ORAL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ABCAVIR-ORAL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ACTIGALL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ACTIGALL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        print(data)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="INTERFERON":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("INTERFERON")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ACTIVASE":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ACTIVASE")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ACTONEL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ACTONEL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="ACTOS":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("ACTOS")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="VERAPAMIL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("VERAPAMIL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CALCITONIN":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CALCITONIN")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CALCIONATE":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CALCIONATE")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CARBATROL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CARBATROL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CASODEX":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CASODEX")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CATAFLAM":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CATAFLAM")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="CATAPRES":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("CATAPRES")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="HALOPERIDOL":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("HALOPERIDOL")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="HARVONI":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("HARVONI")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)


    elif value=="HARVIX":
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST="select details from medicines where medicine='{}'".format("HARVIX")
        cursor.execute(ST)
        data=cursor.fetchall()
        print(data)
        St02="insert into usersdata values('{}','{}','{}','{}')".format(value1,value2,value3,value4)
        cursor.execute(St02)
        cursor02=mycon.cursor()
        cursor02.execute("select * from usersdata")
        data1=cursor02.fetchall()
        print(data1)
        mycon.close()
        messagebox.showinfo("results",data)
    else:
        messagebox.showinfo("results","selected medicine not available")


def medicineappcode():
    value000=entry00.get()
    print(value000)
    
    value001=entry011.get()
    print(value001)
    mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
    cursor00=mycon.cursor()
    ST00="select username from logindetails where passwords='{}'".format(value001) 
    cursor00.execute(ST00)
    data00=cursor00.fetchall()
    print(data00)
    for row01 in data00:
        username01=row01
        print(username01)
    username001=listtostring(username01)
    cursor001=mycon.cursor()
    St01="select passwords from logindetails where username='{}'".format(value000)
    cursor001.execute(St01)
    data001=cursor001.fetchall()
    for row0 in data001:
        password01=row0
        print(password01)
    password001=listtostring(password01)
    print(data001)
    mycon.close()
    if username001==value000 and password001==value001:
        
        window=Tk()
        window.title("KNOW YOUR MEDICINE")
        window.geometry("800x800")

        lbl=Label(window,text="THIS APPLICATION ENLIGHTENS YOU ABOUT YOUR MEDICINES",font="bold",bg="white",anchor="n")
        lbl.grid(column=1,row=0)

        label=Label(window,wraplength=100,text="PLEASE PROVIDE THE REQUIRED INFORMATION HERE",relief="groove")
        label.grid(column=1,row=3)

        btn=Button(window,text="GET RESULTS",bg="white")
        btn.grid(column=4,row=4)

        lbl2=Label(window,text="Medicines Name :")
        lbl2.grid(column=0,row=6)
        global entry
        entry=Entry(window,bd=5)
        entry.grid(column=1,row=6)
        

        lbl3=Label(window,text="Name :")
        lbl3.grid(column=0,row=8)

        global entry1
        entry1=Entry(window,bd=5)
        entry1.grid(column=1,row=8)

        lbl4=Label(window,text="Age")
        lbl4.grid(column=0,row=10)

        global entry2
        entry2=Entry(window,bd=5)
        entry2.grid(column=1,row=10)

        lbl5=Label(window,text="Weight in KG")
        lbl5.grid(column=0,row=12)

        global entry3
        entry3=Entry(window,bd=5)
        entry3.grid(column=1,row=12)

        lbl5=Label(window,text="Country")
        lbl5.grid(column=0,row=14)

        global entry4
        entry4=Entry(window,bd=5)
        entry4.grid(column=1,row=14)

        btn=Button(window,text="ADD NEW MEDICINE",bg="white",command=create_window)
        btn.grid(column=4,row=4)

        btn=Button(window,text="SUBMIT",bg="white",command=getmedicinesname)
        btn.grid(column=4,row=6)

        btn=Button(window,text="RESULTS",bg="white",command=getmedicinesname)
        btn.grid(column=4,row=8)
        window.mainloop()

    else:
        messagebox.showinfo("WELCOME","PASSWORD IS INVALID")

        
window2=Tk()
window2.geometry("400x400")
lbl00=Label(window2,text="WELCOME PLEASE PROVIDE LOGIN DETAILS",font="bold",bg="white",anchor="n")
lbl00.grid(column=1,row=0)
lbl001=Label(window2,text="USERNAME",font="bold",bg="white",anchor="n")
lbl001.grid(column=1,row=3)
lbl002=Label(window2,text="PASSWORD",font="bold",bg="white",anchor="n")
lbl002.grid(column=1,row=7)
entry00=Entry(window2,bd=5)
entry00.grid(column=3,row=3)
entry011=Entry(window2,bd=5)
entry011.grid(column=3,row=7)
btn0112=Button(window2,text="LOGIN",bg="white",command=medicineappcode)
btn0112.grid(column=1,row=10)
window2.mainloop()
def create_window():
    window1=Tk()
    
    def storevalue():
        global value0
        value0=entry0.get()
        value01=entry10.get()
        print(value0)
        print(value01)
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST0="insert into medicines values('{}','{}')".format(value0,value01)
        cursor.execute(ST0)
        cursor1=mycon.cursor()
        St0="select * from medicines where medicine='{}'".format(value0)
        cursor1.execute(St0)
        data=cursor1.fetchall()
        print(data)
        mycon.close()
    def removevalue():
        value02=entry11.get()
        print(value02)
        mycon = sqltr.connect(host ="localhost", user = "root",passwd="", database ="siraju")
        cursor=mycon.cursor()
        ST01="delete from medicines where medicine='{}'".format(value02)
        cursor.execute(ST01)
        mycon.close()
    window1.title("Database")
    window1.geometry("600x600")
    lbl0=Label(window1,text="ADD OR REMOVE MEDICINES FROM HERE",font="bold",bg="white",anchor="n")
    lbl0.grid(column=1,row=0)
    btn0=Button(window1,text="ADD NEW MEDICINE",bg="white",command=storevalue)
    btn0.grid(column=1,row=4)
    btn01=Button(window1,text="REMOVE MEDICINE",bg="white",command=removevalue)
    btn01.grid(column=1,row=10)
    lbl01=Label(window1,text="MEDICINE NAME",font="bold",bg="white",anchor="n")
    lbl01.grid(column=3,row=4)
    lbl02=Label(window1,text="MEDICINE DETAILS",font="bold",bg="white",anchor="n")
    lbl02.grid(column=3,row=7)
    entry0=Entry(window1,bd=5)
    entry0.grid(column=5,row=4)
    entry10=Entry(window1,bd=5)
    entry10.grid(column=5,row=7)
    lbl03=Label(window1,text="MEDICINE NAME",font="bold",bg="white",anchor="n")
    lbl03.grid(column=3,row=12)
    entry11=Entry(window1,bd=5)
    entry11.grid(column=5,row=12)
    window1.mainloop()





