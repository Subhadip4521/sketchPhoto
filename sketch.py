import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "photo_2022-03-19_22-26-05.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
    #it is 2 dimentional formula to convert image to gray scale

def dodge(front, back):
    finalSketch= front*255/(255-back)
    finalSketch[finalSketch>255]=255
    finalSketch[back==255]=255
    return finalSketch.astype('uint8')

ss=imageio.imread(img)          #To read the given image

gray= rgb2gray(ss)   #First we will convert the image to black and white that means gray scale

i=255-gray  # 0,0,0 is black and 255,255,255 is white


#To convert it into blur image
blur =scipy.ndimage.filters.gaussian_filter(i, sigma=15)
#sigma is the intensity of the image

r=dodge(blur, gray)     #This function will convert the image into sketch


cv2.imwrite('flower.png',r)