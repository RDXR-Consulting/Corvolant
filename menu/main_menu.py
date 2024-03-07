from menu.modules import crackers_menu
from menu.modules import miners_menu
from menu.modules import spies_menu
from menu.modules import useful_menu

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

menu()

