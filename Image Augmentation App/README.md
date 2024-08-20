

---

# Image Processing and Content Generation with Google Gemini

This Streamlit application allows users to upload an image and perform various image processing operations, such as grayscale conversion, blurring, sharpening, edge detection, resizing, cropping, rotation, flipping, and thresholding. Additionally, the app integrates with the Google Gemini API to generate content based on the processed image and a user-provided prompt.

## Features

- **Image Upload**: Upload images in JPG, PNG, or JPEG formats.
- **Image Processing**:
  - **Grayscale**: Convert the image to grayscale.
  - **Blur**: Apply Gaussian blur to the image.
  - **Sharpen**: Sharpen the image using Laplacian filter.
  - **Edge Detection**: Detect edges in the image using Canny edge detector.
  - **Resize**: Resize the image by scaling down.
  - **Crop**: Crop a specified region from the image.
  - **Rotate**: Rotate the image 90 degrees clockwise.
  - **Flip**: Flip the image vertically and horizontally.
  - **Threshold**: Apply binary thresholding to the image.
- **Content Generation**: Use Google Gemini API to generate content based on the image and a user-provided prompt.

## Prerequisites

- Python 3.6 or later
- Streamlit
- OpenCV
- NumPy
- Pillow
- python-dotenv
- Google Generative AI SDK

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

3. **Upload an image** and view the processed results.

4. **Enter a prompt** and click the "Generate Content with Google Gemini" button to get generated content based on the image and prompt.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Gemini API**: For providing advanced generative capabilities.
- **Streamlit**: For building interactive web applications with ease.
- **OpenCV**: For image processing functionalities.
- **NumPy**: For numerical operations.

