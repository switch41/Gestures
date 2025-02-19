GESTURE_TEMPLATES = {
    'open_hand': {
        'finger_states': [1, 1, 1, 1, 1],  # All fingers extended
        'threshold': 0.9
    },
    'fist': {
        'finger_states': [0, 0, 0, 0, 0],   # All fingers folded
        'threshold': 0.85
    },
    'point': {
        'finger_states': [0, 1, 0, 0, 0],   # Only index finger extended
        'threshold': 0.88
    }
}

SWIPE_THRESHOLDS = {
    'min_velocity': 0.5,  # px/frame
    'min_distance': 0.3   # normalized screen width
}