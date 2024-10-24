import cv2
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Membuka file explorer untuk memilih gambar
def pilih_gambar():
    root = Tk()
    root.withdraw()  # Menyembunyikan window utama Tkinter
    file_path = askopenfilename(
        title="Pilih gambar",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])  # Filter hanya file gambar
    return file_path

# Membuat folder output jika belum ada
if not os.path.exists('output'):
    os.makedirs('output')

# Memilih gambar dari file explorer
input_path = pilih_gambar()

if input_path:
    # Load the image
    image = cv2.imread(input_path)

    # Cek apakah gambar berhasil dimuat
    if image is None:
        print("Gagal memuat gambar. Pastikan format gambar benar dan file tidak rusak.")
    else:
        # Load the pre-trained ESPCN model
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        
        # Pastikan path model sudah benar
        model_path = 'assets/ESPCN_x4.pb'  # Perbarui path jika model disimpan di folder berbeda
        if os.path.exists(model_path):
            sr.readModel(model_path)
        else:
            print(f"Model tidak ditemukan di: {model_path}")
            exit()

        # Set the model to the desired upscale factor (x4)
        sr.setModel("espcn", 4)

        # Upscale the image
        result = sr.upsample(image)

        # Simpan hasil super-resolution ke folder output
        output_filename = os.path.basename(input_path).split('.')[0] + '_super_resolution.png'
        output_path = os.path.join('output', output_filename)

        # Cek apakah penyimpanan berhasil
        if cv2.imwrite(output_path, result):
            print(f"Hasil gambar super resolution disimpan di: {output_path}")
        else:
            print(f"Gagal menyimpan gambar di: {output_path}")

        # Tampilkan gambar asli dan hasil super resolution
        plt.figure(figsize=(10, 10))

        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')

        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        plt.title('Super Resolution Image')

        plt.show()
else:
    print("Tidak ada gambar yang dipilih.")
