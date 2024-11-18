import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def cartoonize_image(image_path):
    # Membaca gambar
    img = cv2.imread(image_path)
    if img is None:
        print("Gambar tidak ditemukan!")
        return None, None

    # Memperhalus warna dengan filter bilateral (dengan parameter yang lebih baik)
    color_filtered = cv2.bilateralFilter(img, d=9, sigmaColor=100, sigmaSpace=100)

    # Konversi ke skala abu-abu
    gray = cv2.cvtColor(color_filtered, cv2.COLOR_BGR2GRAY)

    # Penguatan tepi dengan Canny dan Adaptive Threshold (penyesuaian threshold)
    edges_canny = cv2.Canny(gray, threshold1=100, threshold2=200)
    edges_adaptive = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=11, C=2
    )
    edges_combined = cv2.bitwise_or(edges_canny, edges_adaptive)

    # Memperhalus masker tepi dengan Gaussian blur
    edges_smoothed = cv2.GaussianBlur(edges_combined, (5, 5), 0)

    # Penajaman warna menggunakan HSV (penyesuaian saturasi dan kecerahan)
    hsv = cv2.cvtColor(color_filtered, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.add(s, 60)  # Meningkatkan saturasi
    v = cv2.add(v, 40)  # Meningkatkan kecerahan
    enhanced_hsv = cv2.merge([h, s, v])
    color_enhanced = cv2.cvtColor(enhanced_hsv, cv2.COLOR_HSV2BGR)

    # Penajaman gambar menggunakan kernel sharpen yang lebih tajam
    sharpening_kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
    sharpened = cv2.filter2D(color_enhanced, -1, sharpening_kernel)

    # Gabungkan tepi dengan gambar berwarna menggunakan alpha blending
    edges_colored = cv2.cvtColor(edges_smoothed, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.addWeighted(sharpened, 0.9, edges_colored, 0.3, 0)  # Meningkatkan alpha blending

    return img, cartoon

def save_image(image, default_filename):
    # Menyimpan gambar
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")],
                                             initialfile=default_filename)
    if save_path:
        cv2.imwrite(save_path, image)
        messagebox.showinfo("Sukses", f"Gambar berhasil disimpan di {save_path}")

def display_image(image, title="Image", window_size=(600, 600)):
    # Menampilkan gambar di Tkinter
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Mengubah warna dari BGR ke RGB untuk Tkinter
    image_pil = Image.fromarray(image)
    image_pil.thumbnail(window_size)  # Sesuaikan ukuran gambar agar pas dalam jendela
    image_tk = ImageTk.PhotoImage(image_pil)

    # Membuat jendela baru dan menambahkan gambar
    window = tk.Toplevel()
    window.title(title)
    label = tk.Label(window, image=image_tk)
    label.image = image_tk  # Menyimpan referensi untuk mencegah gambar hilang
    label.pack()

    # Menambahkan tombol simpan
    save_button = tk.Button(window, text="Simpan Gambar", command=lambda: save_image(image, title))
    save_button.pack(pady=10)

def main():
    # Membuka dialog untuk memilih gambar
    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama

    # Membuka dialog file
    file_path = filedialog.askopenfilename(
        title="Pilih Gambar",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if not file_path:
        messagebox.showinfo("Informasi", "Tidak ada gambar yang dipilih.")
        return

    # Proses kartunisasi
    original, cartoon = cartoonize_image(file_path)
    if original is None or cartoon is None:
        messagebox.showerror("Gagal", "Gagal memproses gambar.")
        return

    # Menampilkan gambar asli dan hasil kartun
    display_image(original, title="Gambar Asli")
    display_image(cartoon, title="Gambar Kartun")

    root.mainloop()

if __name__ == "__main__":
    main()
