import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design
from modules.useful import keygen

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.icon_only_widget.hide()
        self.keygen_button.clicked.connect(self.keygen_change)
        self.keylogger_button.clicked.connect(self.keylogger_change)
        self.mini_keygen_button.clicked.connect(self.keygen_change)
        self.mini_keylogger_button.clicked.connect(self.keylogger_change)
        self.keygen_generate_button.clicked.connect(self.keygen_generate)


    def keygen_change(self):
        self.stackedWidget.setCurrentIndex(0)
    def keylogger_change(self):
        self.stackedWidget.setCurrentIndex(1)

    def keygen_generate(self):
        value_lenght = self.keygen_lenght_lineEdit.text()
        include_lowercase_letters = self.keygen_lower_checkBox.isChecked()
        include_uppercase_letters = self.keygen_upper_checkBox.isChecked()
        include_numbers = self.keygen_number_checkBox.isChecked()
        include_special_chars = self.keygen_spec_checkBox.isChecked()
        
        generated_password = keygen.generate_password(int(value_lenght), include_special_chars, include_lowercase_letters, include_uppercase_letters, include_numbers)
        self.keygen_result_textEdit.setText(generated_password)


app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
window = ExampleApp()  # Создаём объект класса ExampleApp
window.show()  # Показываем окно
app.exec_()

