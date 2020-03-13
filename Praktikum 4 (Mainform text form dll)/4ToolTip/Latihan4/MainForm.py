from PyQt5.QtWidgets import(QWidget,QPushButton,QToolTip)
from OtherForm import * 
from PyQt5.QtGui import QFont

class MainForm(QWidget):  
	def __init__(self):
		super().__init__()
		self.setupUi() 
	def setupUi(self):
		self.resize(400, 300)
		self.move(300, 300)
		self.setWindowTitle('Latihan Menampilkan ToolTip') 
 
		self.button = QPushButton('Other Form')
		self.button1 = QPushButton('Tutup')
		self.button.move(150, 130)
		self.button1.move(150, 170)
		self.button.setParent(self)
		self.button1.setParent(self)

		QToolTip.setFont(QFont('SansSerif',12))
		self.setToolTip('ini adalah <i>ToolTip</i>untuk<b>form</b>')
		
		self.button.setToolTip('''<font color = red>Tombol untuk membuka</font><b> form lain</b>''');
		self.button1.setToolTip('''<font color = blue>Tombol untuk</font><b>keluar</b>''');
 
		self.button.clicked.connect(self.buttonClick)
		self.button1.clicked.connect(self.buttonClick1) 
 
	def buttonClick(self):
		self.form = OtherForm()
		self.form.show() 
 
	def buttonClick1(self):
		self.close()