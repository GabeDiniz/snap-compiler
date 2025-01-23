import pyautogui
import time

print("Move your mouse around the screen. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # Print the position in a single line (overwrites the previous line)
        print(f"Mouse position: X={x}, Y={y}", end="\r")
        time.sleep(0.1)  # Add a small delay to avoid spamming updates
except KeyboardInterrupt:
    print("\nProgram stopped.")
