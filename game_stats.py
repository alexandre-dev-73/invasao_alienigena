class GameStats():
    """Armazena dados estatisticos da Invasão Alienigena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos."""
        self.ai_settings = ai_settings
        self.reset_stats()


    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit