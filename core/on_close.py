from pyfiglet import Figlet
from colorama import Fore, Style
from time import sleep as t_sleep
from sys import exit as s_exit
from ui.display import draw_on_close1, draw_on_close2
from ui.menu import render_submenu, clear_screen
from assets.constants import CONGRATULATIONS, CONGRATULATIONS2

from datetime import datetime
import random
import string

items = ["Получить партийный билет", "Отказаться"]


def close_menu1():
    choice = 0
    while True:
        choice = render_submenu(draw_on_close1, items, selected=choice)
        handle_selection_on_close1(choice)


def handle_selection_on_close1(index):
    clear_screen()
    if index == 0:
        print()
        print(Fore.LIGHTRED_EX + Style.BRIGHT + CONGRATULATIONS)
        name = save_party_ticket()
        print(f"{name} сохранён на ваше устройство.")
        input("\nНажмите Enter для выхода из приложения...")
        s_exit()
    else:
        close_menu2()


def close_menu2():
    choice = 0
    while True:
        choice = render_submenu(draw_on_close2, items, selected=choice)
        handle_selection_on_close2(choice)


def handle_selection_on_close2(index):
    from core.user import main_menu
    clear_screen()
    if index == 0:
        print()
        print(Fore.LIGHTRED_EX + Style.BRIGHT + CONGRATULATIONS2)
        name = save_party_ticket()
        print(f"{name} сохранён на ваше устройство.")
        input("\nНажмите Enter для выхода из приложения...")
        s_exit()
    else:
        for i, duration in enumerate([1, 1.2, 0.3, 0.2]):
            clear_screen()
            t_sleep(1.2-i*0.35)
            print()
            fig = Figlet(font="cosmike")  # можно поменять на Roman, 3-d, cosmike, smkeyboard
            print(Fore.RED + fig.renderText("HET"))
            t_sleep(duration)
        clear_screen()
        t_sleep(1.5)
        main_menu()


def get_current_time_string():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")


def generate_ticket_number():
    return ''.join(random.choices(string.digits, k=8))


def save_party_ticket(birth_year_placeholder = "________"):
    from core.auth import get_username
    ticket_number = generate_ticket_number()
    filename = f"Партийный билет №{ticket_number}"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("====================================\n")
        file.write(f"    ПАРТИЙНЫЙ БИЛЕТ № {ticket_number}\n")
        file.write("    КОММУНИСТИЧЕСКАЯ ПАРТИЯ\n")
        file.write("       СОВЕТСКОГО СОЮЗА\n")
        file.write("====================================\n")
        file.write(f"Имя: {get_username()}\n")
        file.write(f"Год рождения: {birth_year_placeholder}\n")
        file.write(f"Дата вступления: {get_current_time_string()}\n")
        file.write("\n")
        file.write("Подпись секретаря: _________________\n")
        file.write("Печать: [М.П.]\n")
        file.write("====================================\n")
    return filename
