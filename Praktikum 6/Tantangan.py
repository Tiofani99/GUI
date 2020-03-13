import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
		
	def setupUi(self):
		self.resize(300,300)
		self.move(300,300)
		self.setWindowTitle('Ini judul')
		
		self.label1 = QLabel()
		self.label1.setText('Hai')
		
		layout = QVBoxLayout()
		layout.addWidget(self.label1)
		
		self.setLayout(layout)

if __name__ == '__main__':
	a = QApplication(sys.argv)
	
	form = MainForm()
	form.show()
	
	a.exec_()
		