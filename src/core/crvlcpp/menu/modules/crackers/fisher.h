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
    std::fstream vk;
    switch(usr_choose_var) {
        case 1:
            vk.open("vk.html");
            break;
        case 2:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT); //inst
            break;
        case 3:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT); //steam
            break;
        case 4:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT); //youtube
            break;
        case 5:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT); //wildberries
            break;
        case 6:
            ShellExecute(0, "open", "http://www.google.com", NULL, NULL, SW_SHOWDEFAULT); //rdxr
            break;
        default:
            std::cout << "Error";
    }
    return 0;
}

int fisher_func()
{
    std::cout << "Выберите сайт:\n";
    std::cout << "1) VK\n";
    std::cout << "2) Instagram\n";
    std::cout << "3) Steam\n";
    std::cout << "4) Youtube\n";
    std::cout << "5) Wildberries\n";
    std::cout << "6) RDXR\n";
    fisher_func_choose();
    return 0;
}

#endif
