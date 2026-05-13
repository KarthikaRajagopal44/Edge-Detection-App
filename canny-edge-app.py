import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os

# Set page title
st.set_page_config(page_title="Canny Edge Detection")

DEMO_IMAGE = 'edge.jpg'

@st.cache_data
def edge_detection(image, low_thres, high_thresh):
    # PIL images are already RGB. We convert directly to GRAY for Canny.
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edged = cv2.Canny(gray_image, low_thres, high_thresh)
    return edged

st.title("Canny Edge Detection")

img_file_buffer = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", 'png'])

# Logic to handle Image Loading
if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
else:
    # Check if demo image exists to prevent crash
    if os.path.exists(DEMO_IMAGE):
        image = np.array(Image.open(DEMO_IMAGE))
    else:
        st.warning("Please upload an image to get started.")
        st.stop() # Stops the app until an image is uploaded

# UI Sliders
st.subheader('Original Image')
st.image(image, caption="Original Image", use_column_width=True) 

low_thres = st.slider('Lower threshold', min_value=0, max_value=255, value=80)
high_thresh = st.slider('High threshold', min_value=0, max_value=255, value=100)

# Ensure low is not higher than high
if low_thres > high_thresh:
    high_thresh = low_thres + 5

# Run processing
edges = edge_detection(image, low_thres, high_thresh)

st.subheader('Edged Image')
st.image(edges, caption="Edged Image", use_column_width=True) 

# About Section
st.markdown('''
---
# About Author
Hey this is **Karthika Rajagopal**. I hope you like the application.
I am looking for **Collaboration** or **Freelancing** in the field of **Deep Learning** and **Computer Vision**.

- [Resume](https://drive.google.com/file/d/16aKmdHryldvx3OPNwmHhxW-DAoQOypvX/view?usp=sharing)
- [LinkedIn](www.linkedin.com/in/karthika-rajagopal7116)
- [GitHub](https://github.com/KarthikaRajagopal44)
''')