import pygame
import os

# Стандартные текстуры для персонажей и врагов
DEFAULT_PLAYER_IMAGE = pygame.Surface((50, 50))
DEFAULT_PLAYER_IMAGE.fill((0, 255, 0))  # Зеленый квадрат

DEFAULT_ENEMY_IMAGE = pygame.Surface((50, 50))
DEFAULT_ENEMY_IMAGE.fill((255, 0, 0))  # Красный квадрат

# Путь к папке с изображениями
MOBS_DIR = "mobs"

def load_image(image_name, default_image):
    """Загружает изображение из папки mobs или использует стандартное изображение."""
    image_path = os.path.join(MOBS_DIR, image_name)
    if os.path.exists(image_path):
        return pygame.image.load(image_path)
    else:
        print(f"Изображение {image_name} не найдено. Используется стандартное изображение.")
        return default_image

class GameObject:
    def __init__(self, x, y, image_name=None, default_image=None):
        self.x = x
        self.y = y
        if image_name and default_image:
            self.image = load_image(image_name, default_image)
        else:
            self.image = default_image
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Обновление логики объекта
        pass

class Player(GameObject):
    def __init__(self, x, y):
        # Используем изображение игрока или стандартное изображение
        player_image = load_image("player.png", DEFAULT_PLAYER_IMAGE)
        super().__init__(x, y, "player.png", player_image)

class Enemy(GameObject):
    def __init__(self, x, y):
        # Используем изображение врага или стандартное изображение
        enemy_image = load_image("enemy.png", DEFAULT_ENEMY_IMAGE)
        super().__init__(x, y, "enemy.png", enemy_image)

# Пример использования:
# player = Player(100, 100)
# enemy = Enemy(200, 100)
