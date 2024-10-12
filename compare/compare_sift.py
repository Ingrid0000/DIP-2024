import cv2

def compare_images(img1_path, img2_path):
    # 讀取兩張圖片
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # 創建SIFT特徵提取器
    sift = cv2.xfeatures2d.SIFT_create()

    # 在兩張圖片上檢測關鍵點和計算特徵描述子
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # 創建FLANN匹配器
    flann = cv2.FlannBasedMatcher()

    # 使用knnMatch進行特徵匹配
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    # 進行篩選，保留較好的匹配結果
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # 計算相似度
    similarity = len(good_matches) / max(len(descriptors1), len(descriptors2))

    return similarity

# 示例用法
img1_path = "/home/vboxuser/DIP/00009_TE_1976x1312.png"
img2_path = "/home/vboxuser/DIP/Compressed.png"
similarity = compare_images(img1_path, img2_path)
print('相似度：', similarity)

