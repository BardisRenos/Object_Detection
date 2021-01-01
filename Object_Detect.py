from util import *
import cv2




if __name__ == '__main__':
    image_path = '/home/renos/Pictures/100100_d2_front.png'
    image = read_image(image_path)
    show_image_with_opencv(read_image(image_path))
