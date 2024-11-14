import cv2
import mediapipe as mp
from PIL import Image
import numpy as np

def remove_background_with_mediapipe(image_path, output_path):
    # Inisialisasi model segmentasi mediapipe
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
        
        # Baca gambar menggunakan OpenCV
        image = cv2.imread(image_path)
        if image is None:
            print("Gambar tidak ditemukan!")
            return
        
        # Konversi gambar ke RGB (mediapipe menggunakan format RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Lakukan segmentasi untuk mendeteksi orang
        results = selfie_segmentation.process(image_rgb)
        
        # Ekstrak mask dari hasil segmentasi
        mask = results.segmentation_mask > 0.5
        
        # Buat latar belakang menjadi transparan
        bg_removed = np.zeros_like(image)
        bg_removed[mask] = image[mask]

        # Konversi hasil ke format RGB untuk kompatibilitas dan simpan
        bg_removed_pil = Image.fromarray(cv2.cvtColor(bg_removed, cv2.COLOR_BGR2RGBA)).convert("RGB")
        bg_removed_pil.save(output_path)
        
        print(f"Hasil telah disimpan di: {output_path}")

# Contoh penggunaan fungsi
remove_background_with_mediapipe("output/tesAja.png", "output/no_bg.png")
