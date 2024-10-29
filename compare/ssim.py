import cv2
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy as np


img1 = np.array(Image.open('/home/vboxuser/DIP/00013_TE_1920x1280.png'))
img2 = np.array(Image.open('/home/vboxuser/DIP/HaarWaveletDecomposition-main/13_wavelets_inv.jp2'))


if __name__ == "__main__":
	
    print(ssim(img1, img2, channel_axis = -1))
