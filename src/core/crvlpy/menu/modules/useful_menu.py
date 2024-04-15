from menu.modules.useful import rundata as run


def usr_choose_useful_act():
    return int(input("Выберите инструмент: "))


def usr_choose_useful():
    user_choice_var = usr_choose_useful_act()
    if user_choice_var == 1:
        run.rundata_func()
    if user_choice_var == 2:
        pass
    if user_choice_var == 3:
        pass


def useful():
    print("╭────────────────────────────────────────────╮")
    print("│            П О Л Е З Н О С Т И             │")
    print("│============================================│")
    print("│ 1) Случайные данные (имя, фамилия и тд.    │")
    print("│ 2) Скрипты                                 │")
    print("│ 3) Быстрый сбор данных о системе           │")
    print("│ 4) КОРОВА                                  │")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_useful()
