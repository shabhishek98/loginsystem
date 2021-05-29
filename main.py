from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql

root = tkinter.Tk()
root.title('LOG IN SYSTEM')
root.geometry('400x300+550+250')

uname = StringVar()
passw = StringVar()

def exit():
    root.destroy()
    print('Hello')
def sign_up():
    root.destroy()
    root2 = Tk()
    root2.title('New User')
    root2.geometry('400x300+550+250')
    Lab = Label(root2, text='Welcome to KJSCE', bg='blue', relief='groove', borderwidth='10', font=('times new roman', '20', 'bold'))
    Lab.pack(fill='both')

    uname = StringVar()
    passw = StringVar()
    confirm_pass = StringVar()

    Fm1 = Frame(root2)
    Fm1.pack()

    Lab1 = Label(Fm1, text='Username', font=('times new roman', '13', 'bold'))
    Lab1.pack(side=LEFT, padx='35', pady='5')

    Tb1 = Entry(Fm1, width='20', textvariable=uname, font=('times new roman', '13',))
    Tb1.pack(pady='5')

    Fm2 = Frame(root2)
    Fm2.pack()

    Lab2 = Label(Fm2, text='Password', font=('times new roman', '13', 'bold'))
    Lab2.pack(side=LEFT, padx='35', pady='5')

    Tb2 = Entry(Fm2, width='20', textvariable=passw, font=('times new roman', '13',))
    Tb2.pack(pady='5')

    Fm3 = Frame(root2)
    Fm3.pack()

    Lab3 = Label(Fm3, text='Confirm Password', font=('times new roman', '13', 'bold'))
    Lab3.pack(side=LEFT, pady='5', padx='3')

    Tb3 = Entry(Fm3, width='20', textvariable=confirm_pass, font=('times new roman', '13'))
    Tb3.pack(pady='5')

    Fm4 = Frame(root2)
    Fm4.pack()

    def data():
        con = pymysql.Connect(host='localhost', user='root', password='', database='detail')
        cur = con.cursor()
        cur.execute("insert into user values(%s, %s)", (uname.get(), passw.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Info', 'Account has been created')



    def done():
        if uname.get() =="" or passw.get() =="" or confirm_pass.get() == "":
            messagebox.showerror('Error', 'All fields are required')

        else:
            con = pymysql.Connect(host='localhost', user='root', password='', database='detail')
            cur = con.cursor()
            cur.execute('select * from user where username=%s', uname.get())
            variable = cur.fetchall()
            con.commit()
            con.close()
            try:
                if variable[0][0] == uname.get():
                    messagebox.showerror('Error', 'Username already exist')

            except Exception:
                if passw.get() == confirm_pass.get():
                    data()
                else:
                    messagebox.showerror('Error', 'Please enter right password')

    Bt1 = Button(Fm4, text='DONE', font=('times new roman', '13', 'bold'), bg='grey', command=done)
    Bt1.pack(side=LEFT)


def log_in():
    global uname
    global passw

    if uname.get() == "" or passw.get() == "":
        messagebox.showerror("Error", 'All fields are required')

    else:
        con = pymysql.Connect(host='localhost', user='root', password='', database='detail')
        cur = con.cursor()
        cur.execute('select * from user where username=%s', uname.get())
        fetched_passw = cur.fetchall()
        con.commit()
        con.close()
        try:
            if passw.get() == fetched_passw[0][1]:
                messagebox.showinfo('login Successful', 'Welcome to Somaiya Campus')
            else:
                messagebox.showerror('Error', 'Wrong Password or Username')
        except Exception:
            messagebox.showerror('Error', 'Username does not exist')

def delete():
    root.destroy()
    root3 = Tk()
    root3.title('Delete Account')
    root3.geometry('400x300+550+250')
    uname = StringVar()
    passw = StringVar()

    frm1 = Frame(root3)
    frm1.pack()

    lab = Label(frm1, text='Username', font=('times new roman', '13', 'bold'))
    lab.pack(side=LEFT, padx='10', pady='20')

    tb = Entry(frm1, width='20', textvariable=uname, font=('times new roman', '13'))
    tb.pack(pady='20')

    frm2 = Frame(root3)
    frm2.pack()

    lab = Label(frm2, text='password', font=('times new roman', '13', 'bold'))
    lab.pack(side=LEFT, padx='10', pady='20')

    tb = Entry(frm2, width='20', textvariable=passw, font=('times new roman', '13'))
    tb.pack(pady='20')


    def delete_account():
        con = pymysql.Connect(host='localhost', user='root', password='', database='detail')
        cur = con.cursor()
        cur.execute('select * from user where username=%s', uname.get())
        variable1 = cur.fetchall()
        try:
            if variable1[0][1] == passw.get():
                cur.execute('Delete from user where username=%s', uname.get())
                messagebox.showinfo('info', 'Account has been deleted')
                con.commit()
                con.close()
            else:
                messagebox.showerror('Error', 'Wrong password')
        except Exception:
            messagebox.showerror('Error', 'Username does not exist')

    frm3 = Frame(root3)
    frm3.pack()

    bt = Button(frm3, text='Delete', font=('times new roman', '13', 'bold'),bg='grey', command=delete_account)
    bt.pack()


lab = Label(root, text='Welcome to KJSCE', bg='blue', relief='groove', borderwidth='10', font=('times new roman', '20','bold'))
lab.pack(fill='both')

fm1 = Frame(root)
fm1.pack()

lab1 = Label(fm1, text='Username', font=('times new roman', '13', 'bold'),)
lab1.pack(side=LEFT, padx='10', pady='20')

tb1 = Entry(fm1, textvariable=uname, width='20', font=('times new roman', '13'))
tb1.pack(pady='20')

fm2 = Frame(root)
fm2.pack()

lab2 = Label(fm2, text='Password', font=('times new roman', '13', 'bold'))
lab2.pack(side=LEFT, padx='10',)

tb2 = Entry(fm2, textvariable=passw,  width='20', font=('times new roman', '13'))
tb2.pack()

fm3 = Frame(root)
fm3.pack(pady='10')

bt1 = Button(fm3, text='Log In', font=('times new roman', '13', 'bold'), bg='grey', command=log_in)
bt1.pack(side=LEFT, padx='20')

bt2 = Button(fm3, text='Sign UP', font=('times new roman', '13', 'bold'),bg='grey', command=sign_up)
bt2.pack(side=LEFT, padx='25')

bt3 = Button(fm3, text='Exit', font=('times new roman', '13', 'bold'), bg='grey', command=exit).pack()

fm4 = Frame(root).pack()

bt4 = Button(fm4, text='Delete my Account', font=('times new roman', '13', 'bold'), bg='grey', command=delete)
bt4.pack()

lab3 = Label(fm4, text='"Sign UP if you are new"', font=('times new roman', '13', 'bold'))
lab3.pack()

root.mainloop()

