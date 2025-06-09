from core.user import main_menu
from core.auth import prompt_for_user

from colorama import init
init(autoreset=True)


if __name__ == "__main__":
    prompt_for_user()
    main_menu()



# Загрузку данных из файлов (poems.txt, songs.txt, quotes.txt)
# Аудио сопровождение при старте
# Анимации в стиле old terminal
# Псевдоинсталлятор с вводом «серийного ключа трудящегося»
# Реализовать скрытые команды (например, debug, exit-now).