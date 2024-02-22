#ifndef SPIES_MENU_H
#define SPIES_MENU_H

#include "spies/keylogger.h"

using namespace std;

int usr_choose_spies_act()
{
    cout << "Выберите инструмент: ";
    int usr_choose_spies_var; cin >> usr_choose_spies_var; cin.ignore(32767, '\n');
    return usr_choose_spies_var;
}

int usr_choose_spies()
{
    int user_choose_var = usr_choose_spies_act();
    switch(user_choose_var)
    {
        case 1:
            keylogger_func();
            break;
        default:
            cout << "Error";
    }
    return 0;
}


void spies()
{
  cout << "Кейлоггер - 1\n";
  cout << "В разработке - 2\n";
  cout << "В разработке - 3\n";
  usr_choose_spies();
}


#endif
