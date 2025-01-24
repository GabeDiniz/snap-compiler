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

Define the area of the screen you want to capture by setting the SCREENSHOT_REGION variable in the script.

Determine Width and Height by calculating width = x2 - x1 | height = y2 - y1.

```
SCREENSHOT_REGION = (200, 163, 632, 831)  # x, y, width, height
```
