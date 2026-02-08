# Real-Time Object Detection using YOLOv8

This project implements a real-time object detection system using the YOLOv8 deep learning model by Ultralytics. The system is capable of detecting multiple objects in live webcam streams or images with high accuracy.

---

## 🚀 Features
- Real-time object detection using webcam
- Pre-trained YOLOv8 model for fast inference
- Supports multiple object classes (COCO dataset)
- Easy to extend with custom datasets
- Clean and modular Python implementation

---

## 🛠 Technologies Used
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install ultralytics opencv-python
2️⃣ Run real-time detection (webcam)
yolo predict model=yolov8n.pt source=0

3️⃣ Run detection on an image
yolo predict model=yolov8n.pt source=example.jpg


Results will be saved in:

runs/detect/predict/

📌 Sample Output

Add screenshots or demo GIF here

🔮 Future Improvements

Train YOLOv8 on a custom dataset

Add object counting functionality

Deploy as a web application using Streamlit

Improve inference speed with model optimization

📄 License

MIT License


---

## ✅ STEP 2: Add Proof (Screenshots or Video)

This is **huge for recruiters**.

### 🔹 Do this
1. Run YOLO again:
```bat
yolo predict model=yolov8n.pt source=0


Take a screenshot (bounding boxes visible)

Create a folder in repo:

screenshots/


Upload the image to GitHub

Add it under Sample Output in README
