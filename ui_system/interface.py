import cv2

class KioskInterface:
    def __init__(self, config):
        self.config = config
        self.menu_stack = []
        self.current_state = 'main_menu'
        self.selection_index = 0
        self.feedback_text = "Welcome! Use gestures to navigate."

    def update(self, gestures):
        for gesture in gestures:
            if gesture['type'] == 'swipe_left':
                self._handle_swipe(-1)
            elif gesture['type'] == 'swipe_right':
                self._handle_swipe(1)
            elif gesture['type'] == 'select':
                self._handle_selection()

        # Update feedback text based on the current state
        self.feedback_text = f"Current state: {self.current_state}, Selection: {self.selection_index}"

    def _handle_swipe(self, direction):
        if self.menu_stack:
            self.selection_index = max(0, min(
                len(self.current_menu().items) - 1,
                self.selection_index + direction
            ))
        
        self.feedback_text = f"Swiped {'left' if direction == -1 else 'right'}"

    def _handle_selection(self):
        if self.menu_stack:
            selected_item = self.current_menu().items[self.selection_index]
            if selected_item.action:
                selected_item.action()
        
        self.feedback_text = "Item selected!"

    def current_menu(self):
        return self.menu_stack[-1] if self.menu_stack else None

    def render(self, frame):
        """Renders the UI elements onto the provided frame."""
        height, width, _ = frame.shape
        cv2.putText(frame, f"State: {self.current_state}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Selection: {self.selection_index}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, self.feedback_text, (20, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        return frame