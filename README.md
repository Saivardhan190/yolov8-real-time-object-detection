🚀 Real-Time Object Detection using YOLOv8

This project implements a real-time object detection system using YOLOv8 by Ultralytics.
The application can detect multiple objects in uploaded images through a deployed Streamlit web app, as well as via local webcam inference.

🌐 Live Demo

👉 Open the App

✨ Features

Real-time object detection using YOLOv8

Image upload–based detection via Streamlit Web App

Supports multiple object classes (COCO dataset)

Fast and accurate inference

Modular and easy-to-extend Python implementation

Ready for custom dataset training

🛠️ Technologies Used

Python

YOLOv8 (Ultralytics)

OpenCV

PyTorch

Streamlit

▶️ How to Run the Project Locally
1️⃣ Install dependencies
pip install ultralytics streamlit opencv-python-headless

2️⃣ Run the Streamlit web app
streamlit run app.py


Then open:

http://localhost:8501

3️⃣ Run real-time detection via webcam (CLI)
yolo predict model=yolov8n.pt source=0

4️⃣ Run detection on an image
yolo predict model=yolov8n.pt source=example.jpg

📂 Output

Detection results are automatically saved to:

runs/detect/predict/

📸 Sample Output

Add screenshots or a demo GIF here showing detected objects.

🔮 Future Improvements

Train YOLOv8 on a custom dataset

Add object counting

Support video uploads

Improve inference speed with model optimization

Add class-filtering options in UI

📄 License

MIT License
