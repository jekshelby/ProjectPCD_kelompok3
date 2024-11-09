import cv2
import matplotlib.pyplot as plt
import os

input_path = "output/tesAja.jpeg"

image = cv2.imread(input_path)

# Load the pre-trained ESPCN model
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# path model disimpan di folder 
model_path = 'assets/model/ESPCN_x4.pb'  

# Set the model to the desired upscale factor (x4)
sr.setModel("espcn", 4)

# Upscale the image
result = sr.upsample(image)

# Post-processing: Cobalah tanpa sharpening
kernel = cv2.getGaussianKernel(5, 1.5)
sharpen_filter = -1 * kernel * kernel.T + 1
sharpened_result = cv2.filter2D(result, -1, sharpen_filter)

# Simpan hasil super-resolution ke folder output dengan nama fixed
output_path = os.path.join('output', 'super_resolution.png')

# Cek apakah penyimpanan berhasil
if cv2.imwrite(output_path, result):  # Simpan tanpa post-processing untuk uji coba
    print(f"Hasil gambar super resolution disimpan di: {output_path}")
else:
    print(f"Gagal menyimpan gambar di: {output_path}")
    
# Tampilkan gambar asli dan hasil super resolution
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1, 2, 2)

# Tampilkan hasil tanpa sharpen
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))  
plt.title('Super Resolution Image')
plt.show()