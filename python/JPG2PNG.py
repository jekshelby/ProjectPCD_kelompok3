import cv2
from PIL import Image
import os

input_file = "output/tesAja.jpeg"
output_folder = "output"
base_name = os.path.splitext(input_file)[0]
output_file = f"{base_name}.png"

image = cv2.imread(input_file)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_image = Image.fromarray(image)
pil_image.save(output_file, format="PNG")
print(f"Konversi dari JPG/JPEG ke PNG berhasil: {output_file}")
