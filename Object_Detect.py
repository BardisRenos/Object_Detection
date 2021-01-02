from util import *
import cv2


# Creating a class object in order to keep the images to each category separately. By creating this class
# we have the opportunity of keep track the images before and after the preprocessing.
class ImageCategories(object):
    pass

    def __init__(self):
        self.oculus_mask_threshold = None  # Oculus mask without pills black and white
        self.image_gray_with_circle = None  # Oculus image with boundary and gray
        self.image_gray_scale = None  # Oculus image in gray scale
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

    def convert_to_gray_scale(self, image_to_gray):
        self.image_gray_scale = cv2.cvtColor(image_to_gray, cv2.COLOR_BGR2GRAY)

    def image_preprocessing(self, given_image):
        self.convert_to_gray_scale(given_image)
        self.pure_image = given_image

        _, self.image_threshold_bw = cv2.threshold(self.image_gray_scale, 190, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        self.image_morph = cv2.morphologyEx(self.image_threshold_bw, cv2.MORPH_CLOSE, kernel, iterations=9)
        self.image_mask = 255 - self.image_morph
        self.background = cv2.dilate(self.image_mask, kernel, iterations=5)
        dist_transform = cv2.distanceTransform(self.image_mask, cv2.DIST_L2, 3)
        _, self.foreground = cv2.threshold(dist_transform, 0.237 * dist_transform.max(), 255, 0)
        self.the_unknown_image = self.background - self.foreground
        self.foreground = np.uint8(self.foreground)

    def creating_boundary_image(self):
        self.pure_image = read_image(image_path)
        self.image_copy = self.pure_image.copy()
        self.image_to_show = self.pure_image.copy()
        h, w = self.image_copy.shape[:2]
        cv2.circle(self.image_copy, ((w // 2) + 1, (h // 2) - 5), 622, (255, 255, 255), 350)

    def markers_creation(self):
        self.image_preprocessing()

        _, self.image_markers = cv2.connectedComponents(self.foreground, connectivity=8)
        # An issue right now is that, the entire background pixels is given value equal to 0.
        # This means watershed considers this region as unknown. So let us add 10 to all labels.
        # So that sure background is not 0, but 10
        self.image_markers = self.image_markers + 10
        # Now, mark the region of unknown with zero
        self.image_markers[self.the_unknown_image == 255] = 0
        # show_2_images_with_matplot(sure_fg, markers, "The foreground", "The result")

    def plot_an_image(self, given_image):
        show_image_with_opencv(given_image)

    def plot_2_images(self):
        show_2_images_with_matplot(self.pure_image, self.image_threshold_bw, "Morph Image", "Threshold")

    def plot_multiple_images_without_titles(self):
        show_images_stages_without_titles(self.pure_image, self.image_gray_scale, self.image_threshold_bw,
                                          self.image_morph,
                                          self.image_mask, self.background)


if __name__ == '__main__':
    A = ImageCategories()
    image_path = '/home/renos/Pictures/100100_d2_front.png'
    image = read_image(image_path)
    A.image_preprocessing(image)
    # A.plot_2_images()
    A.plot_multiple_images_without_titles()
