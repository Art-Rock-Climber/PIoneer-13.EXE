from colorama import Fore, Style
from ui.menu import clear_screen
from assets.constants import FAKE_PROGRAM_NAME, FAKE_PROGRAM_NAME_RU, REAL_PROGRAM_NAME, REAL_PROGRAM_NAME_RU, POEMS_TITLE
from pyfiglet import Figlet

rows = [
    "input",
    "username",
]


def draw_title_main(username=None):
    #clear_screen()
    print(Fore.LIGHTRED_EX + Style.BRIGHT + FAKE_PROGRAM_NAME_RU)
    print(Fore.WHITE + FAKE_PROGRAM_NAME)
    print(Fore.LIGHTRED_EX + "=" * 60)
    print(Fore.WHITE + "Версия: 1.0  |  Министерство электронной промышленности СССР")
    print(Fore.LIGHTRED_EX + "=" * 60)
    print(Style.RESET_ALL)


def draw_title_admin(username=None):
    #clear_screen()
    print(Fore.LIGHTRED_EX + Style.BRIGHT + REAL_PROGRAM_NAME_RU)
    print(Style.RESET_ALL + REAL_PROGRAM_NAME)
    print(Fore.LIGHTRED_EX + "=" * 60)
    print(Fore.WHITE + "Версия: 1.0  |  Министерство электронной промышленности СССР")
    print(Fore.LIGHTRED_EX + "=" * 60)
    print(Style.RESET_ALL)


def draw_keyboard(figlet_font="smkeyboard"):
    fig = Figlet(font=figlet_font)
    for row in rows:
        print(Fore.WHITE + fig.renderText(row), end="")


def draw_poems():
    print(POEMS_TITLE)

def draw_title_poem(title, poem_text):
    #clear_screen()
    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"\n  {title}\n")
    print(Fore.WHITE + poem_text)
    print(Style.RESET_ALL)
