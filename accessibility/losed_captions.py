import cv2
class ClosedCaptions:
    def __init__(self, config):
        self.config = config
        self.current_text = ""
        
    def update(self, text):
        self.current_text = text
        
    def render(self, frame):
        if self.current_text:
            cv2.putText(frame, self.current_text, (50, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame