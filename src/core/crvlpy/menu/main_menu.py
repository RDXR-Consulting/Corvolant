from menu.modules.crackers_menu import crackers
from menu.modules.miners_menu import miners
from menu.modules.spies_menu import spies
from menu.modules.useful_menu import useful
def usr_choose_menu_act():
    return(input(int("Выберите раздел:\n")))


def usr_choose_menu():
    user_choose_var = usr_choose_menu_act()
    if user_choose_var == 1:
        crackers()
    if user_choose_var == 2:
        miners()
    if user_choose_var == 3:
        spies()
    if user_choose_var == 4:
        useful()


def menu():
    print("ГЛАВНОЕ МЕНЮ\n")
    print("1) Взломщики\n")
    print("2) Майнеры\n")
    print("3) Шпионы\n")
    print("4) Полезности\n")
    usr_choose_menu()

menu()

