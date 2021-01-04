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


def show_4_images_with_matplot(image1, image2, image3, image4):
    plt.figure(figsize=(20, 12))
    plt.subplot(221), plt.imshow(image1, cmap='gray'), plt.title("Stage one")
    plt.subplot(222), plt.imshow(image2, cmap='gray'), plt.title("Stage two")
    plt.subplot(223), plt.imshow(image3, cmap='gray'), plt.title("Stage three")
    plt.subplot(224), plt.imshow(image4, cmap='gray'), plt.title("Stage four")
    plt.show()


def show_images_stages(img1, img2, img3, img4, img5, img6, title1, title2, title3, title4, title5, title6):
    plt.figure(figsize=(20, 12))

    plt.subplot(231), plt.imshow(img1, cmap='gray'), plt.title(title1)
    plt.subplot(232), plt.imshow(img2, cmap='gray'), plt.title(title2)
    plt.subplot(233), plt.imshow(img3, cmap='gray'), plt.title(title3)

    plt.subplot(234), plt.imshow(img4, cmap='gray'), plt.title(title4)
    plt.subplot(235), plt.imshow(img5, cmap='gray'), plt.title(title5)
    plt.subplot(236), plt.imshow(img6, cmap='gray'), plt.title(title6)
    plt.show()


def show_images_stages_without_titles(img1, img2, img3, img4, img5, img6):
    plt.figure(figsize=(20, 12))

    plt.subplot(231), plt.imshow(img1, cmap='gray')
    plt.subplot(232), plt.imshow(img2, cmap='gray')
    plt.subplot(233), plt.imshow(img3, cmap='gray')

    plt.subplot(234), plt.imshow(img4, cmap='gray')
    plt.subplot(235), plt.imshow(img5, cmap='gray')
    plt.subplot(236), plt.imshow(img6, cmap='gray')
    plt.show()


def show_9_images_stages_without_titles(img1, img2, img3, img4, img5, img6, img7, img8, img9):
    plt.figure(figsize=(20, 12))

    plt.subplot(251), plt.imshow(img1, cmap='gray')
    plt.subplot(252), plt.imshow(img2, cmap='gray')
    plt.subplot(253), plt.imshow(img3, cmap='gray')

    plt.subplot(254), plt.imshow(img4, cmap='gray')
    plt.subplot(255), plt.imshow(img5, cmap='gray')
    plt.subplot(256), plt.imshow(img6, cmap='gray')

    plt.subplot(257), plt.imshow(img7, cmap='gray')
    plt.subplot(258), plt.imshow(img8, cmap='gray')
    plt.subplot(259), plt.imshow(img9, cmap='gray')

    plt.show()


def show_image_with_opencv(image):
    cv2.imshow("Given Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
