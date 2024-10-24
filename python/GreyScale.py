# Kode 1
import cv2 as cv
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
if not os.path.exists('output'):
    os.makedirs('output')

# Memilih gambar dari file explorer
input_path = pilih_gambar()

# Memeriksa apakah ada file yang dipilih
if input_path:
    # Membaca gambar asli
    image = cv.imread(input_path)

    # Menampilkan gambar asli
    # cv.imshow('Original', image)

    # Mengonversi gambar menjadi grayscale
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Menampilkan gambar grayscale
    # cv.imshow('Grayscale', gray_image)

    # Menyimpan gambar grayscale ke dalam folder assets
    output_path = os.path.join('output', 'grayscale_image.png')
    cv.imwrite(output_path, gray_image)

    print(f"Gambar grayscale berhasil disimpan di {output_path}")

    cv.waitKey(0)
    cv.destroyAllWindows()

else:
    print("Tidak ada gambar yang dipilih.")



# Kode 2
# import cv2 as cv
# import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# # Membuka file explorer untuk memilih gambar
# def pilih_gambar():
#     root = Tk()
#     root.withdraw()  # Menyembunyikan window utama Tkinter
#     file_path = askopenfilename(
#         title="Pilih gambar",
#         filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])  # Filter hanya file gambar
#     return file_path

# # Membuat folder assets jika belum ada
# if not os.path.exists('output'):
#     os.makedirs('output')

# # Memilih gambar dari file explorer
# input_path = pilih_gambar()

# # Memeriksa apakah ada file yang dipilih
# if input_path:
#     # Membaca gambar dalam mode grayscale
#     img = cv.imread(input_path, cv.IMREAD_GRAYSCALE)

#     # Menampilkan gambar grayscale
#     cv.imshow('Grayscale Image', img)

#     # Menyimpan gambar grayscale ke dalam folder assets
#     output_path = os.path.join('output', 'grayscale_image.png')
#     cv.imwrite(output_path, img)

#     print(f"Gambar grayscale berhasil disimpan di {output_path}")

#     cv.waitKey(0)
#     cv.destroyAllWindows()

# else:
#     print("Tidak ada gambar yang dipilih.")

