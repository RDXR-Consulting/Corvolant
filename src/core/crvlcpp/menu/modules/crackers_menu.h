#ifndef CRACKERS_MENU_H
#define CRACKERS_MENU_H

#include "crackers/bruteforce.h"
#include "crackers/fisher.h"


int usr_choose_crackers_act()
{
    std::cout << "Выберите инструмент: ";
    int usr_choose_crackers_var;  std::cin >> usr_choose_crackers_var;  std::cin.ignore(32767, '\n');
    return usr_choose_crackers_var;
}

int usr_choose_crackers()
{
    int user_choose_var = usr_choose_crackers_act();
    if(user_choose_var == 1)
    {
        bruteforce_func();
    }
    if(user_choose_var == 2)
    {
        fisher_func();
    }
    else
    {
        std::cout << "Error";
    }
    return 0;
}


void crackers()
{
    std::cout <<"\n╭────────────────────────────────────────────╮\n"
                "│             В З Л О М Щ И К И              │\n"
                "│============================================│\n"
                "│ 1) Брутфорс                                │\n"
                "│ 2) Фишер                                   │\n"
                "│ 3) Анализ сетей                            │\n"
                "│ 4) Ботнет                                  │\n"
                "│ 5) Генератор помех                         │\n"
                "│ 0) Назад                                   │\n"
                "╰────────────────────────────────────────────╯\n";
    usr_choose_crackers();
}


#endif
