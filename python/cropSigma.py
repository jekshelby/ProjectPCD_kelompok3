import cv2
import numpy as np

# Baca gambar
image_path = "output/tesAja.jpeg"
image = cv2.imread(image_path)
clone = image.copy()

# Variabel global
rect_start = (100, 100)  # Posisi awal (kiri atas)
rect_end = (300, 400)    # Posisi akhir (kanan bawah)
selected_corner = None   # Corner yang sedang di-drag
dragging = False         # Status dragging

# Fungsi untuk menggambar persegi dengan pegangan (handle)
def draw_rectangle_with_handles(img, start, end):
    temp_image = img.copy()
    cv2.rectangle(temp_image, start, end, (0, 255, 0), 2)

    # Tambahkan titik pegangan di sudut persegi
    handle_size = 10
    corners = [
        start, (end[0], start[1]),  # Kiri atas, kanan atas
        end, (start[0], end[1])    # Kanan bawah, kiri bawah
    ]
    for corner in corners:
        cv2.rectangle(temp_image,
                      (corner[0] - handle_size, corner[1] - handle_size),
                      (corner[0] + handle_size, corner[1] + handle_size),
                      (0, 0, 255), -1)
    return temp_image

# Fungsi untuk memeriksa apakah klik berada di handle
def is_in_handle(x, y, handle_center, handle_size=10):
    return (handle_center[0] - handle_size <= x <= handle_center[0] + handle_size and
            handle_center[1] - handle_size <= y <= handle_center[1] + handle_size)

# Fungsi callback mouse
def mouse_callback(event, x, y, flags, param):
    global rect_start, rect_end, selected_corner, dragging, image, clone

    handle_size = 10
    corners = [
        rect_start, (rect_end[0], rect_start[1]),  # Kiri atas, kanan atas
        rect_end, (rect_start[0], rect_end[1])    # Kanan bawah, kiri bawah
    ]

    if event == cv2.EVENT_LBUTTONDOWN:
        # Periksa apakah klik berada di salah satu handle
        for i, corner in enumerate(corners):
            if is_in_handle(x, y, corner, handle_size):
                selected_corner = i
                dragging = True
                break

    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        # Ubah posisi sudut berdasarkan corner yang di-drag
        if selected_corner == 0:       # Kiri atas
            rect_start = (x, y)
        elif selected_corner == 1:     # Kanan atas
            rect_start = (rect_start[0], y)
            rect_end = (x, rect_end[1])
        elif selected_corner == 2:     # Kanan bawah
            rect_end = (x, y)
        elif selected_corner == 3:     # Kiri bawah
            rect_start = (x, rect_start[1])
            rect_end = (rect_end[0], y)

        # Gambarkan ulang
        image = draw_rectangle_with_handles(clone, rect_start, rect_end)

    elif event == cv2.EVENT_LBUTTONUP:
        # Hentikan dragging
        dragging = False
        selected_corner = None

# Tampilkan gambar awal dengan persegi dan pegangan
image = draw_rectangle_with_handles(clone, rect_start, rect_end)
cv2.imshow("Interactive Rectangle", image)

# Pasang callback
cv2.setMouseCallback("Interactive Rectangle", mouse_callback)

# Loop untuk menunggu aksi pengguna
while True:
    cv2.imshow("Interactive Rectangle", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):  # Simpan area cropping jika tombol 'c' ditekan
        x1, y1 = rect_start
        x2, y2 = rect_end

        # Pastikan koordinat valid
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        cropped_image = clone[y1:y2, x1:x2]
        output_path = "output/cropped_image_mouse.png"
        cv2.imwrite(output_path, cropped_image)
        print(f"Hasil cropping disimpan di: {output_path}")

    if key == ord("q"):  # Keluar program jika tombol 'q' ditekan
        break

cv2.destroyAllWindows()
