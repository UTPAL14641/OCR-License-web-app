# OCR-License-web-app

This web application uses Flask and EasyOCR to perform Optical Character Recognition (OCR) on images. It allows users to upload an image, processes it using OCR, and displays the result with highlighted text.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Flask
- OpenCV (cv2)
- EasyOCR

You can install them using the following command:

```bash
pip install flask opencv-python easyocr

Clone the repository:

git clone https://github.com/UTPAL14641/flask-image-ocr-app.git
cd flask-image-ocr-app

Install the required Python packages:
pip install -r requirements.txt
Run the Flask app:
bash
python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Upload an image using the provided form, and click the "Process Image" button.

View the OCR result with highlighted text on the result page.

Folder Structure
templates: Contains HTML templates used by Flask.
static: Stores static assets, such as stylesheets and processed images.
Troubleshooting
If you encounter issues, consider the following troubleshooting steps:

Check the browser console for errors.
Inspect the terminal running the Flask app for any error messages.
Ensure correct folder structure and file paths.
Verify the dependencies are correctly installed.
