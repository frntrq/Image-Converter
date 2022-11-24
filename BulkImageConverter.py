import sys, os
from PIL import Image

def convert_to_PNG(original_image_folder, converted_image_folder, convert_to_format):

    #create converted image folder if not exists
    if not os.path.exists(converted_image_folder):
        os.mkdir(converted_image_folder)

    for file in os.listdir(original_image_folder):
        file_dir = original_image_folder + "/" + file
        print(file_dir)
        current_img = Image.open(file_dir)
        name, ext = os.path.splitext(file)
        converted_image = converted_image_folder + "/" + name + "." + convert_to_format
        current_img.save(converted_image)

    print("All Done!")
    
convert_to_PNG(sys.argv[1], sys.argv[2], sys.argv[3])