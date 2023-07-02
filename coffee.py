import os
import time
import random
import string


def wellcome():
    os.system("clear")
    print(
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠿⠿⠛⠛⠋⠉⠛⠛⠻⠿⠿⣿⣿⣿⣿\n⣿⣿⣿⠀⠐⠾⠿⠷⠶⠶⠶⠶⠾⠿⠷⠒⠀⣿⣿⣿\n⣿⣿⣿⡆⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠈⠁⠀⣉⡉⢻\n⣿⣿⣿⣷⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠤⠐⣸⠿⢃⣼\n⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣾⣿⣿\n⡿⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⢿\n⣷⣤⣀⠀⠀⠀⠉⠙⠒⠂⠀⠒⠋⠉⠀⠀⢀⣀⣤⣾\n⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿")
    time.sleep(1)
    os.system("clear")


def print_menu():
    print("1. Открыть одноразовый почтовый ящик")
    print("2. Сгенерировать пароль")
    # Добавьте остальные пункты меню здесь


def handle_menu_choice(choice):
    if choice == '1':
        open_temp_mail()
    elif choice == '2':
        generate_password()
    # Добавьте обработку остальных пунктов меню здесь


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
