from ui.menu import clear_screen, render_menu
from ui.display import draw_title_main
from assets.constants import menu_items
from core.auth import prompt_for_user, get_username


def main_menu():
    while True:
        choice = render_menu(draw_title_main, menu_items, get_username(), figlet_label="CCCP")
        handle_selection_user(choice)


def handle_selection_user(index):
    clear_screen()
    if index == 0:
        print("Вы открыли раздел об основах марксизма...")
    elif index == 1:
        print("🎶 'Взвейтесь кострами, синие ночи...' 🎶")
    elif index == 2:
        print("📜 'Бей в барабаны, звени, медь труда...'")
    elif index == 3:
        prompt_for_user()
        return
    elif index == 4:
        print(f"До свидания, товарищ {get_username()}.")
        exit(0)
    input("\nНажмите Enter для возврата в меню...")


