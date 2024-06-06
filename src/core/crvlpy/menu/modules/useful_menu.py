from menu.modules.useful import randata as ran
from menu.modules.useful import scripts as scr
from menu.modules.useful import fastCollector as fcol
from menu.moduules.useful import cow

def usr_choose_useful_act():
    return int(input("Выберите инструмент: "))



def useful():
    print("╭────────────────────────────────────────────╮\n"
          "│            П О Л Е З Н О С Т И             │\n"
          "│============================================│\n"
          "│ 1) Случайные данные (имя, фамилия и тд.    │\n"
          "│ 2) Скрипты                                 │\n"
          "│ 3) Быстрый сбор данных о системе           │\n"
          "│ 4) КОРОВА                                  │\n"
          "│ 0) Выйти                                   │\n"
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
            exit()
        else:
            print("Вы ввели что-то неправильное")
