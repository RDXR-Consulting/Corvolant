from modules import crackers_menu as crack, miners_menu as mine, spies_menu as spy

def usr_choose_menu_act():
    usr_choose_menu = input(int("Выберите раздел:\n"))

usr_choose = usr_choose_menu_act()
def usr_choose_menu():
    if usr_choose == 1:
        crack.crackers()
    if usr_choose == 2:
        mine.miners()
    if usr_choose == 3:
        spy.spies()
def menu():
    print("ГЛАВНОЕ МЕНЮ\n")
    print("1) Взломщики\n")
    print("2) Майнеры\n")
    print("3) Шпионы\n")
    usr_choose_menu()
    return 0
