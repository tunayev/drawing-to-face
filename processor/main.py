
import argparse
import os
from utils import Cropper
from utils import Combiner


""" def get_input(prompt):
    value = input(prompt)
    return int(value) if value else None

input_dir = input("Enter the path to the images: ")
output_dir = input("Enter the path to save the output images: ")

cropped_width = get_input("Cropped width: ")
cropped_height = get_input("Cropped height: ")
desired_width = get_input("Desired width: ")
desired_height = get_input("Desired height: ")
top_offset = get_input("Offset from the top (leave blank if it should be centered): ")
left_offset = get_input("Offset from left (leave blank if it should be centered): ") """


parser = argparse.ArgumentParser()
# Select mode, crop or combine
parser.add_argument("--mode", required=True, choices=["crop", "combine"], help="crop or combine")
parser.add_argument("--input_dir_a", help="path to folder A")
parser.add_argument("--input_dir_b", help="path to folder B")
parser.add_argument("--input_dir", help="path to folder containing images")
parser.add_argument("--output_dir", help="output path")
parser.add_argument("--cropped_width", help="cropped width")
parser.add_argument("--cropped_height", help="cropped height")
parser.add_argument("--desired_width", help="desired width")
parser.add_argument("--desired_height", help="desired height")
parser.add_argument("--top_offset", required=False, default=0, help="offset from the top")
parser.add_argument("--left_offset", required=False, default=0, help="offset from left")

args = parser.parse_args()
output_dir, input_dir, cropped_width, cropped_height, desired_width, desired_height, top_offset, left_offset, input_dir_a, input_dir_b = args.output_dir, args.input_dir, args.cropped_width, args.cropped_height, args.desired_width, args.desired_height, args.top_offset, args.left_offset, args.input_dir_a, args.input_dir_b

if args.mode == "crop":
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            processor = Cropper(image_path)
            cropped_image = processor.crop(cropped_width, cropped_height, top_offset, left_offset)
            processed_image = processor.resize(cropped_image, desired_width, desired_height)
            processor.save_image(processed_image, output_dir)
elif args.mode == "combine":
    # Combine images in two directories with the Combiner class, match the names of the images
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir_a):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            image_a_path = os.path.join(input_dir_a, filename)
            sketchName = filename.split('.')[0] + '-sz1.JPG'
            # check if the sketch exists
            if not os.path.exists(os.path.join(input_dir_b, sketchName)):
                continue
            processor = Combiner(image_a_path, os.path.join(input_dir_b, sketchName))
            combined_image = processor.combine()
            processor.save_image(combined_image, output_dir)
