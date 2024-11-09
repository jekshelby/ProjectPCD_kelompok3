import cv2
import matplotlib.pyplot as plt
import os

input_path = "output/tesAja.jpeg"

# Membaca gambar input
image = cv2.imread(input_path)

# Membuat objek DnnSuperResImpl
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Path model ESPCN disimpan
model_path = 'assets/model/ESPCN_x4.pb'

# Membaca model
sr.readModel(model_path)

# Set model dengan faktor skala x4
sr.setModel("espcn", 4)

# Upscale gambar
result = sr.upsample(image)

# Post-processing: Cobalah tanpa sharpening jika tidak perlu
# Hanya simpan gambar tanpa sharpening terlebih dahulu untuk uji coba
output_path = os.path.join('output', 'super_resolution.jpg')

# Cek apakah penyimpanan berhasil
if cv2.imwrite(output_path, result):
    print(f"Hasil gambar super resolution disimpan di: {output_path}")
else:
    print(f"Gagal menyimpan gambar di: {output_path}")

# Tampilkan gambar asli dan hasil super resolution
plt.figure(figsize=(10, 10))

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# Menampilkan hasil super resolution
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Super Resolution Image')

# Tampilkan gambar
plt.show()
