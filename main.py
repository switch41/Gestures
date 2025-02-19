import cv2
import argparse
from config import Config
from gesture_engine.detector import HandDetector
from gesture_engine.classifier import GestureClassifier
from ui_system.interface import KioskInterface
from hardware.display_controller import KioskHardwareController
from accessibility.voice_feedback import VoiceFeedbackSystem

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['kiosk', 'debug'], default='kiosk')
    parser.add_argument('--hardware', choices=['real', 'mock'], default='mock')
    args = parser.parse_args()

    config = Config(args.mode)
    detector = HandDetector(config)
    classifier = GestureClassifier(config)
    ui = KioskInterface(config)
    hardware = KioskHardwareController(config, args.hardware)
    
    # FIXED: Removed 'config' argument from VoiceFeedbackSystem
    voice = VoiceFeedbackSystem()

    cap = cv2.VideoCapture(0)

    previous_state = None
    last_detected_gesture = None  # Store last gesture to prevent duplicate logging
    frame_counter = 0  # Add a counter to limit excessive logging

    try:
        while True:
            success, frame = cap.read()
            if not success:
                continue

            # Process frame
            hands = detector.detect(frame)
            frame_counter += 1  # Increase frame count

            # Ensure gestures is always defined
            gestures = []

            # Limit logs to every 10 frames (adjust as needed)
            if frame_counter % 10 == 0:
                print(f" Detected hands: {len(hands)}")

            if hands:
                gestures = classifier.classify(hands)
                gestures = [g for g in gestures if g['type'] is not None]  # Remove None types
                
                if gestures and gestures != last_detected_gesture:  # Only log new gestures
                    print(f" Recognized gestures: {gestures}")
                    last_detected_gesture = gestures
            else:
                if frame_counter % 10 == 0:  # Limit "No hands detected" spam
                    print(" No hands detected.")

            # Update UI state
            ui.update(gestures)

            # Sync hardware only if the state has changed
            if ui.current_state != previous_state:
                print(f" Syncing hardware with UI state: {ui.current_state}")
                hardware.sync(ui.current_state)
                previous_state = ui.current_state

            # Generate feedback
            feedback_frame = ui.render(frame)
            voice.speak(ui.feedback_text)

            # Show output in debug mode
            if args.mode == 'debug':
                cv2.imshow('Kiosk Debug', feedback_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n User exited with 'q'. Shutting down...")
                    break

    except KeyboardInterrupt:
        print("\n🚨 Program interrupted by user. Shutting down...")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        hardware.cleanup()
        print(" Cleanup complete. Program exited.")

if __name__ == "__main__":
    main()
