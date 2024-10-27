import cv2
import os

def compress_image_opencv(input_path, output_path, quality):
    image = cv2.imread(input_path)
    initial_size = os.path.getsize(input_path)
    
    # Ensure output_path has a filename and extension
    output_file = os.path.join(output_path, 'compressed_image.jpeg')
    
    # Save the image with specified quality
    cv2.imwrite(output_file, image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    
    compressed_size = os.path.getsize(output_file)
    return initial_size, compressed_size

input_path = r'.\assets\image\mew.jpeg'
output_path = r'.\output'  # Ensure this is a valid directory

# Ensure the directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

initial_size, compressed_size = compress_image_opencv(input_path, output_path, quality=85)
print(f'Initial Size: {initial_size} bytes')
print(f'Compressed Size: {compressed_size} bytes')
