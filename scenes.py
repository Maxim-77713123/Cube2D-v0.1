import pygame  # Добавим импорт pygame

class MenuScene:
    def __init__(self, game):
        self.game = game

    def update(self):
        pass

    def render(self, screen):
        # Пример использования pygame для отрисовки текста
        font = pygame.font.Font(None, 36)
        text = font.render("Привет, это меню!", True, (255, 255, 255))
        screen.blit(text, (100, 100))
