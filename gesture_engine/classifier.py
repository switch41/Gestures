import numpy as np
from collections import deque

class GestureClassifier:
    def __init__(self, config):
        self.config = config
        self.history = deque(maxlen=10)  # Store the last 10 frames for analysis
        
    def classify(self, hands):
        gestures = []
        for hand in hands:
            num_fingers = self._count_fingers(hand['landmarks'])
            gesture = self._classify_single(hand['landmarks'], num_fingers)
            
            # Default gesture if no specific match
            if not gesture:
                gesture = "open_hand"  

            gestures.append({
                'type': gesture,
                'fingers': num_fingers,  # Include finger count
                'handedness': hand['handedness']
            })
        
        return gestures
    
    def _classify_single(self, landmarks, num_fingers):
        """ Classify hand gestures based on landmark positions and finger count. """
        lm_array = np.array([[lm[0], lm[1]] for lm in landmarks])  # Corrected to use tuple indexing

        # Simple classification based on finger count
        if num_fingers == 0:
            return "fist"
        elif num_fingers == 5:
            return "open_hand"
        elif num_fingers == 1:
            return "pointing"
        elif num_fingers == 2:
            return "peace"
        return "unknown"

    def _count_fingers(self, landmarks):
        """ Count the number of extended fingers. """
        # Finger tip and base landmark indices (from MediaPipe)
        finger_tips = [4, 8, 12, 16, 20]
        finger_bases = [2, 6, 10, 14, 18]

        count = 0
        for tip, base in zip(finger_tips, finger_bases):
            if landmarks[tip][1] < landmarks[base][1]:  # Tip is above base (finger extended)
                count += 1

        return count
