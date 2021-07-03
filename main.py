import pytesseract
import cv2

# setting this command so that pytesseract api can work properly
# pointing this tesseract command to local installation of tesseract ocr 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# reading the image
image = cv2.imread(r"C:\Users\user\code\pyprojects\Optical-Character-Recognition-Project\images\ocr_sample.jpg")
# converting default colour code of opencv's BGR to RGB so that tesseract can understand
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_RGB))


cv2.imshow("Input", image)
cv2.waitKey(0)
