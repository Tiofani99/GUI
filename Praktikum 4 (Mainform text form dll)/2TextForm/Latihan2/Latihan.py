from PyQt5.QtWidgets import QWidget,QLabel

class Latihan(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(400,200)
		self.move(300,300)
		self.setWindowTitle('Latihan 2 <Tag HTML>')
		
		self.label1=QLabel('<h1>Rekayasa <font color = red>Perangkat</font> <font color = blue> Lunak </font></h1>')
		self.label1.move(10,10)
		self.label1.setParent(self)
		
		self.label2=QLabel('<h3><b> Peserta Praktikum Pemrograman GUI<b></h3>')
		self.label2.move(10,50)
		self.label2.setParent(self)
		
		self.label3=QLabel('<ol> <li>Monkey D Luffy</li><li>Roronoa Zorro</li><li>Takiya Genji</li></ol>')
		self.label3.move(20,75)
		self.label3.setParent(self)