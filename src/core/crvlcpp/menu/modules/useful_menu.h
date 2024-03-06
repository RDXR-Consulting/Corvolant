#ifndef USEFUL_MENU_H
#define USEFUL_MENU_H

#include "useful/randata.h"


int usr_choose_useful_act()
{
    std::cout << "Выберите инструмент: ";
    int usr_choose_useful_var; std::cin >> usr_choose_useful_var; cin.ignore(32767, '\n');
    return usr_choose_useful_var;
}

int usr_choose_useful()
{
    int user_choose_var = usr_choose_useful_act();
    if(user_choose_var == 1)
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
    std::cout << "Случайные данные - 1\n";
    std::cout << "В разработке - 2\n";
    std::cout << "В разработке - 3\n";
  usr_choose_useful();
}


#endif
