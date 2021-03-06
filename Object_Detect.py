from util import *
import cv2
from skimage import measure, color, io


# Creating a class object in order to keep the images to each category separately. By creating this class
# we have the opportunity of keep track the images before and after the preprocessing.
class ImageCategories(object):
    pass

    def __init__(self):
        self.image_mask_threshold = None  # Creating the mask without pills black and white
        self.image_gray_with_circle = None  # Image with boundary and gray
        self.image_gray_scale = None  # Image in gray scale
        self.image_circle_combination = None  # Image with the mask (black and white circle) and the pills
        self.image_threshold_bw = None  # Image with black background and white colored objects (if is needed)
        self.image_no_bg = None  # Image without background only the colored pills
        self.pure_image = None  # Image-colored (with pills) as it is from the camera.
        self.image_copy = None  # Simple keeping an image copy for further processing
        self.foreground = None  # Keeping the foreground of the image after thresholding
        self.background = None  # Keeping the background of the image after dilation
        self.the_unknown_image = None  # Keeping the different image from the background and foreground (unknown)
        self.image_markers = None  # Storing the image with markers
        self.image_label2rgb = None  # Storing the image of labels to RGB area (Shows the image)
        self.image_mask = None  # Storing the mask image (Which is the invert of morph)
        self.image_morph = None  # Storing the morph image (Which is before the mask)
        self.image_to_show = None  # Storing the image that is only showing how is the image before preprocessing
        self.dist_transform = None  # Storing the distance transform
        self.image_with_circle_colored = None  # Storing the image with the circle in colored mode

    def convert_to_gray_scale(self, image_to_gray):
        self.image_gray_scale = cv2.cvtColor(image_to_gray, cv2.COLOR_BGR2GRAY)

    def creating_boundary_image(self, given_image):
        self.image_copy = given_image.copy()
        self.image_to_show = given_image.copy()
        self.image_with_circle_colored = given_image.copy()

        h, w = self.image_copy.shape[:2]
        cv2.circle(self.image_copy, ((w // 2) + 1, (h // 2) - 5), 622, (255, 255, 255), 350)
        cv2.circle(self.image_with_circle_colored, ((w // 2) + 1, (h // 2) - 5), 622, (255, 255, 255), 350)

    def image_preprocessing(self, given_image):
        self.convert_to_gray_scale(given_image)
        self.pure_image = given_image

        _, self.image_threshold_bw = cv2.threshold(self.image_gray_scale, 240, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        self.image_morph = cv2.morphologyEx(self.image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=9)
        self.image_mask = 255 - self.image_morph

        self.background = cv2.dilate(self.image_mask, kernel, iterations=5)
        self.dist_transform = cv2.distanceTransform(self.image_mask, cv2.DIST_L2, 3)
        _, self.foreground = cv2.threshold(self.dist_transform, 0.285 * self.dist_transform.max(), 255, 0)
        self.the_unknown_image = self.background - self.foreground
        self.foreground = np.uint8(self.foreground)

    def markers_creation(self):
        _, self.image_markers = cv2.connectedComponents(self.foreground, connectivity=8)
        self.image_markers = self.image_markers + 10
        self.image_markers[self.the_unknown_image == 255] = 0

    def watershed(self):
        self.image_markers = cv2.watershed(self.pure_image, self.image_markers)
        self.pure_image[self.image_markers == -1] = [0, 255, 0]
        self.image_to_show[self.image_markers == -1] = [0, 255, 0]
        self.image_label2rgb = color.label2rgb(self.image_markers, bg_label=0)

    def plot_an_image_with_opencv(self, given_image):
        show_image_with_opencv(given_image)

    def plot_an_image_with_matplotlib(self, given_image):
        show_image_with_matplot(given_image)

    def plot_2_images(self, image1, image2):
        show_2_images_with_matplot(image1, image2, "First Image", "Second Image")

    def plot_4_images(self):
        show_4_images_with_matplot(self.the_unknown_image, self.image_markers, self.foreground, self.the_unknown_image)

    def plot_images_stages(self):
        show_images_stages(self.pure_image, self.image_gray_scale, self.image_threshold_bw,
                           self.image_morph, self.image_mask, self.background,
                           "The input image", "Image to Gray", "Threshold Image", "Image Morph",
                           "Image with the Mask", "Background Image")

    def plot_9_images_stages(self):
        show_9_images_stages_without_titles(self.image_to_show, self.image_with_circle_colored, self.image_threshold_bw,
                                            self.image_mask, self.background, self.dist_transform,
                                            self.foreground, self.image_label2rgb, self.pure_image)


if __name__ == '__main__':
    # Creating the ImageCategories object
    image_category = ImageCategories()

    # The path of the image that will be processed
    image_path = '/home/renos/Pictures/100100_d2_front.png'
    # Reading the image from the path
    image = read_image(image_path)

    # Applying image preprocessing steps
    image_category.creating_boundary_image(image)
    image_category.image_preprocessing(image_category.image_copy)
    image_category.markers_creation()
    image_category.watershed()

    # Plotting the images through the stages of image preprocessing
    # image_category.plot_9_images_stages()

    # Plotting the last image that the pills are watersheds
    image_category.plot_an_image_with_opencv(image_category.image_to_show)
