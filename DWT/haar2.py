import numpy as np
import pywt
import cv2
import matplotlib.pyplot as plt


def haar_img():
    img_u8 = cv2.imread("/home/vboxuser/DIP/00001_TE_2096x1400.png")
    img_f32 = cv2.cvtColor(img_u8, cv2.COLOR_BGR2GRAY).astype(np.float32)

    plt.figure('二維小波一級變換')
    coeffs = pywt.dwt2(img_f32, 'haar')
    cA, (cH, cV, cD) = coeffs

    # 將各個子圖進行拼接，最後得到一張圖
    AH = np.concatenate([cA, cH], axis=1)
    VD = np.concatenate([cV, cD], axis=1)
    img = np.concatenate([AH, VD], axis=0)
    return img

if __name__ == '__main__':
    img = haar_img()

    plt.imshow(img, 'gray')
    plt.title('img')
    cv2.imwrite('二維小波一級變換.jpg', img)
    plt.show()
