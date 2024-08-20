import os
import cv2
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
def get_gemini_response(input_text, image_parts, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, image_parts[0]['data'], prompt])
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

if uploaded_file is not None:
    # Convert the uploaded image to a format OpenCV can process
    image = Image.open(uploaded_file)
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Display original image
    st.image(image, caption='Original Image', use_column_width=True)

    # Perform various image processing operations
    operations = {
        "Grayscale": lambda img: cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
        "Blurred": lambda img: cv2.GaussianBlur(img, (5, 5), 0),
        "Sharpened": lambda img: cv2.convertScaleAbs(cv2.Laplacian(img, cv2.CV_64F)),
        "Edge-Detected": lambda img: cv2.Canny(img, 100, 200),
        "Resized": lambda img: cv2.resize(img, (0, 0), fx=0.5, fy=0.5),
        "Cropped": lambda img: img[50:150, 50:150],  # Example crop dimensions
        "Rotated": lambda img: cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE),
        "Vertically Flipped": lambda img: cv2.flip(img, 0),
        "Horizontally Flipped": lambda img: cv2.flip(img, 1),
        "Thresholded": lambda img: cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)[1]
    }

    for op_name, op_func in operations.items():
        processed_img = op_func(image_cv)
        st.image(processed_img, caption=f'{op_name} Image', use_column_width=True)

    # Generate description about the image automatically
    image_parts = input_image_setup(uploaded_file)
    default_prompt = "Describe the content of this image in detail."
    description = get_gemini_response("Describe the image content", image_parts, default_prompt)
    st.write("Image Description:")
    st.write(description)

    # Optionally, allow custom prompt input for additional content generation
    prompt = st.text_input("Enter a custom prompt:")
    if prompt:
        response = get_gemini_response("Analyze this image", image_parts, prompt)
        st.write("Generated Content:")
        st.write(response)

    # Additional section for detailed analysis
    submit = st.button("Explain the Image to Me 👇")
    if submit:
        input_prompt = """
        You are an expert in object detection. Your task is to provide information based on the image below in the following format:
        
        1. What is written in the image
        2. Write a brief paragraph on the image
        """
        response = get_gemini_response(input_prompt, image_parts, input_prompt)
        st.subheader("Here is the Response:")
        st.write(response)
