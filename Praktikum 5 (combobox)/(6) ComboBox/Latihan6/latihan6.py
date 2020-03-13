import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(280,90)
		self.move(300,300)
		self.setWindowTitle('Latihan ComboBox')
		
		self.combomakan = QComboBox()
		self.combomakan.addItem('--Pilih Makanan--')
		self.combomakan.addItem('Mendhoan')
		self.combomakan.addItem('Cireng')
		self.combomakan.addItem('Gethuk')
		self.combomakan.addItem('Tahu Bulat')
		self.combomakan.addItem('Ketan Susu')
		
		self.combominum = QComboBox()
		self.combominum.addItem('--Pilih Minuman--')
		self.combominum.addItem('Es Cincau')
		self.combominum.addItem('Milkshake')
		self.combominum.addItem('Chatime')
		self.combominum.addItem('Thaitea')
		self.combominum.addItem('Kopi hitam')
		
		self.pilihan = QPushButton('Pilihan Anda')
		
		layout = QVBoxLayout()
		layout.addWidget(self.combomakan)
		layout.addWidget(self.combominum)
		layout.addWidget(self.pilihan)
		self.pilihan.clicked.connect(self.dapatkanPesanan)
		
		self.setLayout(layout)
	
	def dapatkanPesanan(self):
		if self.combomakan.currentText() == '--Pilih Makanan--' or self.combominum.currentText() == '--Pilih Minuman--':
			QMessageBox.information(self,'Informasi','Anda belum memesan makanan/minuman')
		else :
			QMessageBox.information(self,'Informasi','Anda memilih : '+self.combomakan.currentText()+' & '+self.combominum.currentText())
		
if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	
	a.exec_()
		