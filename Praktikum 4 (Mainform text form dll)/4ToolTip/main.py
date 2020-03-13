import sys
from PyQt5.QtWidgets import QApplication

from ToolTip import *

if __name__ == '__main__':
	a=QApplication(sys.argv)
	
	minform = ToolTip()
	minform.show()
	
	a.exec()