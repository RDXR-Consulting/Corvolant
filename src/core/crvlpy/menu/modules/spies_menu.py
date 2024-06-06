from menu.modules.spies import keylogger as keylog
from menu.modules.spies import blackBox as box
from menu.modules.spies import osint


def usr_choice_spies_act():
    return int(input("Выберите инструмент: "))


def spiesmenu():
    print(
        "╭────────────────────────────────────────────╮\n"
        "│                Ш П И О Н Ы                 │\n"
        "│============================================│\n"
        "│ 1) Кейлоггер                               │\n"
        "│ 2) Троян (черный ящик)                     │\n"
        "│ 3) Поисковая лаборатория(список осинт)     │\n"
        "│ 0) Выйти                                   │\n"
        "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите раздел: "))
    if usr_choose == 1:
        keylog.keylogger_func()
        choosing = False
    elif usr_choose == 2:
        box.blackBox_func
        choosing = False
    elif usr_choose == 3:
        osint.osint_func()
        choosing = False
    elif usr_choose == 0:
        exit()
    else:
        print("Вы ввели что-то неправильное")
