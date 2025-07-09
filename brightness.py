import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageOps
import os
from scipy.signal import fftconvolve

#get image data and convert to grayscale
filename = 'IMG_2473.jpg'
imagenew = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+filename)
# image1 = imagenew.convert('L')
img1=imagenew.rotate(270) #rotate image 
img1.show()

#convert image to float to prevent integre overflow at 255
image1_np=np.array(img1, dtype='float64')

print("Image 1 shape: ",image1_np.shape)



#define brightness factor
brite_f= 50            
                    

#convolve kernel and image arrays
brite_img = image1_np + brite_f
brite_img[brite_img>255] = 255

#write the image
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'bright'+filename, brite_img.astype(np.uint8))

#show convoluted image (image blurred)
brite_img2	= Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'bright'+filename)

brite_img2.show()




