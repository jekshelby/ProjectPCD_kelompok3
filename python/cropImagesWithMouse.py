import cv2

# Variabel global untuk menyimpan koordinat awal dan akhir
start_point = None
end_point = None
cropping = False

# Fungsi callback untuk menangani event mouse
def mouse_crop(event, x, y, flags, param):
   global start_point, end_point, cropping

   # Ketika klik kiri ditekan, catat koordinat awal
   if event == cv2.EVENT_LBUTTONDOWN:
      start_point = (x, y)
      cropping = True

   # Ketika mouse bergerak dengan klik kiri ditahan, update titik akhir
   elif event == cv2.EVENT_MOUSEMOVE:
      if cropping:
            end_point = (x, y)

   # Ketika klik kiri dilepas, catat koordinat akhir dan set cropping selesai
   elif event == cv2.EVENT_LBUTTONUP:
      end_point = (x, y)
      cropping = False

      # Lakukan crop ketika kedua titik sudah dipilih
      if start_point and end_point:
            x1, y1 = start_point
            x2, y2 = end_point
            crop_img = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]

            # Simpan dan tampilkan hasil crop
            cv2.imwrite('hasil_crop_mouse.jpg', crop_img)
            cv2.imshow("Hasil Crop", crop_img)

# Baca gambar
image = cv2.imread('colors.jpg')
clone = image.copy()

# Tampilkan jendela dan pasang callback
cv2.namedWindow("Gambar")
cv2.setMouseCallback("Gambar", mouse_crop)

while True:
   # Tampilkan gambar asli, dengan area crop (jika ada)
   if not cropping and start_point and end_point:
      cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
   cv2.imshow("Gambar", image)

   key = cv2.waitKey(1) & 0xFF

   # Tekan 'r' untuk reset gambar ke kondisi awal
   if key == ord("r"):
      image = clone.copy()
      start_point, end_point = None, None

# Tekan 'q' untuk keluar
   elif key == ord("q"):
      break

# Tutup semua jendela
cv2.destroyAllWindows()
