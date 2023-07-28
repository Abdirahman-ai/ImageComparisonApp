

import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from skimage.metrics import structural_similarity as ssim
import tkinter.ttk as ttk

def resize_images(image1, image2, new_size):
    # Maintain the aspect ratio while resizing
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]
    aspect_ratio1 = w1 / h1
    aspect_ratio2 = w2 / h2

    if aspect_ratio1 > aspect_ratio2:
        new_width = int(new_size * aspect_ratio1)
        new_height = new_size
    else:
        new_width = new_size
        new_height = int(new_size / aspect_ratio2)

    image1 = cv2.resize(image1, (new_width, new_height))
    image2 = cv2.resize(image2, (new_width, new_height))
    return image1, image2

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        return image

def compare_images(image1, image2):
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(gray_image1, gray_image2, full=True)
    return score, diff

def show_difference_image():
    file_path1 = filedialog.askopenfilename()
    file_path2 = filedialog.askopenfilename()

    if file_path1 and file_path2:
        image1 = cv2.imread(file_path1)
        image2 = cv2.imread(file_path2)

        # Optionally, resize the images (uncomment the next line if needed)
        image1, image2 = resize_images(image1, image2, new_size=500)

        ssim_score, diff_image = compare_images(image1, image2)

        # Display the SSIM score and result
        result_label.config(text=f"SSIM Score: {ssim_score:.4f}")


        # Display the SSIM score and result
        if ssim_score == 1.0:
            message = "The images are identical."
        elif ssim_score > 0.8:
            message = "The images are very similar."
        else:
            message = "The images have differences."
        message_label.config(text=message)

        # Convert the difference image to a suitable data type for RGB conversion
        diff_image = cv2.convertScaleAbs(diff_image)

        # Convert the difference image to a Tkinter-compatible format and display it
        diff_image_rgb = cv2.cvtColor(diff_image, cv2.COLOR_BGR2RGB)
        diff_image_pil = Image.fromarray(diff_image_rgb)
        diff_image_tk = ImageTk.PhotoImage(diff_image_pil)
        diff_label.config(image=diff_image_tk)
        diff_label.image = diff_image_tk  # Keep a reference to prevent garbage collection

    
# Create the Tkinter application and the GUI layout
root = tk.Tk()
root.title("Image Comparison App")

# Create an introductory label
intro_label = tk.Label(root, text="Welcome to Image Comparison App!", font=("Arial", 16, "bold"))
intro_label.grid(row=0, column=0, columnspan=2, padx=30, pady=30)

# Create buttons and labels
load_button = tk.Button(root, text="Load Images", command=show_difference_image)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
message_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
diff_label = tk.Label(root)

# Grid layout for other widgets
load_button.grid(row=1, column=0, padx=40, pady=40)
result_label.grid(row=1, column=1, padx=40, pady=40)
message_label.grid(row=2, column=0, columnspan=2, padx=40, pady=40)
diff_label.grid(row=3, column=0, columnspan=2, padx=40, pady=40)

root.mainloop()
