#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    Paths.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.04.22   23:09
-------------------------------------------------------------------------------
   @Change:   2022.04.22
-------------------------------------------------------------------------------
"""

import os


BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
ICON_PATH = os.path.join(BASE_PATH, 'Utils', '1.ICO')


if __name__ == '__main__':
    print(BASE_PATH)

