from PyQt5.QtWidgets import QWidget, QPushButton,QMessageBox 

class OtherForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi() 
 
	def setupUi(self):
		self.resize(400, 300)
		self.move(300, 300)
		self.setWindowTitle('Form Lain') 
 
		self.button = QPushButton('About')
		self.button.move(150, 130)
		self.button.setParent(self) 
		
		self.button1 = QPushButton('Tutup')
		self.button1.move(310,260)
		self.button1.setParent(self)
 
		self.button.clicked.connect(self.buttonClick) 
		self.button1.clicked.connect(self.buttonClick1)
 
	def buttonClick(self):
		QMessageBox.about(self,'About','Dibuat oleh Tim RPL \nVersi 1.0\nCopyright@2019')
	
	def buttonClick1(self):
		self.close()