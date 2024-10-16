from skimage.metrics import peak_signal_noise_ratio as psnr
from PIL import Image
import numpy as np


img1 = np.array(Image.open('/home/vboxuser/DIP/B&W.png'))
img2 = np.array(Image.open('/home/vboxuser/DIP/Compressed.png'))


if __name__ == "__main__":
    print(psnr(img1, img2))
