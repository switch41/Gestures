import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, config):
        self.config = config
        self.mp_hands = mp.solutions.hands
        self.detector = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=self.config.min_detection_confidence,
            min_tracking_confidence=self.config.min_tracking_confidence
        )

    def detect(self, frame):
        results = self.detector.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return self._format_detection(results)

    def _format_detection(self, results):
        output = []
        if results.multi_hand_landmarks:
            for i, hand in enumerate(results.multi_hand_landmarks):
                landmarks = [(lm.x, lm.y, lm.z) for lm in hand.landmark]  # Keep as tuple
                handedness = results.multi_handedness[i].classification[0].label  # Left/Right hand
                output.append({
                    'landmarks': landmarks,  
                    'handedness': handedness  
                })
        return output
