import cv2
import numpy as np
import streamlit as st
import os
import pathlib
import textwrap
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to set up the image input for Gemini API
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI for uploading and processing images
st.title("Image Processing and Content Generation with Google Gemini")
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

# Image processing operations
if uploaded_file is not None:
    # Convert the uploaded image to a format OpenCV can process
    image = Image.open(uploaded_file)
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Display original image
    st.image(image, caption='Original Image', use_column_width=True)

    # Grayscale
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    st.image(gray_image, caption='Grayscale Image', use_column_width=True)

    # Blur
    blurred_image = cv2.GaussianBlur(image_cv, (5, 5), 0)
    st.image(blurred_image, caption='Blurred Image', use_column_width=True)

    # Sharpen
    sharpened_image = cv2.Laplacian(image_cv, cv2.CV_64F)
    sharpened_image = cv2.convertScaleAbs(sharpened_image)  # Normalize the sharpened image
    st.image(sharpened_image, caption='Sharpened Image', use_column_width=True)

    # Edge Detection
    edges = cv2.Canny(image_cv, 100, 200)
    st.image(edges, caption='Edge-Detected Image', use_column_width=True)

    # Resize
    resized_image = cv2.resize(image_cv, (0, 0), fx=0.5, fy=0.5)
    st.image(resized_image, caption='Resized Image', use_column_width=True)

    # Cropping - Assumes specific crop values (can be customized)
    x, y, w, h = 50, 50, 100, 100  # Example crop dimensions
    cropped_image = image_cv[y:y+h, x:x+w]
    st.image(cropped_image, caption='Cropped Image', use_column_width=True)

    # Rotate
    rotated_image = cv2.rotate(image_cv, cv2.ROTATE_90_CLOCKWISE)
    st.image(rotated_image, caption='Rotated Image', use_column_width=True)

    # Flip
    flipped_image_vert = cv2.flip(image_cv, 0)
    flipped_image_horiz = cv2.flip(image_cv, 1)
    st.image(flipped_image_vert, caption='Vertically Flipped Image', use_column_width=True)
    st.image(flipped_image_horiz, caption='Horizontally Flipped Image', use_column_width=True)

    # Threshold
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    st.image(binary_image, caption='Thresholded Image', use_column_width=True)

   
