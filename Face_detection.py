import cv2

# 1. Loading haarcascade face algorithm (XML File)
# Dhyan rahe ki XML file aapke isi 'pro-ai' folder mein honi chahiye
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Initialize camera (0/1/-1 jo aapke system par chale)
cam = cv2.VideoCapture(0) 

while True:
    # 3. Reading frame from camera
    ret, frame = cam.read()
    
    # Safety check agar camera frame na de paye
    if not ret or frame is None:
        break
        
    # 4. Converting color image into grayscale image
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 5. Obtaining face coordinates by passing algorithm
    faces = face_cascade.detectMultiScale(grayImg, scaleFactor=1.3, minNeighbors=5)
    
    # 6. Drawing rectangle on the face coordinates
    for (x, y, w, h) in faces:
        # Green box banana face par
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        
        # Face ke upar text likhna
        cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
    # 7. Display output
    cv2.imshow('Face Detection System', frame)
    
    # 'q' key dabane par exit karna
    key = cv2.waitKey(10) & 0xFF
    if key == ord('q'):
        break

# Cleanup
cam.release()
cv2.destroyAllWindows()
