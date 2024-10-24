import cv2 as cv
import numpy as np
from rembg import remove
from PIL import Image
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

# Membuat folder output jika belum ada
if not os.path.exists('output'):
    os.makedirs('output')

# Memilih gambar dari file explorer
input_path = pilih_gambar()

if input_path:
    # Variabel untuk menggambar persegi
    drawing = False
    ix, iy = -1, -1
    final_x, final_y = -1, -1

    # Fungsi untuk menggambar persegi berdasarkan klik mouse
    def draw_rectangle(event, x, y, flags, param):
        global ix, iy, drawing, final_x, final_y, img

        if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y

        elif event == cv.EVENT_MOUSEMOVE:
            if drawing:
                img_temp = img.copy()
                cv.rectangle(img_temp, (ix, iy), (x, y), (0, 255, 0), 2)
                cv.imshow('Image', img_temp)

        elif event == cv.EVENT_LBUTTONUP:
            drawing = False
            final_x, final_y = x, y
            cv.rectangle(img, (ix, iy), (final_x, final_y), (0, 255, 0), 2)
            cv.imshow('Image', img)

    # Load gambar yang dipilih
    img = cv.imread(input_path)

    # Cek ukuran gambar, jika lebih besar dari 450x600, resize
    height, width = img.shape[:2]
    if height > 600 and width > 450:
        img = cv.resize(img, (450, 600))
        print("Gambar di-resize ke 450x600.")
    else:
        print("Gambar tidak lebih besar dari 450x600, ditampilkan dalam ukuran asli.")

    cv.namedWindow('Image')
    cv.setMouseCallback('Image', draw_rectangle)

    while True:
        cv.imshow('Image', img)
        key = cv.waitKey(1)
        if key == 27:  # Tekan ESC untuk keluar
            break

    # Cek apakah area yang dipilih valid
    if ix >= 0 and iy >= 0 and final_x >= 0 and final_y >= 0 and ix < final_x and iy < final_y:
        selected_area = img[iy:final_y, ix:final_x]

        if selected_area.size > 0:  # Pastikan area yang dipilih tidak kosong
            selected_area_pil = Image.fromarray(cv.cvtColor(selected_area, cv.COLOR_BGR2RGB))
            background_removed = remove(selected_area_pil)

            # Simpan gambar tanpa background ke dalam folder output
            output_path = os.path.join('output', 'output_image.png')

            # Ubah background_removed ke format RGB
            background_removed = background_removed.convert("RGBA")

            try:
                background_removed.save(output_path)  # Simpan hasil remove dengan PIL
                print(f"Gambar berhasil disimpan di {output_path}")
            except Exception as e:
                print(f"Error saat menyimpan gambar: {e}")

            # Tampilkan hasil tanpa background
            background_removed_np = np.array(background_removed)
            cv.imshow('Background Removed', background_removed_np)
            cv.waitKey(0)
        else:
            print("Area yang dipilih kosong.")
else:
    print("Tidak ada gambar yang dipilih.")

cv.destroyAllWindows()
