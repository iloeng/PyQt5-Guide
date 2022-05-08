# -*- coding: utf-8 -*-
from enum import Enum
from PyQt5.QtWidgets import QGraphicsItem


class EGraphItemType(Enum):
    EGraphItemType_Rect = QGraphicsItem.UserType + 1  # 矩形
    EGraphItemType_Ellipse = EGraphItemType_Rect + 1  # 椭圆
