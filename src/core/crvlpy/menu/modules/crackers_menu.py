from menu.modules.crackers import bruteforce as brut
from menu.modules.crackers import fisher as fish

from src.core.crvlpy.menu.main_menu import menu


def usr_choice_crackers_act():
    return int(input("Выберите инструмент: "))


def usr_choice_crackers():
    user_choice_var = usr_choice_crackers_act()
    if user_choice_var == 1:
        brut.bruteforce_func()
    elif user_choice_var == 2:
        fish.fisher_func()
    elif user_choice_var == 0:
        menu()
    else:
        print("Error")


def crackers():
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
    usr_choice_crackers()
