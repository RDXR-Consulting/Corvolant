abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passcode = "CFWWSWQ"
str = ""
found = False

# Рекурсивный брутфорс
def brut_rec(n):
    global found, str
    for i in range(len(abc)):
        str += abc[i]
        if n > 1:
            brut_rec(n - 1)
            if found:
                return
        if str == passcode:
            found = True
            break
        else:
            str = str[:-1]

# Функция для запуска брутфорса
def bruteforce_func():
    global found, str
    for rd in range(1, 11):  # Какие длины паролей перебирать
        brut_rec(rd)
        if found:
            break
    print(str)
    return 0