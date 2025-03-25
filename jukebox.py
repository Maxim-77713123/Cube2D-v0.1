import pygame
import os
import random

class Jukebox
    def __init__(self)
        self.music_folder = jukebox  # Папка с музыкой
        pygame.mixer.init()  # Инициализация pygame mixer для работы с музыкой

    def play_music(self)
        Воспроизводит музыку, если файл jukebox.txt существует или выбирает случайную музыку из папки.
        track_name = self.get_track_name()

        if track_name
            track_path = os.path.join(self.music_folder, track_name)

            if os.path.exists(track_path)
                pygame.mixer.music.load(track_path)  # Загружаем музыку
                pygame.mixer.music.play(-1)  # Воспроизводим музыку бесконечно
                print(fИграет музыка {track_name})
            else
                print(fОшибка Музыка {track_name} не найдена.)
        else
            print(Ошибка Не удалось найти трек для воспроизведения.)

    def get_track_name(self)
        Получаем название трека для воспроизведения.
        # Проверяем наличие файла jukebox.txt
        track_name = None
        if os.path.exists(jukebox.txt)
            with open(jukebox.txt, r) as file
                track_name = file.read().strip()  # Читаем название трека из файла
            print(fНайден файл jukebox.txt. Воспроизводим {track_name}.)
        else
            # Если файл jukebox.txt не найден, выбираем случайный трек
            print(Файл jukebox.txt не найден. Выбираем случайную музыку.)
            music_files = [f for f in os.listdir(self.music_folder) if f.endswith(.mp3)]
            if music_files
                track_name = random.choice(music_files)  # Случайный трек
            else
                print(Ошибка В папке jukebox нет музыкальных файлов.)
        return track_name

    def stop_music(self)
        Останавливает музыку.
        pygame.mixer.music.stop()
        print(Музыка остановлена.)
