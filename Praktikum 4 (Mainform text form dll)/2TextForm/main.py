import sys
from PyQt5.QtWidgets import QApplication

from TextForm import *

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	minform = TextForm()
	minform.show()
	
	a.exec()