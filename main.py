import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *
from pajaro import *
from colision import *
from mirilla import *
from shot import *
import sys

def main():
    pygame.init()

    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(titulo)

    mostrar_portada = toleportada(2)

    if mostrar_portada:
        iniciar_juego = tolemenu()

        if iniciar_juego:
            fondo = FondoBase()
            montañas = FondoMontañas()

            moving_sprites = pygame.sprite.Group()
            pajaro = Pajaro(0, 700)
            moving_sprites.add(pajaro)

            mirilla = Mirilla(crosshair_img)

            clock = pygame.time.Clock()

            num_balas = 3
            score = 0  # Se inicializa el puntaje

            pajaro.movimiento()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    handle_shooting(event, pantalla)

                pantalla.fill(WHITE)
                pantalla.blit(fondo.image, fondo.rect)

                num_balas, score = handle_collisions(pajaro, moving_sprites, mirilla, num_balas, score)
                handle_crosshair(num_balas, mirilla, pantalla)

                moving_sprites.draw(pantalla)
                moving_sprites.update()

                pantalla.blit(montañas.image, montañas.rect)

                pygame.display.update()
                clock.tick(60)

if __name__ == "__main__":
    main()