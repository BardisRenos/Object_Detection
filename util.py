#! /usr/bin python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_image(path):
    return cv2.imread(path)


def show_image_with_opencv(image):
    cv2.imshow("Given Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
