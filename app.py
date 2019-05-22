import glob
import cv2
import numpy as np
import sys
import os


'''
例えばfilesディレクトリにwowwow.pngがある場合
saveディレクトリには
フォルダwowowが作成され、中には240 300 460 700 1040という名前の画像ファイルが5つできる
(拡張子を入れるとLINE bot APIでは正しく動作しないので注意)。
'''

sizes = [240, 300, 460, 700, 1040]
path_to_save = 'C:\\work\\python\\resizeImg\\save' #出来上がった画像が保存されるpath
path_to_files = 'C:\\work\\python\\resizeImg\\files\\*.png' #元画像jpegでもいけると思う。

files = glob.glob(path_to_files)

for f in files:
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    imgH, imgW = img.shape[:2]
    name, ext = os.path.splitext(os.path.basename(f))
    os.mkdir(path_to_save + '\\' + name)
    for s in sizes:
        cv2.imwrite(path_to_save + '\\' + name + '\\' + str(s) + ".jpg", cv2.resize(img, (s, int(s*imgH/imgW))))
        os.rename(path_to_save + '\\' + name + '\\' + str(s) + ".jpg", path_to_save + '\\' + name + '\\' + str(s))
