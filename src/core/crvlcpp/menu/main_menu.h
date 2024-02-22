#ifndef MAIN_MENU_H
#define MAIN_MENU_H

#include "modules/crackers_menu.h"
#include "modules/miners_menu.h"
#include "modules/spies_menu.h"
#include "modules/useful_menu.h"

using namespace std;

int usr_choose_menu_act()
{
  cout << "Выберите раздел: ";
  int usr_choose_menu_var; cin >> usr_choose_menu_var; cin.ignore(32767, '\n');
  return usr_choose_menu_var;
}

int usr_choose_menu()
{
  int user_choose_var = usr_choose_menu_act();
  switch(user_choose_var)
    {
      case 1:
        crackers();
        break;
      case 2:
        miners();
        break;
      case 3:
        spies();
        break;
      default:
        std::cout << "Error";
    }
    return 0;
}


int menu()
{
  //gui - запуск
  cout << "ГЛАВНОЕ МЕНЮ\n";
  cout << "1) Взломщики\n";
  cout << "2) Майнеры\n";
  cout << "3) Шпионы\n";
  cout << "4) Полезное\n";
  usr_choose_menu();
  return 0;
}

#endif
