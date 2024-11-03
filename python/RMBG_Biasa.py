import cv2 as cv
import os
from rembg import remove

image = cv.imread("output/tesAja.jpeg")

gray_image = remove(image)

output_path = os.path.join('output', 'NoBG_image.png')
cv.imwrite(output_path, gray_image)

cv.waitKey(0)
cv.destroyAllWindows()