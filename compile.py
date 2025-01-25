import os
import sys
from fpdf import FPDF

# Directory to save screenshots
OUTPUT_DIR = "screenshots"

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
    if len(sys.argv) != 2:
        print("Usage: python compile.py <output_filename>")
        sys.exit(1)
    elif not os.path.exists(OUTPUT_DIR):
        print(f"Error: The '{OUTPUT_DIR}' folder does not exist. Make sure you the folder exists in the current directory.")
        sys.exit(1)
    
    output_filename = sys.argv[1]
    if not output_filename.endswith(".pdf"):
        output_filename += ".pdf"

    print("Compiling screenshots into PDF...\nPlease be patient. This script can take a while if there are a lot of screenshots.")
    compile_screenshots_to_pdf(output_filename)
    print("Done!")

if __name__ == "__main__":
    main()