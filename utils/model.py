import joblib
import cv2
import numpy as np
from .preproccess import preprocess_digit_image
from sklearn.neural_network import MLPClassifier


class MNISTModel:

    model: MLPClassifier = joblib.load("euler_mnist.model")

    def predict_digit(self, digit_data: str):

        image_data = preprocess_digit_image(digit_data)

        predicted_value = self.model.predict(image_data)

        return predicted_value
