import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageOps
import os


#get image data and convert to grayscale
filename = 'IMG_2473.jpg'
imagenew = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+filename)

img1=imagenew.rotate(270) #rotate image 
img1.show()

#convert image to float to prevent integre overflow at 255
image1_np=np.array(img1, dtype='float64')

#red channel
img_r = image1_np[:,:,0]
r_fact = 0.2

#green channel
img_g = image1_np[:,:,1]
g_fact = 0.4

#blue channel
img_b = image1_np[:,:,2]
b_fact = 0.4

# combined grayscale image
img_gray = r_fact*img_r + g_fact*img_g + b_fact*img_b


print("Image 1 shape: ",image1_np.shape)

#print("Gray Image shape: ",img_gray.shape)


#normalizing values in the range 0-255 to prevent int overflow
img_gray[img_gray>255] = 255

#write the images
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'red'+filename, img_r.astype(np.uint8))
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'green'+filename, img_g.astype(np.uint8))
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'blue'+filename, img_b.astype(np.uint8))
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'grayscale'+filename, img_gray.astype(np.uint8))

#show channels and grayscale
red_img	= Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'red'+filename)
green_img = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'green'+filename)
blue_img = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'blue'+filename)
gray_img = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'grayscale'+filename)

red_img.show()
green_img.show()
blue_img.show()
gray_img.show()




