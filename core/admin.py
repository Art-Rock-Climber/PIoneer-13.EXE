from ui.menu import clear_screen, render_menu
from ui.display import draw_title_admin, draw_loadings
from assets.constants import admin_menu_items
from core.auth import prompt_for_user
from core.user import main_menu

from sys import exit as s_exit


def admin_menu():
    choice = 0
    while True:
        choice = render_menu(draw_title_admin, admin_menu_items,
                             selected=choice, username="PIoneer", figlet_label=None)
        if handle_selection_admin(choice):
            break


def handle_selection_admin(index):
    clear_screen()
    if index == 0:
        draw_loadings(title="Диагностика системы: [секретно]")
        return False
    elif index == 1:
        print("\nДоступ к архиву: загружаются материалы...\n")
    elif index == 2:
        print("\nРедактирование параметров: 🔧\n")
    elif index == 3:
        prompt_for_user()
        main_menu()
        return True
    elif index == 4:
        print("До свидания, товарищ PIoneer.")
        s_exit()
    input("Нажмите Enter для возврата...")
    return False
