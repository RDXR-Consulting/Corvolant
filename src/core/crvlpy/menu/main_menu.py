
from menu.modules.crackers_menu import crackers as crack
from modules.miners_menu import miners as mine
from modules.spies_menu import spies as spy



from modules import useful_menu as useful
def usr_choose_menu_act():
    usr_choose_menu = input(int("Выберите раздел:\n"))
    return usr_choose_menu


def usr_choose_menu():
    if usr_choose_menu() == 1:
        crack.crackers()
    if usr_choose_menu() == 2:
        mine.miners()
    if usr_choose_menu() == 3:
        spy.spies()
    if usr_choose_menu() == 4:
        useful.usr_choose_useful()


def menu():
    print("ГЛАВНОЕ МЕНЮ\n")
    print("1) Взломщики\n")
    print("2) Майнеры\n")
    print("3) Шпионы\n")
    print("4) Полезности\n")
    usr_choose_menu()
    return 0
