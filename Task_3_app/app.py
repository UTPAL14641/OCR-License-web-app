from flask import Flask, render_template, request, redirect, url_for
import cv2
import easyocr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    input_folder = 'uploads'
    output_folder = 'static/output'

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(input_folder, filename)
        file.save(file_path)

        output_filename = process_image(file_path, output_folder)
        output_path = os.path.join(output_folder, output_filename)

        return render_template('result.html', input_image=filename, output_image=output_filename)

    return redirect(url_for('index'))

def process_image(input_path, output_folder):
    reader = easyocr.Reader(['en'])
    img = cv2.imread(input_path)
    results = reader.readtext(img)

    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Draw the red box
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        # Draw the green text
        cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    output_filename = f"output_{os.path.basename(input_path)}"
    output_path = os.path.join(output_folder, output_filename)
    cv2.imwrite(output_path, img)

    return output_filename  # Return just the filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

if __name__ == '__main__':
    app.run(debug=True)
