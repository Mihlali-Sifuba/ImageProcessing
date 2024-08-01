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

    if image is None:
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    
    # Apply Otsu's optimum thresholding method
    k, thresholded_image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

    print(k)
    # Create a resizable window
    cv2.namedWindow("Otsu's Thresholding", cv2.WINDOW_NORMAL)

    # Display the result
    cv2.imshow("Otsu's Thresholding", thresholded_image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")