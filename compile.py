from fpdf import FPDF
import os

# Directory to save screenshots
OUTPUT_DIR = "screenshots"
PDF_OUTPUT = "compiled_screenshots.pdf"

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
    print("Compiling screenshots into PDF...")
    compile_screenshots_to_pdf(PDF_OUTPUT)
    print("Done!")

if __name__ == "__main__":
    main()