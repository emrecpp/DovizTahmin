# -*- coding: utf-8 -*-
from app.ui.ui_DialogMain import Ui_DialogMain
from app.imports import *

class GUIBind(QObject):
    def init(self, parent):
        self.parent = parent
        self.ui: Ui_DialogMain = parent.ui
        self.ui.widSonuc.setVisible(False)
        self.ui.frameOutputImage.setVisible(False)
        self.ui.btnPredict.clicked.connect(parent.Predict)
        self.parent.sigUpdateValue.connect(self.parent.slot_updateValue)
        self.parent.sigInfoBar.connect(self.slot_infoBar)
        self.parent.sigShowOutputCard.connect(self.slot_showOutputCard)

        font_predict = self.ui.btnPredict.font()
        font_predict.setBold(True)
        self.ui.btnPredict.setFont(font_predict)


        #self.ui.calendarPicker.setDateFormat(QtCore.TextDate)
        self.ui.calendarPicker.setDateFormat('dd.MM.yyyy')
        self.menu_dovizTipi = RoundMenu(parent=self.parent)
        self.menu_dovizTipi.itemHeight = 40
        act_dolar, act_euro = Action(QIcon(':/images/dollar.png'), "Dolar"), Action(QIcon(':/images/euro.png'), "Euro")
        act_dolar.triggered.connect(lambda: self.ui.btnDovizTipi.setText("Dolar"))
        act_euro.triggered.connect(lambda: self.ui.btnDovizTipi.setText("Euro"))

        self.menu_dovizTipi.addAction(act_dolar)
        self.menu_dovizTipi.addAction(act_euro)
        self.ui.btnDovizTipi.setMenu(self.menu_dovizTipi)

    def slot_infoBar(self, data:dict):
        type = data.get("type", None)
        if type == "warning":
            InfoBar.warning(title="Uyarı", content=data.get("content", "Bilinmiyor"), isClosable=True, position=InfoBarPosition.BOTTOM, parent=self.parent)

    def slot_showOutputCard(self, show:bool):
        self.ui.widSonuc.setVisible(show)
