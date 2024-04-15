from menu.modules.crackers import bruteforce as brut
from menu.modules.crackers import fisher as fish


def usr_choose_crackers_act():
    return int(input("Выберите инструмент: "))

def usr_choose_crackers():
    user_choose_var = usr_choose_crackers_act()
    if user_choose_var == 1:
        brut.bruteforce_func()
    elif user_choose_var == 2:
        fish.fisher_func()
    else:
        print("Error")

def crackers():
    print("╭────────────────────────────────────────────╮")
    print("│             В З Л О М Щ И К И              │")
    print("│============================================│")
    print("│ 1) Брутфорс                                │")
    print("│ 2) Фишер                                   │")
    print("│ 3) Анализ сетей                            │")
    print("│ 4) Ботнет (кукольный театр ддос + реверс)  │")
    print("│ 5) Генератор помех (сети и реверс)         │")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_crackers()
