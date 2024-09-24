# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogMainruDIrc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
        DialogMain.resize(494, 355)
        icon = QIcon()
        icon.addFile(u":/images/turkish-lira.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogMain.setWindowIcon(icon)
        DialogMain.setStyleSheet(u"QLabel{\n"
"color:rgb(66,66,66);\n"
"font-weight:800;\n"
"font-size:14pt;\n"
"}\n"
"#widSonuc{\n"
"background-color:rgb(247,247,247);\n"
"border-radius:12px;\n"
"border:2px solid rgb(230,230,230)\n"
"}")
        self.gridLayout = QGridLayout(DialogMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 45, 20, 20)
        self.frame = QFrame(DialogMain)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_4)
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
        self.btnDovizTipi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btnDovizTipi, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)

        self.btnPredict = PushButton(self.frame)
        self.btnPredict.setObjectName(u"btnPredict")
        self.btnPredict.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btnPredict, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 8, 0, 1, 2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_5)
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
        self.calendarPicker.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.calendarPicker, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 1, 0, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 1)

        self.widSonuc = QWidget(self.frame)
        self.widSonuc.setObjectName(u"widSonuc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widSonuc.sizePolicy().hasHeightForWidth())
        self.widSonuc.setSizePolicy(sizePolicy)
        self.widSonuc.setMinimumSize(QSize(0, 125))
        self.gridLayout_3 = QGridLayout(self.widSonuc)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frameOutputImage = QFrame(self.widSonuc)
        self.frameOutputImage.setObjectName(u"frameOutputImage")
        self.frameOutputImage.setMinimumSize(QSize(0, 30))
        self.frameOutputImage.setFrameShape(QFrame.StyledPanel)
        self.frameOutputImage.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frameOutputImage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.lblOutputImage = QLabel(self.frameOutputImage)
        self.lblOutputImage.setObjectName(u"lblOutputImage")
        self.lblOutputImage.setMinimumSize(QSize(32, 32))
        self.lblOutputImage.setMaximumSize(QSize(32, 32))
        self.lblOutputImage.setScaledContents(True)
        self.lblOutputImage.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lblOutputImage, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frameOutputImage, 1, 0, 1, 1)

        self.lblOutput = QLabel(self.widSonuc)
        self.lblOutput.setObjectName(u"lblOutput")
        self.lblOutput.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblOutput, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widSonuc, 7, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)


        self.retranslateUi(DialogMain)

        QMetaObject.connectSlotsByName(DialogMain)
    # setupUi

    def retranslateUi(self, DialogMain):
        DialogMain.setWindowTitle(QCoreApplication.translate("DialogMain", u"D\u00f6viz Fiyat Tahmin | Emre Demircan & M\u00fccahit Nas", None))
        self.label_2.setText(QCoreApplication.translate("DialogMain", u"D\u00f6viz Tipi", None))
        self.btnDovizTipi.setText(QCoreApplication.translate("DialogMain", u"D\u00f6viz Tipi Se\u00e7in", None))
        self.btnPredict.setText(QCoreApplication.translate("DialogMain", u"Tahmin Et", None))
        self.label.setText(QCoreApplication.translate("DialogMain", u"Hedef Tarih", None))
        self.lblOutputImage.setText("")
        self.lblOutput.setText(QCoreApplication.translate("DialogMain", u"Ba\u015fl\u0131yor...", None))
    # retranslateUi

