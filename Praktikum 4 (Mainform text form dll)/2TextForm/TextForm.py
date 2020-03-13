from PyQt5.QtWidgets import QWidget,QLabel

class TextForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(400,200)
		self.move(300,300)
		self.setWindowTitle('Implementasi Tag HTML')
		
		self.label1=QLabel('<h1>Hello <font color = red>World</font></h1>')
		self.label1.move(10,10)
		self.label1.setParent(self)
		
		self.label2=QLabel('''Hidup adalah perjuangan, dan <b> Hidup adalah pilihan </b> <i> Tidak Memilih </i>, Termasuk dari <u> pilihan tersebut </i>''')
		self.label2.setWordWrap(True)
		self.label2.move(10,50)
		self.label2.setParent(self)
		