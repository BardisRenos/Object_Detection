from util import *
import cv2


# Creating a class object in order to keep the images to each category separately. By creating this class
# we have the opportunity of keep track the images before and after the preprocessing.
class ImageCategories(object):
    pass

    def __init__(self):
        self.oculus_mask_threshold = None  # Oculus mask without pills black and white
        self.image_gray_with_circle = None  # Oculus image with boundary and gray scale
        self.image_circle_combination = None  # Image with Oculus mask (black and white circle) and the pills
        self.image_threshold_bw = None  # Image with black background and white colored objects (if is needed)
        self.image_no_bg = None  # Image without background only the colored pills
        self.pure_image = None  # Oculus image-colored (with pills) as it is from the camera.
        self.image_copy = None  # Simple keeping an image copy for further processing
        self.foreground = None  # Keeping the foreground of the image after thresholding
        self.background = None  # Keeping the background of the image after dilation
        self.the_unknown_image = None  # Keeping the different image from the background and foreground (unknown)
        self.image_markers = None  # Storing the image with markers
        self.image_label2rgb = None  # Storing the image of labels to RGB area (Shows the image)
        self.image_mask = None  # Storing the mask image (Which is the invert of morph)
        self.image_morph = None  # Storing the morph image (Which is before the mask)
        self.image_to_show = None  # Storing the image that is only showing how is the image before preprocessing


def image_preprocessing(self):
    # self.creating_boundary_image(ImageDetails.image_path)

    _, thresh = cv2.threshold(self.image_gray_with_circle, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    self.image_morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=9)
    self.image_mask = 255 - self.image_morph
    self.background = cv2.dilate(self.image_mask, kernel, iterations=5)
    dist_transform = cv2.distanceTransform(self.image_mask, cv2.DIST_L2, 3)
    _, self.foreground = cv2.threshold(dist_transform, 0.237 * dist_transform.max(), 255, 0)
    self.the_unknown_image = self.background - self.foreground
    self.foreground = np.uint8(self.foreground)

    return dist_transform


if __name__ == '__main__':
    image_path = '/home/renos/Pictures/100100_d2_front.png'
    image = read_image(image_path)
    show_image_with_opencv(image_preprocessing(image=image))
