import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,fram = cap.read()
    frame= cv2.medianBlur(fram,5)
    #frame = cv2.GaussianBlur(fram,(5,5),0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    pic= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    cv2.imshow('Camera',frame)
    cv2.imshow('Threshhold',pic)
    #print(pic)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
#When Everything is done then release te camera
cap.release()
cv2.destroyAllWindows()
