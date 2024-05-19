# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import (CalendarPicker, DropDownPushButton, PushButton)
import images_rc

class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        if not DialogMain.objectName():
            DialogMain.setObjectName(u"DialogMain")
        DialogMain.resize(494, 354)
        icon = QIcon()
        icon.addFile(u":/images/turkish-lira.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogMain.setWindowIcon(icon)
        DialogMain.setStyleSheet(u"QLabel{\n"
"color:rgb(66,66,66);\n"
"font-weight:800;\n"
"font-size:14pt;\n"
"}")
        self.gridLayout = QGridLayout(DialogMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 45, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.frame = QFrame(DialogMain)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widOutput = QWidget(self.frame)
        self.widOutput.setObjectName(u"widOutput")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widOutput.sizePolicy().hasHeightForWidth())
        self.widOutput.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widOutput)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblOutput = QLabel(self.widOutput)
        self.lblOutput.setObjectName(u"lblOutput")
        self.lblOutput.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblOutput, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widOutput, 8, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnDovizTipi = DropDownPushButton(self.frame_2)
        self.btnDovizTipi.setObjectName(u"btnDovizTipi")
        self.btnDovizTipi.setMinimumSize(QSize(200, 0))

        self.gridLayout_4.addWidget(self.btnDovizTipi, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.btnPredict = PushButton(self.frame)
        self.btnPredict.setObjectName(u"btnPredict")

        self.gridLayout_2.addWidget(self.btnPredict, 7, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.calendarPicker = CalendarPicker(self.frame_3)
        self.calendarPicker.setObjectName(u"calendarPicker")
        self.calendarPicker.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.calendarPicker, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.retranslateUi(DialogMain)

        QMetaObject.connectSlotsByName(DialogMain)
    # setupUi

    def retranslateUi(self, DialogMain):
        DialogMain.setWindowTitle(QCoreApplication.translate("DialogMain", u"D\u00f6viz Fiyat Tahmin | Emre Demircan & Yusuf K\u0131l\u0131\u00e7", None))
        self.lblOutput.setText(QCoreApplication.translate("DialogMain", u"TextLabel", None))
        self.btnDovizTipi.setText(QCoreApplication.translate("DialogMain", u"D\u00f6viz Tipi Se\u00e7in", None))
        self.label_2.setText(QCoreApplication.translate("DialogMain", u"D\u00f6viz Tipi", None))
        self.btnPredict.setText(QCoreApplication.translate("DialogMain", u"Predict", None))
        self.label.setText(QCoreApplication.translate("DialogMain", u"Tarih", None))
    # retranslateUi

