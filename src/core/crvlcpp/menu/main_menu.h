#ifndef MAIN_MENU_H
#define MAIN_MENU_H

#include "modules/crackers_menu.h"
#include "modules/miners_menu.h"
#include "modules/spies_menu.h"
#include "modules/useful_menu.h"


int usr_choose_menu_act()
{
  std::cout << "Выберите раздел: ";
  int usr_choose_menu_var; cin >> usr_choose_menu_var; cin.ignore(32767, '\n');
  return usr_choose_menu_var;
}

int usr_choose_menu()
{
  int user_choose_var = usr_choose_menu_act();
  if(user_choose_var ==1)
  {
      crackers();
  }
  if(user_choose_var ==2)
  {
      miners();
  }
  if(user_choose_var ==3)
  {
      spies();
  }
  if(user_choose_var ==4)
  {
      useful();
  }
  else
  {
      std::cout << "Error";
  }
    return 0;
}


int menu()
{
  //gui - запуск
  std::cout <<"╭────────────────────────────────────────────╮\n"
              "│          Г Л А В Н О Е    М Е Н Ю          │\n"
              "│============================================│\n"
              "│ 1) Взломщики                               │\n"
              "│ 2) Майнеры                                 │\n"
              "│ 3) Шпионы                                  │\n"
              "│ 4) Полезности                              │"
              "\n│                                            │\n"
              "╰────────────────────────────────────────────╯\n";
  usr_choose_menu();
  return 0;
}

#endif
