from glob import glob
from pygame import mixer
from ui.display import draw_songs_title
from ui.menu import render_submenu

mixer.init()
mixer.music.set_volume(0.5)
current_track = None
is_paused = False
_songs = {}


def load_songs():
    global _songs
    for path in glob("songs\\*.mp3"):
        _songs[path.split("\\")[-1].replace(".mp3", "")] = path


def song_menu():
    choice = 0
    while True:
        choice = render_submenu(draw_songs_title, song_items(), selected=choice)
        if choice == len(_songs):
            mixer.music.stop()
            break
        handle_selection_song(choice)


def handle_selection_song(index):
    global current_track, is_paused
    song_path = _songs[list(_songs.keys())[index]]

    # Если это новый трек (не текущий)
    if song_path != current_track:
        mixer.music.stop()
        mixer.music.load(song_path)
        mixer.music.play()
        current_track = song_path
        is_paused = False

    # Если это текущий трек
    else:
        if is_paused:
            mixer.music.unpause()
            is_paused = False
        else:
            mixer.music.pause()
            is_paused = True


def song_items():
    titles = [f"{i}) {title}" for i, title in enumerate(list(_songs.keys()), start=1)]
    titles.append("← Назад")
    return titles


def get_songs():
    return _songs
