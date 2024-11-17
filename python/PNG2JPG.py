import cv2
from PIL import Image

input_file = "output/wew.png"
output_folder = "output"
base_name = input_file.split('.')[0]
output_file = f"{base_name}.jpg"

image = cv2.imread(input_file)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pil_image = Image.fromarray(image)
pil_image.save(output_file, format="JPEG", quality=100)
print(f"Konversi dari PNG ke JPG berhasil: {output_file}")
