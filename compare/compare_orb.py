import cv2

def compare_images_orb(img1_path, img2_path):
    # 讀取兩張圖片
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # 創建ORB特徵提取器
    orb = cv2.ORB_create()

    # 在兩張圖片上檢測關鍵點和計算特徵描述子
    keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

    # 創建BFMatcher匹配器
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 使用match進行特徵匹配
    matches = bf.match(descriptors1, descriptors2)

    # 進行篩選，保留較好的匹配結果
    good_matches = sorted(matches, key=lambda x: x.distance)[:int(len(matches) * 0.15)]

    # 計算相似度
    similarity = len(good_matches) / max(len(descriptors1), len(descriptors2))

    return similarity

# 示例用法
img1_path = "/home/vboxuser/DIP/00009_TE_1976x1312.png"
img2_path = "/home/vboxuser/DIP/Compressed.png"
similarity = compare_images_orb(img1_path, img2_path)
print('相似度：', similarity)

