'''
The function haar_forward takes a 2D color or grayscale image and
returns an array of the same shape as the input image containing
multi-resolution haar wavelet coefficients.The number of levels
of decomposition is a user-provided parameter.

The function haar_inverse takes multi-resolution haar wavelets and
the levels of decomposition as inputs and reconstructs the original
input. The number of levels provided should be the same as the for
the decomposition.

Please note that if the X (or Y) dimension is of odd length, the
last column (or row) is not processed during the decomposition.
'''

import numpy as np

def haar_forward(image,levels=3):


    def one_level_decomp(img):

        Y,X = img.shape[0],img.shape[1]
        Y,X = (Y//2)*2, (X//2)*2

        a = img[:,0:X:2,...].copy()
        b = img[:,1:X:2,...].copy()

        img[:, :X//2,...] = (a + b)/2
        img[:,X//2:X,...] = (a - b)/2

        a = img[0:Y:2,:,...].copy()
        b = img[1:Y:2,:,...].copy()

        img[:Y//2, :,...] = (a + b)/2
        img[Y//2:Y,:,...] = (a - b)/2

        return img

    def multi_scale_decomp(img,levels):

        H,W = img.shape[0],img.shape[1]

        for s in range(levels):
            img[:(H>>s),:(W>>s),...] = one_level_decomp(img[:(H>>s),:(W>>s),...])

        return img

    return multi_scale_decomp(image,levels)


def haar_inverse(image,levels=3):


    def one_level_recomp(img):

        Y,X = img.shape[0],img.shape[1]
        Y,X = (Y//2)*2, (X//2)*2

        a = img[:, :X//2,...].copy()
        b = img[:,X//2:X,...].copy()

        img[:,0:X:2,...] = a + b
        img[:,1:X:2,...] = a - b


        a = img[:Y//2, :,...].copy()
        b = img[Y//2:Y,:,...].copy()

        img[0:Y:2,:,...] = a + b
        img[1:Y:2,:,...] = a - b

        return img

    def multi_scale_recomp(img,levels):

        H,W = img.shape[0],img.shape[1]

        for s in reversed(range(levels)):
            img[:(H>>s),:(W>>s),...] = one_level_recomp(img[:(H>>s),:(W>>s),...])

        return img

    return multi_scale_recomp(image,levels)



