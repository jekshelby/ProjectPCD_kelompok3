# Ocr show with terimnal only
import cv2 as cv
import easyocr

# read image
image_path = 'image/test1.png'
img = cv.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# hanya menampilkan teks dan skor di terminal
for t in text_:
    _, text, score = t

    if score > threshold:
        print(f"'{text}'")
