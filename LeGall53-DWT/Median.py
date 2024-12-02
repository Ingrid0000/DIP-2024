import cv2
import numpy as np
 
img = cv2.imread('/home/vboxuser/DIP/Compressed_LeGall53_Multi-level_13.png',cv2.IMREAD_GRAYSCALE)

median = cv2.medianBlur(img, 5)
cv2.imshow("original_img", img)
cv2.imwrite('Compressed_LeGall53_Multi-level_13_median.jp2', median)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyWindow()

