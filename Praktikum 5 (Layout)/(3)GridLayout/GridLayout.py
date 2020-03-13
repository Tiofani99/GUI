from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout 
 
class GridLayout(QWidget):  
	def __init__(self):
		super().__init__()
		self.GridUI() 
 
	def GridUI(self):
		self.resize(300, 100)
		self.move(300,300)
		self.setWindowTitle('Penerapan QGridLayout') 
 
		self.button1 = QPushButton('SEMAR')
		self.button2 = QPushButton('GARENG')
		self.button3 = QPushButton('PETRUK')
		self.button4 = QPushButton('BAGONG') 
 
		layout = QGridLayout()
		layout.addWidget(self.button1, 0, 0)
		layout.addWidget(self.button2, 0, 1)
		layout.addWidget(self.button3, 1, 0)
		layout.addWidget(self.button4, 1, 1) 
 
		self.setLayout(layout) 