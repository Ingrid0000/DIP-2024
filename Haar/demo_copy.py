'''
Demo showing forward and inverse Haar wavelet decomposition.
The input can be in color or grayscale.

Please note that in order to save as an image, a clipping operation
is performed on the Haar wavelets, which discards negative values.
'''

import cv2
import numpy as np
from timeit import default_timer as timer
from PIL import Image
from haar_wavelets import haar_forward, haar_inverse



def main():

    ref = Image.open("/home/vboxuser/DIP/00013_TE_1920x1280.png")
    ref = np.asarray(ref).astype(np.float32)

    LEVELS = 3
    start = timer()
    hwt = haar_forward(ref.copy(), LEVELS) # forward transform
    inv = haar_inverse(hwt.copy(), LEVELS)  # backward transform
    end = timer()

    Image.fromarray(hwt.clip(0,255).astype(np.uint8)).save("13_wavelets_for.png") # save visualization
    cv2.imwrite('13_wavelets_for.jp2', hwt.clip(0,255).astype(np.uint8))
    Image.fromarray(inv.clip(0,255).astype(np.uint8)).save("13_wavelets_inv.png") # save reconstructed image
    cv2.cvtColor(inv, cv2.COLOR_RGB2BGR,inv)
    cv2.imwrite('13_wavelets_inv.jp2', inv.astype(np.uint8))
    
    print("Time taken in seconds for forward and inverse Haar wavelet transform:", end-start)

    
if __name__ == "__main__":
    main()
