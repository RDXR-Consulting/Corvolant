#DunastyC 5.03.24#
from menu.modules.spies.keylogger import keylogger

def usr_choose_spies_act():
    return int(input("Выберите инструмент: "))

def usr_choose_spies():
    user_choose_var = usr_choose_spies_act()
    if user_choose_var == 1:
        keylogger()
    else:
        print("Error")

def spies():
    print("Кейлоггер - 1")
    print("В разработке - 2")
    print("В разработке - 3")
    usr_choose_spies()

spies()