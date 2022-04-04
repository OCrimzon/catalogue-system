#importing libraries
import cv2
from pyzbar import pyzbar

#function for reading the barcode/qr-code
def readCodes(frame):
    Codes = pyzbar.decode(frame)
    for code in Codes:
        x, y, w, h = code.rect
    
        #decoding the info from the code, then drawing a rectangle around it to visually see if the machine has detected the code
        CodesInfo = code.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #adding text to the top of the rectangle to show the decoded information
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, CodesInfo, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        #exporting the information into a text document.
        with open("codeResult.txt", mode = 'w') as file:
            file.write("Recognised QR-Code: " + CodesInfo)

    return frame

#main function for turning on the camera and then calling the decoding function
#

def mainFunction():
    #turning on the camera using opencv
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #keep running until the "Esc" key is pressed
    while ret:
        ret, frame = camera.read()
        frame = readCodes(frame)
        cv2.imshow('QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #release the camera that we turned on
    camera.release()
    cv2.destroyAllWindows()
#call the main function to trigger the program
if __name__ == '__main__':
    mainFunction()