import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

# Define a class to receive the characteristics of each line detection (object-oriented programming: line is a object)
class Line():
    def __init__(self):
        # was the line detected in the last frame or not
        self.detected = False
        #x values for detected line pixels
        self.cur_fitx = None
        #y values for detected line pixels
        self.cur_fity = None
        # x values of the last N fits of the line
        self.prev_fitx = []
        #polynomial coefficients for the most recent fit
        self.current_poly = [np.array([False])]
        #best polynomial coefficients for the last iteration
        self.prev_poly = [np.array([False])]

    def average_pre_lanes(self):
        tmp = copy(self.prev_fitx)
        tmp.append(self.cur_fitx)
        self.mean_fitx = np.mean(tmp, axis=0)

    def append_fitx(self):
        if len(self.prev_fitx) == N:
            self.prev_fitx.pop(0)
        self.prev_fitx.append(self.mean_fitx)

    def process(self, ploty):
        self.cur_fity = ploty
        self.average_pre_lanes()
        self.append_fitx()
        self.prev_poly = self.current_poly