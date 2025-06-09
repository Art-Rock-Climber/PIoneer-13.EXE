import os
import sys
import cv2
import time
import numpy as np


class VideoToASCII:
    def __init__(self, video_path, output_size=(150, 25), frame_rate=15):
        self.video_path = video_path
        self.output_size = output_size
        self.frame_rate = frame_rate
        self.ascii_chars = "@%#*+=-:. "

    def play(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Ошибка загрузки видео")
            return

        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Конвертируем кадр в ASCII
                ascii_frame = self._frame_to_ascii(frame)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(ascii_frame)
                time.sleep(1/self.frame_rate)

        finally:
            cap.release()

    def _frame_to_ascii(self, frame):
        # Конвертируем в градации серого и изменяем размер
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, self.output_size, interpolation=cv2.INTER_LINEAR)

        # Нормализуем и конвертируем в ASCII
        normalized = resized / 255.0
        ascii_str = ""
        for row in normalized:
            for pixel in row:
                index = int(pixel * (len(self.ascii_chars) - 1))
                ascii_str += self.ascii_chars[index]
            ascii_str += "\n"
        return ascii_str


v = VideoToASCII('media_mat/ussr.mp4')
v.play()




'''
# Создаем простое видео с текстом
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('intro.mp4', fourcc, 20.0, (640, 480))

for i in range(100):
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.putText(frame, "Communist Quest", (150, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.putText(frame, f"Loading... {i}%", (200, 300),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    out.write(frame)

out.release()
'''