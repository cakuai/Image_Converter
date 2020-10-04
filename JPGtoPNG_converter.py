import os
import sys
from PIL import Image, ImageFilter

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create one

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# loop through pokedex

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    # assume user will enter "/" for folder
    cleanname = os.path.splitext(img)
    # convert images to png
    img.save(f"{output_folder}{cleanname}.png", "png")
# save them to the new folder
