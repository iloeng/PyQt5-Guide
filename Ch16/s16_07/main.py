# -*- coding: utf-8 -*-
"""
    本案例需要提前设置环境变量TRAINDEVHOME，
	并准备'$TRAINDEVHOME/test/chapter19/ks19_02/input.txt'文件。
"""

import sys 	
from PyQt5.QtWidgets import QApplication 

from Ch16.s16_07.cdialog import CDialog

if __name__ == "__main__":	
	app = QApplication(sys.argv)
	dialog = CDialog(None)	
	dialog.show()
	
	sys.exit(app.exec_())
