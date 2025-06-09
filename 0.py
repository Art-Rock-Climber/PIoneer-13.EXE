import spacy
import os
import sys
import time
from progress.bar import IncrementalBar
from progress.spinner import Spinner, MoonSpinner
#from video_to_ascii import VideoToASCII



class Game:
    def __init__(self):
        self.running = True
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            self.install_spacy_model()

    def install_spacy_model(self):
        print("Требуется модель spaCy. Установить? (y/n)", end=' ', flush=True)
        if input().lower() == 'y':
            os.system("python -m spacy download en_core_web_sm")
            print("Модель установлена. Перезапустите программу.")
        sys.exit(0)

    def clear_screen(self):
        """Кроссплатформенная очистка экрана"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def clear_lines(self, lines=1):
        """Очищает указанное количество предыдущих строк"""
        for _ in range(lines):
            sys.stdout.write('\033[F')  # Переместить курсор вверх
            sys.stdout.write('\033[K')  # Очистить строку

    def get_valid_input(self, prompt, valid_options):
        """Получает валидный ввод с перезаписью ошибочных попыток"""
        while True:
            user_input = input(prompt).strip()
            doc = self.nlp(user_input.lower())

            for token in doc:
                if token.lemma_ in valid_options:
                    return token.lemma_

            # Если ввод неверный:
            self.clear_lines()
            sys.stdout.write('\033[K')  # Очистить текущую строку
            sys.stdout.flush()

    def loading(self):
        mylist = list(range(8))
        bar = IncrementalBar('Загрузка', max=len(mylist))
        for _ in mylist:
            bar.next()
            time.sleep(0.5)
        bar.finish()

    def start(self):
        while self.running:
            self.clear_screen()
            self.loading()
            self.clear_screen()
            print("≡" * 40)
            print("You are an adventurer seeking the legendary Communist Manifesto")
            print("Paths lead: north, east, west, south")
            print("≡" * 40)

            direction = self.get_valid_input(
                "Direction (north/east/west/south): ",
                ['north', 'east', 'west', 'south']
            )

            getattr(self, f"{direction}_path")()

    def north_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("NORTH: Ancient oak tree with strange engravings")
        print("The bark seems to pulse with energy")
        print("≡" * 40)

        action = self.get_valid_input(
            "Inspect or ignore? ",
            ['inspect', 'ignore']
        )

        if action == 'inspect':
            self.show_outcome("\nYou discover the 'Red Star Fruit'!\nIt fills you with revolutionary fervor!", "win")
        else:
            self.show_outcome("\nGhosts of fallen comrades appear!\nThey condemn your lack of curiosity!", "lose")

    def east_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("EAST: Abandoned collective farm")
        print("Rusted tractors bear hammer-and-sickle symbols")
        print("≡" * 40)

        action = self.get_valid_input(
            "Explore or avoid? ",
            ['explore', 'avoid']
        )

        if action == 'explore':
            self.show_outcome("\nYou find a secret meeting of reactionaries!\nThey report you to the authorities!",
                              "lose")
        else:
            self.show_outcome("\nAn old farmer shares his last bread with you\n'For the collective!' he whispers",
                              "win")

    def west_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("WEST: Raging river of class struggle")
        print("The waters foam with revolutionary potential")
        print("≡" * 40)

        action = self.get_valid_input(
            "Swim or build raft? ",
            ['swim', 'build']
        )

        if action == 'swim':
            self.show_outcome("\nThe current of dialectics overwhelms you!\nYou sink into historical irrelevance!",
                              "lose")
        else:
            self.show_outcome(
                "\nYou construct a raft from bourgeois textbooks!\nThe collective spirit carries you across!", "win")

    def south_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("SOUTH: Cave of dialectical materialism")
        print("A red glow emanates from within")
        print("≡" * 40)

        action = self.get_valid_input(
            "Enter or move on? ",
            ['enter', 'move']
        )

        if action == 'enter':
            self.show_outcome(
                "\nYou find the Manifesto glowing with truth!\nThe workers of the world unite around you!", "win")
        else:
            self.show_outcome("\nOpportunism leads to ideological decay!\nYou become a footnote in history!", "lose")

    def show_outcome(self, message, result):
        print(message)
        print("\n" + "≡" * 40)
        print("☆ VICTORY! ☆" if result == "win" else "☠ DEFEAT... ☠")
        print("≡" * 40 + "\n")
        self.play_again()

    def play_again(self):
        choice = self.get_valid_input(
            "Continue the revolution? (yes/no): ",
            ['yes', 'no']
        )

        if choice == 'no':
            self.running = False
            print("\nThe struggle continues... Goodbye, comrade!")


if __name__ == "__main__":
    game = Game()
    game.start()




'''import spacy
import os


# pi.exe - Program for communist International EXperience Exchange
# (Political Identity EXEcutioner)


class Game:
    def __init__(self):
        self.state = "start"
        self.nlp = spacy.load("en_core_web_sm")


    def clear_screen(self):
        """Очищает консоль в зависимости от ОС"""
        os.system('cls' if os.name == 'nt' else 'clear')


    def parse_input(self, input_text):
        doc = self.nlp(input_text)
        for token in doc:
            if token.lemma_ in ['north', 'east', 'west', 'south', 'inspect',
                                'ignore', 'explore', 'avoid', 'swim', 'build', 'enter', 'move']:
                return token.lemma_
        return None

    def start(self):
        print("You are an adventurer on a quest to find a legendary treasure hidden deep within an ancient forest.")
        print("You stand at the entrance of the forest, with paths leading to the north, east, west, and south.")
        choice = self.parse_input(input("Which way do you go? (north, east, west, south): ").strip().lower())
        if choice == 'north':
            self.state = "north"
            self.north_path()
        elif choice == 'east':
            self.state = "east"
            self.east_path()
        elif choice == 'west':
            self.state = "west"
            self.west_path()
        elif choice == 'south':
            self.state = "south"
            self.south_path()
        else:
            print("Invalid choice. Try again.")
            self.start()

    def north_path(self):
        print("You head north and encounter a colossal ancient oak tree that radiates a mysterious aura.")
        print("Do you inspect the tree or ignore it and continue your journey?")
        choice = self.parse_input(input("Type 'inspect' or 'ignore': ").strip().lower())
        if choice == 'inspect':
            print("You find a magical fruit that grants you immense strength. You continue your journey with newfound power!")
            self.end_game("win")
        elif choice == 'ignore':
            print("A cursed spirit emerges from the tree and haunts you. You run away in fear, abandoning your quest.")
            self.end_game("lose")
        else:
            print("Invalid choice. Try again.")
            self.north_path()

    def east_path(self):
        print("You head east and discover an abandoned village with eerie silence all around.")
        print("Do you explore the village or avoid it and move on?")
        choice = self.parse_input(input("Type 'explore' or 'avoid': ").strip().lower())
        if choice == 'explore':
            print("You trigger a hidden trap and fall into a pit. Your quest ends here.")
            self.end_game("lose")
        elif choice == 'avoid':
            print("A helpful villager appears and guides you to a safe path through the forest. You continue your journey.")
            self.end_game("win")
        else:
            print("Invalid choice. Try again.")
            self.east_path()

    def west_path(self):
        print("You head west and reach a raging river that blocks your path.")
        print("Do you swim across the river or build a raft to float over?")
        choice = self.parse_input(input("Type 'swim' or 'build': ").strip().lower())
        if choice == 'swim':
            print("The current is too strong, and you drown. Your quest ends here.")
            self.end_game("lose")
        elif choice == 'build':
            print("You successfully build a raft and cross the river safely. You continue your journey.")
            self.end_game("win")
        else:
            print("Invalid choice. Try again.")
            self.west_path()

    def south_path(self):
        print("You head south and find the entrance to a dark cave, rumored to hold the legendary treasure.")
        print("Do you enter the cave or move on?")
        choice = self.parse_input(input("Type 'enter' or 'move': ").strip().lower())
        if choice == 'enter':
            print("You bravely enter the cave and find the legendary treasure! You are victorious!")
            self.end_game("win")
        elif choice == 'move':
            print("You decide it's too dangerous and leave. Your quest ends here.")
            self.end_game("lose")
        else:
            print("Invalid choice. Try again.")
            self.south_path()

    def end_game(self, result):
        if result == "win":
            print("Congratulations! You have completed your quest successfully!")
        else:
            print("Game Over. Better luck next time.")
        self.play_again()

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("\033[H\033[J", end="")
            self.start()
        else:
            print("Thank you for playing! Goodbye.")


game = Game()
game.start()'''

'''
import spacy
import os


class Game:
    def __init__(self):
        self.state = "start"
        self.nlp = spacy.load("en_core_web_sm")
        self.running = True  # Флаг для контроля основного цикла

    def clear_screen(self):
        """Очистка консоли с обработкой для PyCharm"""
        print("\033[H\033[J", end="")

    def parse_input(self, input_text):
        doc = self.nlp(input_text.lower())
        for token in doc:
            if token.lemma_ in ['north', 'east', 'west', 'south', 'inspect',
                                'ignore', 'explore', 'avoid', 'swim', 'build',
                                'enter', 'move']:
                return token.lemma_
        return None

    def start(self):
        """Основной игровой цикл"""
        while self.running:
            self.clear_screen()
            print("≡" * 40)
            print("You are an adventurer seeking the legendary Communist Manifesto")
            print("Paths lead: north, east, west, south")
            print("≡" * 40)

            choice = self.parse_input(input("Direction (north/east/west/south): "))

            if choice == 'north':
                self.north_path()
            elif choice == 'east':
                self.east_path()
            elif choice == 'west':
                self.west_path()
            elif choice == 'south':
                self.south_path()
            else:
                print("! Invalid direction. Try again")
                input("Press Enter to continue...")

    # Северный путь (уже реализован)
    def north_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("NORTH: Ancient oak tree with strange engravings")
        print("The bark seems to pulse with energy")
        print("≡" * 40)

        while True:
            choice = self.parse_input(input("Inspect or ignore? "))

            if choice == 'inspect':
                print("\nYou discover the 'Red Star Fruit'!")
                print("It fills you with revolutionary fervor!")
                self.end_game("win")
                break
            elif choice == 'ignore':
                print("\nGhosts of fallen comrades appear!")
                print("They condemn your lack of curiosity!")
                self.end_game("lose")
                break
            else:
                print("! Invalid choice")

    # Восточный путь
    def east_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("EAST: Abandoned collective farm")
        print("Rusted tractors bear hammer-and-sickle symbols")
        print("≡" * 40)

        while True:
            choice = self.parse_input(input("Explore or avoid? "))

            if choice == 'explore':
                print("\nYou find a secret meeting of reactionaries!")
                print("They report you to the authorities!")
                self.end_game("lose")
                break
            elif choice == 'avoid':
                print("\nAn old farmer shares his last bread with you")
                print("'For the collective!' he whispers")
                self.end_game("win")
                break
            else:
                print("! Invalid choice")

    # Западный путь
    def west_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("WEST: Raging river of class struggle")
        print("The waters foam with revolutionary potential")
        print("≡" * 40)

        while True:
            choice = self.parse_input(input("Swim or build raft? "))

            if choice == 'swim':
                print("\nThe current of dialectics overwhelms you!")
                print("You sink into historical irrelevance!")
                self.end_game("lose")
                break
            elif choice == 'build':
                print("\nYou construct a raft from bourgeois textbooks!")
                print("The collective spirit carries you across!")
                self.end_game("win")
                break
            else:
                print("! Invalid choice")

    # Южный путь
    def south_path(self):
        self.clear_screen()
        print("≡" * 40)
        print("SOUTH: Cave of dialectical materialism")
        print("A red glow emanates from within")
        print("≡" * 40)

        while True:
            choice = self.parse_input(input("Enter or move on? "))

            if choice == 'enter':
                print("\nYou find the Manifesto glowing with truth!")
                print("The workers of the world unite around you!")
                self.end_game("win")
                break
            elif choice == 'move':
                print("\nOpportunism leads to ideological decay!")
                print("You become a footnote in history!")
                self.end_game("lose")
                break
            else:
                print("! Invalid choice")

    def end_game(self, result):
        """Обработка окончания игры"""
        print("\n" + "≡" * 40)
        if result == "win":
            print("☆ VICTORY: You advanced the cause! ☆")
        else:
            print("☠ DEFEAT: Revisionism triumphs... ☠")
        print("≡" * 40 + "\n")

        self.play_again()

    def play_again(self):
        """Цикл повтора игры"""
        while True:
            choice = self.parse_input(input("Continue the revolution? (yes/no): "))

            if choice == 'yes':
                break
            elif choice == 'no':
                self.running = False
                print("\nThe struggle continues... Goodbye, comrade!")
                break
            else:
                print("! Invalid choice")


if __name__ == "__main__":
    game = Game()
    game.start()
'''
