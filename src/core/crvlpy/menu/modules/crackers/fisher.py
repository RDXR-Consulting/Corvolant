import webbrowser

def fisher_func_choose_act():
    print("Выберите сайт для фишинга:")
    fisher_func_choose_act = int(input())
    return fisher_func_choose_act

def fisher_func_choose():
    usr_choose_var = fisher_func_choose_act()
    urls = {
        1: "http://www.vk.com",
        2: "http://www.instagram.com",
        3: "http://www.store.steampowered.com",
        4: "http://www.youtube.com",
        5: "http://www.wildberries.ru/",
        6: "http://www.google.com"
    }
    if usr_choose_var in urls:
        webbrowser.open_new_tab(urls[usr_choose_var])
    else:
        print("Error")

def fisher_func():
    print("Выберите сайт:")
    print("1) VK")
    print("2) Instagram")
    print("3) Steam")
    print("4) Youtube")
    print("5) Wildberries")
    print("6) RDXR")
    fisher_func_choose()

fisher_func()
