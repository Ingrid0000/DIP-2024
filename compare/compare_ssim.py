import cv2
import numpy as np
#from skimage.measure import compare_ssim 原因：因為在skimage高版本中原來的compare_psnr和compare_ssim已經被移除
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import peak_signal_noise_ratio as compare_psnr

def compare_images_pixel(img1_path, img2_path):
    # 讀取兩張圖片
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # 確保兩張圖片具有相同的尺寸
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

    # 計算結構相似性（SSIM）指標
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ssim_score = compare_ssim(img1_gray, img2_gray)

    # 計算方差參數
    img1_var = np.var(img1_gray)
    img2_var = np.var(img2_gray)
    var_diff = np.abs(img1_var - img2_var)

    # 綜合考慮SSIM指標和方差參數，得到最終的相似度評分
    similarity = ssim_score * (1 - var_diff)

    return similarity

# 示例用法
img1_path = "/home/vboxuser/DIP/00009_TE_1976x1312.png"
img2_path = "/home/vboxuser/DIP/Compressed.png"
similarity = compare_images_pixel(img1_path, img2_path)
print('相似度：', similarity)

