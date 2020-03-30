import sys
import PyQt5

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class home(QWidget):
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
		self.labelLuasRumah = QLabel()
		self.labelLuasTanah = QLabel()
		self.labelHarga = QLabel()
		self.labelHargaA = QLabel()
		self.hasil = QLabel('<b><font size = 4 > PBB sebanyak :  </font></b>')
		
		
		self.labelJudul.setText('<b><font size = 8 > Hitung Pajak Bumi dan Bangunan </font></b>')
		self.labelJudul.setStyleSheet('font-family: Product sans;')
		self.labelJudul.setAlignment(Qt.AlignCenter)
		
		self.logo.setText('<img src = "logo.jpg">')
		self.logo.setAlignment(Qt.AlignCenter)
		
		self.labelLuasRumah.setText('Masukan luas Rumah dalam satuan meter persegi : ')
		self.labelLuasRumah.setStyleSheet('font-family: Product sans;')
		self.labelLuasTanah.setText('Masukan luas Tanah dalam satuan meter persegi : ')
		self.labelLuasTanah.setStyleSheet('font-family: Product sans;')
		self.labelHargaA.setText('Masukan harga bangunan dalam satuan meter persegi: ')
		self.labelHargaA.setStyleSheet('font-family: Product sans;')
		self.labelHarga.setText('Masukan harga tanah dalam satuan meter persegi: ')
		self.labelHarga.setStyleSheet('font-family: Product sans;')
		
		self.Lr = QLineEdit()
		self.Lb = QLineEdit()
		self.Hrg = QLineEdit()
		self.HrgA = QLineEdit()
		
		self.hitung = QPushButton()
		self.hitung.setText('HITUNG')
		self.hitung.setStyleSheet('background-color:rgb(51,51,51);color : white');
		
		self.clear = QPushButton()
		self.clear.setText('Clear')
		self.clear.setStyleSheet('background-color:rgb(51,51,51);color : white'); # Dari stackOverFlow
		
		
		isi = QGridLayout()
		isi.addWidget(self.labelLuasRumah,0,0)
		isi.addWidget(self.Lr,0,1)
		isi.addWidget(self.labelLuasTanah,1,0)
		isi.addWidget(self.Lb,1,1)
		isi.addWidget(self.labelHargaA,2,0)
		isi.addWidget(self.HrgA,2,1)
		isi.addWidget(self.labelHarga,3,0)
		isi.addWidget(self.Hrg,3,1)
		
		isi.addWidget(self.hitung,4,0,1,2)
		isi.addWidget(self.clear,5,0,1,2)
		
		layout = QVBoxLayout()
		layout.addWidget(self.logo)
		layout.addWidget(self.labelJudul)
		layout.addLayout(isi)
		layout.addWidget(self.hasil)
		
		self.hitung.clicked.connect(self.hitungClick)
		self.clear.clicked.connect(self.clearClick)
		
		self.setLayout(layout)
		
	def center(self):
		frameGm = self.frameGeometry()
		screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
		centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())
	
	def clearClick(self):
		self.Lr.clear()
		self.Lb.clear()
		self.Hrg.clear()
		self.HrgA.clear()
		self.hasil.setText('<b><font size = 4 > PBB sebanyak :  </font></b>')
	
	def hitungClick(self):
		LR = float(self.Lr.text())
		LT = float(self.Lb.text())
		HRG = float(self.Hrg.text())
		HRGR = float(self.HrgA.text())
		
		njopB = LR*HRGR
		njopT = LT*HRG
		njopD = njopB+njopT #NJOP (Nilai Jual Objek Pajak)
		
		njop = njopD-12000000 #NJOPKP
		print(njop)
		if(njop<1000000000):
			h = njop*0.2
			#print('Sebelum 0.5 : '+str(h))
			pbb =float (0.005 * h)
			#print(pbb)
			total= int(pbb)
			self.hasil.setText('<b><font size = 6 > PBB sebanyak :  Rp %s </font></b>'%str(total))
		else:
			h = njop*0.4
			#print(h)
			pbb = float(0.005 *h)
			total= int(pbb)
			#print(pbb)
			self.hasil.setText('<b><font size = 6 > PBB sebanyak :  Rp %s </font></b>'%str(total))

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	form = Home()
	form.show()
	
	a.exec_()
		
		
		