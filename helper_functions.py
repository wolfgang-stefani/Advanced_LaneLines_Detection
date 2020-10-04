import math
import cv2

# function that takes an image, object points, and image points, performs the camera calibration, image distortion correction
# and returns the undistorted image
def cal_undistort(img, objpoints, imgpoints, mtx, dist):
    undist = cv2.undistort(img, mtx, dist, None, mtx)  # undist war im Kurs dst (destination)
    return undist