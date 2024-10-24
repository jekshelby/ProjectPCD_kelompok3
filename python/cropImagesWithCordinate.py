import cv2

# Membaca gambar
image = cv2.imread('colors.jpg')

# Mendapatkan dimensi gambar
h, w, _ = image.shape
print(f"Ukuran gambar: {w}x{h}")

# Input dari pengguna untuk menentukan area crop
x = int(input("Masukkan koordinat x (titik awal crop): "))
y = int(input("Masukkan koordinat y (titik awal crop): "))
crop_width = int(input("Masukkan lebar crop: "))
crop_height = int(input("Masukkan tinggi crop: "))

# Memastikan crop tidak melebihi ukuran gambar
if x + crop_width > w or y + crop_height > h:
 print("Ukuran crop melebihi ukuran gambar.")
else:
   # Crop gambar
   cropped_image = image[y:y+crop_height, x:x+crop_width]

   # Menampilkan gambar yang di-crop
   cv2.imshow("Cropped Image", cropped_image)

   # Menunggu input dari keyboard
   key = cv2.waitKey(0) & 0xFF  # Mendapatkan input dari keyboard

   if key == ord('s'):  # Jika tombol 's' ditekan
      # Simpan gambar hasil crop
      cv2.imwrite('cropped_image.jpg', cropped_image)
      print("Gambar berhasil disimpan sebagai 'cropped_image.jpg'")
   else:
      print("Gambar tidak disimpan.")

   # Menutup semua jendela
   cv2.destroyAllWindows()

# Inpu sesuai object
# koordinat x = 385
# koordinat y = 155
# lebar crop = 466
# tinggi crop = 458