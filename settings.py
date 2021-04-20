class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienigena"""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #Configurações da espaçonave
        self.ship_speed_factor = 1.5

        #Configurações dos projetéis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        #Configuração dos alienigenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1


