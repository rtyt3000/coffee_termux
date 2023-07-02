import os
import random
import time
import string


def wellcome():
    os.system("clear")
    print(
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠿⠿⠛⠛⠋⠉⠛⠛⠻⠿⠿⣿⣿⣿⣿\n⣿⣿⣿⠀⠐⠾⠿⠷⠶⠶⠶⠶⠾⠿⠷⠒⠀⣿⣿⣿\n⣿⣿⣿⡆⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠈⠁⠀⣉⡉⢻\n"
        "⣿⣿⣿⣷⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠤⠐⣸⠿⢃⣼\n⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣾⣿⣿\n⡿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⢿\n⣷⣤⣀⠀⠀⠀⠉⠙⠒⠂⠀⠒⠋⠉⠀⠀⢀⣀⣤⣾\n⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿")
    time.sleep(1)
    os.system("clear")


def print_menu():
    print("1. Открыть одноразовый почтовый ящик")
    print("2. Сгенерировать пароль")
    print('3. Проверить пароль')
    # Добавьте остальные пункты меню здесь


def handle_menu_choice(choice):
    if choice == '1':
        open_temp_mail()
    elif choice == '2':
        generate_password()
    elif choice == '3':
        check_password()


def open_temp_mail():
    while True:
        print("https://tempail.com/ru")
        print("0. Выход")
        choice = input("Введите номер пункта: ")
        if choice == "0":
            os.system("clear")
            break


def generate_password():
    length = input("Введите длину пароля: ")
    try:
        length = int(length)
        password = generate_password_string(length)
        os.system("clear")
        time.sleep(1)
        print(f"Сгенерированный пароль: {password}")
        time.sleep(1)
    except ValueError:
        print("Некорректная длина пароля.")


def generate_password_string(length):
    if length < 1 or length > 150:
        return "Длина пароля должна быть от 1 до 150 символов."
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password


def check_password():
    while True:
        print('Проверьте свой пароль')
        print("0. Выход")
        password_check_input = input("Введите номер пункта: ")
        if password_check_input == "0":
            os.system("clear")
            break
        elif password_check_input != "0":
            print(check_password_strength(password_check_input))
            os.system("clear")
            break


def check_password_strength(password):
    score = 0
    criteria = {
        'digits': lambda p: any(char.isdigit() for char in p),
        'symbols': lambda p: any(char in string.punctuation for char in p),
        'uppercase': lambda p: any(char.isupper() for char in p),
        'lowercase': lambda p: any(char.islower() for char in p),
        'length': lambda p: len(p) >= 8
    }

    for criterion in criteria.values():
        if criterion(password):
            score += 2

    return min(10, score)


def main():
    wellcome()
    while True:
        print_menu()
        choice = input("Введите номер пункта меню: ")
        handle_menu_choice(choice)
        if choice == "0":
            break


if __name__ == "__main__":
    main()
