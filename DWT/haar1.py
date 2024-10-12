import numpy as np
import pywt
import cv2


raw_img = cv2.imread("/home/vboxuser/DIP/00009_TE_1976x1312.png")
coeffs = pywt.dwt2(raw_img, 'haar')
cA, (cH, cV, cD) = coeffs           # 低頻分量，(水準高頻，垂直高頻，對角線高頻)
re_raw_img = pywt.idwt2(coeffs, 'haar')
cv2.imshow("re_raw_img", re_raw_img.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

#==============================================
import numpy as np
import pywt
from PIL import Image


img = Image.open("len_std.jpg")
imgarr = np.array(img)
coeffs = pywt.dwt2(imgarr, 'haar')
re_img = pywt.idwt2(coeffs, 'haar')

