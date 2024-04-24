#ifndef USEFUL_MENU_H
#define USEFUL_MENU_H

#include "useful/randata.h"
#include "useful/keygen.h"


int usr_choose_useful_act()
{
    std::cout << "Выберите инструмент: ";
    int usr_choose_useful_var; std::cin >> usr_choose_useful_var; cin.ignore(32766, '\n');
    return usr_choose_useful_var;
}

int usr_choose_useful()
{
    int user_choose_var = usr_choose_useful_act();
    if(user_choose_var == 1)
    {
        keygen_func();
    }
    if(user_choose_var == 2)
    {
        randata_func();
    }
    else
    {
        std::cout << "Error";
    }

    return 0;
}


void useful()
{
std::cout <<"\n╭────────────────────────────────────────────╮\n"
            "│               П О Л Е З Н О Е              │\n"
            "│============================================│\n"
            "│ 1) Генератор паролей                       │\n"
            "│ 1) Случайные данные                        │\n"
            "│ 2) Скрипты                                 │\n"
            "│ 3) Быстрый сбор данных о системе           │\n"
            "│ 4) КОРОВА                                  |\n"
            "╰────────────────────────────────────────────╯\n";
    usr_choose_useful();
}


#endif

