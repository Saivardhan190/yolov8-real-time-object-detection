# 🚀 Real-Time Object Detection Web Application using YOLOv8
📌 Project Overview

This project is a real-time object detection system built using YOLOv8 (You Only Look Once), a state-of-the-art deep learning model for object detection developed by Ultralytics.

The application allows users to upload images through a web interface and automatically detects and localizes objects using bounding boxes and class labels. The model is deployed as a Streamlit web application, making it easily accessible without requiring local setup.

This project demonstrates end-to-end machine learning engineering, including model inference, dependency management, cloud deployment, and troubleshooting real-world deployment issues.

# 🌐 Live Demo
  https://yolov8-real-time-object-detection-ghytfmpxr4kkk2qypagjut.streamlit.app/


# 🎯 Problem Statement

Object detection is a core computer vision task used in applications such as:

Surveillance systems

Autonomous driving

Retail analytics

Healthcare imaging

Smart cities

The challenge is to detect multiple objects in a single image accurately and efficiently, while keeping inference time low enough for real-time usage.

# 🧠 Solution Approach

This project solves the problem using YOLOv8, a single-stage object detection model that performs object localization and classification in a single forward pass of a neural network.

## Why YOLOv8?

High accuracy with low latency

Single-stage detection (faster than RCNN-based approaches)

Industry adoption and active maintenance

Easy integration with Python applications

## ⚙️ How YOLOv8 Works (High-Level)

The input image is passed through a Convolutional Neural Network (CNN) backbone.

## The model predicts:

Bounding box coordinates

Object confidence scores

Class probabilities

Non-Maximum Suppression (NMS) removes duplicate or overlapping detections.

Final detections are rendered as bounding boxes with class labels.

YOLOv8 processes the entire image in one pass, enabling real-time performance.

## 🏗️ Project Architecture
yolov8-real-time-object-detection/
│
├── app.py                  # Streamlit web application
├── runtime.txt             # Python version configuration (Python 3.11)
├── requirements.txt        # Dependency list for Streamlit deployment
├── README.md               # Project documentation
└── runs/                   # YOLO output directory (auto-generated)

# ✨ Key Features

🔍 Object detection using YOLOv8

🖼 Upload image and get instant detection results

📦 Pretrained COCO dataset support (80 object classes)

🌐 Deployed as a web application using Streamlit

🧩 Modular design for easy extension

🚀 Cloud-ready deployment

# 🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
YOLOv8 (Ultralytics)	Object detection model
PyTorch	Deep learning framework
OpenCV	Image processing
Streamlit	Web application framework


# ▶️ Running the Project Locally
1️⃣ Clone the repository
git clone https://github.com/Saivardhan190/yolov8-real-time-object-detection.git
cd yolov8-real-time-object-detection

2️⃣ Install dependencies
pip install ultralytics streamlit opencv-python-headless

3️⃣ Run the Streamlit app
streamlit run app.py


Open your browser at:

http://localhost:8501

4️⃣ Run YOLO via command line (optional)
yolo predict model=yolov8n.pt source=0

## 📂 Output Results

Detected images with bounding boxes are automatically saved to:

runs/detect/predict/

## ☁️ Deployment Details

The application is deployed on Streamlit Cloud.

Deployment Challenges Solved:

Fixed Python version incompatibility by pinning Python 3.11

Resolved OpenCV installation issues using opencv-python-headless

Disabled Poetry-based installs by removing pyproject.toml

Managed dependency conflicts via requirements.txt

Cleared Streamlit cache to rebuild clean environments

This reflects real-world ML deployment problem-solving, not just model development.

## 📸 Sample Output

Add screenshots or a GIF here showing detected objects with bounding boxes.

##🔮 Future Enhancements

Train YOLOv8 on a custom dataset

Add object counting functionality

Support video file uploads

Improve inference speed with model optimization

Add class-selection filters in UI

##📄 License

MIT License
