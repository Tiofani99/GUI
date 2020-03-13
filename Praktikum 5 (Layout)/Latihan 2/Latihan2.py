from PyQt5.QtWidgets import QWidget, QHBoxLayout , QLabel, QLineEdit
 
class Latihan2(QWidget):
	def __init__(self):   
		super().__init__()   
		self.horizontalUi() 
 
	def horizontalUi(self):
		self.resize(300, 100)   
		self.move(300,300)   
		self.setWindowTitle('Latihan 2') 
 
		self.label1 = QLabel('Masukan Nama Anda : ')
		self.TextBox = QLineEdit()
 
		layout = QHBoxLayout()
		layout.addWidget(self.label1)
		layout.addWidget(self.TextBox)
 
		self.setLayout(layout) 