import os
import argparse

def add_suffix_to_files(input_folder, suffix):
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    for filename in os.listdir(input_folder):
        if os.path.isfile(os.path.join(input_folder, filename)):
            base_name, extension = os.path.splitext(filename)
            new_filename = f"{base_name}-{suffix}{extension}"
            old_path = os.path.join(input_folder, filename)
            new_path = os.path.join(input_folder, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed: {filename} to {new_filename}")

def parse_args():
    parser = argparse.ArgumentParser(description="Add a suffix to each file name in a folder.")
    parser.add_argument("input_folder", help="Path to the input folder containing files.")
    parser.add_argument("suffix", help="Suffix to be added to each file name.")

    return parser.parse_args()

def main():
    args = parse_args()
    add_suffix_to_files(args.input_folder, args.suffix)

if __name__ == "__main__":
    main()
