import os
import sys
from PIL import Image, ImageFilter

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ folder exists, if not, then create one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    # assume user will enter "/" for folder
    cleanname = os.path.splitext(filename)[0]
    # convert images to png and also save them
    img.save(f"{output_folder}{cleanname}.png", "png")
    print("The file is successfully converted!")

