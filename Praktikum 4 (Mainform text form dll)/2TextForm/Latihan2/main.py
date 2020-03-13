import sys
from PyQt5.QtWidgets import QApplication

from Latihan import *

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	minform = Latihan()
	minform.show()
	
	a.exec()