class AudioSystem:
    def __init__(self):
        self.volume = 50
        
    def set_volume(self, level):
        self.volume = max(0, min(100, level))
        
    def play_sound(self, sound_id):
        pass    