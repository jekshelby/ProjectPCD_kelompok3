import cv2 as cv

# Variabel global untuk menyimpan koordinat awal dan akhir
start_point = None
end_point = None
cropping = False

# Fungsi callback untuk menangani event mouse
def mouse_crop(event, x, y, flags, param):
   global start_point, end_point, cropping, crop_img, image

   # Ketika klik kiri ditekan, catat koordinat awal
   if event == cv.EVENT_LBUTTONDOWN:
      start_point = (x, y)
      cropping = True

   # Ketika mouse bergerak dengan klik kiri ditahan, update titik akhir
   elif event == cv.EVENT_MOUSEMOVE:
      if cropping:
            end_point = (x, y)
            image = clone.copy()
            
            # Gambar persegi panjang yang menandai area cropping
            cv.rectangle(image, start_point, end_point, (0, 255, 0), 2)
            
            # Hitung lebar dan tinggi area crop
            width = abs(end_point[0] - start_point[0])
            height = abs(end_point[1] - start_point[1])

            # Tampilkan informasi secara vertikal
            info_texts = [
               f"Koordinat X: {x} Pixel",
               f"Koordinat Y: {y} Pixel",
               f"Lebar Crop: {width} Pixel",
               f"Tinggi Crop: {height} Pixel"
            ]
            
            # Tampilkan setiap baris teks secara vertikal
            for i, text in enumerate(info_texts):
                cv.putText(image, text, (10, 30 + i * 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            cv.imshow("Gambar", image)

   # Ketika klik kiri dilepas, catat koordinat akhir dan set cropping selesai
   elif event == cv.EVENT_LBUTTONUP:
      end_point = (x, y)
      cropping = False

      # Lakukan crop ketika kedua titik sudah dipilih
      if start_point and end_point:
            x1, y1 = start_point
            x2, y2 = end_point
            crop_img = clone[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
            cv.imshow("Hasil Crop", crop_img)

# Baca gambar
image = cv.imread('assets/image/mew.jpeg')
clone = image.copy()
crop_img = None  # Variabel untuk menyimpan hasil crop

# Tampilkan jendela dan pasang callback
cv.namedWindow("Gambar")
cv.setMouseCallback("Gambar", mouse_crop)

while True:
   # Tampilkan gambar asli
   cv.imshow("Gambar", image)

   key = cv.waitKey(1) & 0xFF

   # Tekan 'r' untuk reset gambar ke kondisi awal
   if key == ord("r"):
      image = clone.copy()
      start_point, end_point = None, None

   # Tekan 's' untuk menyimpan gambar hasil crop dan langsung keluar
   elif key == ord("s") and crop_img is not None:
      cv.imwrite('hasil_crop_mouse.jpg', crop_img)
      print("Gambar hasil crop telah disimpan sebagai 'hasil_crop_mouse.jpg'.")
      break

   # Tekan 'q' untuk keluar tanpa menyimpan
   elif key == ord("q"):
      break

# Tutup semua jendela
cv.destroyAllWindows()
