import pygame

def handle_collisions(pajaro, moving_sprites, mirilla, num_balas, score):
    if pygame.sprite.collide_rect(pajaro, mirilla):
        num_balas -= 1
        score += 1
    return num_balas, score