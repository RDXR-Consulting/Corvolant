import random

def generate_password(length, include_special_chars, include_lowercase_letters, include_uppercase_letters, include_numbers):
    # Символы
    numbers = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "#$%&'()*+,-./:;<=>?@^_`{|}~"
    chars = ""
    # Создание списка символов в зависимости от включения специальных символов
    if include_special_chars:
        chars += special_chars
    if include_lowercase_letters:
        chars += lowercase_letters
    if include_uppercase_letters:
        chars += uppercase_letters
    if include_numbers:
        chars += numbers

    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
    return password

def keygen_func():
    length = int(input('Введите длинну:'))
    include_special_chars = False
    include_lowercase_letters = True
    include_uppercase_letters = False
    include_numbers = False

    password = generate_password(length, include_special_chars, include_lowercase_letters, include_uppercase_letters, include_numbers)
    return length, include_special_chars, include_lowercase_letters, include_uppercase_letters, include_numbers