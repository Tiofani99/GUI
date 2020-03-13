from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout

class VBoxLayout(QWidget):
	def __init__(self):
		super().__init__()
		self.verticalUi()
	
	def verticalUi(self):
		self.resize(300,200)
		self.move(300,300)
		self.setWindowTitle('Penerapan QVBoxLayout')
		
		self.button1 = QPushButton('Start')
		self.button2 = QPushButton('Stop')
		self.button3 = QPushButton('Pause')
		self.button4 = QPushButton('Forward')
		self.button5 = QPushButton('Previous')
		
		layout = QVBoxLayout()
		layout.addWidget(self.button1)
		layout.addWidget(self.button2)
		layout.addWidget(self.button3)
		layout.addWidget(self.button4)
		layout.addWidget(self.button5)
		
		self.setLayout(layout)