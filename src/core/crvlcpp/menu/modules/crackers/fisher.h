#ifndef FISHER_H
#define FISHER_H


//system("start iexplore.exe \"www.cyberforum.ru\""); - мб пойдет как открывашка


int fisher_func_choose_act()
{
	std::cout << "Выберите сайт для фишинга:";
	int fisher_func_choose_act; std::cin >> fisher_func_choose_act; std::cin.ignore(32767, '\n');
	return fisher_func_choose_act; 
}

int fisher_func_choose()
{
	int usr_choose_var = fisher_func_choose_act();
    switch(usr_choose_var) {
        case 1:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT);
            break;
        default:
            std::cout << "Error";
    }
    return 0;
}

int fisher_func()
{
    std::cout << "poh";
    return 0;
}


#endif
