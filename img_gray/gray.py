import cv2

img = cv2.imread('/home/vboxuser/DIP/00001_TE_2096x1400.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('B&W_01.png', img_gray)
cv2.imshow('Image', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
