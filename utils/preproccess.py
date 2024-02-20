import cv2
import base64
import numpy as np




def preprocess_digit_image(base64_image_data:str):

    image_data = base64_image_data.split(',')[1]

    image_bytes = base64.b64decode(image_data)

    np_array = np.frombuffer(image_bytes, dtype=np.uint8)

    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    return image

