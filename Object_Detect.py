from util import *
import cv2


def image_preprocessing(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    image_morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=9)
    image_mask = 255 - image_morph
    background = cv2.dilate(image_mask, kernel, iterations=5)
    dist_transform = cv2.distanceTransform(image_mask, cv2.DIST_L2, 3)
    _, foreground = cv2.threshold(dist_transform, 0.237 * dist_transform.max(), 255, 0)
    the_unknown_image = background - foreground
    foreground = np.uint8(foreground)

    return image_morph

if __name__ == '__main__':
    image_path = '/home/renos/Pictures/100100_d2_front.png'
    image = read_image(image_path)
    show_image_with_opencv(image_preprocessing(image=image))
