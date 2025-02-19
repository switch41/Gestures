class KioskHardwareController:
    def __init__(self, config, hardware_mode='mock'):
        self.config = config
        self.hardware_mode = hardware_mode
        self.display_brightness = 100
        self.touch_enabled = False

        if hardware_mode == 'real':
            self._initialize_hardware()

    def _initialize_hardware(self):
        """Initialize real hardware components."""
        try:
            import serial
            self.serial_conn = serial.Serial('/dev/ttyUSB0', 9600)
            print("Hardware initialized successfully.")
        except Exception as e:
            print(f"Hardware initialization failed: {e}")
            self.hardware_mode = 'mock'

    def set_brightness(self, level):
        """Set display brightness."""
        self.display_brightness = max(0, min(100, level))
        if self.hardware_mode == 'real':
            self.serial_conn.write(f'BRIGHTNESS {self.display_brightness}\n'.encode())

    def enable_touch(self, enable=True):
        """Enable or disable touch input."""
        self.touch_enabled = enable
        if self.hardware_mode == 'real':
            self.serial_conn.write(b'TOUCH_ENABLE\n' if enable else b'TOUCH_DISABLE\n')

    def cleanup(self):
        """Clean up hardware resources."""
        if self.hardware_mode == 'real':
            self.serial_conn.close()

    def sync(self, state):
        """
        Sync hardware components with the UI state.
        :param state: The current UI state that the hardware should reflect.
        """
        print(f"Syncing hardware with UI state: {state}")

        # Define default UI states if 'state' is a string
        state_mappings = {
            "main_menu": {"brightness": 80, "touch_enabled": True},
            "idle": {"brightness": 30, "touch_enabled": False},
            "active": {"brightness": 100, "touch_enabled": True},
        }

        # If state is a string, map it to predefined settings
        if isinstance(state, str):
            state = state_mappings.get(state, {"brightness": 100, "touch_enabled": False})

        # Adjust brightness
        brightness_level = state.get("brightness", 100)
        self.set_brightness(brightness_level)

        # Enable/Disable touch
        touch_status = state.get("touch_enabled", False)
        self.enable_touch(touch_status)


class MockKioskHardwareController:
    """Mock hardware controller for testing."""
    def __init__(self, config):
        self.config = config
        self.display_brightness = 100
        self.touch_enabled = False

    def set_brightness(self, level):
        self.display_brightness = max(0, min(100, level))
        print(f"[Mock] Brightness set to {self.display_brightness}")

    def enable_touch(self, enable=True):
        self.touch_enabled = enable
        print(f"[Mock] Touch {'enabled' if enable else 'disabled'}")

    def cleanup(self):
        print("[Mock] Hardware cleanup complete")
