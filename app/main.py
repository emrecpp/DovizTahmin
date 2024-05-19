import sys, os
from threading import Thread
sys.path.append(f"Ui{os.sep}") # otherwise it will cause error because "import images_rc" can't found in Ui file.
from app.imports import *
from app.ui.ui_DialogMain import Ui_DialogMain


class Main(FramelessWindow):
    sigUpdateValue = Signal(dict)
    def __init__(self):
        super().__init__()

    def init(self):
        self.setTitleBar(StandardTitleBar(self))

        self.ui = Ui_DialogMain()
        self.ui.setupUi(self)

        from app.GUIBind import GUIBind
        self.guibind = GUIBind()
        self.guibind.init(parent=self)

    isStartedPredict = False
    def Predict(self):
        if self.isStartedPredict:
            return
        self.isStartedPredict = True
        self.thrPredict = Thread(target=self.Thread_Predict, daemon=True)
        self.thrPredict.start()

    def Thread_Predict(self):
        from predict import predict_dollar_price
        for x in predict_dollar_price(datetime(2025, 5, 15)):
            self.sigUpdateValue.emit({"tarih":x[0], "fiyat":x[1]})
            #print(x)
        self.isStartedPredict = False
    def slot_updateValue(self, dictionary:dict):
        tarih:datetime = dictionary.get("tarih", None)
        fiyat:float = dictionary.get("fiyat", None)
        print(tarih, fiyat)
        self.ui.lblOutput.setText(f"{tarih.strftime('%d.%m.%Y')} - {fiyat:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.init()
    main.show()
    sys.exit(app.exec())