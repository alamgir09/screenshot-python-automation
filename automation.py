#!/usr/bin/python3

import os 
import shutil
import glob

desktop_path = os.path.expanduser('~/Desktop')
screenshots_folder = os.path.expanduser('~/Desktop/Screenshots')


# # Create Screenshots folder if doesn't exist
# if not os.path.exists(screenshots_folder):
#     os.makedirs(screenshots_folder)

# Pattern for screen shots
pattern = "Screen Shot *"

# Move the screenshots
for screenshot in glob.glob(os.path.join(desktop_path, pattern)):
    shutil.move(screenshot, screenshots_folder)
    print(f"Moved: {screenshot}")

print("All screenshots have been moved.")

