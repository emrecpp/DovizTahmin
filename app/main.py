import sys, os
sys.path.append(f"Ui{os.sep}img") # otherwise it will cause error because "import images_rc" can't found in Ui file.
import sys, os

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from app.ui.ui_MainWindow import Ui_MainWindow
from qfluentwidgets import *
from qframelesswindow import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())