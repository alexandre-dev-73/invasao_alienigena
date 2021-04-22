class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienigena"""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #Configurações da espaçonave
        self.ship_limit = 3

        #Configurações dos projetéis
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Configuração dos alienigenas
        self.fleet_drop_speed = 10

        #A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        #A taxa com que aos pontos para cada alienigena aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configuraçoes que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction igual a 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1

        #Pontuação
        self.alien_points = 50


    def increase_speed(self):
        """Aumewnta as configuraçoes de velocidade."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

