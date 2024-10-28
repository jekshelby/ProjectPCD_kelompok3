import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os


def compress_image(image_path, quality=70):
    # Baca gambar
    img = cv2.imread(image_path)
    
    # Encode gambar dengan kompresi JPEG
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)  # Menggunakan '.jpg' untuk encoding ke format JPEG
    
    # Decode gambar yang sudah dikompres
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    
    return decoded_img, encoded_img  # Mengembalikan gambar hasil decode dan gambar encoded untuk penyimpanan

# Fungsi untuk memilih file gambar
def select_image():
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    file_path = filedialog.askopenfilename(title="Pilih gambar", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    return file_path

# Fungsi untuk membuat folder jika belum ada
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Contoh penggunaan
image_path = select_image()  # Meminta pengguna untuk memilih gambar
if image_path:
    original_img = cv2.imread(image_path)
    compressed_img, encoded_img = compress_image(image_path, quality=70)

    # Menampilkan hasil
    cv2.imshow('Original', original_img)
    cv2.imshow('Compressed', compressed_img)

    # Menentukan folder penyimpanan
    save_directory = './output'
    ensure_directory_exists(save_directory)  # Membuat folder jika belum ada

    # Membuat path lengkap untuk menyimpan gambar
    save_path = os.path.join(save_directory, 'compressed_image.jpg')

    # Menyimpan gambar hasil kompresi
    with open(save_path, 'wb') as f:
        f.write(encoded_img)  # Menyimpan gambar terkompresi

    print(f"Gambar telah disimpan di {save_path}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Tidak ada gambar yang dipilih.")
