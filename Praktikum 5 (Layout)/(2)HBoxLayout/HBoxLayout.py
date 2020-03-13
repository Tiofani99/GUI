from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout 
 
class HBoxLayout(QWidget):
	def __init__(self):   
		super().__init__()   
		self.horizontalUi() 
 
	def horizontalUi(self):
		self.resize(300, 100)   
		self.move(300,300)   
		self.setWindowTitle('Penerapan QHBoxLayout') 
 
		self.button1 = QPushButton('Start')   
		self.button2 = QPushButton('Pause')   
		self.button3 = QPushButton('Stop') 
 
		layout = QHBoxLayout()
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		layout.addWidget(self.button3) 
 
		self.setLayout(layout) 