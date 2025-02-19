import pyttsx3

class VoiceFeedbackSystem:
    def __init__(self, config):
        self.config = config
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
    def announce(self, text):
        if self.config.voice_feedback:
            self.engine.say(text)
            self.engine.runAndWait()