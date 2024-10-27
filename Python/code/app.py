import os
import time
from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf
import io

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load ESRGAN model using TensorFlow's built-in methods
MODEL_PATH = r'C:\Users\Shoun\esg\Python\code'  # Directory containing saved_model.pb and variables/
model = tf.saved_model.load(MODEL_PATH)

def preprocess_image(image_data):
    hr_image = tf.image.decode_image(image_data)
    if hr_image.shape[-1] == 4:
        hr_image = hr_image[..., :-1]
    if hr_image.shape[-1] == 1:
        hr_image = tf.image.grayscale_to_rgb(hr_image)  # Convert grayscale to RGB
    hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
    hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
    hr_image = tf.cast(hr_image, tf.float32)
    return tf.expand_dims(hr_image, 0)

def save_image(image):
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

@app.route('/upscale', methods=['POST'])
def upscale_image():
    print("Received a request")
    file = request.files['image']
    image_data = file.read()
    hr_image = preprocess_image(image_data)
    print("Image processed")

    start = time.time()
    inference_fn = model.signatures["serving_default"]
    inference_result = inference_fn(hr_image)
    print("Inference result keys:", inference_result.keys())  # Print available keys
    fake_image = inference_result[next(iter(inference_result.keys()))]  # Use the first key found
    fake_image = tf.squeeze(fake_image)
    print("Time Taken: %f" % (time.time() - start))

    img_byte_arr = save_image(fake_image)

    print("Sending response")
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True)
