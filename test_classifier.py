import numpy as np
from gesture_engine.classifier import GestureClassifier

def create_sample_hand_landmarks():
    # Create sample landmarks for a hand with 2 fingers extended (peace sign)
    landmarks = []
    for i in range(21):  # MediaPipe uses 21 landmarks
        if i in [8, 12]:  # Index and middle finger tips
            landmarks.append([0.5, 0.3])  # Tips above base
        else:
            landmarks.append([0.5, 0.5])  # Base positions
    return landmarks

def main():
    # Create a simple config (empty for now as it's not used in the basic implementation)
    config = {}
    
    # Initialize the classifier
    classifier = GestureClassifier(config)
    
    # Create sample hand data
    sample_hands = [{
        'landmarks': create_sample_hand_landmarks(),
        'handedness': 'Right'
    }]
    
    # Classify the gesture
    results = classifier.classify(sample_hands)
    
    # Print results
    print("Classification Results:")
    for result in results:
        print(f"Gesture: {result['type']}")
        print(f"Number of fingers: {result['fingers']}")
        print(f"Handedness: {result['handedness']}")
        print("---")

if __name__ == "__main__":
    main() 