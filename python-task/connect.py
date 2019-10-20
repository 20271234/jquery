import mysql.connector
class DBConnect:
    con=''
    def getConn():
        DBConnect.con = mysql.connector.connect(user='root',
                                          password='MyNewPass',
                                          host='localhost',
                                          database='pruthiraj')
        return DBConnect.con
    
