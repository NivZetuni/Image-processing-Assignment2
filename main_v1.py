import argparse

import cv2
# load image as grayscale
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("imgName", help = "Prints the supplied argument.")

    args = parser.parse_args()
    imgName = args.imgName

    img = cv2.imread(imgName, cv2.IMREAD_GRAYSCALE)


    # convert to binary. Inverted, so you get white symbols on black background
    _ , thres = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    # find contours in the thresholded image (this gives all symbols)
    contours, hierarchy = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ##############################################
    maxArea = 0
    for cnt in contours:
        currArea = cv2.contourArea(cnt)
        if currArea > maxArea:
            maxArea = currArea

    ###############################################


    width = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < maxArea/10:
            rect = cv2.boundingRect(cnt)
            x, y, w, h = rect
            if w > width:
                width = w

    # ##############################################

    margin = 2
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < maxArea/10:
            rect = cv2.boundingRect(cnt)
            x, y, w, h = rect
            cropped = img[y - margin:y + h + margin, x - margin:x + w + margin]
            kernel = np.ones((width, 1), np.uint8)
            dilate_shape = cv2.dilate(cropped.copy(), kernel, iterations=1)
            eroded_shape = cv2.erode(dilate_shape.copy(), kernel, iterations=1)
            img[y - margin:y + h + margin,x - margin:x + w + margin] = eroded_shape  # we copy the eroded_shape back into the original_image

    #
    # ############################################



    # display result
    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()