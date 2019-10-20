from tkinter import*
import connect
import operateaccount
class Update :
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Update Record")
        self.root.geometry("700x600")
        self.name1=StringVar()
        self.balance1=StringVar()
        
        self.l1=Label(self.root,text="enter Roll no: ",
                      fg='red',
                      font="Times 20")
        self.l2=Label(self.root,text="name:",
                      fg='red',
                      font="Times 20")
        self.l3=Label(self.root,text="addresee:",
                      fg='red',
                      font="Times 20")
        self.l5=Label(self.root,text="enter bookid:",
                      fg='red',
                      font="Times 20")
        self.b1=Button(self.root,text="display",
                      width=10,height=1,
                      fg='red',
                      font="Times 20",command=self.disp)
        self.e1=Entry(self.root,width=20,
                      font="Times 20")
        self.e2=Entry(self.root,textvariable=self.name1,width=20,
                      font="Times 20")
        self.e3=Entry(self.root,textvariable=self.balance1,width=20,
                      font="Times 20")
        self.e4=Entry(self.root,width=20,
                      font="Times 20")
        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")
        self.b2=Button(self.root,text="exit",
                      width=10,height=1,
                      fg='blue',
                      font="Times 20",command=self.exitWindow)
        self.b3=Button(self.root,text="issue",
                      width=10,height=1,
                      fg='green',
                      font="Times 20",command=self.rec_update)
        self.b4=Button(self.root,text="BACK TO MENU",
                      width=20,height=2,
                      fg='blue',
                      font="Times 20",command=self.menu)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.l2.place(x=100,y=220)
        self.e2.place(x=300,y=220)
        self.l3.place(x=100,y=300)
        self.e3.place(x=300,y=300)
        self.l5.place(x=100,y=340)
        self.e4.place(x=300,y=340)
        self.b1.place(x=250,y=400)
        self.l4.place(x=200,y=500)
        self.b2.place(x=400,y=445)
        self.b3.place(x=450,y=500)
        self.b4.place(x=500,y=550)
    def clear(self):
         self.e1.delete(0,END)
         self.e2.delete(0,END)
         self.e3.delete(0,END)
    def menu(self):
      self.root.destroy()
      takeop = Tk()
      operateaccount.TakeOperation(takeop)
    def disp(self):
         no=self.e1.get()
         if no=='':
             self.msg.set("plese enter valid roll no")
         else:
             try:
                 no=int(no)
                 Update.con=connect.DBConnect.getConn()
                 print("connected to database")
                 cur=Update.con.cursor()
                 query="select * from addstudent  where rollno=%d"%no
                 Update.con.commit()
                 cur.execute(query)
                 #Update.con.commit()
                 record=cur.fetchone()
                 self.name1.set(record[1])
                 self.balance1.set(record[2])
                     
                 print("display record")
                 
             except Exception as ms:
                 self.msg.set(ms)
                 print(ms)
             finally:
                 if Update.con!='':
                     Update.con.close()
                     print("conn released")
         return
    def rec_update(self):
         no=self.e1.get()
         name=self.e2.get()
         balance=self.e3.get()
         roll=self.e4.get()
         if no=='':
             self.msg.set("plese enter valid roll")
         elif name=='':
             self.msg.set("plese enter valid student name")
         elif balance=='':
             self.msg.set("plese enter valid address")
         elif roll=='':
             self.msg.set("plese enter book id")
         else:
             try:
                 no=int(no)
                 roll=int(roll)
                 name=name
                 balance=balance
                 Update.con=connect.DBConnect.getConn()
                 print("connected to database")
                 cur=Update.con.cursor()
                 cur.execute("select * from addbook where bookid=%d" %roll)
                 row=cur.fetchone()
                 if row[3]=='y' or row[3]=='Y':
                     cur.execute("insert into py_issuebook values(%d,%d,'%s')" %(no,roll,name))
                     Update.con.commit()
                     try: 
                         Update.con=connect.DBConnect.getConn()
                         print("connected to database")
                         cur=Update.con.cursor()
                         cur.execute("update addbook set status='n' where bookid=%d" %roll)
                         Update.con.commit()
                         table=cur.fetchone()
                         print(table)
                         self.msg.set("sucessfully updated")
                     except Exception as ms:
                         msg.set(ms)
                         print(ms)
                         print("2")
                 else:
                     self.msg.set("book already issued")
                     
                 
                         
                 
             except Exception as ms:
                 print(ms)
                 print("3")
                 
             finally:
                 if Update.con!='':
                     self.clear()
                     Update.con.close()
                     print("conn released")


    def exitWindow(self):
        self.root.destroy()
        return

