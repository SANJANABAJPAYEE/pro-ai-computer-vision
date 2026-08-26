# Pro-AI Computer Vision Projects

This repository contains real-time Artificial Intelligence and Computer Vision projects .

---

## 📦 Project 1: Real-Time Moving Object Detection System
A system designed to detect movement and track dynamic entities in live video streams.

### 🛠️ Key Steps & Workflow
1. **Image Resizing:** Optimized input frame dimension using `imutils` for lighter computation.
2. **Grayscale Conversion:** Transformed color channels to intensity scales for efficient pixel analysis.
3. **Gaussian Smoothing:** Applied blur to clear out sensor noise and unnecessary pixel grains.
4. **Frame Subtraction:** Calculated the absolute difference (`cv2.absdiff`) against the background frame.
5. **Thresholding & Contours:** Binarized spatial changes and mapped active boundaries using structural contours.

---

## 🎭 Project 2: Real-Time Face Detection Pipeline
An automated pipeline that locates and highlights human faces within live webcam configurations.

### 🛠️ Key Steps & Workflow
1. **Algorithm Loading:** Initialized the pre-trained **Haar Cascade Frontalface Classifier**.
2. **Pre-processing:** Normalized image inputs by switching color matrices into standard grayscale.
3. **Multi-Scale Scaling:** Leveraged `detectMultiScale` to scan multi-distance facial architectures.
4. **Spatial Geometry:** Parsed coordinate points `(x, y, w, h)` to render instantaneous identification markers.

---

## 💻 Tech Stack Used
- **Language:** Python
- **Libraries:** OpenCV (`opencv-contrib-python`), `imutils`

