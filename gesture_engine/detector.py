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
        # Convert mediapipe results to standard format
        output = []
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                output.append({
                    'landmarks': hand.landmark,
                    'handedness': results.multi_handedness[0].classification[0].label
                })
        return output