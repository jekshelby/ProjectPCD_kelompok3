import cv2 as cv
import numpy as np
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
    # Variabel untuk menggambar persegi dan menyimpan koordinat
    drawing = False
    mode = 'rectangle'  # Mode awal: 'rectangle' atau 'brush'
    brush_radius = 10  # Ukuran brush
    selected_areas = []  # Menyimpan area persegi panjang
    brush_strokes = []  # Menyimpan titik brush

    # Fungsi untuk menggambar persegi atau brush berdasarkan klik mouse
    def draw_selection(event, x, y, flags, param):
        global ix, iy, drawing, img

        if mode == 'rectangle':
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
                selected_areas.append((ix, iy, final_x, final_y))
                cv.rectangle(img, (ix, iy), (final_x, final_y), (0, 255, 0), 2)
                cv.imshow('Image', img)

        elif mode == 'brush':
            if event == cv.EVENT_LBUTTONDOWN:
                drawing = True
                cv.circle(img, (x, y), brush_radius, (0, 255, 0), -1)
                brush_strokes.append((x, y))

            elif event == cv.EVENT_MOUSEMOVE:
                if drawing:
                    cv.circle(img, (x, y), brush_radius, (0, 255, 0), -1)
                    brush_strokes.append((x, y))

            elif event == cv.EVENT_LBUTTONUP:
                drawing = False

    # Load gambar yang dipilih
    img = cv.imread(input_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2BGRA)  # Ubah menjadi format 4 channel (RGBA)

    # Cek ukuran gambar, jika lebih besar dari 450x600, resize
    height, width = img.shape[:2]
    if height > 600 and width > 450:
        img = cv.resize(img, (450, 600))
        print("Gambar di-resize ke 450x600.")
    else:
        print("Gambar tidak lebih besar dari 450x600, ditampilkan dalam ukuran asli.")

    cv.namedWindow('Image')
    cv.setMouseCallback('Image', draw_selection)

    while True:
        cv.imshow('Image', img)
        key = cv.waitKey(1)
        
        if key == 27:  # Tekan ESC untuk keluar
            break
        elif key == ord('m'):  # Tekan "m" untuk mengganti mode
            mode = 'brush' if mode == 'rectangle' else 'rectangle'
            print(f"Mode seleksi berubah menjadi: {mode}")

    # Menghapus area yang dipilih
    for (x1, y1, x2, y2) in selected_areas:
        img[y1:y2, x1:x2, 3] = 0  # Set alpha channel menjadi 0 untuk area persegi panjang

    # Menghapus area berdasarkan brush strokes
    for (x, y) in brush_strokes:
        cv.circle(img, (x, y), brush_radius, (0, 0, 0, 0), -1)  # Set alpha channel menjadi 0 untuk brush strokes

    # Simpan gambar hasil ke dalam folder output
    output_path = os.path.join('output', 'output_image.png')

    # Konversi ke format Image PIL dan simpan
    result_img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGRA2RGBA))
    result_img.save(output_path)
    print(f"Gambar tanpa bagian yang dipilih berhasil disimpan di {output_path}")

    # Tampilkan hasil tanpa bagian yang dipilih
    cv.imshow('Final Image', img)
    cv.waitKey(0)

else:
    print("Tidak ada gambar yang dipilih.")

cv.destroyAllWindows()
