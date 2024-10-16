# DIP-2024

10/16小結

1.Le Gall 5/3 參考網址
https://github.com/KaiserLew/LeGall53-DWT/blob/master/LeGall53.py
將圖片輸入並做三次CDF5/3小波轉換，顯示小波轉換的圖片以及最終壓縮後的圖片

程式修正:dwt和idwt函式中的width與height作者皆寫相反


2.基於https://blog.csdn.net/weixin_36815313/article/details/108531674
和https://blog.csdn.net/qq_42951560/article/details/115456471
寫出兩種計算PSNR的程式碼以參照

10/13小結

1.參照此網址
https://medium.com/@ryanwmccoy/exploring-image-compression-with-fourier-and-wavelet-transformations-using-python-0b3c15a72703
寫出了小波壓縮的程式碼並進行壓縮

2.使用 cv2.imwrite('Compressed.png', img_compressed) 儲存壓縮過後的檔案

3.安裝 pip install opencv-contrib-python 以進行圖像對比
https://medium.com/@leo81005/%E8%A7%A3%E6%B1%BA-import-cv2-xfeatures2d-%E7%94%A2%E7%94%9F%E9%8C%AF%E8%AA%A4%E7%9A%84%E5%95%8F%E9%A1%8C-56658e652e85

4.參照
https://blog.csdn.net/qq_41290252/article/details/134290491
寫出SSIM、SIFT、SURF、ORB等四種比較的程式碼
但 SURF 方法 import函式庫失敗，SSIM、SIFT、ORB三種方法的相似度差異極大
其中SIFT的相似度最正常，相似度約為0.6

P.S.無法正常使用ImageMagick，因此放棄使用JPEG2000進行比對
https://imagemagick.org/script/download.php

照此網站的指示安裝
https://itsfoss.com/install-imagemagick-ubuntu/

確認已安裝，但卡在
display: delegate library support not built-in '' (X11) @ error/display.c/DisplayImageCommand/1907.
此錯誤無法排解

P.P.S.參照此網址
https://blog.csdn.net/wsp_1138886114/article/details/116780542
寫出 bior.py, code.py, db2.py, haar1.py, haar2.py
並另外修改出 biorcopy.py 為可自行導入圖片的版本
