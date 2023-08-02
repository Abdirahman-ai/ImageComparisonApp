import sys
# Prints out the location of the Virtual Environment
# To run the program correctly, navigate to this location
# then activate it with the following commands
# source myenv/bin/activate
print(sys.executable)

import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from skimage.metrics import structural_similarity as ssim

# A function to resize two images while maintaining their aspect ratio
def resize_images(image1, image2, new_size):
    # Get the dimensions of the images
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]

    # Calculate the aspect ratios
    aspect_ratio1 = w1 / h1
    aspect_ratio2 = w2 / h2

    # Determine the new dimensions while maintaining the aspect ratio
    if aspect_ratio1 > aspect_ratio2:
        new_width = int(new_size * aspect_ratio1)
        new_height = new_size
    else:
        new_width = new_size
        new_height = int(new_size / aspect_ratio2)

    # Resize the images
    image1 = cv2.resize(image1, (new_width, new_height))
    image2 = cv2.resize(image2, (new_width, new_height))
    return image1, image2

# A function to open an image file and return the image data
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        return image

# A function to compare two images using Structural Similarity Index (SSIM)
def compare_images(image1, image2):
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(gray_image1, gray_image2, full=True)
    return score, diff

# ... (previous code)

# A function to update the displayed images and comparison results
def update_images():
    # Ask the user to select two image files
    file_path1 = filedialog.askopenfilename()
    file_path2 = filedialog.askopenfilename()

    if file_path1 and file_path2:
        # Load the selected images
        image1 = cv2.imread(file_path1)
        image2 = cv2.imread(file_path2)

        # Calculate the maximum size that fits within the application window
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        max_size = min(window_width // 2, window_height - 100)

        # Resize the images to fit the maximum size while maintaining their aspect ratio
        image1, image2 = resize_images(image1, image2, max_size)

        # Compare the images and get the SSIM score and difference image
        ssim_score, diff_image = compare_images(image1, image2)

        # Display the SSIM score and result
        result_label.config(text=f"SSIM Score: {ssim_score:.4f}")

        # Display the similarity message based on the SSIM score
        if ssim_score == 1.0:
            message = "The images are identical."
        elif ssim_score > 0.8:
            message = "The images are very similar."
        else:
            message = "The images have differences."
        message_label2.config(text=message)

        # Clear the diff_label before displaying the difference image
        diff_label.config(image=None)

        # Convert the difference image to a suitable data type for RGB conversion
        diff_image = cv2.convertScaleAbs(diff_image)

        # Convert the difference image to a Tkinter-compatible format and display it
        diff_image_rgb = cv2.cvtColor(diff_image, cv2.COLOR_BGR2RGB)
        diff_image_pil = Image.fromarray(diff_image_rgb)
        diff_image_tk = ImageTk.PhotoImage(diff_image_pil)

        # Update diff_label with the new difference image and resize it
        diff_label.config(image=diff_image_tk, width=max_size, height=max_size)
        diff_label.image = diff_image_tk  # Keep a reference to prevent garbage collection

        # Display the original images side by side
        image1_pil = Image.fromarray(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
        image2_pil = Image.fromarray(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
        image1_tk = ImageTk.PhotoImage(image1_pil)
        image2_tk = ImageTk.PhotoImage(image2_pil)

        image_label1.config(image=image1_tk)
        image_label2.config(image=image2_tk)

        image_label1.image = image1_tk  # Keep a reference to prevent garbage collection
        image_label2.image = image2_tk  # Keep a reference to prevent garbage collection

# ... (rest of the code)

# Create the Tkinter application and the GUI layout
root = tk.Tk()
root.title("Image Comparison App")

# ... (previous code)

# Create a description label
description_text = "This application allows you to compare two images and shows their structural similarity.\n\n"
description_text += "1. Click the 'Load Images' button to select two images you want to compare.\n"
description_text += "2. The images will be displayed side by side, and the difference image will be shown above.\n"
description_text += "3. The Structural Similarity Index (SSIM) score will indicate the similarity between the images.\n"
description_text += "4. A higher SSIM score indicates a higher similarity between the images.\n\n"
description_text += "Please note that SSIM values close to 1.0 indicate the images are nearly identical, while values\n"
description_text += "closer to 0 indicate more dissimilarity. Images that are visually similar tend to have higher SSIM scores."

message_label = tk.Label(root, text=description_text, font=("Arial", 12), justify='left', anchor='w')
message_label.grid(row=1, column=0, columnspan=2, padx=30, pady=10)

# ... (previous code)

# Create buttons and labels for the image comparison
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
message_label2 = tk.Label(root, text="", font=("Arial", 12, "bold"))
diff_label = tk.Label(root)
image_label1 = tk.Label(root)
image_label2 = tk.Label(root)
load_button = tk.Button(root, text="Load Images", command=update_images)

# Grid layout for other widgets
result_label.grid(row=2, column=0, columnspan=40, padx=40, pady=10)
message_label2.grid(row=3, column=0, columnspan=40, padx=40, pady=10)
image_label1.grid(row=4, column=0, padx=40, pady=10)
image_label2.grid(row=4, column=1, padx=40, pady=10)
diff_label.grid(row=5, column=0, columnspan=40, padx=40, pady=10)
load_button.grid(row=6, column=0, columnspan=40, padx=40, pady=20)

root.mainloop()
