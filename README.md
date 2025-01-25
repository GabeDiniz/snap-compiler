# 📸 Snap-Compiler

Snap compiler is a Python-based automation tool designed to capture screenshots of a specific region on your screen, navigate using the right-arrow key, and compile the captured images into a single PDF file. This project is perfect for creating visual documentation, archiving slides, or saving screen content in an organized and efficient manner.

# 🚧 Prerequisites

Before running Snap-Compiler, ensure you run the following to install the required libraries

```bash
pip install -r requirements.txt
```

# 🚀 Getting Started

#### Determine the Region

Determine the region of your screenshot by running `python mouse_location.py` to figure out the x, y, x2, y2 coordinates of your screenshot location. Note: place your mouse at the top left of your screen before running this script to get accurate readings.

#### Customize the Region

Define the area of the screen you want to capture by setting the SCREENSHOT_REGION variable in main.py.

Determine Width and Height by calculating width = x2 - x1 | height = y2 - y1 that you obtained from the step above.

```
SCREENSHOT_REGION = (200, 163, 632, 831)  # x, y, width, height
```

#### Customize the Number of Screenshots

Define how many screenshots you want to take in main.py and the delay between them.

```
total_screenshots = 10
delay_between_actions = 2  # Adjust delay if needed
```

#### Screenshot and compile

Run main.py to take your screenshots, then run compile.py to compile all of the screenshots into 1 PDF. Note, if you want to change the dimensions of the screenshot on the PDF, edit the following line in compile.py. This is where the image will be placed and where dimensions of the screenshot are set.

```
pdf.image(img_path, x=0, y=0, w=210, h=297)  # A4 size
```
