#! /usr/bin/python

import argparse
from PIL import Image
import os

def change_color(input_folder, output_folder, target_color, replacement_color):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            image = image.convert("RGBA")

            data = list(image.getdata())
            new_data = [(r, g, b, a) if (r, g, b) != target_color else replacement_color for r, g, b, a in data]

            new_image = Image.new("RGBA", image.size)
            new_image.putdata(new_data)

            output_path = os.path.join(output_folder, filename)
            new_image.save(output_path)

            print(f"Processed: {filename}")

def parse_args():
    parser = argparse.ArgumentParser(description="Change one color to another in multiple images.")
    parser.add_argument("input_folder", help="Path to the input folder containing images.")
    parser.add_argument("output_folder", help="Path to the output folder for modified images.")
    parser.add_argument("target_color", type=lambda x: tuple(map(int, x.split(','))), help="Target color (R,G,B). Example: 255,0,0")
    parser.add_argument("replacement_color", type=lambda x: tuple(map(int, x.split(','))), help="Replacement color (R,G,B). Example: 0,255,0")

    return parser.parse_args()

def main():
    args = parse_args()
    change_color(args.input_folder, args.output_folder, args.target_color, args.replacement_color)

if __name__ == "__main__":
    main()
