import numpy as np
import cv2
import matplotlib.pyplot as plt
import pywt
import pywt.data


def test_pywt():
    original = cv2.imread('/home/vboxuser/DIP/00009_TE_1976x1312.png')
    img_f32 = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY).astype(np.float32)
    
    # 圖像的小波變換，圖形的逼近和細節
    titles = ['Approximation', ' Horizontal detail', 'Vertical detail', 'Diagonal detail']
    coeffs2 = pywt.dwt2(img_f32, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    plt.imshow(img_f32)
    plt.colorbar(shrink=0.8)
    fig = plt.figure(figsize=(12, 3))
    for i, a in enumerate([LL, LH, HL, HH]):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    img_f32 = np.uint8(img_f32)
    
    fig.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    test_pywt()


