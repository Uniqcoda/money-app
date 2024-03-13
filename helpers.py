from PIL import Image
import os

def process_img(input_path, target_size):
    with Image.open(input_path) as img:
        # Crop to a square aspect ratio based on the shortest side
        min_side = min(img.size)
        # If w,h => 4000,3000 
        left = (img.width - min_side) / 2 # 500
        top = (img.height - min_side) / 2   # 0
        right = (img.width + min_side) / 2  # 3500
        bottom = (img.height + min_side) / 2  # 3000
        cropped_img = img.crop((left, top, right, bottom))

        # Resize the cropped image to the target size
        resized_img = cropped_img.resize(target_size)
    return resized_img

def process_images(input_folder, output_folder, target_size=(1024, 1024)):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    processed_count = 0

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        try:
            # Resize the cropped image to the target size
            resized_img = process_img(input_path, target_size)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path)

            processed_count += 1
        except (IOError, OSError, Image.UnidentifiedImageError):
            print(f"Skipping non-image file: {filename}")

    print("Image processing complete.")
    return processed_count

def get_total(labels):
    total_pence = 0
    for label in labels:
        pence = int(label[:-1])  # Extracting numeric value from label
        total_pence += pence

    # Convert total pence to pounds and pence
    total_pounds = total_pence / 100
    return "{:.2f}".format(total_pounds)
