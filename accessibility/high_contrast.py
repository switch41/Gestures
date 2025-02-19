class HighContrastMode:
    def __init__(self, config):
        self.config = config
        self.active = False
        
    def toggle(self):
        self.active = not self.active
        self.config.high_contrast_mode = self.active