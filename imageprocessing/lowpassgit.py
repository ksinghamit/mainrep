from scipy import fftpack
import numpy as np
import imageio
from PIL import Image, ImageDraw
import os

imagenew = Image.open('IMG_2471.jpg')

#convert image to numpy array
image1 = imagenew.convert('L')
image1=image1.rotate(270)
image1_np=np.array(image1)

#fft of image
fft1 = fftpack.fftshift(fftpack.fft2(image1_np))

#Create a low pass filter image
x,y = image1_np.shape[0],image1_np.shape[1]
#size of circle
e_x,e_y=500,500
#create a box 
bbox=((x/2)-(e_x/2),(y/2)-(e_y/2),(x/2)+(e_x/2),(y/2)+(e_y/2))

low_pass=Image.new("L",(image1_np.shape[0],image1_np.shape[1]),color=0)

draw1=ImageDraw.Draw(low_pass)
draw1.ellipse(bbox, fill=1)
#low_pass.show()

low_pass_np=np.array(low_pass)

#Display matrix size of images
print('image', image1_np.shape)
print('FFT',fft1.shape)
print('Low Pass',low_pass_np.shape)

#multiply both the images
filtered=np.multiply(fft1,low_pass_np.transpose())

#inverse fft
ifft2 = np.real(fftpack.ifft2(fftpack.ifftshift(filtered)))
ifft2 = np.maximum(0, np.minimum(ifft2, 255))

#save the image
imageio.imsave('fft-then-ifft.jpg', ifft2.astype(np.uint8))
imagefft=Image.open('fft-then-ifft.jpg')

image1.save('original_gray.jpg')

#display compression
gr_size = os.stat('original_gray.jpg').st_size
com_size = os.stat('fft-then-ifft.jpg').st_size
print('Original size: ',os.stat('IMG_2471.jpg').st_size,' bytes')
print('Grayscale size: ',gr_size,' bytes')
print('Compressed size: ',com_size,' bytes')
print('Compression ratio: ',(1-com_size/gr_size)*100,'%')

imagefft.show()
image1.show()
