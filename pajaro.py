import pygame
import random

class Pajaro(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animacion = False
        self.sprites = []
        for i in range(1, 10):
            self.sprites.append(pygame.image.load(f"imagenes/pajaro{i}.png").convert_alpha())

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
        self.direccion = 'derecha'

    def movimiento(self):
        self.animacion = True

    def update(self):
        if self.animacion:
            self.sprite_actual += 0.1
            if int(self.sprite_actual) >= len(self.sprites):
                self.sprite_actual = 0

            if self.direccion == 'derecha':
                self.rect.x += 2
                self.rect.y -= 7

                if self.rect.right < 0 or self.rect.bottom < 0:
                    self.rect.topleft = (self.rect.topleft[0] + 2, 700)

                if self.rect.topleft[0] >= 768:
                    self.rect.topleft = (0, 700)

            elif self.direccion == 'izquierda':
                self.rect.x -= 2
                self.rect.y -= 7

                if self.rect.right < 0 or self.rect.bottom < 0:
                    self.rect.topleft = (self.rect.topleft[0] - 2, 700)

                if self.rect.topleft[0] < 0:
                    self.rect.topleft = (700, 700)

            self.image = self.sprites[int(self.sprite_actual)]

    def change_direction(self, direction):
        self.direccion = direction
