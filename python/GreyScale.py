import cv2 as cv
import os

image = cv.imread("output/tesAja.jpeg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

output_path = os.path.join('output', 'grayscale_image.png')
cv.imwrite(output_path, gray_image)

cv.waitKey(0)
cv.destroyAllWindows()