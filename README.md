# Gesture Kiosk System

## Overview
This project is a gesture-based kiosk system that utilizes computer vision and machine learning to detect and classify hand gestures. It provides an interactive, touchless interface for kiosks, enhancing accessibility and user experience.

## Features
- **Real-time hand detection** using OpenCV and Mediapipe
- **Gesture classification** for different kiosk interactions
- **UI Integration** to update the kiosk interface based on recognized gestures
- **Hardware synchronization** to control kiosk hardware components
- **Voice feedback system** for accessibility

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/kiosk-gesture.git
   ```
2. Navigate to the project directory:
   ```bash
   cd kiosk-gesture
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
- Run `python main.py --mode debug` to enable debug mode with UI preview.
- Use predefined hand gestures to interact with the kiosk system.
- The system provides voice feedback and updates the UI accordingly.

## Improvements Needed
The following features are yet to be implemented:
- **Swipe gestures** to enable navigation between options.
- **Enhanced voice command support** to improve accessibility.
- **Better UI synchronization** to prevent lagging issues.
- **Optimized gesture recognition** to improve accuracy in varying lighting conditions.

## Future Enhancements
To take this project to the next level, the following upgrades can be considered:
- **AI-powered gesture prediction** to anticipate user movements.
- **Integration with external APIs** for real-time data fetching.
- **Support for multiple users** with personalized gesture profiles.
- **Cloud-based model training** for continuous improvement in accuracy.

## Contributor
- **switch41**

## License
This project is licensed under the MIT License.

