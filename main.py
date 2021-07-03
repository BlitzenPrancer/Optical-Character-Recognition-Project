import pytesseract
import cv2

# setting this command so that pytesseract api can work properly
# pointing this tesseract command to local installation of tesseract ocr 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# reading the image
image = cv2.imread(r"C:\Users\user\code\pyprojects\Optical-Character-Recognition-Project\images\ocr_sample.jpg")
# converting default colour code of opencv's BGR to RGB so that tesseract can understand
img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img_RGB))

# the below method will give us the details about each character and its positioning on the image
results = pytesseract.image_to_boxes(img_RGB)
ih, iw, ic = image.shape
# now i'm splitting all the results by space and converting to a list
for box in results.splitlines():
    box = box.split(' ')
    print(box) # printing the list

    # accesing bounding box location in the list
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image,(x, ih - y), (w, ih - h), (0, 255, 0), 2)

    # putting text on the image
    cv2.putText(image, box[0], (x, ih-h), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)


cv2.imshow("Input", image)
cv2.waitKey(0)
