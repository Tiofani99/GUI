import sys
from PyQt5.QtWidgets import QApplication

from Latihan import *

if __name__ == '__main__' :
	a=QApplication(sys.argv)
	
	form = Latihan()
	form.show()
	
	a.exec()