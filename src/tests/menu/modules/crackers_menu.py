#DunastyC 5.03.24#
from menu.modules.crackers import bruteforce as brut
from menu.modules.crackers import fisher as fish
from art import tprint

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
    tprint("Взломщики")
    print("╭────────────────────────────────────────────╮")
    print("│             В З Л О М Щ И К И              │")
    print("│                                            │")
    print("│ 1) Брутфорс                                │")
    print("│ 2) Фишер                                   │")
    print("│ 3) В разработке                            │")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_crackers()