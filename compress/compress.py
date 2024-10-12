#Import libraries
import cv2
import numpy as np
import pywt
from matplotlib import pyplot as plt

#Read in the image
image = cv2.imread('/home/vboxuser/DIP/00009_TE_1976x1312.png', 0)
 
#Find the coefficients
coeffs = pywt.dwt2(image, 'bior1.3')
cA, (cH, cV, cD) = coeffs

#Apply a thresholding limit
threshold = 20

#Using the thresholding limit for the wavelet transform
cA_thresholded = pywt.threshold(cA, threshold, mode='soft')
cH_thresholded = pywt.threshold(cH, threshold, mode='soft')

#Compress the image
coeffs_thresholded = (cA_thresholded, (cH_thresholded, cV, cD))
img_compressed = pywt.idwt2(coeffs_thresholded, 'bior1.3')

#Save compressed image
cv2.imwrite('Compressed.png', img_compressed)

#Show the resulting image after compression
plt.imshow(img_compressed, cmap='gray')
plt.title('Compressed Image'), plt.xticks([]), plt.yticks([])
plt.show()

