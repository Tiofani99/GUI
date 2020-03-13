import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Daftar import * 

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(300,100)
		self.move(300,300)
		self.setWindowTitle('Kuis Pemrograman GUI')
		
		self.label1 = QLabel('Username')
		self.label2 = QLabel('Password')
		
		self.usertxt = QLineEdit()
		self.pwtxt = QLineEdit()
		self.pwtxt.setEchoMode(QLineEdit.Password)
		
		self.btnLogin = QPushButton('Login')
		self.btnClear = QPushButton('Clear')
		
		layout = QGridLayout()
		layout.addWidget(self.label1,0,0)
		layout.addWidget(self.usertxt,0,1,1,2)
		layout.addWidget(self.label2,1,0)
		layout.addWidget(self.pwtxt,1,1,1,2)
		layout.addWidget(self.btnLogin,2,1)
		layout.addWidget(self.btnClear,2,2)
		self.setLayout(layout)
		
		self.btnClear.clicked.connect(self.FClear)
		self.btnLogin.clicked.connect(self.FLogin)
		
	def FLogin(self):
		user = self.usertxt.text()
		pw = self.pwtxt.text()
		
		if not user or not pw :
			QMessageBox.information(self,'Perhatian','Username atau password tidak boleh kosong')
		else:
			if user == '17104016' and pw =='12345':
				self.form = Daftar()
				self.form.show() 
				self.close()
			else:
				QMessageBox.information(self,'Perhatian','Username atau password Salah')
		
		
	def FClear(self):
		self.usertxt.clear()
		self.pwtxt.clear()
		
if __name__ == '__main__':
	a = QApplication(sys.argv)
	
	form = MainForm()
	form.show()
	
	a.exec_()