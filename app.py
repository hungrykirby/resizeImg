import glob
import cv2
import numpy as np
import sys
import os

sizes = [240, 300, 460, 700, 1040]
path_to_save = 'C:\\work\\python\\resizeImg\\save'
path_to_files = 'C:\\work\\python\\resizeImg\\files\\*.png'
files = glob.glob(path_to_files)
#print(files)
for f in files:
    #print(f)
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    imgH, imgW = img.shape[:2]
    name, ext = os.path.splitext(os.path.basename(f))
    os.mkdir(path_to_save + '\\' + name) 
    for s in sizes:
        #print(f, name)
        #os.mkdir(path_to_save + '\\' + name) 
        cv2.imwrite(path_to_save + '\\' + name + '\\' + str(s) + ".jpg", cv2.resize(img, (s, int(s*imgH/imgW))))
        os.rename(path_to_save + '\\' + name + '\\' + str(s) + ".jpg", path_to_save + '\\' + name + '\\' + str(s))