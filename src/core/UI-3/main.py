import sys
from PyQt5 import QtWidgets
import design

class CorvolantApp(QtWidgets.QMainWindow, design.Ui_Corvolant):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.icon_widget.hide()
        self.pushButton_5.hide()
        self.stackedWidget_2.setCurrentIndex(0)
        self.icon_miners_button.clicked.connect(self.miners_button_page_change)
        self.icon_spies_button.clicked.connect(self.spies_button_page_change)
        self.icon_useful_button.clicked.connect(self.useful_button_page_change)

        self.name_miners_button.clicked.connect(self.miners_button_page_change)
        self.name_spies_button.clicked.connect(self.spies_button_page_change)
        self.name_useful_button.clicked.connect(self.useful_button_page_change)

        self.pushButton_9.clicked.connect(self.keylogger_page_change)
        self.pushButton_17.clicked.connect(self.keygen_page_change)
        self.pushButton_7.clicked.connect(self.home_page_change)
        self.pushButton_6.clicked.connect(self.home_page_change)
      
    def miners_button_page_change(self):
        self.stackedWidget.setCurrentIndex(0)
    def spies_button_page_change(self):
        self.stackedWidget.setCurrentIndex(1)
    def useful_button_page_change(self):
        self.stackedWidget.setCurrentIndex(2)
    def keygen_page_change(self):
        self.stackedWidget_2.setCurrentIndex(1)
    def keylogger_page_change(self):
        self.stackedWidget_2.setCurrentIndex(3)
    def home_page_change(self):
        self.stackedWidget_2.setCurrentIndex(0)




app = QtWidgets.QApplication(sys.argv)
window = CorvolantApp()
window.show()
app.exec_()
