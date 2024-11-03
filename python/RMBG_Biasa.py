import cv2 as cv
from rembg import remove

image = cv.imread("output/tesAja.jpeg")

RB_image = remove(image)

result_path = file_path.replace(".jpg", "_grayscale.jpg")
cv.imwrite(result_path, RB_image)

cv.destroyAllWindows()