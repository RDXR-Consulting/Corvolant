#ifndef CRVL_KEYGEN_H
#define CRVL_KEYGEN_H

#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <string>

// - - - - - - - - - - - - - - - - - - - - - - - - - Используемые символы - - - - - - - - - - - - - - - - - - - - - - - - - //

// Буквы в нижнем регистре
std::string sb0 = "a"; std::string sb1 = "b"; std::string sb2 = "c"; std::string sb3 = "d"; std::string sb4 = "e"; std::string sb5 = "f"; std::string sb6 = "g"; std::string sb7 = "h"; std::string sb8 = "i"; std::string sb9 = "j";
std::string sb10 = "k"; std::string sb11 = "l"; std::string sb12 = "m"; std::string sb13 = "n"; std::string sb14 = "o"; std::string sb15 = "p"; std::string sb16 = "q"; std::string sb17 = "r"; std::string sb18 = "s"; std::string sb19 = "t";
std::string sb20 = "u"; std::string sb21 = "v"; std::string sb22 = "w"; std::string sb23 = "y"; std::string sb24 = "z";
// Буквы в верхнем регистре
std::string u_sb0 = "A"; std::string u_sb1 = "B"; std::string u_sb2 = "C"; std::string u_sb3 = "D"; std::string u_sb4 = "E"; std::string u_sb5 = "F"; std::string u_sb6 = "G"; std::string u_sb7 = "H"; std::string u_sb8 = "I"; std::string u_sb9 = "J";
std::string u_sb10 = "K"; std::string u_sb11 = "L"; std::string u_sb12 = "M"; std::string u_sb13 = "N"; std::string u_sb14 = "O"; std::string u_sb15 = "P"; std::string u_sb16 = "Q"; std::string u_sb17 = "R"; std::string u_sb18 = "S"; std::string u_sb19 = "T";
std::string u_sb20 = "U"; std::string u_sb21 = "V"; std::string u_sb22 = "W"; std::string u_sb23 = "Y"; std::string u_sb24 = "Z";
// Цифры
std::string nb0 ="0"; std::string nb1 ="1"; std::string nb2 ="2"; std::string nb3 ="3"; std::string nb4 ="4"; std::string nb5 ="5"; std::string nb6 ="6"; std::string nb7 ="7"; std::string nb8 ="8"; std::string nb9 ="9";
// Специальные символы
std::string sp = "#"; std::string dr = "$"; std::string pt = "%"; std::string ad = "&"; std::string qtMk = "'"; std::string oPs = "("; std::string cOps = ")"; std::string  sr = "*"; std::string ps = "+";
std::string cma = ","; std::string mn = "-"; std::string dt = "."; std::string sh = "/"; std::string oSqrBt = "["; std::string cSqrBt = "]"; std::string cn = ":"; std::string sn = ";"; std::string msn = ">";
std::string lts = "<"; std::string qMk = "?"; std::string els = "="; std::string at = "@"; std::string dgr = "^"; std::string ulg = "_"; std::string  ahe = "`";  std::string oBc = "{"; std::string cBc = "}";
std::string cr = "|"; std::string tde = "~";

// - - - - - - - - - - - - - - - - - - - - - - - - - -  Словари символов - - - - - - - - - - - - - - - - - - - - - - - - - - //

std::string lc_dictionary[25] = // нРег
        {
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24
        };

std::string uc_dictionary[25] = // вРег
        {
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24
        };

std::string n_dictionary[10] = // цифр
        {
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9
        };

std::string ss_dictionary[30] = // спецСимвол
        {
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string lcUc_dictionary[50] = // нРег + вРег
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24
        };

std::string lcN_dictionary[35] = // нРег + цифр
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9
        };

std::string lcSs_dictionary[55] = // нРег + спецСмвл
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Специальные символы
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string lcUcN_dictionary[60] = // нРег + вРег + цифр
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9
        };

std::string lcUcSs_dictionary[80] = // нРег + вРег + спецСмвл
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string lcNSs_dictionary[65] = // нРег + цифр + спецСмвл
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9,
                // Специальные символы
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string  ucN_dictionary[35] = // вРег + цифр
        {
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9
        };

std::string ucSs_dictionary[55] = // вРег + спецСмвл
        {
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                // Специальные символы
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string ucNSs_dictionary[65] = // вРег + цифр + спецСмвл
        {
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9,
                // Специальные символы
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };

std::string lcUcNSs_dictionary[90] = //нРег + вРег + цифр + спецСмвл
        {
                // Буквы в нижнем регистре
                sb0, sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8, sb9, sb10, sb11, sb12, sb13, sb14, sb15, sb16,
                sb17, sb18, sb19, sb20, sb21, sb22, sb23, sb24,
                // Буквы в верхнем регистре
                u_sb0, u_sb1, u_sb2, u_sb3, u_sb4, u_sb5, u_sb6, u_sb7, u_sb8, u_sb9, u_sb10, u_sb11, u_sb12,
                u_sb13, u_sb14, u_sb15, u_sb16, u_sb17, u_sb18, u_sb19, u_sb20, u_sb21, u_sb22, u_sb23, u_sb24,
                // Цифры
                nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9,
                // Специальные символы
                sp, dr, pt, ad, qtMk, oPs, cOps, cOps, sr, ps, cma, mn, dt, sh, oSqrBt, cSqrBt, cn, sn, msn,
                lts, qMk, els, at, dgr, ulg, ahe, oBc, cBc, cr, tde
        };






// - - - - - - - - - - - - - - - - - - - - - - - - - Генератор паролей - - - - - - - - - - - - - - - - - - - - - - - - - - - //


int usr_choose_keygen_act_length()
{
    std::cout << "Укажите количество символов в пароле: ";
    int usr_choose_keygen_length; std::cin >> usr_choose_keygen_length;
    return usr_choose_keygen_length;
}

int usr_choose_keygen_act_lowcase()
{
    std::cout << "Укажите используемые символы\n 0 - не использовать, 1 - использовать \n";
    std::cout << "Символы в нижнем регистре: ";
    int usr_choose_keygen_lowcase; std::cin >> usr_choose_keygen_lowcase; cin.ignore(32766, '\n');
    return usr_choose_keygen_lowcase;
}

int usr_choose_keygen_act_upcase()
{
    std::cout << "Символы в верхнем регистре: ";
    int usr_choose_keygen_upcase; std::cin >> usr_choose_keygen_upcase; cin.ignore(32766, '\n');
    return usr_choose_keygen_upcase;
}

int usr_choose_keygen_act_nums()
{
    std::cout << "Цифры: ";
    int usr_choose_keygen_nums; std::cin >> usr_choose_keygen_nums; cin.ignore(32766, '\n');
    return usr_choose_keygen_nums;
}

int usr_choose_keygen_act_specsyms()
{
    std::cout << "Специальные символы (!, *, /): ";
    int usr_choose_keygen_specsyms; std::cin >> usr_choose_keygen_specsyms; cin.ignore(32766, '\n');
    return usr_choose_keygen_specsyms;
}

int lc_keygen() // нРег
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lc_dictionary[rand() % 25];
        std::cout << password[i];
    }
}

int uc_keygen() // вРег
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = uc_dictionary[rand() % 25];
        std::cout << password[i];
    }
}

int n_keygen() // цифр
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = n_dictionary[rand() % 25];
        std::cout << password[i];
    }
}

int ss_keygen() // цифр
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = ss_dictionary[rand() % 25];
        std::cout << password[i];
    }
}

int lcUc_keygen() // нРег + вРег
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcUc_dictionary[rand() % 50];
        std::cout << password[i];
    }
}

int lcN_keygen() // нРег + цифр
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcN_dictionary[rand() % 35];
        std::cout << password[i];
    }
}

int lcSs_keygen() // нРег + спецСмвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcSs_dictionary[rand() % 55];
        std::cout << password[i];
    }
}

int lcUcN_Keygen() // нРег + вРег + цифр
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcUcN_dictionary[rand() % 60];
        std::cout << password[i];
    }
}

int lcUcSs_keygen() // нРег + вРег + спецСмвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcUcSs_dictionary[rand() % 80];
        std::cout << password[i];
    }
}

int lcNSs_keygen() //нРег + цифр + спецСмвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcNSs_dictionary[rand() % 65];
        std::cout << password[i];
    }
}

int ucN_keygen() // нРег + цифр
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = ucN_dictionary[rand() % 35];
        std::cout << password[i];
    }
}

int ucSs_keygen() // вРег + спецСмвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = ucSs_dictionary[rand() % 55];
        std::cout << password[i];
    }
}

int ucNSs_keygen() // вРег + цифр + спецСимвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = ucNSs_dictionary[rand() % 65];
        std::cout << password[i];
    }
}

int lcUcNSs_keygen() // нРег + вРег + цифр + спецСимвл
{
    srand(time(nullptr));
    int usr_choose_length = usr_choose_keygen_act_length();
    std::string password [usr_choose_length];
    for(int i = 0; i < usr_choose_length; i++)
    {
        password[i] = lcUcNSs_dictionary[rand() % 90];
        std::cout << password[i];

    }

    return 0;
}

//------------------------

int usr_choose_keygen()
{
    cout << "обсада";

    int usr_choose_lowcase = usr_choose_keygen_act_lowcase();   // нРег
    int usr_choose_upcase = usr_choose_keygen_act_upcase();     // вРег
    int usr_choose_nums = usr_choose_keygen_act_nums();         // цифр
    int usr_choose_specsyms = usr_choose_keygen_act_specsyms(); // спецСимв

    if(usr_choose_lowcase == 1)
    {
        lc_keygen();
    }

    else if(usr_choose_upcase == 1)
    {
        uc_keygen();
    }

    else if(usr_choose_nums == 1)
    {
        n_keygen();
    }

    else if(usr_choose_specsyms == 1)
    {
        ss_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_upcase == 1) // нРег + вРег
    {
        lcUc_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_nums == 1) // нРег + цифр
    {
        lcN_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_specsyms == 1) //нРег + спецСимвол
    {
        lcSs_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_upcase == 1 && usr_choose_nums == 1) // нРег + вРег + цифр
    {
        lcUcN_Keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_upcase == 1 && usr_choose_specsyms == 1) //нРег + вРег + спецСимвол
    {
        lcUcSs_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_upcase == 1 && usr_choose_specsyms == 1) // нРег + цифр + спецСимвол
    {
        lcNSs_keygen();
    }

    else if(usr_choose_upcase == 1 && usr_choose_nums == 1) // вРег + цифр
    {
        ucN_keygen();
    }

    else if(usr_choose_upcase == 1 && usr_choose_specsyms == 1 )     // вРег + спецСимвол
    {
        ucSs_keygen();
    }

    else if(usr_choose_upcase == 1 && usr_choose_nums == 1 && usr_choose_specsyms == 1)    // вРег + цифр + спецСимвол
    {
        ucNSs_keygen();
    }

    else if(usr_choose_lowcase == 1 && usr_choose_upcase == 1 && usr_choose_nums == 1 && usr_choose_specsyms == 1) // нРег + вРег + цифр + спецСимвол
    {
        lcUcNSs_keygen();
    }

    else
    {
        std::cout << "\nОшибка!";
    }
}

int keygen_func()
{
    usr_choose_keygen();
    return 0;
}

#endif
