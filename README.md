# DIP-2024
# 12/02小結

1.https://blog.csdn.net/Leo_whj/article/details/110394374 使用median濾波器將多階反小波轉換的影像降噪。

# 11/29小結

實現多階反小波轉換，但圖像變得較模糊，且檔案(png)變大。

可能原因:

(1)每一層小波轉換會生成更多的數據分量，尤其是高頻分量未經適當壓縮或量化。

(2)小波轉換後的數據表現形式（如浮點數）如果未經適當處理，會佔用更多的存儲空間。

(3)多層轉換會保留過多的細節，而這些細節在沒有壓縮的情況下會增加數據量。

# 10/30小結

1.https://github.com/achanta/HaarWaveletDecomposition/tree/main 的 Haar壓縮可執行，且可處理彩色的圖片
Haar資料夾中的demo_copy.py，較demo.py增加第29及32行，使圖片能夠儲存成正確的色彩空間

2.compare資料夾中，psnr.py和ssim.py皆可執行彩色圖片的比較
ssim.py的執行結果，顯示小波轉換的失真極小，ssim數值皆在0.96以上
https://blog.csdn.net/qq_42951560/article/details/115463083 ssim.py參考資料
https://blog.csdn.net/xwyljt/article/details/124408257  ssim.py參考資料

3.新增 color_dwt 和 color_idwt 函數，對每個顏色通道分別進行 DWT 和 IDWT，將 LeGall53.py 改為可以執行彩色圖片的程式
legall53_copy.py為增加彩色通道的一次小波轉換程式
Compressed_LeGall53_color_image_09.jp2為一次小波轉換的彩色圖片
https://blog.csdn.net/youcans/article/details/121174708 cv2.split的介紹
https://blog.csdn.net/youcans/article/details/121174740 cv2.merge的介紹

4.可嘗試進行編碼
https://github.com/ghallak/jpeg-python/blob/master/encoder.py
https://github.com/fangwei123456/python-jpeg-encoder/blob/master/jpegEncoder.py
https://github.com/tbpaolini/PyJpegDecoder/blob/master/jpeg_decoder.py

5.https://www.ece.iastate.edu/~zambreno/assets/pdf/PanZam12A.pdf LeGall53 小波轉換的係數參考資料
https://www.mdpi.com/2079-9292/7/7/120 Daubechies Wavelet Transform的係數參考資料
https://zh.wikipedia.org/zh-tw/%E5%A4%9A%E8%B4%9D%E8%A5%BF%E5%B0%8F%E6%B3%A2 Daubechies Wavelet Transform的維基百科，並附上ChatGPT的程式碼解說

6.https://github.com/ivansinichkin/Wavelet_Haar_DaubechiesD4/blob/main/Daubechies.py
https://github.com/fukuroder/daubechies_wavelet_coefficients/blob/master/test.py
https://github.com/larshb/2d-dwt/tree/master
Daubechies Wavelet Transform參考資料

# 10/29小結

1.若使用pywt.dwt2以及pywt.idwt2進行壓縮，haar、db2、bior壓縮解壓縮成同一圖片，三者的PSNR相同
使用pywt.wavedec2及pywt.waverec2亦然

2.https://blog.csdn.net/qq_43657442/article/details/109380852 wavedec2參考資料
https://blog.csdn.net/weixin_40074642/article/details/139522549?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-139522549-blog-129525054.235^v43^pc_blog_bottom_relevance_base7&spm=1001.2101.3001.4242.2&utm_relevant_index=4 wavedec2參考資料
https://blog.csdn.net/qq_40723205/article/details/125981439?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-125981439-blog-109380852.235^v43^pc_blog_bottom_relevance_base7&spm=1001.2101.3001.4242.1&utm_relevant_index=3 wavedec2參考資料
https://blog.csdn.net/neoyek/article/details/83041469?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-83041469-blog-109380852.235^v43^pc_blog_bottom_relevance_base7&spm=1001.2101.3001.4242.2&utm_relevant_index=4 waverec函數介紹
https://blog.csdn.net/weixin_42613360/article/details/129525054 waverec參數介紹

# 10/28小結

1.https://jpegai.github.io/test_images/
dataset

2.https://blog.csdn.net/ccsss22/article/details/134276610
MATLAB小波轉換

3.legall53多次壓縮後，解壓縮與預期不符

4.jp2壓縮率大幅提升，PSNR下降
不同dataset的PSNR差異巨大（01、13成果極好，02、06、08差不多，09最差）
PSNR對高頻較敏感，故高頻細節多的圖片，處理後PSNR數值較好

5.可開啟JPEG2000的影像，之後的實驗結果都儲存成.jp2

6.**目標**haar、db2、bior壓縮解壓縮成同一圖片，並比較PSNR

# 10/16小結

1.Le Gall 5/3 參考網址
https://github.com/KaiserLew/LeGall53-DWT/blob/master/LeGall53.py
將圖片輸入並做三次CDF5/3小波轉換，顯示小波轉換的圖片以及最終壓縮後的圖片

程式修正:dwt和idwt函式中的width與height作者皆寫相反


2.基於https://blog.csdn.net/weixin_36815313/article/details/108531674
和https://blog.csdn.net/qq_42951560/article/details/115456471
寫出兩種計算PSNR的程式碼以參照

# 10/13小結

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
