# Image Classification using TensorFlow and TensorFlow Hub

This project demonstrates how to perform image classification using the MobileNetV2 model from TensorFlow Hub. The script loads an image, processes it, and classifies it into one of the 1000 categories of the ImageNet dataset.

## Requirements

- Python 3.x
- TensorFlow 2.x
- TensorFlow Hub
- PIL (Pillow)
- NumPy

To install the necessary libraries, you can use the following pip command:
 
pip install tensorflow tensorflow-hub pillow numpy

Usage
Prepare your image: Save the image you want to classify in the same directory as the script, or provide the path to its location.
Modify the script: Replace "image.jpeg" in the image_file_path variable with the path to your image file.
Run the script: Execute the script using Python. The script will output the top 5 predicted labels along with their confidence levels.
Files
classify_image.py: The main Python script that loads the model, processes the image, and performs the classification.
Function Descriptions
load_and_prepare_image(file_path)
Loads and prepares an image for classification. The image is converted to RGB, resized to 224x224 pixels, and preprocessed according to MobileNetV2's requirements.

classify_image(image)
Classifies the image using the pre-loaded MobileNetV2 model. Outputs the top 5 predictions with their confidence levels.

Example Output
After running the script with an image of a Labrador retriever, you might see an output similar to:

makefile
Copy code
labrador_retriever: 95.67%
golden_retriever: 2.30%
kuvasz: 0.52%
chesapeake_bay_retriever: 0.41%
curly-coated_retriever: 0.37%
This output indicates the model's confidence in each of its top 5 predictions.

License
This project is licensed under the MIT License
