
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #Inicializa o jogo e cria um objeto para tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    #cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    #Cria um alienigena
    alien = Alien(ai_settings, screen)

    #Inicia o laço principal do jogo
    while True:

        #Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
