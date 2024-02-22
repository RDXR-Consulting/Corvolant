#ifndef CRACKERS_MENU_H
#define CRACKERS_MENU_H

#include "crackers/bruteforce.h"

using namespace std;

int usr_choose_crackers_act()
{
    cout << "Выберите инструмент: ";
    int usr_choose_crackers_var; cin >> usr_choose_crackers_var; cin.ignore(32767, '\n');
    return usr_choose_crackers_var;
}

int usr_choose_crackers()
{
    int user_choose_var = usr_choose_crackers_act();
    switch(user_choose_var)
    {
        case 1:
            bruteforce_func();
            break;
        default:
            cout << "Error";
    }
    return 0;
}


void crackers()
{
    cout << "Брутфорс - 1\n";
    cout << "В разработке - 2\n";
    cout << "В разработке - 3\n";
    usr_choose_crackers();
}


#endif
