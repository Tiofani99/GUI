from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout,QLabel,QRadioButton , QLineEdit, QLabel
 
class Latihan3(QWidget):  
	def __init__(self):
		super().__init__()
		self.GridUI() 
 
	def GridUI(self):
		self.resize(300, 100)
		self.move(300,300)
		self.setWindowTitle('Latihan 3') 
		
		
		self.label1 = QLabel('<b>Nama</b>')
		self.label2 = QLabel('<b>Umur</b>')
		self.label3 = QLabel('<b>Hobby</b>')
		self.label4 = QLabel('<b>Jenis Kelamin <b>')
		self.button = QPushButton('SUBMIT')
		self.textbox1= QLineEdit()
		self.textbox2= QLineEdit()
		self.textbox3= QLineEdit()
		
		self.radiobutton = QRadioButton('Laki-laki')
		self.radiobutton2 = QRadioButton('Perempuan')
		
		layout = QGridLayout()
		layout.addWidget(self.label1, 0, 0)
		layout.addWidget(self.textbox1, 0, 1,1,3)
		layout.addWidget(self.label2, 1, 0)
		layout.addWidget(self.textbox2, 1, 1,1,3)
		layout.addWidget(self.label3, 2, 0)
		layout.addWidget(self.textbox3, 2, 1,1,3)
		layout.addWidget(self.label4, 3, 0)
		layout.addWidget(self.radiobutton, 3, 1)
		layout.addWidget(self.radiobutton2, 3, 2)
		layout.addWidget(self.button,4,0,1,4)
		
 
		self.setLayout(layout) 