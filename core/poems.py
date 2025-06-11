from glob import glob
from ui.display import draw_poems_title, draw_poem
from ui.menu import render_submenu, clear_screen

_poems = {}


def load_poems():
    global _poems
    for file in glob("poems\\*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            _poems[file.split("\\")[-1].replace(".txt", "")] = f.read()


def poem_menu():
    choice = 0
    while True:
        choice = render_submenu(draw_poems_title, poem_items(), selected=choice)
        if choice == len(_poems):
            break
        handle_selection_poem(choice)


def handle_selection_poem(index):
    clear_screen()
    if index < len(_poems):
        title = list(_poems.keys())[index]
        draw_poem(title, _poems[title])
    input("\nНажмите Enter для возврата в меню...")


def poem_items():
    titles = [f"{i}) {title}" for i, title in enumerate(list(_poems.keys()), start=1)]
    titles.append("← Назад")
    return titles


def get_poems():
    return _poems
