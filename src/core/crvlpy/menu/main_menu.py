from menu.modules import crackers_menu
from menu.modules import miners_menu
from menu.modules import spies_menu
from menu.modules import useful_menu
#from art import tprint
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from menu import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Crackers_Button.clicked.connect(self.browse_folder)
        self.comboBox.hide()

    def browse_folder(self):
        self.comboBox.show()

def usr_choose_menu_act():
    return int(int(input("Выберите раздел:")))

def usr_choose_menu():
    user_choose_var = usr_choose_menu_act()
    if user_choose_var == 1:
        crackers_menu.crackers()
    if user_choose_var == 2:
        miners_menu.miners()
    if user_choose_var == 3:
        spies_menu.spies()
    if user_choose_var == 4:
        useful_menu.useful()

def menu():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
#   tprint("Corvolant")
    print("╭────────────────────────────────────────────╮")
    print("│          Г Л А В Н О Е    М Е Н Ю          │")
    print("│                                            │")
    print("│ 1) Взломщики                               │")
    print("│ 2) Майнеры                                 │")
    print("│ 3) Шпионы                                  │")
    print("│ 4) Полезности                              │")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_menu()

