// Стандартные библиотеки
#include <iostream>
#include <windows.h>

// Пользовательские библиотеки
#include "menu/main_menu.h"

// Пространства имен
using namespace std;

int main()
{
  SetConsoleCP(65001);
  SetConsoleOutputCP(65001);
  // запуск ГИ
  cout << "ПРИВЕТСТВИЕ\n";
  // Запуск меню
  menu();
  return 0;
}
