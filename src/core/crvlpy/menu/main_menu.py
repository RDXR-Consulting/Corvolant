from menu.modules.crackers import crackers
from menu.modules.miners_menu import miners
from menu.modules.spies_menu import spies
from menu.modules.useful_menu import useful
def usr_choose_menu_act():
    usr_choose_menu = input(int("Выберите раздел:\n"))
    return usr_choose_menu


def usr_choose_menu():
    if usr_choose_menu()== 1:
        crackers()
    if usr_choose_menu() == 2:
        miners()
    if usr_choose_menu() == 3:
        spies()
    if usr_choose_menu() == 4:
        useful()


def menu():
    print("ГЛАВНОЕ МЕНЮ\n")
    print("1) Взломщики\n")
    print("2) Майнеры\n")
    print("3) Шпионы\n")
    print("4) Полезности\n")
    usr_choose_menu()

menu()

