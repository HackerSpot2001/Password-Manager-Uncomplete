from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QMessageBox,QLineEdit, QTabWidget, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from sqlite3 import connect
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        loadUi("main.ui",self)
        # self.tableWidget = self.findChild(QTableWidget,"tableWidget")
        self.tableWidget = QTableWidget()
        self.setUrl = self.findChild(QLineEdit,"lineEdit")
        self.setEmailOrUsername = self.findChild(QLineEdit,"lineEdit_2")
        self.setPassword = self.findChild(QLineEdit,"lineEdit_3")
        self.tab = self.findChild(QTabWidget,"tabWidget")
        self.pushBtn = self.findChild(QPushButton,"pushButton")
        self.tab.tabBar().setVisible(False)
        self.pushBtn.clicked.connect(self.saveCred)
        self.conn = connect("cred.db")
        self.cur = self.conn.cursor()
        self.sql = ""
        self.showAllCredentials()
        # self.sql = """ CREATE TABLE credentials (
        #         url TEXT NOT NULL,
        #         userName VARCHAR(255) NOT NULL,
        #         password VARCHAR(255) NOT NULL
        #         ); """
        # self.cur.execute(self.sql)
        # self.conn.commit()

    def saveCred(self):
        try:
            if (self.setUrl.text() == "") or (self.setEmailOrUsername.text() == "") or (self.setPassword.text() == ""):
                QMessageBox.warning(self,"Warning","Please fill all Feilds!")

            else:
                self.sql = f"INSERT INTO credentials (url,userName,password) VALUES ('{self.setUrl.text()}','{self.setEmailOrUsername.text()}','{self.setPassword.text()}');"
                self.cur.execute(self.sql)
                self.conn.commit()
                self.setUrl.setText("")
                self.setPassword.setText("")
                self.setEmailOrUsername.setText("")
                self.showAllCredentials()

        except Exception as e:
            QMessageBox.warning(self,"Warning",str(e))
            self.conn.close()
    

    def showAllCredentials(self):
        pass

        # self.sql = "SELECT url,userName,password from credentials;"

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())