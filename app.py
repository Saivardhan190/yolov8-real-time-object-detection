import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="YOLOv8 Object Detection", layout="centered")

st.title("🔍 YOLOv8 Real-Time Object Detection")
st.write("Upload an image to detect objects using YOLOv8")

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)

    results = model.predict(img_array, conf=0.25)

    annotated_frame = results[0].plot()
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    st.image(annotated_frame, caption="Detected Objects", use_column_width=True)
