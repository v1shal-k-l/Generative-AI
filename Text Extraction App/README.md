

---

# Text Extraction from Images Using Google Gemini

This Streamlit application allows users to upload an image and extract text from it using the Google Gemini API. The app converts the image to a format suitable for the API, sends it for processing, and displays the extracted text based on user-provided prompts.

## Features

- **Image Upload**: Upload images in JPG, JPEG, or PNG formats.
- **Text Extraction**: Extract text from the uploaded image using the Google Gemini API.
- **Custom Prompts**: Provide custom prompts to guide the text extraction process.

## Prerequisites

- Python 3.6 or later
- Streamlit
- Pillow
- google-generativeai
- python-dotenv

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the root directory and add your Google API key:

    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

2. **Open your browser** and navigate to `http://localhost:8501` to access the application.

3. **Upload an image** in JPG, JPEG, or PNG format.

4. **Enter a prompt** for text extraction. The default prompt is "Extract the text in the image verbatim."

5. **Click the "Extract Text" button** to process the image and extract the text.

6. **View the extracted text** displayed below the image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Gemini API**: For providing advanced text extraction capabilities.
- **Streamlit**: For building interactive web applications.
- **Pillow**: For image processing functionalities.

## Contact

For questions or feedback, please contact [Your Name] at [Your Email Address].

---
