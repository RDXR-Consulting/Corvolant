#DunastyC 5.03.24#
from menu.modules.spies import keylogger as keylog

def usr_choose_spies_act():
    return int(input("Выберите инструмент: "))

def usr_choose_spies():
    user_choose_var = usr_choose_spies_act()
    if user_choose_var == 1:
        keylog.keylogger_func()
    else:
        print('error')
        pass

def spies():
    print("╭────────────────────────────────────────────╮")
    print("│                Ш П И О Н Ы                 │")
    print("│============================================│")
    print("│ 1) Кейлоггер                               │")
    print("│ 2) Троян (черный ящик)                     │")
    print("│ 3) Поисковая лаборатория(список осинтинстру│")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_spies()
