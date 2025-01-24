import pyautogui
import time
from fpdf import FPDF
import os

# Define the coordinates and dimensions of the area to capture
SCREENSHOT_REGION = (230, 140, 590, 780)  # x, y, width, height

# Directory to save screenshots
OUTPUT_DIR = "screenshots"

# Parameters
contents_screenshots = 8
total_screenshots = 636
delay_between_actions = 2  # Adjust delay if needed

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to take screenshots of a specific area and save them
def take_screenshot(index):
    screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
    file_path = os.path.join(OUTPUT_DIR, f"screenshot_{index:03d}.png")
    screenshot.save(file_path)
    return file_path


# Main script
def main():
    for i in range(contents_screenshots + total_screenshots):
        print(f"Taking screenshot {i+1}/{contents_screenshots + total_screenshots}...")
        take_screenshot(i)
        
        print("Next page...")
        pyautogui.moveTo(522, 1005)
        pyautogui.click() 
        
        if i + 1 == contents_screenshots:
            print("FINISHED TABLE OF CONTENTS... SLEEPING FOR 15")
            time.sleep(15)
            print("\nContinuing...")
        time.sleep(delay_between_actions)

if __name__ == "__main__":
    main()
