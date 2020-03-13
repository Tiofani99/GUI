import sys
from PyQt5.QtWidgets import QApplication

from Dosen import *

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	minform = Dosen()
	minform.show()
	
	a.exec()