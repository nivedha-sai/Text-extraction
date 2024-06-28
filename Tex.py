import cv2
from PIL import Image
import pytesseract

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    cv2.imshow('Text detection', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('test1.jpg', image)
        break

cap.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Ensure the path includes tesseract.executable
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    image_path = 'test1.jpg'
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print(text)

tesseract()
