#include <iostream>
#include <windows.h>

#include "menu/main_menu.h"

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
