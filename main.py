import pyautogui
import time
from fpdf import FPDF
import os

# Define the coordinates and dimensions of the area to capture
SCREENSHOT_REGION = (200, 163, 632, 831)  # x, y, width, height

# Directory to save screenshots
OUTPUT_DIR = "screenshots"
PDF_OUTPUT = "compiled_screenshots.pdf"

# Parameters
contents_screenshots = 8
total_screenshots = 2
delay_between_actions = 2  # Adjust delay if needed

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to take screenshots of a specific area and save them
def take_screenshot(index):
    screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
    file_path = os.path.join(OUTPUT_DIR, f"screenshot_{index:03d}.png")
    screenshot.save(file_path)
    return file_path

# Function to compile screenshots into a PDF
def compile_screenshots_to_pdf(output_pdf):
    pdf = FPDF()
    screenshots = sorted(os.listdir(OUTPUT_DIR))
    
    for screenshot in screenshots:
        if screenshot.endswith(".png"):
            img_path = os.path.join(OUTPUT_DIR, screenshot)
            pdf.add_page()
            pdf.image(img_path, x=0, y=0, w=210, h=297)  # A4 size
    pdf.output(output_pdf, "F")
    print(f"PDF saved as {output_pdf}")

# Main script
def main():
    for i in range(contents_screenshots + total_screenshots):
        print(f"Taking screenshot {i+1}/{contents_screenshots + total_screenshots}...")
        take_screenshot(i)
        
        print("Next page...")
        pyautogui.moveTo(515, 1020)
        pyautogui.click() 
        
        if i + 1 == contents_screenshots:
            print("FINISHED TABLE OF CONTENTS... SLEEPING FOR 15")
            time.sleep(15)
            print("\nContinuing...")
        time.sleep(delay_between_actions)
    
    print("Compiling screenshots into PDF...")
    compile_screenshots_to_pdf(PDF_OUTPUT)
    print("Done!")

if __name__ == "__main__":
    main()
