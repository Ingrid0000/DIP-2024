import cv2
from skimage.metrics import mean_squared_error
from skimage.metrics import peak_signal_noise_ratio

img1 = cv2.imread('/home/vboxuser/DIP/B&W.png')
img2 = cv2.imread('/home/vboxuser/DIP/Compressed.png')

MSE = mean_squared_error(img1, img2)
PSNR = peak_signal_noise_ratio(img1, img2)

print('MSE: ', MSE)
print('PSNR: ', PSNR)