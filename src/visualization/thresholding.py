import numpy as np
import cv2
import pathlib
import os

image_path = 'data/raw/Mona Lisa.jpg'
image_path = pathlib.Path(image_path)

# Callback function for trackbar
def update_threshold(val: int, image: np.ndarray) -> None:
    threshold = val
    _, thresh_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('Thresholded Image', thresh_image)

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
    if image is None:
        raise FileNotFoundError(f"Unable to read the image file '{image_path}'.")

    # Create a window
    cv2.namedWindow('Thresholded Image', cv2.WINDOW_NORMAL)

    # Initialize trackbar
    initial_threshold = 127
    cv2.createTrackbar('Threshold', 'Thresholded Image', initial_threshold, 255, lambda val: update_threshold(val, image))

    # Display the initial thresholded image
    update_threshold(initial_threshold, image)

    # Wait until the user presses a key
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")