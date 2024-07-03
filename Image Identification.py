# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qoe8_XWMt0HCPRLxmDeKs5w1HOroROZW
"""

pip install tensorflow

import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np

# Load a pre-trained model (e.g., MobileNetV2) from TensorFlow Hub
model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4")
])
model.build([None, 224, 224, 3])  # Batch input shape

def load_and_prepare_image(file_path):
    # Load and prepare an image from local file system
    image = Image.open(file_path).convert('RGB')  # Convert image to RGB
    image = image.resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.array([image])
    return image


def classify_image(image):
    # Classify the image and return top 5 categories
    predictions = model.predict(image)
    # Adjust the predictions array to match the expected shape of 1000 classes
    predictions = np.squeeze(predictions)
    predictions = predictions[1:]  # Skip the first prediction (background class)
    top_5 = tf.keras.applications.mobilenet_v2.decode_predictions(np.expand_dims(predictions, axis=0), top=5)[0]
    return top_5

# Example usage
image_file_path = "image.jpeg" # Replace with your local image file path
image = load_and_prepare_image(image_file_path)
predictions = classify_image(image)

for _, label, confidence in predictions:
    print(f"{label}: {confidence*10:.2f}%")