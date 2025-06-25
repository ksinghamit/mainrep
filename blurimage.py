import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageOps
import os
from scipy.signal import fftconvolve

#get image data and convert to grayscale
filename = 'IMG_2473.jpg'
imagenew = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+filename)
image1 = imagenew.convert('L')
image1=image1.rotate(270) #rotate image 

image1_np=np.array(image1)

print("Image 1 shape: ",image1_np.shape)

image1.show()

#define blur kernel
kernel = np.array([
				   [ 2, 4, 2],
                   [ 4, 8, 4],
                   [ 2, 4, 2]
                    ])/ 32                  
                    

#convolve kernel and image arrays
convolution2= fftconvolve(image1_np, kernel)

#write the image
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'blurredfft'+filename, convolution2.astype(np.uint8))

#show convoluted image (image blurred)
convol_img2	= Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'blurred'+filename)

convol_img2.show()




