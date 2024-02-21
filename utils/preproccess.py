import cv2
import base64
import numpy as np




def preprocess_digit_image(base64_image_data:str):

    image_data = base64_image_data.split(',')[1]

    image_bytes = base64.b64decode(image_data)

    np_array = np.frombuffer(image_bytes, dtype=np.uint8)

    image = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)

    cleaned_image:np.ndarray = image[:, :, 3]

    flattened_image = cleaned_image.flatten()

    reshaped_image = flattened_image.reshape(1, -1) // 12

    return reshaped_image

