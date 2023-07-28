# Image Comparison App

The Image Comparison App is a simple graphical user interface (GUI) application that allows users to load two images, compare them using the Structural Similarity Index (SSIM), and visualize the differences between the images.

### Requirements

* Python 3.6+
* OpenCV (cv2) library
* NumPy library
* scikit-image library
* Tkinter library
* Pillow (PIL) library
* Install the required libraries using pip:

### Install the required libraries using pip:
 ```shell
pip install opencv-python numpy scikit-image pillow
 ```
## How to Run the App
* Clone the repository or download the ImageDiff.py file to your local machine.
* Open a terminal or command prompt and navigate to the directory containing ImageDiff.py.
* Run the application using Python:
```
python3 ImageDiff.py
```
## Usage
* Upon running the application, a graphical user interface (GUI) window will appear.
* Click the "Load Images" button to load two images for comparison. A file dialog will open, allowing you to choose the images you want to compare.
* The SSIM score and result will be displayed below the "Load Images" button. The SSIM score indicates the similarity between the two images, with 1.0 being identical and 0.0 being completely different.
* A message will be displayed based on the SSIM score. If the images are identical, the message will indicate "The images are identical." If the images are very similar (SSIM score > 0.8), the message will display "The images are very similar." Otherwise, the message will state "The images have differences."
* The difference image between the two loaded images will be displayed below the result message. The difference image highlights the areas where the two images differ.
* You can try loading different pairs of images and observe the SSIM score and differences between them.

## Notes

* The SSIM comparison is performed on grayscale versions of the loaded images for better accuracy.
* Optionally, you can resize the images by uncommenting the resize_images function call inside the show_difference_image function.

## Customization

* To change the background image of the GUI, replace "background_image.jpg" with the path to your desired background image inside the set_background_image function.
* For further customization, you can explore the Tkinter options and styles to modify the GUI's appearance, as well as adjust the layout and positioning of the widgets.

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute the application as per the terms of the MIT License. If you have any suggestions or improvements, please feel free to contribute to the project
