import os
from PIL import Image
from pathlib import Path

# Path to the directory that contains the images
src_folder_path = '/Users/chris/Projects/punks-assets-master/accessories'

# Path to the directory where the grayscale images will be stored
dst_folder_path = src_folder_path + '-bw'

# Create the destination directory if it doesn't exist
Path(dst_folder_path).mkdir(parents=True, exist_ok=True)

# List all files in the directory
for filename in os.listdir(src_folder_path):
    # Check if the file is an image
    if filename.endswith('.png'):
        # Open the image file
        img = Image.open(os.path.join(src_folder_path, filename)).convert('RGBA')

        # Convert RGB channels to grayscale
        gray = img.convert('L')

        # Create new RGBA image using grayscale for RGB and original alpha
        final = Image.merge('RGBA', (gray, gray, gray, img.split()[3]))

        # Save the grayscale image to the destination directory
        final.save(os.path.join(dst_folder_path, filename))

print('All PNG images have been converted to grayscale and saved to the new folder.')
