import cv2 as cv
import urllib.request
import numpy as np
import pytesseract as ocr
import serial

ser = serial.Serial("/dev/ttyACM0", 115200)
url='http://192.168.1.63/cam-hi.jpg'
img=None
ctr = 0

def decode_image():
    img_cap=urllib.request.urlopen(url)
    img_np=np.array(bytearray(img_cap.read()),dtype=np.uint8)
    return cv.imdecode(img_np,-1)

def extract_ocr(img):
    _, binary_image = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    cv.imshow("Binary", binary_image)
    return ocr.image_to_string(binary_image)
    
while True:
    img = decode_image()
    cv.imshow("ESP32-Cam", img)
    print("ctr", ctr)

    if ctr > 3:
        ctr = 0
        text = extract_ocr(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
        print("*******", text)
        if "RED" in text:
            print("RED Detected")
            ser.write(b'1')
        elif "BLUE" in text:
            print("BLUE Detected")
            ser.write(b'2')
        else:
            print("No Text Detection")
    else:
        ctr+=1

    k = cv.waitKey(5)
    if k == ord('q'):
        break

cv.destroyAllWindows()
