import pygame
from objects import GameObject

class EnemyAI:
    def __init__(self, enemy, player):
        self.enemy = enemy
        self.player = player

    def update(self):
        # Преследование игрока
        if self.enemy.rect.x < self.player.rect.x:
            self.enemy.rect.x += 2
        elif self.enemy.rect.x > self.player.rect.x:
            self.enemy.rect.x -= 2
        
        if self.enemy.rect.y < self.player.rect.y:
            self.enemy.rect.y += 2
        elif self.enemy.rect.y > self.player.rect.y:
            self.enemy.rect.y -= 2
