import os
import argparse
import glob
from PIL import Image

def set_alpha(file_path, alpha_value):
    image = Image.open(file_path)
    # Separate the alpha channel if the image has one
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        alpha = image.convert('RGBA').split()[3]
        alpha = alpha.point(lambda i: 0 if i == 0 else alpha_value)  # Reduce opacity by 50%
        image.putalpha(alpha)
    else:
        # If the image doesn't have an alpha channel, add one
        image = image.convert('RGBA')
        alpha = Image.new('L', image.size, alpha_value)  # 128 corresponds to 50% opacity
        image.putalpha(alpha)
    image.save(file_path)

def parse_args():
    parser = argparse.ArgumentParser(description="Set alpha value of given image")
    parser.add_argument("alpha", type=int, help="Alpha value")
    parser.add_argument("files", nargs="+", help="List of files or wildcards to print contents from.")

    return parser.parse_args()

def main():
    args = parse_args()
    
    # Use glob to expand wildcards
    file_paths = [file for pattern in args.files for file in glob.glob(pattern)]
    
    if not file_paths:
        print("No matching files found.")
    else:
        for file_path in file_paths:
            set_alpha(file_path, args.alpha)

if __name__ == "__main__":
    main()
