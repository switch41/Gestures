class CalibrationTool:
    def __init__(self, detector, classifier):
        self.detector = detector
        self.classifier = classifier
        
    def run_calibration(self):
        print("Starting calibration...")
        self._calibrate_hand_sizes()
        self._calibrate_gesture_thresholds()
        
    def _calibrate_hand_sizes(self):
        pass
    
    def _calibrate_gesture_thresholds(self):
        pass