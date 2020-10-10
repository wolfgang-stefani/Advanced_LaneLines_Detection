# Advanced Lane Finding

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)
![Lanes Image](./examples/example_output.jpg)

In this project, a software pipeline was written to identify the lane boundaries in a video. 

The steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit a polynomial to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

The images for camera calibration are stored in the folder called `camera_cal`.  The images in `test_images` are for testing the pipeline on single frames. If you want to extract more test images from the videos, you can simply use an image writing method like `cv2.imwrite()`, i.e., you can read the video in frame by frame as usual, and for frames you want to save for later you can write to an image file.

## Pipeline in a nutshell (for a very detailed description including how camera calibration is implemented, see this file [add LINK]):

## Step 1: Read in an image

![](./output_images/original.png)


## Step 2: Distortion correction
![](./writeup/1.png)


## Step 3: Thresholding
Various combinations of color and gradient thresholds were tested.
(Note: This step is visualized with “test4.jpg” instead of “test6.jpg” as for all the other steps because here you can see the advantages of s-channel when road has bad sun/shadow conditions)

![](./writeup/2.png)

### Steps in detail:
![](./writeup/3.png)


## Step 4: Perspective Transform
First, identifying four source points src (pick four points in a trapezoidal shape (similar to region masking) and after four destination points dst.
![](./writeup/4.png)

## Step 5: Grayscale
![](./writeup/5.png)

## Step 6: Detect lane pixels (sliding windows method) and fit a polynomial to find the lane boundary
Explicit Decision which pixels are part of the lines and which belong to the left respectively to the right line.
![](./writeup/6.png)

### Steps in detail:
![](./writeup/7.png)

## Step 7: Drawing
This includes:
a) Draw the lines on a blank (zeroed) image
b) Warp this image back to original image space using inverse perspective Matrix (Minv)
c) Combine the result with the original image
![](./writeup/8.png)