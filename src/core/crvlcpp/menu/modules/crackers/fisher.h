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
    std::fstream inst;
    std::fstream steam;
    std::fstream yt;
    std::fstream wb;
    std::fstream rdxr;
    switch(usr_choose_var)
    {
        case 1:
            vk.open("vk.txt");
            ShellExecute(0, "open", "http://www.vk.com", NULL, NULL, SW_SHOWDEFAULT); //inst
            break;
        case 2:
            inst.open("inst.html");
            ShellExecute(0, "open", "http://www.instagram.com", NULL, NULL, SW_SHOWDEFAULT); //inst
            break;
        case 3:
            steam.open("steam.html");
            ShellExecute(0, "open", "http://www.store.steampowered.com", NULL, NULL, SW_SHOWDEFAULT); //steam
            break;
        case 4:
            yt.open("yt.html");
            ShellExecute(0, "open", "http://www.youtube.com", NULL, NULL, SW_SHOWDEFAULT); //youtube
            break;
        case 5:
            wb.open("wb.html");
            ShellExecute(0, "open", "http://www.wildberries.ru/", NULL, NULL, SW_SHOWDEFAULT); //wildberries
            break;
        case 6:
            rdxr.open("rdxr.html");
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
