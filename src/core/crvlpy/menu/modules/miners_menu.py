from menu.modules.miners import autominer as mnr
from menu.modules.miners import transport as trp
from menu.modules.miners import asicminer as amr


def minermenu():
    print("╭────────────────────────────────────────────╮\n"
          "│              М А Й Н Е Р Ы                 │\n"
          "│============================================│\n"
          "│ 1) Автомайнер (вкл по нажатию автоматом    │\n"
          "│ 2) Переносчик (транспорт)                  │\n"
          "│ 3) ASIC - майнинг                          │\n"
          "│ 0) Назад                                   │\n"
          "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите раздел: "))
        if usr_choose == 1:
            mnr.autominer_func()
            choosing = False
        elif usr_choose == 2:
            trp.transport_func()
            choosing = False
        elif usr_choose == 3:
            amr.asicminer_func()
            choosing = False
        elif usr_choose == 0:
            exit()
        else:
            print("Вы ввели что то неправильное")
