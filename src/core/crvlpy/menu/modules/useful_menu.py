from menu import main_menu
from menu.modules.useful import randata as ran
from menu.modules.useful import scripts as scr
from menu.modules.useful import fastCollector as fcol
from menu.modules.useful import cow

def usefulmenu():
    print("╭────────────────────────────────────────────╮\n"
          "│            П О Л Е З Н О С Т И             │\n"
          "│============================================│\n"
          "│ 1) Генератор паролей                       │\n"
          "│ 2) Случайные данные (имя, фамилия и тд.)   │\n"
          "│ 3) Скрипты                                 │\n"
          "│ 4) Быстрый сбор данных о системе           │\n"
          "│ 5) КОРОВА                                  │\n"
          "│ 0) Назад                                   │\n"
          "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите раздер: "))
        if usr_choose == 1:
            ran.rundata_func()
            choosing = False
        elif usr_choose == 2:
            scr.scripts_func()
            choosing = False
        elif usr_choose == 3:
            fcol.fastCollector_func
            choosing = False
        elif usr_choose == 4:
            cow.cow_func()
            choosing = False
        elif usr_choose == 0:
            main_menu.glavmenu()
        else:
            print("Вы ввели что-то неправильное")
