import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *  
from pajaro import *
from shoot import handle_shooting
import sys

def main():
    pygame.init()

    Tamaño_pantalla = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption(titulo)

    mostrar_portada = toleportada(3)

    if mostrar_portada:
        iniciar_juego = tolemenu()

        if iniciar_juego:
            print("sisas")
            
            fondo = FondoBase()
            montañas = FondoMontañas()

            moving_sprites = pygame.sprite.Group()
            vuelo = Vuelo(100, 100)
            moving_sprites.add(vuelo)

            clock = pygame.time.Clock()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    handle_shooting(event, screen)

                screen.fill(WHITE)

                screen.blit(fondo.image, fondo.rect)
                vuelo.movimiento()
                screen.blit(montañas.image, montañas.rect)

                moving_sprites.draw(screen)
                moving_sprites.update(0.25)

                pygame.display.update()
                clock.tick(60)
    
if __name__ == "__main__":
    main()
