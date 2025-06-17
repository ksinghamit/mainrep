from scipy import fftpack
import numpy as np
import imageio
from PIL import Image, ImageDraw
import os
from scipy.ndimage import convolve

#get image data and convert to grayscale
filename = 'IMG_2471.jpg'
imagenew = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+filename)
image1 = imagenew.convert('L')
image1=image1.rotate(270)
image1_np=np.array(image1)
image1.show()


#define edge detecting kernel
kernel = np.array([
				   [ 0,  1,  0],
                   [ 1, -4,  1],
                   [ 0,  1,  0]
                    ]) / 10

#convolve kernel and image arrays
convolution= convolve(image1_np, kernel)

#write the image
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'convoluted'+filename, convolution.astype(np.uint8))

#show convoluted image (image containing the edges)
convol_img	= Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'convoluted'+filename)

convol_img.show()



