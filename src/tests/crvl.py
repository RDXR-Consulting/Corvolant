#DunastyC 5.03.24#
#from art import tprint
from menu import main_menu
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design

def main():
    main_menu.menu()

if __name__ == "__main__":
    main()

