from tkinter import*
import connect
import operateaccount
class Delete :
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Delete Record")
        self.root.geometry("700x600")
        self.b2=Button(self.root,text="exit",
                      width=20,height=2,
                      fg='blue',
                      font="Times 20",command=self.exitWindow)
        self.l1=Label(self.root,text="account no: ",
                      fg='red',
                      font="Times 20")
        self.e1=Entry(self.root,width=20,
                      font="Times 20")
        self.b1=Button(self.root,text="delete",
                      width=20,height=3,
                      fg='red',
                      font="Times 20",command=self.delete)
        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")
        self.b3=Button(self.root,text="BACK TO MENU",
                      width=20,height=2,
                      fg='blue',
                      font="Times 20",command=self.menu)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.b2.place(x=100,y=220)
        self.l4.place(x=300,y=220)
        self.b1.place(x=100,y=330)
        self.b3.place(x=400,y=450)

    def menu(self):
        self.root.destroy()
        takeop = Tk()
        operateaccount.TakeOperation(takeop)

    def delete(self):
        no =self.e1.get()
        if no=='':
            self.msg.set("plese enter account5 no")
        else:
            try:
                no=int(no)
                Delete.con=connect.DBConnect.getConn()
                print(" connectedb to database")
                cur=Delete.con.cursor()
                cur.execute("delete from py_issuebook where bookid=%d"%no)
                
                Delete.con.commit()
               
                co=Delete.con.cursor()
                cur.execute("update addbook set status='y' where bookid=%d"%no)
                Delete.con.commit()
                self.msg.set("deleted sucessfully")
            except Exception as ms:
                self.msg.set(ms)
            finally:
                if Delete.con!='':
                   Delete.con.close()
                   print("connection released")
        return
    def exitWindow(self):
        self.root.destroy()
        return
