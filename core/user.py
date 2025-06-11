from ui.menu import clear_screen, render_menu
from ui.display import draw_title_main
from assets.constants import menu_items
from core.auth import prompt_for_user, get_username
from core.poems import poem_menu, load_poems, get_poems
from core.songs import song_menu, load_songs, get_songs
from core.on_close import close_menu1

from colorama import Fore, Style

visited_info = False   # Посещены ли основы марксизма
visited_poems = False  # Посещены ли стихи
visited_songs = False  # Посещены ли песни


def main_menu():
    choice = 0
    while True:
        update_exit()
        choice = render_menu(draw_title_main, menu_items,
                             selected=choice, username=get_username(), figlet_label="CCCP")
        handle_selection_user(choice)


def handle_selection_user(index):
    global visited_info, visited_poems, visited_songs
    clear_screen()
    if index == 0:
        visited_info = True
        with open("Основы марксизма.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    elif index == 1:  # песни
        visited_poems = True
        if len(get_songs()) == 0:
            load_songs()
        song_menu()
        return
    elif index == 2:  # стихи
        visited_songs = True
        if len(get_poems()) == 0:
            load_poems()
        poem_menu()
        return
    elif index == 3:
        visited_info = visited_poems = visited_songs = False
        prompt_for_user()
        main_menu()
        return
    elif index == 4:
        if can_exit():
            visited_info = visited_poems = visited_songs = False
            close_menu1()  # f"До свидания, товарищ {get_username()}."
        else:
            return
    input("\nНажмите Enter для возврата в меню...")


def can_exit():
    return visited_info and visited_poems and visited_songs


def update_exit():
    menu_items[-1] = "✕ " + ("Выход" if can_exit() else Fore.LIGHTBLACK_EX + "Выход (недоступно)")
