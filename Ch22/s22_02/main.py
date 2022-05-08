# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from Ch22.s22_02.cdialog import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())
