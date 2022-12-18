import cv2
import numpy as np
import time

# Replace Invisibility Cloak with original background pixels
def replace_frame(Mask):
    global frame
    for i in range(height):
        for j in range(width):
            if int(Mask[i,j]) == 255:
                for k in range(3):
                    frame[i,j,k] = img[i,j,k]
    return frame

def mask(frame):
    Upper_hsv = np.array([255,255,255])
    Lower_hsv = np.array([0,100,100])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5,5),np.uint8)
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    frame = replace_frame(Mask)
    return frame

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    for i in range(40):
        ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    if(ret):
        img = frame

    time.sleep(5)

    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if(ret):
            frame = mask(frame)
            cv2.imshow("output", frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        else:
            break
    cv2.destroyAllWindows()
    cap.release()