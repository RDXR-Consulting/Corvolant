from PyQt5 import QtWidgets
import design
import sys

class CorvolantApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.icon_widget.hide()
        self.icon_miners_button.clicked.connect(self.miners_button_page_change)
        self.icon_spies_button.clicked.connect(self.spies_button_page_change)
        self.icon_useful_button.clicked.connect(self.useful_button_page_change)

        self.name_miners_button.clicked.connect(self.miners_button_page_change)
        self.name_spies_button.clicked.connect(self.spies_button_page_change)
        self.name_useful_button.clicked.connect(self.useful_button_page_change)
      
    def miners_button_page_change(self):
        self.stackedWidget.setCurrentIndex(0)
    def spies_button_page_change(self):
        self.stackedWidget.setCurrentIndex(1)
    def useful_button_page_change(self):
        self.stackedWidget.setCurrentIndex(2)



app = QtWidgets.QApplication(sys.argv)
window = CorvolantApp()
window.show()
app.exec_()
