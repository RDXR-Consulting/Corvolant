#DunastyC 5.03.24#
from cracker.bruteforce import bruteforce
from cracker.fisher import fisher

def usr_choose_crackers_act():
    return int(input("Выберите инструмент: "))

def usr_choose_crackers():
    user_choose_var = usr_choose_crackers_act()
    if user_choose_var == 1:
        bruteforce()
    elif user_choose_var == 2:
        fisher()
    else:
        print("Error")

def crackers():
    print("Брутфорс - 1")
    print("Фишер - 2")
    print("В разработке - 3")
    usr_choose_crackers()

crackers()