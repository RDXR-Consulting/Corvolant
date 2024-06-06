from menu import main_menu
from menu.modules.crackers import bruteforce as bfr
from menu.modules.crackers import fisher as fsh
from menu.modules.crackers import analyzer as anl
from menu.modules.crackers import botnet as btn
from menu.modules.crackers import jammer as jam


def crackmenu():
    print("╭────────────────────────────────────────────╮\n"
          "│          Г Л А В Н О Е    М Е Н Ю          │\n"
          "│============================================│\n"
          "│ 1) Брутфорс                                │\n"
          "│ 2) Фишер                                   │\n"
          "│ 3) Анализ сетей                            │\n"
          "│ 4) Ботнет                                  │\n"
          "│ 5) Генератор помех                         │\n"
          "│ 0) Назад                                   │\n"
          "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите инструмент: "))
        if usr_choose == 1:
            bfr.bruteforce_func()
            choosing = False
        elif usr_choose == 2:
            fsh.fisher_func()
            choosing = False
        elif usr_choose == 3:
            anl.analyzer_func()
            choosing = False
        elif usr_choose == 4:
            btn.botnet_func()
            choosing = False
        elif usr_choose == 5:
            jam.jammer_func()
            choosing = False
        elif usr_choose == 0:
            main_menu.glavmenu()
        else:
            print("Вы ввели что то неправильное")
