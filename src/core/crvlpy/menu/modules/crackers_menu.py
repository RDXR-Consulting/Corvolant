from menu.modules.crackers import bruteforce as brut
from menu.modules.crackers import fisher as fish

from src.core.crvlpy.menu.main_menu import menu


def usr_choose_crackers_act():
    return int(input("Выберите инструмент: "))


def usr_choose_crackers():
    user_choose_var = usr_choose_crackers_act()
    if user_choose_var == 1:
        brut.bruteforce_func()
    elif user_choose_var == 2:
        fish.fisher_func()
    elif user_choose_var == 0:
        menu()
    else:
        print("Error")


def crackers():
    print("╭────────────────────────────────────────────╮\n│             В З Л О М Щ И К И              "
          "│\n│============================================│\n│ 1) Брутфорс                                │\n│ 2) "
          "Фишер                                   │\n│ 3) Анализ сетей                            │\n│ 4) Ботнет ("
          "кукольный театр ддос + реверс)  │\n│ 5) Генератор помех (сети и реверс)         │\n│ 0) Назад              "
          "                     │\n│                                            "
          "│\n╰────────────────────────────────────────────╯\n")
    usr_choose_crackers()
