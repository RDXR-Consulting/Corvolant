from menu.modules import crackers_menu
from menu.modules import miners_menu
from menu.modules import spies_menu
from menu.modules import useful_menu


def glavmenu():
    print("╭────────────────────────────────────────────╮\n"
          "│          Г Л А В Н О Е    М Е Н Ю          │\n"
          "│============================================│\n"
          "│ 1) Взломщики                               │\n"
          "│ 2) Майнеры                                 │\n"
          "│ 3) Шпионы                                  │\n"
          "│ 4) Полезности                              │\n"
          "│ 0) Выйти                                   │\n"
          "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите раздел: "))
        if usr_choose == 1:
            crackers_menu.crackmenu()
            choosing = False
        elif usr_choose == 2:
            miners_menu.miners()
            choosing = False
        elif usr_choose == 3:
            spies_menu.spies()
            choosing = False
        elif usr_choose == 4:
            useful_menu.useful()
            choosing = False
        elif usr_choose == 0:
            exit()
        else:
            print("Вы ввели что то неправильное")
