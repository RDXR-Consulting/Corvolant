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
    print("1) Случайные данные\n")
    print("2) В разработке\n")
    print("3) В разработке\n")
    usr_choose_useful()