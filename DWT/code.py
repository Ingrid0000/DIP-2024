import pywt


db3 = pywt.Wavelet('db3')  # 創建一個小波物件
print(db3)
"""
Family name:    Daubechies
Short name:     db
Filters length: 6             #濾波器長度
Orthogonal:     True          #正交
Biorthogonal:   True          #雙正交
Symmetry:       asymmetric    #對稱性，不對稱
DWT:            True          #離散小波變換
CWT:            False         #連續小波變換
"""

def dwt_and_idwt():
    '''
    DWT 與 IDWT （離散的小波變換=>分解與重構）
    使用db2 小波函數做dwt
    '''

    x = [3, 7, 1, 1, -2, 5, 4, 6]
    cA, cD = pywt.dwt(x, 'db2')      # 得到近似值和細節係數
    print(cA)                        # [5.65685425 7.39923721 0.22414387 3.33677403 7.77817459]
    print(cD)                        # [-2.44948974 -1.60368225 -4.44140056 -0.41361256  1.22474487]
    print(pywt.idwt(cA, cD, 'db2'))  # [ 3.  7.  1.  1. -2.  5.  4.  6.]

    # 傳入小波物件，設置模式
    w = pywt.Wavelet('sym3')
    cA, cD = pywt.dwt(x, wavelet=w, mode='constant')
    print(cA, cD)
    print(pywt.Modes.modes)
    # [ 4.38354585  3.80302657  7.31813271 -0.58565539  4.09727044  7.81994027]
    # [-1.33068221 -2.78795192 -3.16825651 -0.67715519 -0.09722957 -0.07045258]
    # ['zero', 'constant', 'symmetric', 'periodic', 'smooth', 'periodization', 'reflect', 'antisymmetric', 'antireflect']

    print(pywt.idwt([1, 2, 0, 1], None, 'db3', 'symmetric'))
    print(pywt.idwt([1, 2, 0, 1], [0, 0, 0, 0], 'db3', 'symmetric'))
    # [ 0.83431373 -0.23479575  0.16178801  0.87734409]
    # [ 0.83431373 -0.23479575  0.16178801  0.87734409]


def wavelet_packets():
    # 小波包 wavelet packets
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    wp = pywt.WaveletPacket(data=X, wavelet='db3', mode='symmetric', maxlevel=3)
    print(wp.data)            # [1 2 3 4 5 6 7 8 9]
    print(wp.level)           # 0    #分解級別為0
    print(wp['ad'].maxlevel)  # 3

    # 訪問小波包的子節點
    # 第一層：
    print(wp['a'].data)       # [ 4.52111203  1.54666942  2.57019338  5.3986205   8.20681003 11.18125264]
    print(wp['a'].path)       # a

    # 第2 層
    print(wp['aa'].data)      # [ 3.63890166  6.00349136  2.89780988  6.80941869 15.41549196]
    print(wp['ad'].data)      # [ 1.25531439 -0.60300027  0.36403471  0.59368086 -0.53821027]
    print(wp['aa'].path)      # aa
    print(wp['ad'].path)      # ad

    # 第3 層時：
    print(wp['aaa'].data)
    print([node.path for node in wp.get_level(3, 'natural')])  # 獲取特定層數的所有節點,第3層有8個
    # ['aaa', 'aad', 'ada', 'add', 'daa', 'dad', 'dda', 'ddd']

    # 依據頻帶頻率進行劃分
    print([node.path for node in wp.get_level(3, 'freq')])
    # ['aaa', 'aad', 'add', 'ada', 'dda', 'ddd', 'dad', 'daa']

    # 從小波包中 重建數據
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    wp = pywt.WaveletPacket(data=X, wavelet='db1', mode='symmetric', maxlevel=3)
    print(wp['ad'].data)  # [-2,-2]

    new_wp = pywt.WaveletPacket(data=None, wavelet='db1', mode='symmetric')
    new_wp['a'] = wp['a']
    new_wp['aa'] = wp['aa'].data
    new_wp['ad'] = wp['ad'].data
    new_wp['d'] = wp['d']
    print(new_wp.reconstruct(update=False))
    # new_wp['a'] = wp['a']  直接使用高低頻也可進行重構
    # new_wp['d'] = wp['d']
    print(new_wp)  #: None
    print(new_wp.reconstruct(update=True))  # 更新設置為True時。
    print(new_wp)
    # : [1. 2. 3. 4. 5. 6. 7. 8.]

    # 獲取葉子結點
    print([node.path for node in new_wp.get_leaf_nodes(decompose=False)])
    print([node.path for node in new_wp.get_leaf_nodes(decompose=True)])
    # ['aa', 'ad', 'd']
    # ['aaa', 'aad', 'ada', 'add', 'daa', 'dad', 'dda', 'ddd']

    # 從小波包樹中移除結點
    dummy = wp.get_level(2)
    for i in wp.get_leaf_nodes(False):
        print(i.path, i.data)
    # aa [ 5. 13.]
    # ad [-2. -2.]
    # da [-1. -1.]
    # dd [-1.11022302e-16  0.00000000e+00]
    node = wp['ad']
    print(node)  # ad: [-2. -2.]
    del wp['ad']  # 刪除結點
    for i in wp.get_leaf_nodes(False):
        print(i.path, i.data)
    # aa [ 5. 13.]
    # da [-1. -1.]
    # dd [-1.11022302e-16  0.00000000e+00]

    print(wp.reconstruct())  # 進行重建
    # [2. 3. 2. 3. 6. 7. 6. 7.]

    wp['ad'].data = node.data  # 還原已刪除的結點
    print(wp.reconstruct())
    # [1. 2. 3. 4. 5. 6. 7. 8.]

    assert wp.a == wp["a"]
    print(wp["a"])
    # a: [ 2.12132034  4.94974747  7.77817459 10.60660172]


if __name__ == '__main__':
    dwt_and_idwt()
    wavelet_packets()

