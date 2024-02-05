import time

from helpers import process_images

# Set your input and output folders
input_folder = 'raw_images'
output_folder = 'images'

# Record start time
start_time = time.time()

# Call the process_images function
processed_count = process_images(input_folder, output_folder)

# Record end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
print(f"Number of processed images: {processed_count}")
