#ifndef USEFUL_MENU_H
#define USEFUL_MENU_H

#include "useful/randata.h"

using namespace std;

int usr_choose_useful_act()
{
    cout << "Выберите инструмент: ";
    int usr_choose_useful_var; cin >> usr_choose_useful_var; cin.ignore(32767, '\n');
    return usr_choose_useful_var;
}

int usr_choose_useful()
{
    int user_choose_var = usr_choose_useful_act();
    switch(user_choose_var)
    {
        case 1:
            randata_func();
            break;
        default:
            cout << "Error";
    }
    return 0;
}


void useful()
{
  cout << "Случайные данные - 1\n";
  cout << "В разработке - 2\n";
  cout << "В разработке - 3\n";
  usr_choose_useful();
}


#endif

