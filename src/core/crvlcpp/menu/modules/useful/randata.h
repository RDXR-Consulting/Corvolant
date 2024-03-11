#ifndef RANDATA_H
#define RANDATA_H

#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#include <iostream>
#include <string>

#include <ctime>
#include <cstdlib>

using namespace std;


int randata_func()
{
    srand(time(nullptr));//<--
    string nb0 ="0"; string nb1 ="1"; string nb2 ="2"; string nb3 ="3"; string nb4 ="4"; string nb5 ="5"; string nb6 ="6"; string nb7 ="7"; string nb8 ="8"; string nb9 ="9";


    string sb0 = "a"; string sb1 = "b"; string sb2 = "c"; string sb3 = "d"; string sb4 = "e"; string sb5 = "f"; string sb6 = "g"; string sb7 = "h"; string sb8 = "i"; string sb9 = "j";
    string sb10 = "k"; string sb11 = "l"; string sb12 = "m"; string sb13 = "n"; string sb14 = "o"; string sb15 = "p"; string sb16 = "q"; string sb17 = "r"; string sb18 = "s"; string sb19 = "t";
    string sb20 = "u"; string sb21 = "v"; string sb22 = "w"; string sb23 = "y"; string sb24 = "z";

    string u_sb0 = "A"; string u_sb1 = "B"; string u_sb2 = "C"; string u_sb3 = "D"; string u_sb4 = "E"; string u_sb5 = "F"; string u_sb6 = "G"; string u_sb7 = "H"; string u_sb8 = "I"; string u_sb9 = "J";
    string u_sb10 = "K"; string u_sb11 = "L"; string u_sb12 = "M"; string u_sb13 = "N"; string u_sb14 = "O"; string u_sb15 = "P"; string u_sb16 = "Q"; string u_sb17 = "R"; string u_sb18 = "S"; string u_sb19 = "T";
    string u_sb20 = "U"; string u_sb21 = "V"; string u_sb22 = "W"; string u_sb23 = "Y"; string u_sb24 = "Z";

    string arr[45] = {
            nb0,nb1,nb2,nb3,nb4,nb5,nb6,nb7,nb8,nb9,sb0,sb1,sb2,sb3,sb4,sb5,sb6,sb7,sb8,sb9,sb10,sb11,sb12,sb13,sb14,sb15,sb16,sb17,sb18,sb19,sb20,sb21,sb22,sb23,sb24};


    string password[45];
    for(int i = 0; i<45; i++)

        password[i] = arr[rand() % 45 ];
    for(int i = 0; i < 45; i++)
        cout << password[i];

    return 0;
}


#endif
