#ifndef RANDATA_H
#define RANDATA_H

#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#include <iostream>
#include <string>

#include <ctime>
#include <cstdlib>




int randata_func()
{
   srand(time(nullptr));
    // ----- Словарь символов -----
    // Цифры
    string nb0 ="0"; string nb1 ="1"; string nb2 ="2"; string nb3 ="3"; string nb4 ="4"; string nb5 ="5"; string nb6 ="6"; string nb7 ="7"; string nb8 ="8"; string nb9 ="9";
    // Буквы в нижнем регистре
    string sb0 = "a"; string sb1 = "b"; string sb2 = "c"; string sb3 = "d"; string sb4 = "e"; string sb5 = "f"; string sb6 = "g"; string sb7 = "h"; string sb8 = "i"; string sb9 = "j";
    string sb10 = "k"; string sb11 = "l"; string sb12 = "m"; string sb13 = "n"; string sb14 = "o"; string sb15 = "p"; string sb16 = "q"; string sb17 = "r"; string sb18 = "s"; string sb19 = "t";
    string sb20 = "u"; string sb21 = "v"; string sb22 = "w"; string sb23 = "y"; string sb24 = "z";
    // Буквы в верхнем регистре
    string u_sb0 = "A"; string u_sb1 = "B"; string u_sb2 = "C"; string u_sb3 = "D"; string u_sb4 = "E"; string u_sb5 = "F"; string u_sb6 = "G"; string u_sb7 = "H"; string u_sb8 = "I"; string u_sb9 = "J";
    string u_sb10 = "K"; string u_sb11 = "L"; string u_sb12 = "M"; string u_sb13 = "N"; string u_sb14 = "O"; string u_sb15 = "P"; string u_sb16 = "Q"; string u_sb17 = "R"; string u_sb18 = "S"; string u_sb19 = "T";
    string u_sb20 = "U"; string u_sb21 = "V"; string u_sb22 = "W"; string u_sb23 = "Y"; string u_sb24 = "Z";
    // Специальные символы
    string sp = "#"; string dr = "$"; string pt = "%"; string ad = "&"; string qtMk = "'"; string oPs = "("; string cOps = ")"; string  sr = "*"; string ps = "+";
    string cma = ","; string mn = "-"; string dt = "."; string sh = "/"; string oSqrBt = "["; string cSqrBt = "]"; string cn = ":"; string sn = ";"; string msn = ">";
    string lts = "<"; string qMk = "?"; string els = "="; string at = "@"; string dgr = "^"; string ulg = "_"; string  ahe = "`";  string oBc = "{"; string cBc = "}";
    string cr = "|"; string tde = "~";

    // ----- Подключение словаря символов -----
    string arr[90] =
            {       // Цифры
                    nb0,nb1,nb2,nb3,nb4,nb5,nb6,nb7,nb8,nb9,
                    // Буквы в нижнем регистре
                    sb0,sb1,sb2,sb3,sb4,sb5,sb6,sb7,sb8,sb9,sb10,sb11,sb12,sb13,sb14,sb15,sb16,sb17,sb18,sb19,sb20,sb21,sb22,sb23,sb24,
                    // Буквы в верхнем регистре
                    u_sb0,u_sb1,u_sb2,u_sb3,u_sb4,u_sb5,u_sb6,u_sb7,u_sb8,u_sb9,u_sb10,u_sb11,u_sb12,u_sb13,u_sb14,u_sb15,u_sb16,u_sb17,u_sb18,u_sb19,u_sb20,u_sb21,u_sb22,u_sb23,u_sb24,
                    // Специальные символы
                    sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn, lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
            };

    string password[90];
    for(int i = 0; i<90; i++)

        password[i] = arr[rand() % 90 ];
    for(int i = 0; i < 90; i++)
        std::cout << password[i];

    return 0;
}


#endif
