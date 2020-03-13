import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(300,100)
		self.move(300,300)
		self.setWindowTitle('Demo QCheckBox')
		
		self.label=QLabel()
		self.label.setText('Bahasa Pemrograman Favorit anda ')
		
		self.java = QCheckBox()
		self.java.setText('Java')
		self.pytho = QCheckBox()
		self.pytho.setText('Python')
		self.ruby = QCheckBox()
		self.ruby.setText('Ruby')
		self.php = QCheckBox()
		self.php.setText('PHP')
		
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.java)
		hbox1.addWidget(self.pytho)
		hbox1.addWidget(self.ruby)
		hbox1.addWidget(self.php)
		
		self.tombolOK = QPushButton('&OK')
		self.tombolexit = QPushButton('Keluar')
		
		hbox2 = QHBoxLayout()
		hbox2.addStretch()
		hbox2.addWidget(self.tombolOK)
		hbox2.addWidget(self.tombolexit)
		
		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addLayout(hbox1)
		horizontalLine=QFrame();
		horizontalLine.setFrameShape(QFrame.HLine)
		horizontalLine.setFrameShadow(QFrame.Sunken)
		layout.addWidget(horizontalLine)
		layout.addLayout(hbox2)
		layout.addStretch()
		self.setLayout(layout)
		
		self.tombolOK.clicked.connect(self.okButtonKlik)
		self.tombolexit.clicked.connect(self.close)
		
	def okButtonKlik(self):
		choices = []
		if self.java.isChecked():choices.append('Java')
		if self.pytho.isChecked():choices.append('Python')
		if self.ruby.isChecked():choices.append('Ruby')
		if self.php.isChecked():choices.append('PHP')
		QMessageBox.information(self,'Informasi',repr(choices))
		
if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()
		
		
		
