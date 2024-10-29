import cv2
import pywt
import numpy as np
from matplotlib import pyplot as plt
    
#Read in the image
image = cv2.imread('/home/vboxuser/DIP/B&W_09.png', 0)

w = 'db2'  # 小波種類
l = 4          # 小波層次

#Find the coefficients
coeffs = pywt.wavedec2(image,w,l)
img_compressed = pywt.waverec2(coeffs, w)

#Save compressed image
cv2.imwrite('Compressed_db2_4_09.jp2', img_compressed)
