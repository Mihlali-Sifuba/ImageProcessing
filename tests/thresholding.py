import cv2
import os
import pathlib


image_path = 'data/raw/Mona Lisa.jpg'
image_path = pathlib.Path(image_path)
try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale


    # Apply simple thresholding
    _, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Create a resizable window
    cv2.namedWindow('Simple Thresholding', cv2.WINDOW_NORMAL)

    # Display the result
    cv2.imshow('Simple Thresholding', thresholded_image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")