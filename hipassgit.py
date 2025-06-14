from scipy import fftpack
import numpy as np
import imageio
from PIL import Image, ImageDraw
import os
from scipy.ndimage import convolve
#from skimage import data



# Define Prewitt kernels for detecting vertical and horizontal edges
prewitt_vertical = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

prewitt_horizontal = np.array([[-1, -1, -1],
                               [ 0,  0,  0],
                               [ 1,  1,  1]])


filename = 'IMG_2471.jpg'
imagenew = Image.open(filename)

#convert image to numpy array and convert to grayscale
image1 = imagenew.convert('L')
image1=image1.rotate(270)
image1_np=np.array(image1)


# Apply the Prewitt filter in the vertical direction (horizontal edges)
edges_vertical = convolve(image1, prewitt_vertical)

# Apply the Prewitt filter in the horizontal direction (vertical edges)
edges_horizontal = convolve(image1, prewitt_horizontal)

# Combine the results by taking the magnitude of the gradient
edges_magnitude = np.sqrt(edges_vertical**2 + edges_horizontal**2)


#save images
imageio.imwrite('combined_edges'+filename, edges_magnitude.astype(np.uint8))
imageio.imwrite('vertical_edges'+filename, edges_vertical.astype(np.uint8))
imageio.imwrite('hzntl_edges'+filename, edges_horizontal.astype(np.uint8))
image1.save('original_gray'+filename)

#open images
image_vrt = Image.open('vertical_edges'+filename)
image_hz = Image.open('hzntl_edges'+filename)
image_mg= Image.open('combined_edges'+filename)

#display images
image_vrt.show(title='Vertical edges')
image_hz.show(title='Horizontal edges')
image_mg.show(title='Combined edges')
image1.show(title='Original')

