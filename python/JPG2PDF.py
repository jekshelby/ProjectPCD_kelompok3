from PIL import Image

input_file = "output/tesAja.jpeg"
output_folder = "output"
base_name = input_file.split('.')[0]
output_file = f"{base_name}.pdf"

image = Image.open(input_file)

# Mengonversi gambar ke mode RGB (PDF membutuhkan gambar dalam mode RGB)
if image.mode != "RGB":
    image = image.convert("RGB")

# Menyimpan gambar dalam format PDF
image.save(output_file, format="PDF")
print(f"Konversi dari JPG/JPEG ke PDF berhasil: {output_file}")
