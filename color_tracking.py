import imutils # Resize
import cv2
import numpy as np

# ====== STANDARD FIXED HSV RANGES (No Camera Tuning Required) ======
# Hum yahan standard RED color track kar rahe hain
redLower = (0, 100, 100)
redUpper = (10, 255, 255)

# Camera Initialize (0 matlab default webcam, agar dikkat ho toh 1 ya -1 karein)
camera = cv2.VideoCapture(0) 

while True:
    (grabbed, frame) = camera.read() # Read the Frame
    
    # Safety Check: Agar camera khali frame de toh crash na ho
    if not grabbed or frame is None:
        print("Camera frame nahi mil paa raha hai.")
        break

    frame = imutils.resize(frame, width=1000) # Consistent processing width
    
    blurred = cv2.GaussianBlur(frame, (11, 11), 0) # Noise reduction
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) # Convert BGR to HSV

    mask = cv2.inRange(hsv, redLower, redUpper) # Masking the target color
    mask = cv2.erode(mask, None, iterations=2)   # Cleaning edge pixels
    mask = cv2.dilate(mask, None, iterations=2)  # Solidifying target shape

    # Finding Contours (Boundaries)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    center = None
    
    # Agar screen par targeted color ka koi object hai
    if len(cnts) > 0:
        # Sabse bada contour select karna (noise ignore karne ke liye)
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        # Centroid (Center point) nikalne ke liye moments ka use
        M = cv2.moments(c)
        
        # Zero division error se bachne ke liye safe condition
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            # Agar object ka size ek limit se bada hai (radius > 10 pixels)
            if radius > 10:
                # Target object par yellow color ka outer circle banana
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Exact center point par ek red dot draw karna
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                
                print(f"Center Coordinate: {center}, Object Radius: {radius}")
                
                # Direction Automation Control Logic
                if radius > 250:
                    print("Action: STOP (Object too close)")
                else:
                    if center[0] < 150:
                        print("Direction Action: MOVE RIGHT")
                    elif center[0] > 450:
                        print("Direction Action: MOVE LEFT")
                    elif radius < 250:
                        print("Direction Action: MOVE FRONT")
                    else:
                        print("Direction Action: STOP")
                        
    cv2.imshow("Color Tracking System", frame)
    
    # Windows surface mapping exit check
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
