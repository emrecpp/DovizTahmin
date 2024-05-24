import sys, os
from threading import Thread
sys.path.append(f"Ui{os.sep}") # otherwise it will cause error because "import images_rc" can't found in Ui file.
sys.path.append("..\\")
from app.imports import *
from app.ui.ui_DialogMain import Ui_DialogMain
from predict import DolarOrEuro


class Main(FramelessWindow):
    sigUpdateValue = Signal(dict)
    sigInfoBar = Signal(dict)
    sigShowOutputCard = Signal(bool)

    def __init__(self):
        super().__init__()

    def init(self):
        self.setTitleBar(StandardTitleBar(self))

        self.ui = Ui_DialogMain()
        self.ui.setupUi(self)

        from app.GUIBind import GUIBind
        self.guibind = GUIBind()
        self.guibind.init(parent=self)

        '''self.ui.widSonuc.setVisible(True)
        self.ui.widSonuc.setFixedHeight(120)
        self.ui.lblOutputImage.setPixmap(QPixmap(":/images/dollar.png"))
        self.ui.lblOutputImage.setFixedSize(32, 32)

        self.ui.lblOutput.setText(
        f"<div><span>Tarih: </span><span style='font-weight:400'>05.04.2024</div>")'''

    isStartedPredict = False
    def Predict(self):
        if self.isStartedPredict:
            InfoBar.warning(title="Uyarı", content="Tahmin etme işlemi devam etmekte.", isClosable=True, position=InfoBarPosition.BOTTOM,
                          duration=3000, parent=self)

            return

        self.isStartedPredict = True
        target_date:QDate = self.ui.calendarPicker.getDate()

        self.thrPredict = Thread(target=self.Thread_Predict, args=(target_date,), daemon=True)
        self.thrPredict.start()

    def Thread_Predict(self, target_date:QDate):
        if target_date.year() == 0:
            self.sigInfoBar.emit({"type":"warning", "content": "Lütfen tarih seçiniz."})
            self.sigShowOutputCard.emit(False)
            self.isStartedPredict = False
            return
        if target_date < QDate.currentDate():
            self.sigInfoBar.emit({"type":"warning", "content": "Geçmiş tarih seçilemez."})
            self.sigShowOutputCard.emit(False)
            self.isStartedPredict = False
            return

        if not (self.ui.btnDovizTipi.text() in ["Dolar", "Euro"]):
            self.sigInfoBar.emit({"type":"warning", "content": "Lütfen döviz tipi seçiniz."})
            self.sigShowOutputCard.emit(False)
            self.isStartedPredict = False
            return

        self.sigUpdateValue.emit({"settext": "Başlıyor...", "showImage":False})
        self.sigShowOutputCard.emit(True)

        from predict import predict_dollar_or_euro_price, DolarOrEuro


        if self.ui.btnDovizTipi.text() == "Dolar":
            dolarOrEuro = DolarOrEuro.DOLAR
        else:
            dolarOrEuro = DolarOrEuro.EURO

        for x in predict_dollar_or_euro_price(dolarOrEuro, datetime(target_date.year(), target_date.month(), target_date.day())):
            self.sigUpdateValue.emit({"tarih":x[0], "fiyat":x[1], "dolarOrEuro":dolarOrEuro, "showImage":True})
            #print(x)
        self.isStartedPredict = False
    def slot_updateValue(self, dictionary:dict):

        settext:str = dictionary.get("settext", None)

        if settext:
            self.ui.lblOutput.setText(settext)
            return
        else:
            tarih: datetime = dictionary.get("tarih", None)
            fiyat: float = dictionary.get("fiyat", None)
            dolareuro:DolarOrEuro = dictionary.get("dolarOrEuro", None)
            showImage: bool = dictionary.get("showImage", False)
            #print(tarih, fiyat)
            self.ui.frameOutputImage.setVisible(showImage)
            self.ui.lblOutputImage.setPixmap(QPixmap(":/images/dollar.png" if dolareuro == DolarOrEuro.DOLAR else ":/images/euro.png"))
            self.ui.lblOutput.setText(f"<span>Tarih: </span><span style='font-weight:400'>{tarih.strftime('%d.%m.%Y')}</span><br><span>Fiyat: </span><span style='font-weight:400'>{fiyat:.2f}</span>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.init()
    main.show()
    sys.exit(app.exec())