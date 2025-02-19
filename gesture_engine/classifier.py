import numpy as np
from collections import deque

class GestureClassifier:
    def __init__(self, config):
        self.config = config
        self.history = deque(maxlen=10)  # Store the last 10 frames for analysis
        
    def classify(self, hands):
        gestures = []
        for hand in hands:
            gesture = self._classify_single(hand['landmarks'])
            
            # If no specific gesture is detected, default to "open_hand"
            if not gesture:
                gesture = "open_hand"  

            gestures.append({
                'type': gesture,
                'handedness': hand['handedness']
            })
        
        return gestures
    
    def _classify_single(self, landmarks):
        """ Classify hand gestures based on landmark positions. """
        lm_array = np.array([[lm.x, lm.y] for lm in landmarks])

        # Analyze finger positions
        finger_states = self._analyze_fingers(lm_array)
        self.history.append(finger_states)
        
        # Classify gesture
        return self._state_machine_classification()

    def _analyze_fingers(self, lm_array):
        """ Simple classification: Detect open hand or fist """
        # Thumb to pinky distance (simple fist detection)
        thumb_tip = lm_array[4]
        pinky_tip = lm_array[20]
        distance = np.linalg.norm(thumb_tip - pinky_tip)

        if distance < 0.05:  # Small distance → Fist
            return "fist"
        return "open_hand"

    def _state_machine_classification(self):
        """ Use past gestures to determine a final classification """
        if not self.history:
            return "open_hand"

        # If at least 6 out of 10 frames detected a fist, classify as fist
        if list(self.history).count("fist") > 6:
            return "fist"
        
        return "open_hand"
