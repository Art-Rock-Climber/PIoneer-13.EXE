from ui.menu import clear_screen, render_menu
from ui.display import draw_title_main
from assets.constants import menu_items
from core.auth import prompt_for_user, get_username
from core.poems import poem_menu, load_poems, get_poems


def main_menu():
    choice = 0
    while True:
        choice = render_menu(draw_title_main, menu_items,
                             selected=choice, username=get_username(), figlet_label="CCCP")
        handle_selection_user(choice)


def handle_selection_user(index):
    clear_screen()
    if index == 0:
        print("Вы открыли раздел об основах марксизма...")
    elif index == 1:
        print("🎶 'Взвейтесь кострами, синие ночи...' 🎶")
    elif index == 2:  # стихи
        if len(get_poems()) == 0:
            load_poems()
        poem_menu()
        return
    elif index == 3:
        prompt_for_user()
        main_menu()
        return
    elif index == 4:
        print(f"До свидания, товарищ {get_username()}.")
        exit(0)
    input("\nНажмите Enter для возврата в меню...")


