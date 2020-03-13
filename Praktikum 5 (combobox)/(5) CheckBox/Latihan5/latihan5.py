import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
		
	def setupUi(self):
		self.resize(290,180)
		self.move(300,300)
		self.setWindowTitle(' ')
		
		self.tampil = QCheckBox()
		self.tampil.setText('Show Title')
		self.label = QLabel()
		self.label.setText(' ')
		
		layout = QVBoxLayout()
		layout.addWidget(self.tampil)
		layout.addWidget(self.label)
		self.setLayout(layout)
		
		
		self.tampil.stateChanged.connect(self.tampilkan)
		
	def tampilkan(self):
		if self.tampil.isChecked():
			self.setWindowTitle('Contoh QCheckBox')
		else:
			self.setWindowTitle(' ')

if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	
	a.exec_()