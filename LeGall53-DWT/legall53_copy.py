import cv2
import numpy as np
import matplotlib.pyplot as plt

# forward one time dwt using Le Gall 5/3 wavelet
def dwt(img):
    img_data = img.astype(float)
    m, n = img_data.shape
    img_dwt = np.zeros(img.shape)
    imgTrans = np.zeros((m + 4, n + 4))
    mt, nt = imgTrans.shape
    Height = mt / 2
    Width = nt / 2
    imgTrans[2:mt-2, 2:nt-2] = img_data
    imgTransResult = np.copy(imgTrans)
    
    for i in range(2, mt):
        # column (vertical)
        imgTrans[i][0] = imgTrans[i][2]
        imgTrans[i][1] = imgTrans[i][3]
        imgTrans[i][nt - 1] = imgTrans[i][nt - 3]
        imgTrans[i][nt - 2] = imgTrans[i][nt - 4]
        
        for j in range(1, nt - 2, 2):
            # High frequency (vertical)
            j_1 = int(Width + j / 2)
            imgTransResult[i][j_1] = imgTrans[i][j] - (imgTrans[i][j - 1] + imgTrans[i][j + 1]) / 2
            
        for j in range(2, nt - 2, 2):
            # High frequency (diagonal)
            i_1 = int(i / 2)
            j_1 = int(Width + j / 2)
            j_2 = int(j / 2)
            imgTransResult[i][j_2] = imgTrans[i][j] + (imgTransResult[i][j_1 - 1] + imgTransResult[i][j_1 + 1] + 2) / 4

    imgTrans = np.copy(imgTransResult)

    for j in range(2, nt):
        # row (horizontal)
        imgTrans[0][j] = imgTrans[2][j]
        imgTrans[1][j] = imgTrans[3][j]
        imgTrans[mt - 1][j] = imgTrans[mt - 3][j]
        imgTrans[mt - 2][j] = imgTrans[mt - 4][j]
        
        for i in range(1, mt - 2, 2):
            # High frequency (horizontal)
            i_1 = int(Height + i / 2)
            imgTransResult[i_1][j] = imgTrans[i][j] - (imgTrans[i - 1][j] + imgTrans[i + 1][j]) / 2
            
        for i in range(2, mt - 2, 2):
            # High frequency (diagonal)
            i_1 = int(Height + i / 2)
            i_2 = int(i / 2)
            imgTransResult[i_2][j] = imgTrans[i][j] + (imgTransResult[i_1 - 1][j] + imgTransResult[i_1 + 1][j] + 2) / 4

    return imgTransResult[2:mt - 2, 2:nt - 2]


# DWT for color images
def color_dwt(img):
    channels = cv2.split(img)
    dwt_channels = [dwt(channel) for channel in channels]
    return cv2.merge(dwt_channels)

# IDWT
def idwt(img):
    m, n = img.shape
    imgDWT = np.zeros((m + 4, n + 4))
    mt, nt = imgDWT.shape
    height = mt / 2
    width = nt / 2
    imgDWT[2:mt - 2, 2:nt - 2] = img
    imgInTrans = np.copy(imgDWT)

    for j in range(2, nt - 2):
        # row (horizontal)
        imgInTrans[0][j] = imgInTrans[2][j]
        imgInTrans[1][j] = imgInTrans[3][j]
        imgInTrans[mt - 1][j] = imgInTrans[mt - 3][j]
        imgInTrans[mt - 2][j] = imgInTrans[mt - 4][j]

        for i in range(2, mt - 2, 2):
            # High frequency (diagonal)
            imgInTrans[i][j] = imgDWT[int(i / 2)][j] - (imgDWT[int(i / 2 + height - 1)][j] + imgDWT[int(i / 2 + height + 1)][j] + 2) / 4
            
        for i in range(1, mt - 2, 2):
            # High frequency (horizontal)
            imgInTrans[i][j] = imgDWT[int(i / 2 + height)][j] + (imgInTrans[i - 1][j] + imgInTrans[i + 1][j]) / 2

    imgDWT = np.copy(imgInTrans)

    for i in range(2, mt):
        # column (vertical)
        imgInTrans[i][0] = imgInTrans[i][2]
        imgInTrans[i][1] = imgInTrans[i][3]
        imgInTrans[i][nt - 1] = imgInTrans[i][nt - 3]
        imgInTrans[i][nt - 2] = imgInTrans[i][nt - 4]
        
        for j in range(2, nt - 2, 2):
            # High frequency (diagonal)
            imgInTrans[i][j] = imgDWT[i][int(j / 2)] - (imgDWT[i][int(j / 2 + width - 1)] + imgDWT[i][int(j / 2 + width + 1)] + 2) / 4
            
        for j in range(1, nt - 2, 2):
            # High frequency (vertical)
            imgInTrans[i][j] = imgDWT[i][int(j / 2 + width)] + (imgInTrans[i][j - 1] + imgInTrans[i][j + 1]) / 2
            
    return imgInTrans[2:mt - 2, 2:nt - 2]
    

# IDWT for color images
def color_idwt(img):
    channels = cv2.split(img)
    idwt_channels = [idwt(channel) for channel in channels]
    return cv2.merge(idwt_channels)

if __name__ == "__main__":

    img = cv2.imread('/home/vboxuser/DIP/00009_TE_1976x1312.png')  # Read a color image
    ImgShow = color_dwt(img)

    # iDWT
    ImgRe = color_idwt(ImgShow)

    # Save the reconstructed image
    cv2.imwrite('Compressed_LeGall53_color_image_09.jp2', ImgRe)
    plt.show()

