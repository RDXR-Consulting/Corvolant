#from menu.modules.miners import 


def usr_choose_miners_act():
    return int(input("Выберите инструмент: "))

def usr_choose_miners():
    user_choice_var = usr_choose_miners_act()
    if user_choice_var == 1:
        pass
    if user_choice_var == 2:
        pass
    if user_choice_var == 3:
        pass

def miners():
    print("╭────────────────────────────────────────────╮")
    print("│              М А Й Н Е Р Ы                 │")
    print("│============================================│")
    print("│ 1) Автомайнер (вкл по нажатию автоматом    │")
    print("│ 2) Переносчик                              │")
    print("│ 3) ASIC - майнинг                          │")
    print("│                                            │")
    print("╰────────────────────────────────────────────╯\n")
    usr_choose_miners()
    
