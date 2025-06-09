from colorama import Fore
from ui.display import draw_title_main, draw_keyboard
from ui.menu import clear_screen
from assets.constants import ADMIN_CODE

_username = None


def prompt_for_user():
    global _username
    while True:
        draw_title_main()
        draw_keyboard("smkeyboard")
        user_input = input(Fore.WHITE + "\nВведите ваше имя (или введите 3.1415926535): ").strip()

        if is_pi_input(user_input):
            enter_admin_mode()
            continue
        elif user_input:
            _username = user_input
            break


def enter_admin_mode():
    from core.admin import admin_menu
    clear_screen()
    print(Fore.MAGENTA + "\n  ✦ ДОСТУП РАЗРЕШЕН ✦")
    print("  Добро пожаловать в режим администратора.\n")
    print("  Здесь хранятся секретные данные о реальных целях проекта.")
    print("  [!] Внимание: дальнейший просмотр может повлиять на вашу лояльность.")
    input("\nНажмите Enter для продолжения...")
    admin_menu()


def get_username():
    return _username


def is_pi_input(value):
    return value.replace(",", ".") == ADMIN_CODE
