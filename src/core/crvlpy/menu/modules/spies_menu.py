from menu.modules.spies import keylogger as keylog


def usr_choice_spies_act():
    return int(input("Выберите инструмент: "))


def usr_choice_spies():
    user_choice_var = usr_choice_spies_act()
    if user_choice_var == 1:
        keylog.keylogger_func()
    elif user_choice_var == 0:
        pass
    else:
        print('error')
        pass


def spies():
    print(
        "╭────────────────────────────────────────────╮\n"
        "│                Ш П И О Н Ы                 │\n"
        "│============================================│\n"
        "│ 1) Кейлоггер                               │\n"
        "│ 2) Троян (черный ящик)                     │\n"
        "│ 3) Поисковая лаборатория(список осинт)     │\n"
        "│ 0) Назад                                   │\n"
        "╰────────────────────────────────────────────╯\n")
    usr_choice_spies()
