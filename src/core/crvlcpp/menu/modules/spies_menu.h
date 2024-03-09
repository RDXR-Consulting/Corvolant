#ifndef SPIES_MENU_H
#define SPIES_MENU_H

#include "spies/keylogger.h"


int usr_choose_spies_act()
{
    std::cout << "Выберите инструмент: ";
    int usr_choose_spies_var;  std::cin >> usr_choose_spies_var; cin.ignore(32767, '\n');
    return usr_choose_spies_var;
}

int usr_choose_spies()
{
    int usr_choose_var = usr_choose_spies_act();
    if(usr_choose_var == 1)
    {
        keylogger_func();
    }
    else
    {
        std::cout << "Error";
    }
    return 0;
}


void spies()
{
    std::cout <<"\n╭────────────────────────────────────────────╮\n";
    std::cout <<"│                  Ш П И О Н Ы               │\n";
    std::cout <<"│============================================│\n";
    std::cout <<"│ 1) Кейлоггер                               │\n";
    std::cout <<"│ 2) В разработке                            │\n";
    std::cout <<"│ 3) В разработке                            │\n";
    std::cout <<"│                                            │\n";
    std::cout <<"╰────────────────────────────────────────────╯\n";
    usr_choose_spies();
}


#endif
