#DunastyC 5.03.24#
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
    print("Брутфорс - 1")
    print("Фишер - 2")
    print("В разработке - 3")
    usr_choose_crackers()

crackers()