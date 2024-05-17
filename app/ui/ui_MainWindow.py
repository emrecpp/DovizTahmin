# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowTBVwIz.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 278)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnPredict = QPushButton(self.frame)
        self.btnPredict.setObjectName(u"btnPredict")

        self.gridLayout_2.addWidget(self.btnPredict, 2, 0, 1, 1)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_2.addWidget(self.dateEdit, 1, 0, 1, 1)

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


        self.gridLayout_2.addWidget(self.widOutput, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dolar Fiyat Tahmin | Emre Demircan & Yusuf K\u0131l\u0131\u00e7", None))
        self.btnPredict.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.lblOutput.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

