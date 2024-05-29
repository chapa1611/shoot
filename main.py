import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *  
from pajaro import *
from shot import *
import sys

def main():
    pygame.init()

    Tamaño_pantalla = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption(titulo)

    mostrar_portada = toleportada(2)

    if mostrar_portada:
        iniciar_juego = tolemenu()

        if iniciar_juego:
            print("sisas")
            
            fondo = FondoBase()
            montañas = FondoMontañas()

            moving_sprites = pygame.sprite.Group()
            vuelo = Vuelo(0, 700)
            moving_sprites.add(vuelo)


            clock = pygame.time.Clock()

            global can_shoot, last_shot_time
            can_shoot = True
            last_shot_time = 0

            vuelo.movimiento()  # Iniciar la animación

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    handle_shooting(event, screen)

                screen.fill(WHITE)
                screen.blit(fondo.image, fondo.rect)

                # Alternar entre volar_derecha y volar_izquierda basado en la posición x
                
                vuelo.volar_derecha(0.30)
                print("derecha")
                '''
                else:
                    vuelo.volar_izquierda(0.30)
                    print("izquierda")
                '''
                moving_sprites.draw(screen)
                moving_sprites.update(0.30)
                
                screen.blit(montañas.image, montañas.rect)

                pygame.display.update()
                clock.tick(60)

if __name__ == "__main__":
    main()
