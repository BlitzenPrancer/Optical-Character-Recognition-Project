import pytesseract
import cv2

# reading the image
image = cv2.imread(r"C:\Users\user\code\pyprojects\Optical-Character-Recognition-Project\images\ocr_sample.jpg")
cv2.imshow("Input", image)
cv2.waitKey(0)