import cv2   #opencv
import time  #delay
import imutils  #resize

# Camera Initialize (0, 1 ya -1 jo aapke system par chale)
cam = cv2.VideoCapture(0)  
time.sleep(1)

firstFrame = None
area = 500

while True:
    ret, img = cam.read()   # Read frame from camera
    
    if not ret or img is None:
        break
        
    text = "Normal"
    img = imutils.resize(img, width=500)  # Resize for speed
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # Color to Grayscale
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)  # Smoothing

    if firstFrame is None:
        firstFrame = gaussianImg  # Capture first frame as background
        continue
        
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)  # Absolute difference
    _, threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)  # Thresholding
    threshImg = cv2.dilate(threshImg, None, iterations=2) # Dilation

    # Finding Contours
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for c in cnts:
        if cv2.contourArea(c) < area:   # Filter out small noise
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Draw Green Box
        text = "Moving Object detected"
        
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Moving Object Detection", img)

    # Windows safe exit key
    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"): 
        break

cam.release()
cv2.destroyAllWindows()
