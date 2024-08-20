import os
import base64
import google.generativeai as genai
import streamlit as st
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def prep_image(image_file):
    """Prepare the image file for API request."""
    try:
        # Convert the uploaded file to base64
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')

        # Create an image file object
        file = {
            "mime_type": image_file.type,
            "data": encoded_image
        }
        return file
    except Exception as e:
        st.error(f"Error preparing image: {e}")
        return None

def extract_text_from_image(image_file, prompt):
    """Extract text from the image using Google Gemini."""
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content([image_file, prompt])
        return response.text
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        return None

# Streamlit UI setup
st.title("Text Extraction from Images Using Google Gemini")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Prepare the image
    image_file = prep_image(uploaded_file)
    
    if image_file:
        # Get text extraction prompt from the user
        prompt = st.text_input("Enter a prompt for text extraction:", "Extract the text in the image verbatim")
        
        if st.button("Extract Text"):
            # Extract text from image
            text = extract_text_from_image(image_file, prompt)
            
            if text:
                st.subheader("Extracted Text")
                st.write(text)
            else:
                st.write("Failed to extract text from the image.")
