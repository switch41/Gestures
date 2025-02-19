class AnimationEngine:
    def __init__(self):
        self.active_animations = []
        
    def add_animation(self, animation):
        self.active_animations.append(animation)
        
    def update(self, frame):
        for anim in self.active_animations:
            anim.update(frame)
            
class SelectionAnimation:
    def __init__(self, position):
        self.position = position
        self.frame_count = 0
        
    def update(self, frame):
        alpha = abs(255 * (self.frame_count % 30) / 30)
        cv2.circle(frame, self.position, 20, (0, 255, 0, alpha), 4)
        self.frame_count += 1