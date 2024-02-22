#ifndef BRUTEFORCE_H
#define BRUTEFORCE_H

#include <iostream>
#include <string>
#include <vector>
#include <ctime>

std::string abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", pass = "CFWWSWQ";
std::string str;
bool found = false;

// рекурсивный брут
void BrutRec(int n)
{
    for (int i = 0; i < abc.size(); ++i)
    {
        str.push_back(abc[i]);
        if (n > 1)
        {
            BrutRec(n - 1);
            if (found)
            {
                return;
            }
        }
        if (str == pass)
        {
            found = true;
            break;
        }
        else
        {
            str.pop_back();
        }
    }
}


int bruteforce_func() {
#if 1
    for (int rd = 1; rd <= 10; ++rd) // какие длины паролей перебирать
    {
        BrutRec(rd);
        if (found) {
            break;
        }
    }
    std::cout << str << std::endl;
    return 0;
}
#endif
#endif
