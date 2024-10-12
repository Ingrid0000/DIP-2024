import numpy as np
import pywt
from matplotlib import pyplot as plt
from pywt._doc_utils import wavedec2_keys, draw_2d_wp_basis

x = pywt.data.camera().astype(np.float32)
shape = x.shape
max_lev = 3       # 要繪製多少級分解
label_levels = 3  # 圖上要顯式標注多少層

fig, axes = plt.subplots(2, 4, figsize=[14, 8])
for level in range(0, max_lev + 1):
    if level == 0:
        # 顯示原始圖像
        axes[0, 0].set_axis_off()
        axes[1, 0].imshow(x, cmap=plt.cm.gray)
        axes[1, 0].set_title('Image')
        axes[1, 0].set_axis_off()
        continue

    # 繪製標準DWT基的子帶邊界
    # draw_2d_wp_basis(shape, wavedec2_keys(level), ax=axes[0, level], label_levels=label_levels)
    # axes[0, level].set_title('{} level\ndecomposition'.format(level))

    # 計算二維 DWT
    c = pywt.wavedec2(x, 'db2', mode='periodization', level=level)

    # 獨立規範化每個係數陣列以獲得更好的可見性
    c[0] /= np.abs(c[0]).max()
    for detail_level in range(level):
        c[detail_level + 1] = [d / np.abs(d).max() for d in c[detail_level + 1]]

    # 顯示歸一化係數 (normalized coefficients)
    arr, slices = pywt.coeffs_to_array(c)
    axes[1, level].imshow(arr, cmap=plt.cm.gray)
    axes[1, level].set_title('Coefficients\n({} level)'.format(level))
    axes[1, level].set_axis_off()
plt.tight_layout()
plt.show()

