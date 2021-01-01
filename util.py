#! /usr/bin python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_image(path):
    return cv2.imread(path)


def show_2_images_with_opencv(image1, image2):
    numpy_horizontal_concat = np.concatenate((image1, image2), axis=1)
    cv2.imshow('Results', numpy_horizontal_concat)
    cv2.waitKey()
    cv2.destroyAllWindows()


def show_2_images_with_matplot(image1, image2, title1, title2):
    plt.figure(figsize=(20, 12))
    plt.subplot(121), plt.imshow(image1, cmap='gray'), plt.title(title1)
    plt.subplot(122), plt.imshow(image2, cmap='gray'), plt.title(title2)
    plt.show()


def show_image_with_opencv(image):
    cv2.imshow("Given Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
