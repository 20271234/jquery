from tkinter import*
import connect
import operateaccount
class Display :
    def __init__(self,root,msg):
        self.root = root
        self.msg = msg
        self.root.title("Display Record")
        self.root.geometry("700x600")
        self.name1=StringVar()
        self.balance1=StringVar()
        
        self.l1=Label(self.root,text="ROLL NO: ",
                      fg='red',
                      font="Times 20")
        self.l2=Label(self.root,text="name:",
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
        
        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")
        self.b2=Button(self.root,text="exit",
                      width=10,height=1,
                      fg='blue',
                      font="Times 20",command=self.exitWindow)
        self.b3=Button(self.root,text="MENU",
                      width=20,height=1,
                      fg='blue',
                      font="Times 10",command=self.menu)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.l2.place(x=100,y=220)
        self.e2.place(x=300,y=220)
        self.l3.place(x=100,y=330)
        self.e3.place(x=300,y=330)
        self.b1.place(x=250,y=400)
        self.l4.place(x=100,y=500)
        self.b2.place(x=400,y=400)
        self.b3.place(x=450,y=450)
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
                Display.con=connect.DBConnect.getConn()
                print("connected to database")
                cur=Display.con.cursor()
                print("cursor created")
                #print("execute")
                cur.execute("select  bookid from py_issuebook where rollno=%d" %no)
                records=cur.fetchall()
                self.name1.set(records)
                print(records)
                #self.balance1.set(record[2])
                     
                print("display record")
                 
            except Exception as ms:
                self.msg.set(ms)
            finally:
                if Display.con!='':
                    Display.con.close()
                    print("conn released")
        return

    def exitWindow(self):
        self.root.destroy()
        return

