import cv2

image = cv2.imread("jjopoo.jpeg")

print("Image Shape:", image.shape)

print("Pixel Value at (0,0):", image[0,0])