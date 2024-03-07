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
    std::cout <<"\n╭────────────────────────────────────────────╮\n";
    std::cout <<"│             В З Л О М Щ И К И              │\n";
    std::cout <<"│============================================│\n";
    std::cout <<"│ 1) Брутфорс                                │\n";
    std::cout <<"│ 2) Фишер                                   │\n";
    std::cout <<"│ 3) В разработке                            │\n";
    std::cout <<"│                                            │\n";
    std::cout <<"╰────────────────────────────────────────────╯\n";
    usr_choose_crackers();
}


#endif
