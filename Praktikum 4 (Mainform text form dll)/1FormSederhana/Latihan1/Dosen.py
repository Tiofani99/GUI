from PyQt5.QtWidgets import QWidget,QLabel

class Dosen(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(500,200)
		self.move(400,400)
		self.setWindowTitle('Praktikum Pemrograman GUI')
		
		self.label = QLabel('Dosen Pengampu : ')
		self.label.move(70,40)
		self.label.setParent(self)
		
		self.label1 = QLabel('Afandi Nur Aziz Thohari, S.T.,M.Cs')
		self.label1.move(70,55)
		self.label1.setParent(self)
		
		self.label2 = QLabel('Copy Right 2019')
		self.label2.move(230,160)
		self.label2.setParent(self)