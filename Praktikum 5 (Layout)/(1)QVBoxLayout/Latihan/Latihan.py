from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout, QLabel

class Latihan(QWidget):
	def __init__(self):
		super().__init__()
		self.verticalUi()
	
	def verticalUi(self):
		self.resize(300,200)
		self.move(300,300)
		self.setWindowTitle('Penerapan QVBoxLayout')
		
		self.label1=QLabel('<h4><font color = purple><b>Fakultas Teknologi Industri & Informatika </b></font></h4>')
		
		self.button1 = QPushButton('S1 Rekayasa Perangkat Lunak')
		self.button2 = QPushButton('S1 Desain Komunikasi Visual')
		self.button3 = QPushButton('S1 Sistem Informasi')
		self.button4 = QPushButton('S1 Teknik Industri')
		self.button5 = QPushButton('S1 Informatika')
		
		layout = QVBoxLayout()
		layout.addWidget(self.label1)
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		layout.addWidget(self.button3)
		layout.addWidget(self.button4)
		layout.addWidget(self.button5)
		
		self.setLayout(layout)