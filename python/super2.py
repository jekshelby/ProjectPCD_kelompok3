import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('2.jpg')

# Load the pre-trained LapSRN model
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel('LapSRN_x4.pb')  # Model pretrained for 4x resolution

# Set the model to the desired upscale factor (x4)
sr.setModel("lapsrn", 4)

# Upscale the image
result = sr.upsample(image)

# Show the original and upscaled images
plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Super Resolution Image')

plt.show()
