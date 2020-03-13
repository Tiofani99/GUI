import sys
from PyQt5.QtWidgets import QApplication

from FormSederhana import *

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	minform = FormSederhana()
	minform.show()
	
	a.exec()