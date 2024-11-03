import cv2 as cv

image = cv.imread("output/tesAja.jpeg")

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

result_path = file_path.replace(".jpg", "_grayscale.jpg")
cv.imwrite(result_path, gray_image)

cv.destroyAllWindows()