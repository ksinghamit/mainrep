import numpy as np
import cv2


#get image data and convert to grayscale
filename = 'IMG_3230.JPG'
scale_fact = 0.3


image_col = cv2.imread('/home/aksin/Pyprog/ImageProcessing/images/'+filename,1)
image_gr = cv2.imread('/home/aksin/Pyprog/ImageProcessing/images/'+filename,0)
image_unc = cv2.imread('/home/aksin/Pyprog/ImageProcessing/images/'+filename,-1)

#resizing

re_img_col = cv2.resize(image_col,None, fx=scale_fact, fy=scale_fact, interpolation= cv2.INTER_LINEAR)
re_img_gr= cv2.resize(image_gr,None, fx=scale_fact, fy=scale_fact, interpolation= cv2.INTER_LINEAR)
re_img_unc= cv2.resize(image_unc,None, fx=scale_fact, fy=scale_fact, interpolation= cv2.INTER_LINEAR)

cv2.imshow('original color',re_img_col)
cv2.imshow('grayscale image',re_img_gr)
#cv2.imshow('unchanged image',re_img_unc)

#convert image to float to prevent integre overflow at 255
bright_img1=np.array(re_img_col, dtype='float64')
bright_img2=np.array(re_img_gr, dtype='float64')
bright_img3=np.array(re_img_unc, dtype='float64')

print("Original image shape: ",image_col.shape)

#define contrast factor
cont_f= 1.2            
                    

#Increase contrast of the image 
bright_1 = bright_img1 * cont_f
bright_2 = bright_img2 * cont_f
bright_3 = bright_img3 * cont_f

#normalize under 255 int values
bright_1[bright_1>255] = 255
bright_2[bright_2>255] = 255
bright_3[bright_3>255] = 255


#write the image
cv2.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+__name__+filename, bright_1.astype(np.uint8))
cv2.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+__name__+'gray'+filename, bright_2.astype(np.uint8))
#cv2.imwrite('/home/aksin/Pyprog/ImageProcessing/images/'+__name__+filename, bright_img3.astype(np.uint8))

br_im1=cv2.imread('/home/aksin/Pyprog/ImageProcessing/images/'+__name__+filename,-1)
cv2.imshow('More contrast image',br_im1)

br_im2=cv2.imread('/home/aksin/Pyprog/ImageProcessing/images/'+__name__+'gray'+filename,-1)
cv2.imshow('More contrast image2',br_im2)

#show image

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

