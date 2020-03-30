import sys
import PyQt5

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from home import *


class main(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		#self.resize(600,400)
		self.center()
		self.setWindowTitle('Hitung Pajak Bumi dan Bangunan')
		self.setFixedSize(600, 400)
		
		self.logo = QLabel()
		self.labelJudul = QLabel()
		self.logo.setText('<img src = "bg_awal.jpg">')
		self.logo.setAlignment(Qt.AlignCenter)
		
		self.labelJudul.setText('<b><font size = 8 > Hitung Pajak Bumi dan Bangunan </font></b>')
		self.labelJudul.setStyleSheet('font-family: Product sans;')
		self.labelJudul.setAlignment(Qt.AlignCenter)
		
		
		self.hitung = QPushButton()
		self.hitung.setText('Hitung Pajak')
		self.hitung.setStyleSheet('background-color:rgb(51,51,51);color : white');
		
		self.clear = QPushButton()
		self.clear.setText('Keluar')
		self.clear.setStyleSheet('background-color:rgb(51,51,51);color : white'); # Dari stackOverFlow
		
		
		isi = QGridLayout()
		isi.addWidget(self.hitung,0,0)
		isi.addWidget(self.clear,1,0)
		
		layout = QVBoxLayout()
		layout.addWidget(self.labelJudul)
		layout.addWidget(self.logo)
		layout.addLayout(isi)
		
		
		self.hitung.clicked.connect(self.bukaClick)
		self.clear.clicked.connect(self.ExitClick)
		
		self.setLayout(layout)
		
	def center(self):
		frameGm = self.frameGeometry()
		screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
		centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())
	
	def ExitClick(self):
		quit_msg = "Apakah yakin mau keluar?"
		dialog = QMessageBox.question(self, 'Peringatan', quit_msg, QMessageBox.Yes, QMessageBox.No)

		if dialog == QMessageBox.Yes:
			self.close()
			
	
	def bukaClick(self):
		self.form = home()
		self.form.show() 
		self.close()
		
if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	form = main()
	form.show()
	
	a.exec_()
		
		
		