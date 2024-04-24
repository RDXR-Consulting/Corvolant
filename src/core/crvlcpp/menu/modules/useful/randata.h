#ifndef RANDATA_H
#define RANDATA_H


int usr_choose_country_act()
{
    std::cout << "Укажите государство/национальность: ";
    int usr_choose_country_var; cin >> usr_choose_country_var; cin.ignore(32767, '\n');
    return usr_choose_country_var;
}

int usr_choose_age_act()
{
    std::cout << "Укажите возраст: ";
    int usr_choose_country_var; cin >> usr_choose_country_var; cin.ignore(32767, '\n');
    return usr_choose_country_var;
}

int usr_choose_occupation_act()
{
    std::cout << "Укажите возраст: ";
    int usr_choose_occupation_var; cin >> usr_choose_occupation_var; cin.ignore(32767, '\n');
    return usr_choose_occupation_var;
}



int randata_func()
{
    cout << "Россия - 1\n"
            "Америка - 2\n"
            "Китай - 3\n"
            "Европа - 4\n"
    int user_choose_country_var = usr_choose_country_act();

    cout << "(15 - 25 лет) - 1\n"
            "(25 - 35 лет) - 2\n"
            "(35 - 45 лет) - 3\n"
            "(45 - 55 лет) - 4\n"
    int user_choose_age_var = usr_choose_age_act();

}

#endif
