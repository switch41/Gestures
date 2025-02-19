import pyttsx3
import threading
import cv2

class VoiceFeedbackSystem:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        self.queue = []
        self.lock = threading.Lock()
        self.active = False

    def speak(self, text, interrupt=False):
        def _speak_task():
            with self.lock:
                if interrupt:
                    self.engine.stop()
                self.engine.say(text)
                self.engine.runAndWait()
                self.active = False
                
        if interrupt:
            self.queue = [text]
        else:
            self.queue.append(text)
            
        if not self.active:
            self.active = True
            thread = threading.Thread(target=_speak_task)
            thread.start()

    def set_language(self, lang_code='en'):
        # Requires appropriate voice packs
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if lang_code in voice.id:
                self.engine.setProperty('voice', voice.id)
                break

class VisualFeedback:
    def highlight_selection(self, frame, coordinates):
        # Draw animated border around selected UI element
        cv2.rectangle(frame, coordinates[0], coordinates[1], 
                     (0, 255, 0), 3)
        return frame