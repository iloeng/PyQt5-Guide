#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.03   15:38
-------------------------------------------------------------------------------
   @Change:   2022.05.03
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication
from Ch17.s17_02.cdialog import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())

