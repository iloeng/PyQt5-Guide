# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication
from Ch24.s24_02.cdialog import *


if __name__ == "__main__":	
	app = QApplication(sys.argv)
	widget = CDialog()
	widget.show() 	 
	sys.exit(app.exec_())
