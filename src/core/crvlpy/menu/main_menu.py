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
    print("╭────────────────────────────────────────────╮\n"
          "│          Г Л А В Н О Е    М Е Н Ю          │\n"
          "│============================================│\n"
          "│ 1) Взломщики                               │\n"
          "│ 2) Майнеры                                 │\n"
          "│ 3) Шпионы                                  │\n"
          "│ 4) Полезности                              │\n"
          "╰────────────────────────────────────────────╯\n")

    usr_choose_menu()

