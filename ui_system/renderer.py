import cv2

class UIRenderer:
    def __init__(self, config):
        self.config = config
        self.colors = self._load_color_scheme()
        
    def render(self, frame, ui_state):
        self._draw_background(frame)
        self._draw_menu(frame, ui_state)
        return frame
        
    def _draw_menu(self, frame, menu):
        for i, item in enumerate(menu.items):
            color = self.colors['highlight'] if i == menu.selection_index else self.colors['text']
            position = (50, 100 + i * 60)
            cv2.putText(frame, item.label, position, 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        self.config.font_sizes['medium'], 
                        color, 2)
    
    def _load_color_scheme(self):
        if self.config.high_contrast_mode:
            return {'text': (255, 255, 255), 'background': (0, 0, 0), 'highlight': (0, 255, 255)}
        else:
            return {'text': (200, 200, 200), 'background': (50, 50, 50), 'highlight': (0, 255, 0)}