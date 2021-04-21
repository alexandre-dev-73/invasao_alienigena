
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #Inicializa o jogo e cria um objeto para tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria o botão Play
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma instancia para armazenar dados estatisticos do jogo
    stats = GameStats(ai_settings)

    #Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    #cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    aliens =Group()

    #Cria a frota de aliengenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Inicia o laço principal do jogo
    while True:

        #Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
