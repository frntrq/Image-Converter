import sys, os
from PIL import Image

def convert_to_PNG(original_image_path, converted_img_path):
    original = Image.open(original_image_path)
    original.save(converted_img_path)
    print("All Done!")
    
convert_to_PNG(sys.argv[1], sys.argv[2])