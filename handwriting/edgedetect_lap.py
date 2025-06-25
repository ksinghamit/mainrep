import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageOps
import os
from scipy.signal import fftconvolve
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


def edge_detect(filename):
	#get image data and convert to grayscale
	imagenew = Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+filename)
	image1 = imagenew.convert('L')
	image1=image1.rotate(270, expand = True) #rotate image 
    #image1 = image1.transpose(Image.Transpose.ROTATE_270)
	image1_np=np.array(image1)
	image1.show()


	#define edge detecting kernel


	#better edge detection than previous kernel
	# kernel = np.array([
					   # [ -1, -1,  1, -1, -1],
					   # [ -1, 1,  1, 1, -1],
					   # [  1, 1,  1, 1,  1],
					   # [ -1, 1,  1, 1, -1],
					   # [ -1, -1,  1, -1, -1]
						# ]) / 25               
						
	kernel = np.array([
					   [-1,-1, -1, 1, -1, -1, -1],
					   [-1,-1, 1, 1, 1, -1, -1],
					   [-1, 1, 1, 1, 1, 1, -1],
					   [ 1, 1, 1, 1, 1, 1, 1],
					   [-1, 1, 1, 1, 1, 1, -1],
					   [-1,-1, 1, 1, 1, -1, -1],
					   [-1,-1,-1, 1, -1, -1, -1]
						]) / 49      


	#convolve kernel and image arrays
	convolution2= fftconvolve(image1_np, kernel)
	return convolution2.astype(np.uint8) #return image in grayscale



origimage = 'IMG_2473.jpg'

# call function to get image conaining edges

convo2 = edge_detect(origimage)
#write the image
imageio.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+'xdet'+origimage, convo2)
convol_img2	= Image.open('/home/aksin/Pyprog/ImageProcessing/images/'+'xdet'+origimage)
inverted_img = ImageOps.invert(convol_img2)
#show convoluted image (image containing the edges)

convol_img2.show()
inverted_img.show()



