class Config:
    def __init__(self, mode):
        # Gesture detection parameters
        self.min_detection_confidence = 0.7
        self.min_tracking_confidence = 0.5
        self.gesture_cooldown = 0.5
        
        # UI parameters
        self.ui_scale = 1.0
        self.color_scheme = 'default'
        self.font_sizes = {
            'small': 0.8,
            'medium': 1.0,
            'large': 1.2
        }
        
        # Hardware settings
        self.touchscreen_dimensions = (1920, 1080)
        self.proximity_threshold = 1.0  # meters
        
        # Accessibility defaults
        self.voice_feedback = True
        self.high_contrast_mode = False
        
        if mode == 'debug':
            self._set_debug_params()
            
    def _set_debug_params(self):
        self.min_detection_confidence = 0.5
        self.ui_scale = 0.7
        self.voice_feedback = False