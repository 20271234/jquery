from tkinter import*
import mysql.connector
import connect
import operateaccount
class insert:
   con=''
   def __init__(self,root,msg):
      self.root=root
      self.msg=msg
      self.root.title("insert student record")
      self.root.geometry("700x600")
      self.head=Label(self.root,text="record details:",
                      fg='red',
                      font="Times 20")
      
      self.b2=Button(self.root,text="exit",
                      width=10,height=2,
                      fg='blue',font="Times 20",
                      command=self.exitWindow)
      self.l1=Label(self.root,text="roll no: ",
                      fg='red',font="Times 20")
      self.l2=Label(self.root,text="name:",
                      fg='red',font="Times 20")
      self.l3=Label(self.root,text="address:",
                      fg='red',font="Times 20")
      self.b1=Button(self.root,text="insert",
                      width=10,height=2,
                      fg='red',font="Times 20",command=self.nextFrame)
      self.e1=Entry(self.root,width=20,
                      font="Times 20")
      self.e2=Entry(self.root,width=20,
                      font="Times 20")
      self.e3=Entry(self.root,width=20,
                      font="Times 20")
      self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")
      self.b3=Button(self.root,text="BACK TO MENU",
                      width=30,height=1,
                      fg='blue',
                      command=self.menu)
      
      self.head.place(x=200,y=50)
      self.l1.place(x=100,y=110)
      self.e1.place(x=300,y=110)
      self.l2.place(x=100,y=220)
      self.e2.place(x=300,y=220)
      self.l3.place(x=100,y=330)
      self.e3.place(x=300,y=330)
      self.b1.place(x=250,y=400)
      self.b2.place(x=400,y=400)
      self.l4.place(x=100,y=500)
      self.b3.place(x=400,y=450)
   def clear(self):
       self.e1.delete(0,END)
       self.e2.delete(0,END)
       self.e3.delete(0,END)
   def menu(self):
      self.root.destroy()
      takeop = Tk()
      operateaccount.TakeOperation(takeop)
   
   def nextFrame(self):
      #no=None
      #name=''
      #balance=0
      no=self.e1.get()
      name=self.e2.get()
      address=self.e3.get()
      if(no==''):
         self.msg.set("you cannot miss the firlds")
      if(name==''):
         self.msg.set("you cannot miss the firlds")
      if(address==''):
         self.msg.set("you cannot miss the firlds")
      else:
         try:
            no=int(no)
            name=name
            address=address
            insert.con=connect.DBConnect.getConn()
            print("connected to database")
            cur=insert.con.cursor()
            cur.execute("insert into addStudent values(%d,'%s','%s')" %(no,name,address))
            insert.con.commit()
            self.msg.set("sucessfully inserted")
         except Exception as ms:
            self.msg.set(ms)
         finally:
            if insert.con!='':
               self.clear()
               insert.con.close()
               print("connection released")
               
      return
   def exitWindow(self):
      self.root.destroy()
      return
            
