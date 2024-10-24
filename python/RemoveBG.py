# import cv2 as cv
# from rembg import remove

# image = cv.imread('Siddiq.png')
# new_image = remove(image)

# cv.imwrite('frame1.png',new_image)
# # cv.imshow('frame',new_image)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv
from rembg import remove
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Membuka file explorer untuk memilih gambar
def pilih_gambar():
    root = Tk()
    root.withdraw()  # Menyembunyikan window utama Tkinter
    file_path = askopenfilename(
        title="Pilih gambar",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])  # Filter hanya file gambar
    return file_path

# Membuat folder assets jika belum ada
if not os.path.exists('assets'):
    os.makedirs('assets')

# Memilih gambar dari file explorer
input_path = pilih_gambar()

# Memeriksa apakah ada file yang dipilih
if input_path:
    image = cv.imread(input_path)

    # Menghapus background gambar
    new_image = remove(image)

    # Menentukan path untuk menyimpan gambar baru
    output_path = os.path.join('assets', 'output_image.png')

    # Menyimpan gambar hasil tanpa background ke dalam folder assets
    cv.imwrite(output_path, new_image)

    print(f"Gambar berhasil disimpan di {output_path}")

    # Jika ingin menampilkan gambar, aktifkan baris ini
    # cv.imshow('Hasil', new_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("Tidak ada gambar yang dipilih.")
