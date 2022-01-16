import cv2 as cv    #OpenCV library
import numpy as np


def main():
    input_image = cv.imread('OIP.png')   #it is read image and store into variable

    flip_vertical = cv.flip(input_image,0)    #0 for vertical flip of image
    cv.imwrite('flip_ver.png',flip_vertical)   #store into new png photo

    flip_horizontal = cv.flip(input_image,1)   #1 for horizontal flip of image
    cv.imwrite('flip_hori.png',flip_horizontal)    #store into new png photo

    flip_both = cv.flip(input_image,-1)    #-1 for both flip
    cv.imwrite('flip_both.png',flip_both)   #store into new png photo

    input("press enter for continue ...")

if __name__ == '__main__':   #main function
    main()



