class SwipeDetector:
    def __init__(self, config):
        self.config = config
        self.history = []
        
    def detect(self, hand_trajectory):
        if len(hand_trajectory) < 5:
            return None
            
        # Calculate movement vectors
        dx = hand_trajectory[-1][0] - hand_trajectory[0][0]
        dy = hand_trajectory[-1][1] - hand_trajectory[0][1]
        
        # Determine dominant direction
        if abs(dx) > abs(dy):
            return 'swipe_left' if dx < 0 else 'swipe_right'
        else:
            return 'swipe_up' if dy < 0 else 'swipe_down'