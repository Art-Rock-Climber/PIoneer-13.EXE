from colorama import Fore, Style
from pyfiglet import Figlet
import os
import readchar

decorator = "►  " + Fore.RED


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_menu(title_func, menu_items, username=None, figlet_label=None):
    selected = 0
    while True:
        clear_screen()
        title_func(username=username)
        print(Fore.LIGHTGREEN_EX + f"  Пользователь: {username}\n")
        print(Fore.LIGHTBLACK_EX + "   Используйте ↑ и ↓ для навигации. Enter — выбор:\n")
        for i, item in enumerate(menu_items):
            prefix = decorator if i == selected else "   "
            print(prefix + item + Style.RESET_ALL)
        if figlet_label:
            print()
            fig = Figlet(font="cosmike")  # можно поменять на Roman, 3-d, cosmike, smkeyboard
            print(Fore.RED + fig.renderText(figlet_label))

        key = readchar.readkey()
        if key == readchar.key.UP:
            selected = (selected - 1) % len(menu_items)
        elif key == readchar.key.DOWN:
            selected = (selected + 1) % len(menu_items)
        elif key == readchar.key.ENTER:
            return selected
