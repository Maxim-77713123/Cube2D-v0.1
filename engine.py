# engine.py
import pygame
import time

def run():
    """Запуск движка Cube2D."""
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    clock = pygame.time.Clock()

    # Основной игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Очистка экрана
        pygame.display.flip()  # Обновление экрана
        clock.tick(60)  # Ограничение по FPS

    pygame.quit()
