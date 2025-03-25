import pygame
import sys
from objects import Player, Enemy

pygame.init()

# Основные настройки
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cube2D - Стартовая игра для новичков")

# Игровые объекты
player = Player(375, 500)
enemy = Enemy(200, 100)

clock = pygame.time.Clock()

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление игроком
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            player.rect.x += 5
        if keys[pygame.K_UP]:
            player.rect.y -= 5
        if keys[pygame.K_DOWN]:
            player.rect.y += 5

        # Обновление экрана
        screen.fill((0, 0, 0))  # Черный фон
        screen.blit(player.image, player.rect)
        screen.blit(enemy.image, enemy.rect)
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
