import cv2
import argparse
from skimage.metrics import structural_similarity as ssim

def load_images(image_path1, image_path2):
    try:
        image1 = cv2.imread(image_path1)
        image2 = cv2.imread(image_path2)
        return image1, image2
    except Exception as e:
        raise ValueError("Error loading images: " + str(e))

def resize_images(image1, image2, new_size):
    # Maintain the aspect ratio while resizing
    h, w = image1.shape[:2]
    aspect_ratio = w / h
    new_width = int(new_size * aspect_ratio)
    image1 = cv2.resize(image1, (new_width, new_size))
    image2 = cv2.resize(image2, (new_width, new_size))
    return image1, image2

def compare_images_ssim(image1, image2):
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    (score, diff) = ssim(gray_image1, gray_image2, full=True)
    return score, diff

if __name__ == "__main__":
    image_path1 = "/Users/abdikafarahmed/Desktop/1.png"
    image_path2 = "/Users/abdikafarahmed/Desktop/2.png"

    # parser = argparse.ArgumentParser(description="Compare two images using SSIM.")
    # parser.add_argument("image_path1", image_path1)
    # parser.add_argument("image_path2", image_path2)
    # args = parser.parse_args()

    image1, image2 = load_images(image_path1, image_path2)

    # Optionally, resize the images (uncomment the next line if needed)
    image1, image2 = resize_images(image1, image2, new_size=500)

    ssim_score, diff_image = compare_images_ssim(image1, image2)
    print("SSIM Score:", ssim_score)
    
    if ssim_score == 1.0:
        print("The images are identical.")
    elif ssim_score > 0.8:
        print("The images are very similar.")
    else:
        print("The images have differences.")

    # Save the difference image for visualization
    cv2.imwrite("diff_image.jpg", diff_image)

    # Optionally, show the difference image using OpenCV
    cv2.imshow("Difference Image", diff_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
