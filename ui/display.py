from colorama import Fore, Style
from assets.constants import FAKE_PROGRAM_NAME, FAKE_PROGRAM_NAME_RU, REAL_PROGRAM_NAME, REAL_PROGRAM_NAME_RU, POEMS_TITLE
from pyfiglet import Figlet

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn
)
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from time import sleep as t_sleep
import random
from threading import Thread, Event

rows = [
    "input",
    "username",
]

console = Console()
exit_flag = Event()

tasks_info = [
    ("Установление скрытого канала межзвёздной связи", 80),
    ("Расшифровка государственных архивов инопланетных цивилизаций", 100),
    ("Захват пользовательских ЭВМ", 70),
    ("Распространение агитаций вступления в Интернационал", 90),
    ("Инициализация модуля контроля за инфраструктурой", 120),
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


def draw_poems_title():
    print(POEMS_TITLE)


def draw_poem(title, poem_text):
    #clear_screen()
    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"\n  {title}\n")
    print(Fore.WHITE + poem_text)
    print(Style.RESET_ALL)


def draw_songs_title():
    print("Советские песни:")


def simulate_progress(progress, task_id, total):
    while not exit_flag.is_set():
        current = progress.tasks[task_id].completed
        if current >= total:
            progress.reset(task_id)
        else:
            progress.advance(task_id, 1)
        t_sleep(random.uniform(0.05, 0.15))


def draw_loadings(title=None):
    exit_flag.clear()

    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=4),
        Layout(name="footer", size=3),
    )

    layout["header"].update(Align.center(Text(title or "", style="bold red")))

    progress = Progress(
        SpinnerColumn(style="cyan"),
        TextColumn("[bold green]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("{task.completed}/{task.total} ({task.percentage:>3.0f}%)"),
        TimeElapsedColumn(),
        console=console,
        transient=True  # убирает рендер в конце
    )

    layout["footer"].update(
        Align.center(Text("Нажмите [Enter], чтобы вернуться в меню", style="bold magenta"))
    )

    # Создаём задачи до Live
    task_ids = []
    for name, base_total in tasks_info:
        total = random.randint(int(base_total * 0.9), int(base_total * 1.1))
        task_id = progress.add_task(name, total=total)
        task_ids.append(task_id)
        Thread(
            target=simulate_progress, args=(progress, task_id, total), daemon=True
        ).start()

    # Ввод в отдельном потоке
    def wait_for_enter():
        input()
        exit_flag.set()

    Thread(target=wait_for_enter, daemon=True).start()

    with Live(layout, refresh_per_second=10, screen=True):
        while not exit_flag.is_set():
            layout["main"].update(Panel(progress.get_renderable(), border_style="dim"))
            t_sleep(0.1)
