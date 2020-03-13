from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Daftar(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(300, 200)
		self.move(400, 200)
		self.setWindowTitle('Form Pendaftaran')
		self.labelJudul = QLabel('<b>Pendaftaran Calon Anggota Avengers</b>')
		self.labelNama = QLabel('Nama')
		self.textNama = QLineEdit()

		self.labelJK = QLabel('Jenis Kelamin')
		self.radioL = QRadioButton('Laki-Laki')
		self.radioL.setChecked(True)
		self.radioP = QRadioButton('Perempuan')

		self.labelTTL = QLabel('Tanggal Lahir')
		self.tanggal = QDateEdit()
		self.tanggal.setDisplayFormat('dd/MM/yyyy')

		self.labelHobi = QLabel('Hobi')
		self.comboHobi = QComboBox()
		self.comboHobi.addItem('Basket')
		self.comboHobi.addItem('Sepak bola')
		self.comboHobi.addItem('Voli')
		self.comboHobi.addItem('Catur')
		self.comboHobi.addItem('Lainnya')

		self.labelALamat = QLabel('Alamat')
		self.textAlamat = QTextEdit()

		self.btnSubmit = QPushButton('Submit')
		self.btnCancel = QPushButton('Cancel')

		layout = QGridLayout()
		layout.addWidget(self.labelJudul,0, 1, 1, 2)
		layout.addWidget(self.labelNama, 1, 0)
		layout.addWidget(self.textNama, 1, 1, 1, 2)
		layout.addWidget(self.labelJK, 2, 0)
		layout.addWidget(self.radioL, 2, 1, 1, 2)
		layout.addWidget(self.radioP, 3, 1, 1, 2)
		layout.addWidget(self.labelTTL, 4, 0)
		layout.addWidget(self.tanggal, 4, 1, 1, 2)
		layout.addWidget(self.labelHobi, 5, 0)
		layout.addWidget(self.comboHobi, 5, 1, 1, 2)
		layout.addWidget(self.labelALamat, 6, 0)
		layout.addWidget(self.textAlamat, 6, 1, 1, 2)
		layout.addWidget(self.btnSubmit, 7, 1, 1, 1)
		layout.addWidget(self.btnCancel, 7, 2)
		self.setLayout(layout)
		
		self.btnSubmit.clicked.connect(self.submitClick)
		self.btnCancel.clicked.connect(self.cancelClik)
		
	def cancelClik(self):
		self.close()
		
	def submitClick(self):
		nama = str(self.textNama.text())
		ttl = str(self.tanggal.date().toString())
		hobi = str(self.comboHobi.currentText())
		alamat = str(self.textAlamat.toPlainText())
		
		if self.radioL.isChecked():
			QMessageBox.information(self, 'Pendaftaran Berhasil',
			'Nama : ' + nama + '\n' +
			'Jenis Kelamin : Laki-Laki\n' +
			'Tanggal Lahir : ' + ttl+ '\n'+
			'Hobi : '+hobi +'\n'+
			'Alamat : '+alamat+'\n') 
		else:
			QMessageBox.information(self, 'Pendaftaran Berhasil',
			'Nama : ' + nama + '\n' +
			'Jenis Kelamin : Perempuan\n' +
			'Tanggal Lahir : ' + ttl + '\n'+
			'Hobi : '+hobi +'\n'+
			'Alamat : '+alamat+'\n') 